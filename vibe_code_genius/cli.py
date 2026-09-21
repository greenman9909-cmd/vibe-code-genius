import argparse, json, sys
from pathlib import Path
from .engine import plan

def main(argv=None):
    p=argparse.ArgumentParser(prog="vibe-tree")
    sub=p.add_subparsers(dest="command", required=True)
    q=sub.add_parser("plan"); q.add_argument("--intent", required=True); q.add_argument("--out", default=".artifacts/session")
    d=sub.add_parser("debug"); d.add_argument("mode", choices=["on","off"])
    sub.add_parser("tree")
    sub.add_parser("stats")
    f=sub.add_parser("report-failure"); f.add_argument("node"); f.add_argument("--input", default="{}")
    args=p.parse_args(argv); root=Path(__file__).resolve().parent.parent
    if args.command=="plan": print(json.dumps(plan(args.intent, Path(args.out), root), indent=2)); return 0
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
