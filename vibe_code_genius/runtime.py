from __future__ import annotations

import json
import os
import shlex
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from .validation import validate_artifact_file


def now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


FEATURE_IMPLIES = {
    "backend": {"api"},
    "integrations": {"backend", "api"},
}


def expand_features(features: Iterable[str]) -> set[str]:
    enabled = set(features)
    changed = True
    while changed:
        changed = False
        for feature in list(enabled):
            for implied in FEATURE_IMPLIES.get(feature, set()):
                if implied not in enabled:
                    enabled.add(implied)
                    changed = True
    return enabled


def activation_satisfied(key: str | None, enabled: set[str]) -> bool:
    if not key:
        return True
    required = {part.strip() for part in key.split("+") if part.strip()}
    return required.issubset(enabled)


def selected_nodes(tree: dict[str, Any], tier_stop: int = 5, features: Iterable[str] = ()) -> list[dict[str, Any]]:
    enabled = expand_features(features)
    selected = []
    for node in tree["nodes"]:
        if int(node["tier"]) > int(tier_stop):
            continue
        if node.get("optional") and not activation_satisfied(node.get("activation_key"), enabled):
            continue
        selected.append(node)
    return selected


def resolve_features(out: Path, session: dict[str, Any]) -> list[str]:
    enabled = set(session.get("features", []))
    if session.get("reference_url"):
        enabled.add("reference_comparison")

    scope_path = out / "scope.json"
    if scope_path.is_file():
        try:
            scope = _read_json(scope_path)
            if scope.get("status") == "complete":
                enabled.update(scope.get("capabilities") or [])
        except Exception:
            # Invalid scope is handled by the normal artifact validator.
            pass

    return sorted(expand_features(enabled))


def topo_order(nodes: list[dict[str, Any]]) -> list[str]:
    items = {n["id"]: n for n in nodes}
    remaining = set(items)
    order: list[str] = []
    while remaining:
        ready = sorted(
            nid
            for nid in remaining
            if all(p not in remaining for p in items[nid].get("prereqs", []) if p in items)
        )
        if not ready:
            raise ValueError("cycle in selected workflow: " + ",".join(sorted(remaining)))
        order.extend(ready)
        remaining.difference_update(ready)
    return order


def validate_artifact(root: Path, out: Path, node: dict[str, Any]) -> tuple[bool, list[str]]:
    artifact = out / node["expected_artifact_path"]
    schema_path = root / node["artifact_schema"]
    errors = validate_artifact_file(artifact, schema_path)
    return not errors, errors


def _session_path(out: Path) -> Path:
    return out / "session.json"


def init_session(
    out: Path,
    *,
    intent: str,
    reference_url: str | None,
    tier_stop: int,
    features: Iterable[str],
    selected: list[dict[str, Any]],
) -> dict[str, Any]:
    out.mkdir(parents=True, exist_ok=True)
    timestamp = now()
    session = {
        "version": "1.1.0",
        "status": "pending",
        "session_id": f"session-{timestamp.replace(':', '').replace('-', '')}",
        "started_at": timestamp,
        "updated_at": timestamp,
        "intent": intent,
        "reference_url": reference_url,
        "tier_stop": tier_stop,
        "features": sorted(set(features)),
        "active_features": sorted(expand_features(features)),
        "active_skills": ["vibe-code-genius"],
        "nodes": {n["id"]: {"status": "pending", "artifact": n["expected_artifact_path"], "errors": []} for n in selected},
        "artifacts": [],
        "checkpoints": [],
        "budget": {"nodes_count": len(selected)},
        "why_log": [],
    }
    _session_path(out).write_text(json.dumps(session, indent=2) + "\n", encoding="utf-8")
    return session


def load_session(out: Path) -> dict[str, Any]:
    path = _session_path(out)
    if not path.is_file():
        raise FileNotFoundError(f"no session at {path}; run vibe-tree plan first")
    return _read_json(path)


def save_session(out: Path, session: dict[str, Any]) -> None:
    session["updated_at"] = now()
    _session_path(out).write_text(json.dumps(session, indent=2) + "\n", encoding="utf-8")


def refresh_status(root: Path, out: Path, tree: dict[str, Any]) -> dict[str, Any]:
    session = load_session(out)
    active_features = resolve_features(out, session)
    session["active_features"] = active_features
    selected = selected_nodes(tree, session["tier_stop"], active_features)
    by_id = {n["id"]: n for n in selected}

    for node in selected:
        session["nodes"].setdefault(
            node["id"],
            {"status": "pending", "artifact": node["expected_artifact_path"], "errors": []},
        )
    complete: set[str] = set()

    for nid in topo_order(selected):
        node = by_id[nid]
        artifact = out / node["expected_artifact_path"]
        if artifact.exists():
            ok, errors = validate_artifact(root, out, node)
            state = "complete" if ok else "failed"
            session["nodes"][nid] = {
                "status": state,
                "artifact": node["expected_artifact_path"],
                "errors": errors,
            }
            if ok:
                complete.add(nid)
            continue

        blockers = [p for p in node.get("prereqs", []) if p in by_id and p not in complete]
        state = "pending" if blockers else "ready"
        session["nodes"][nid] = {
            "status": state,
            "artifact": node["expected_artifact_path"],
            "errors": [],
            "blocked_by": blockers,
        }

    selected_ids = set(by_id)
    for node in tree["nodes"]:
        if node["id"] in session["nodes"] and node["id"] not in selected_ids and node.get("optional"):
            previous = session["nodes"][node["id"]]
            if previous.get("status") != "complete":
                session["nodes"][node["id"]] = {
                    "status": "skipped",
                    "artifact": node["expected_artifact_path"],
                    "errors": [],
                    "reason": f"inactive capability: {node.get('activation_key')}",
                }

    states = [session["nodes"][nid]["status"] for nid in selected_ids]
    if states and all(s == "complete" for s in states):
        session["status"] = "complete"
    elif any(s == "failed" for s in states):
        session["status"] = "failed"
    elif any(s == "ready" for s in states):
        session["status"] = "ready"
    else:
        session["status"] = "pending"

    session["artifacts"] = sorted(
        n["expected_artifact_path"]
        for n in selected
        if session["nodes"][n["id"]]["status"] == "complete"
    )
    save_session(out, session)
    return session


def ready_nodes(root: Path, out: Path, tree: dict[str, Any], *, include_failed: bool = False) -> list[dict[str, Any]]:
    session = refresh_status(root, out, tree)
    selected = selected_nodes(tree, session["tier_stop"], session.get("active_features", session.get("features", [])))
    runnable = []
    for node in selected:
        state = session["nodes"][node["id"]]
        if state["status"] == "ready":
            runnable.append(node)
            continue
        if include_failed and state["status"] == "failed":
            blockers = state.get("blocked_by") or []
            if not blockers:
                runnable.append(node)
    return runnable


def write_task_packet(root: Path, out: Path, node: dict[str, Any]) -> Path:
    task_dir = out / ".vibe" / "tasks"
    task_dir.mkdir(parents=True, exist_ok=True)
    skill_path = root / node["skill_file"]
    packet = {
        "version": "1.0.0",
        "node": node["id"],
        "name": node["name"],
        "tier": node["tier"],
        "model_hint": node["model"],
        "max_response_tokens": node["max_response_tokens"],
        "prerequisites": node["prereqs"],
        "input_contract": node["input"],
        "output_path": node["expected_artifact_path"],
        "artifact_schema": node["artifact_schema"],
        "skill_file": node["skill_file"],
        "instructions": skill_path.read_text(encoding="utf-8"),
        "rules": [
            "Write only within the declared build/output workspace unless the task explicitly requires source changes.",
            "Do not mark the node complete until the declared artifact validates.",
            "Do not invent evidence, credentials, routes, integrations, metrics, or tool results.",
            "If blocked, record the blocker instead of fabricating a successful artifact.",
        ],
    }
    path = task_dir / f"{node['id']}.json"
    path.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    return path


def execute(
    root: Path,
    out: Path,
    tree: dict[str, Any],
    *,
    executor: str,
    stop_after: int | None = None,
    timeout_seconds: int = 1800,
) -> dict[str, Any]:
    completed_this_run: list[str] = []
    attempts = 0

    while True:
        session = refresh_status(root, out, tree)
        if session["status"] == "complete":
            return {"status": "complete", "completed": completed_this_run, "session": str(_session_path(out))}
        ready = ready_nodes(root, out, tree, include_failed=True)
        if not ready:
            return {"status": "blocked", "reason": "no ready nodes and workflow is incomplete", "completed": completed_this_run}

        node = ready[0]
        task = write_task_packet(root, out, node)
        env = os.environ.copy()
        env.update({
            "VIBE_NODE_ID": node["id"],
            "VIBE_TASK_FILE": str(task.resolve()),
            "VIBE_OUTPUT_DIR": str(out.resolve()),
            "VIBE_ROOT": str(root.resolve()),
            "VIBE_ARTIFACT_PATH": str((out / node["expected_artifact_path"]).resolve()),
            "VIBE_SCHEMA_PATH": str((root / node["artifact_schema"]).resolve()),
        })
        try:
            command = shlex.split(executor)
            if not command:
                return {"status": "failed", "node": node["id"], "error": "empty executor command"}
            proc = subprocess.run(
                command,
                cwd=str(root),
                env=env,
                check=False,
                timeout=timeout_seconds,
            )
        except subprocess.TimeoutExpired:
            session = load_session(out)
            session["nodes"][node["id"]]["status"] = "failed"
            session["nodes"][node["id"]]["errors"] = [f"executor timed out after {timeout_seconds}s"]
            session["status"] = "failed"
            save_session(out, session)
            return {"status": "failed", "node": node["id"], "timeout_seconds": timeout_seconds}

        attempts += 1
        if proc.returncode != 0:
            session = load_session(out)
            session["nodes"][node["id"]]["status"] = "failed"
            session["nodes"][node["id"]]["errors"] = [f"executor exited {proc.returncode}"]
            session["status"] = "failed"
            save_session(out, session)
            return {"status": "failed", "node": node["id"], "exit_code": proc.returncode}

        ok, errors = validate_artifact(root, out, node)
        if not ok:
            session = load_session(out)
            session["nodes"][node["id"]]["status"] = "failed"
            session["nodes"][node["id"]]["errors"] = errors
            session["status"] = "failed"
            save_session(out, session)
            return {"status": "failed", "node": node["id"], "validation_errors": errors}

        completed_this_run.append(node["id"])
        if stop_after is not None and attempts >= stop_after:
            session = refresh_status(root, out, tree)
            return {"status": session["status"], "completed": completed_this_run, "stopped_after": attempts}
