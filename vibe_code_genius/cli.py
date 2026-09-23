import argparse, json, os, sys
from pathlib import Path
from .engine import plan
from .tooling import acquire_reference, preflight_payload, run_slop_check
from .agent_gateway import discovery_payload, create_task_packet
from .project_graph import save_graph, query_graph
from .mission_engine import create_mission
from .local_api import serve
from .validator_engine import run_command
from .capability_router import route

def _auth_from_env(name):
    if not name:
        return None
    value=os.environ.get(name)
    if value is None:
        raise SystemExit(f"environment variable {name!r} is not set")
    return value

def main(argv=None):
    p=argparse.ArgumentParser(prog="vibe-tree")
    sub=p.add_subparsers(dest="command", required=True)

    q=sub.add_parser("plan")
    q.add_argument("--intent", required=True)
    q.add_argument("--out", default=".artifacts/session")
    q.add_argument("--reference-url")
    q.add_argument("--acquire", action="store_true", help="run real reference acquisition after planning")
    q.add_argument("--no-api", action="store_true")
    q.add_argument("--strict-tools", action="store_true")
    q.add_argument("--auth-header-env", help="environment variable containing an explicit API Authorization header")

    a=sub.add_parser("acquire")
    a.add_argument("--url", required=True)
    a.add_argument("--out", default=".artifacts/session")
    a.add_argument("--no-api", action="store_true")
    a.add_argument("--strict-tools", action="store_true")
    a.add_argument("--auth-header-env", help="environment variable containing an explicit API Authorization header")

    c=sub.add_parser("check-tools")
    c.add_argument("--all", action="store_true", help="also check SlopMonster")
    c.add_argument("--json", action="store_true")

    ag=sub.add_parser("agents")
    ag.add_argument("--json", action="store_true")

    t=sub.add_parser("task")
    t.add_argument("--objective", required=True)
    t.add_argument("--repo", default=".")
    t.add_argument("--out", default=".godtree/tasks/task.json")
    t.add_argument("--allow", action="append", default=[])
    t.add_argument("--deny", action="append", default=[])
    t.add_argument("--accept", action="append", default=[])

    g=sub.add_parser("graph")
    g.add_argument("--repo", default=".")
    g.add_argument("--out", default=".godtree/graph.json")
    g.add_argument("--query")

    m=sub.add_parser("mission")
    m.add_argument("--objective", required=True)
    m.add_argument("--repo", default=".")
    m.add_argument("--out", default=".godtree/missions")

    daemon=sub.add_parser("daemon")
    daemon.add_argument("--repo",default=".")
    daemon.add_argument("--host",default="127.0.0.1")
    daemon.add_argument("--port",type=int,default=7331)

    vr=sub.add_parser("verify")
    vr.add_argument("--repo",default=".")
    vr.add_argument("--receipt",default=".godtree/receipts/verify.json")
    vr.add_argument("cmd",nargs=argparse.REMAINDER)

    rr=sub.add_parser("route")
    rr.add_argument("capability")
    rr.add_argument("--prefer")

    s=sub.add_parser("slop-check")
    s.add_argument("path")
    s.add_argument("--allow-proof", action="store_true")

    d=sub.add_parser("debug"); d.add_argument("mode", choices=["on","off"])
    sub.add_parser("tree")
    sub.add_parser("stats")
    f=sub.add_parser("report-failure"); f.add_argument("node"); f.add_argument("--input", default="{}")

    args=p.parse_args(argv); root=Path(__file__).resolve().parent.parent

    if args.command=="plan":
        result=plan(args.intent, Path(args.out), root, reference_url=args.reference_url)
        if args.acquire:
            if not args.reference_url:
                raise SystemExit("--acquire requires --reference-url")
            result["acquisition"]=acquire_reference(
                args.reference_url,
                Path(args.out),
                with_api=not args.no_api,
                strict_tools=args.strict_tools,
                auth_header=_auth_from_env(args.auth_header_env),
            )
        print(json.dumps(result, indent=2)); return 0

    if args.command=="acquire":
        result=acquire_reference(
            args.url,
            Path(args.out),
            with_api=not args.no_api,
            strict_tools=args.strict_tools,
            auth_header=_auth_from_env(args.auth_header_env),
        )
        print(json.dumps(result, indent=2))
        return 0 if result["status"] in {"complete","degraded"} else 1

    if args.command=="check-tools":
        payload=preflight_payload(include_slopmonster=args.all)
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            for item in payload["tools"]:
                state="OK" if item["available"] else "MISSING"
                print(f"{state:7} {item['name']}: {item['resolved'] or item['install']}")
                if item.get("note"): print(f"        {item['note']}")
        return 0 if payload["status"]=="ready" else 1

    if args.command=="agents":
        payload=discovery_payload()
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print("GodTree Agent Gateway — zero-cost-first")
            for item in payload["agents"]:
                state="OK" if item["available"] else "OFF"
                print(f'{state:3} {item["id"]:16} {item["mode"]:12} {item["resolved"] or ""}')
                if item.get("note"): print(f'    {item["note"]}')
        return 0

    if args.command=="task":
        path=create_task_packet(args.objective, Path(args.repo), Path(args.out),
                                allowed=args.allow, forbidden=args.deny, acceptance=args.accept)
        print(str(path))
        return 0

    if args.command=="graph":
        out=save_graph(Path(args.repo), Path(args.out))
        if args.query:
            payload=json.loads(out.read_text(encoding="utf-8"))
            print(json.dumps(query_graph(payload,args.query),indent=2))
        else: print(str(out))
        return 0

    if args.command=="mission":
        print(str(create_mission(args.objective,Path(args.repo),Path(args.out))))
        return 0

    if args.command=="daemon":
        serve(Path(args.repo),args.host,args.port);return 0

    if args.command=="verify":
        cmd=args.cmd[1:] if args.cmd[:1]==["--"] else args.cmd
        result=run_command(Path(args.repo),cmd,Path(args.receipt))
        print(json.dumps(result,indent=2));return 0 if result["status"]=="passed" else 1

    if args.command=="route":
        print(json.dumps(route(args.capability,args.prefer),indent=2));return 0

    if args.command=="slop-check":
        result=run_slop_check(Path(args.path), allow_proof=args.allow_proof)
        print(json.dumps(result, indent=2))
        return 0 if result.get("exit_code")==0 else 1

    if args.command=="tree": print(json.dumps(json.loads((root/"skill-tree.json").read_text()), indent=2)); return 0
    if args.command=="debug":
        path=Path(".vibe-debug"); path.write_text(args.mode+"\n"); print(f"debug {args.mode}"); return 0
    if args.command=="stats":
        import subprocess
        return subprocess.call([sys.executable, str(root/"scripts/stats.py")])
    if args.command=="report-failure":
        import subprocess
        result=subprocess.run([sys.executable, str(root/"scripts/report-failure.py"), args.node], input=args.input, text=True)
        return result.returncode
    return 2
