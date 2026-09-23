import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

from .engine import load_tree, plan
from .runtime import execute, ready_nodes, refresh_status, write_task_packet
from .tooling import acquire_reference, preflight_payload, run_slop_check


def _auth_from_env(name):
    if not name:
        return None
    value = os.environ.get(name)
    if value is None:
        raise SystemExit(f"environment variable {name!r} is not set")
    return value


def _print(value, as_json=False):
    if as_json:
        print(json.dumps(value, indent=2))
    else:
        print(value)


def main(argv=None):
    p = argparse.ArgumentParser(prog="vibe-tree")
    sub = p.add_subparsers(dest="command", required=True)

    q = sub.add_parser("plan", help="create a resumable God Tree session")
    q.add_argument("--intent", required=True)
    q.add_argument("--out", default=".artifacts/session")
    q.add_argument("--reference-url")
    q.add_argument("--tier", type=int, choices=range(1, 6), default=5)
    q.add_argument("--feature", action="append", default=[], help="activate an optional node feature key")
    q.add_argument("--acquire", action="store_true", help="run real reference acquisition after planning")
    q.add_argument("--no-api", action="store_true")
    q.add_argument("--strict-tools", action="store_true")
    q.add_argument("--auth-header-env", help="environment variable containing an explicit API Authorization header")

    a = sub.add_parser("acquire")
    a.add_argument("--url", required=True)
    a.add_argument("--out", default=".artifacts/session")
    a.add_argument("--no-api", action="store_true")
    a.add_argument("--strict-tools", action="store_true")
    a.add_argument("--auth-header-env", help="environment variable containing an explicit API Authorization header")

    st = sub.add_parser("status", help="validate current artifacts and show workflow state")
    st.add_argument("--out", default=".artifacts/session")
    st.add_argument("--json", action="store_true")

    nx = sub.add_parser("next", help="emit task packets for every currently ready node")
    nx.add_argument("--out", default=".artifacts/session")
    nx.add_argument("--json", action="store_true")

    rn = sub.add_parser("run", help="execute ready nodes with an external agent wrapper")
    rn.add_argument("--out", default=".artifacts/session")
    rn.add_argument("--executor", required=True, help="executable that reads VIBE_TASK_FILE and writes the declared artifact")
    rn.add_argument("--stop-after", type=int)
    rn.add_argument("--executor-timeout", type=int, default=1800, help="seconds allowed for one node execution")

    c = sub.add_parser("check-tools")
    c.add_argument("--all", action="store_true", help="also check SlopMonster")
    c.add_argument("--json", action="store_true")

    s = sub.add_parser("slop-check")
    s.add_argument("path")
    s.add_argument("--allow-proof", action="store_true")

    d = sub.add_parser("debug")
    d.add_argument("mode", choices=["on", "off"])
    sub.add_parser("tree")
    sub.add_parser("stats")
    f = sub.add_parser("report-failure")
    f.add_argument("node")
    f.add_argument("--input", default="{}")

    args = p.parse_args(argv)
    root = Path(__file__).resolve().parent.parent

    if args.command == "plan":
        result = plan(
            args.intent,
            Path(args.out),
            root,
            reference_url=args.reference_url,
            tier_stop=args.tier,
            features=args.feature,
        )
        if args.acquire:
            if not args.reference_url:
                raise SystemExit("--acquire requires --reference-url")
            result["acquisition"] = acquire_reference(
                args.reference_url,
                Path(args.out),
                with_api=not args.no_api,
                strict_tools=args.strict_tools,
                auth_header=_auth_from_env(args.auth_header_env),
            )
        print(json.dumps(result, indent=2))
        return 0

    if args.command == "acquire":
        result = acquire_reference(
            args.url,
            Path(args.out),
            with_api=not args.no_api,
            strict_tools=args.strict_tools,
            auth_header=_auth_from_env(args.auth_header_env),
        )
        print(json.dumps(result, indent=2))
        return 0 if result["status"] in {"complete", "degraded"} else 1

    if args.command == "status":
        session = refresh_status(root, Path(args.out), load_tree(root))
        if args.json:
            print(json.dumps(session, indent=2))
        else:
            counts = {}
            for state in session["nodes"].values():
                counts[state["status"]] = counts.get(state["status"], 0) + 1
            summary = ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
            print(f"{session['status']}: {summary}")
        return 1 if session["status"] == "failed" else 0

    if args.command == "next":
        out = Path(args.out)
        nodes = ready_nodes(root, out, load_tree(root))
        packets = []
        for node in nodes:
            task = write_task_packet(root, out, node)
            packets.append({
                "node": node["id"],
                "name": node["name"],
                "task_file": str(task),
                "output": node["expected_artifact_path"],
                "model_hint": node["model"],
            })
        if args.json:
            print(json.dumps({"ready": packets}, indent=2))
        else:
            if not packets:
                print("no ready nodes")
            for item in packets:
                print(f"{item['node']} {item['name']} -> {item['task_file']}")
        return 0

    if args.command == "run":
        result = execute(
            root,
            Path(args.out),
            load_tree(root),
            executor=args.executor,
            stop_after=args.stop_after,
            timeout_seconds=args.executor_timeout,
        )
        print(json.dumps(result, indent=2))
        return 0 if result["status"] in {"complete", "ready", "pending"} else 1

    if args.command == "check-tools":
        payload = preflight_payload(include_slopmonster=args.all)
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            for item in payload["tools"]:
                state = "OK" if item["available"] else "MISSING"
                print(f"{state:7} {item['name']}: {item['resolved'] or item['install']}")
                if item.get("note"):
                    print(f"        {item['note']}")
        return 0 if payload["status"] == "ready" else 1

    if args.command == "slop-check":
        result = run_slop_check(Path(args.path), allow_proof=args.allow_proof)
        print(json.dumps(result, indent=2))
        return 0 if result.get("exit_code") == 0 else 1

    if args.command == "tree":
        print(json.dumps(load_tree(root), indent=2))
        return 0

    if args.command == "debug":
        path = Path(".vibe-debug")
        path.write_text(args.mode + "\n", encoding="utf-8")
        print(f"debug {args.mode}")
        return 0

    if args.command == "stats":
        return subprocess.call([sys.executable, str(root / "scripts" / "stats.py")])

    if args.command == "report-failure":
        result = subprocess.run(
            [sys.executable, str(root / "scripts" / "report-failure.py"), args.node],
            input=args.input,
            text=True,
        )
        return result.returncode

    return 2
