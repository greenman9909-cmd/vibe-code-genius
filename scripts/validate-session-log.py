#!/usr/bin/env python3
import sys
import json
from pathlib import Path
from datetime import datetime

def main():
    log_path = Path(sys.argv[1] if len(sys.argv) > 1 else "first-build/session.log")
    if not log_path.exists():
        print(f"FAIL: log file not found: {log_path}")
        sys.exit(1)

    lines = [line.strip() for line in log_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not lines:
        print("FAIL: session.log is empty")
        sys.exit(1)

    events = []
    for idx, line in enumerate(lines):
        try:
            d = json.loads(line)
            events.append(d)
        except Exception as e:
            print(f"FAIL: line {idx+1} is not valid JSON: {e}")
            sys.exit(1)

    # Check repeating microseconds between consecutive events
    prev_us = None
    for idx, ev in enumerate(events):
        at_str = ev.get("at", "")
        if "." in at_str:
            # e.g. 2026-09-21T22:23:32.503650Z -> 503650
            us_part = at_str.split(".")[1].rstrip("Z")
            if prev_us is not None and us_part == prev_us:
                print(f"FAIL: fabricated timestamps: repeating microseconds '{us_part}' at event {idx+1}")
                sys.exit(1)
            prev_us = us_part

    print(f"PASS: session.log timestamps verified across {len(events)} events")
    sys.exit(0)

if __name__ == "__main__":
    main()
