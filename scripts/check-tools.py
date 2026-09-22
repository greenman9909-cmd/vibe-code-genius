#!/usr/bin/env python3
import argparse
import json
from vibe_code_genius.tooling import preflight_payload

def main():
    p=argparse.ArgumentParser(description="Check external Vibe Code Genius tools.")
    p.add_argument("--all", action="store_true", help="also check SlopMonster")
    p.add_argument("--json", action="store_true")
    args=p.parse_args()
    payload=preflight_payload(include_slopmonster=args.all)
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        for item in payload["tools"]:
            state="OK" if item["available"] else "MISSING"
            print(f"{state:7} {item['name']}: {item['resolved'] or item['install']}")
            if item.get("note"):
                print(f"        {item['note']}")
    raise SystemExit(0 if payload["status"]=="ready" else 1)

if __name__=="__main__":
    main()
