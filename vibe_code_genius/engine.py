from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from .runtime import init_session, selected_nodes, topo_order as runtime_topo_order


def load_tree(root: Path):
    return json.loads((root / "skill-tree.json").read_text(encoding="utf-8"))


def topo_order(tree):
    return runtime_topo_order(tree["nodes"])


def artifact_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()[:12]


def now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def plan(
    intent: str,
    out: Path,
    root: Path,
    reference_url: str | None = None,
    *,
    tier_stop: int = 5,
    features: Iterable[str] = (),
):
    if tier_stop not in {1, 2, 3, 4, 5}:
        raise ValueError("tier_stop must be between 1 and 5")

    out.mkdir(parents=True, exist_ok=True)
    tree = load_tree(root)
    chosen = selected_nodes(tree, tier_stop=tier_stop, features=features)
    order = runtime_topo_order(chosen)
    by_id = {n["id"]: n for n in chosen}

    request = {
        "version": "1.0.0",
        "status": "pending",
        "intent": intent,
        "reference_url": reference_url,
        "tier_stop": tier_stop,
        "features": sorted(set(features)),
        "created_at": now(),
    }
    (out / "request.json").write_text(json.dumps(request, indent=2) + "\n", encoding="utf-8")
    init_session(
        out,
        intent=intent,
        reference_url=reference_url,
        tier_stop=tier_stop,
        features=features,
        selected=chosen,
    )

    lines = [
        "# Build Plan",
        "",
        f"Intent: {intent}",
        f"Tier stop: {tier_stop}",
        f"Reference: {reference_url or 'none'}",
        f"Optional features: {', '.join(sorted(set(features))) or 'none'}",
        "",
        "## Node order",
        "",
    ]
    lines.extend(
        f"{i + 1}. {nid} — {by_id[nid]['name']} -> {by_id[nid]['expected_artifact_path']}"
        for i, nid in enumerate(order)
    )
    (out / "plan.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    return {
        "out": str(out),
        "nodes": len(order),
        "order": order,
        "reference_url": reference_url,
        "tier_stop": tier_stop,
        "features": sorted(set(features)),
    }
