import argparse, json, sys
from pathlib import Path
from .engine import plan

def main(argv=None):
    p=argparse.ArgumentParser(prog="vibe-tree")
    sub=p.add_subparsers(dest="command", required=True)
    q=sub.add_parser("plan"); q.add_argument("--intent", required=True); q.add_argument("--out", default=".artifacts/session")
    d=sub.add_parser("debug"); d.add_argument("mode", choices=["on","off"])
    sub.add_parser("tree")
    args=p.parse_args(argv); root=Path(__file__).resolve().parent.parent
    if args.command=="plan": print(json.dumps(plan(args.intent, Path(args.out), root), indent=2)); return 0
    if args.command=="tree": print(json.dumps(json.loads((root/"skill-tree.json").read_text()), indent=2)); return 0
    if args.command=="debug":
        path=Path(".vibe-debug"); path.write_text(args.mode+"\n"); print(f"debug {args.mode}"); return 0
    return 2
