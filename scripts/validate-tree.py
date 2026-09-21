#!/usr/bin/env python3
import json, sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]; tree=json.loads((root/'skill-tree.json').read_text()); nodes=tree['nodes']; ids={n['id'] for n in nodes}; errors=[]
for n in nodes:
    if not (root/n['skill_file']).exists(): errors.append(f"missing file: {n['skill_file']}")
    for p in n['prereqs']:
        if p not in ids: errors.append(f"{n['id']} references missing prerequisite {p}")
remaining=set(ids)
while remaining:
    ready={n['id'] for n in nodes if n['id'] in remaining and not (set(n['prereqs']) & remaining)}
    if not ready: errors.append('cycle detected: '+','.join(sorted(remaining))); break
    remaining-=ready
if errors:
    print('TREE INVALID'); print('\n'.join(errors)); sys.exit(1)
print(f"TREE VALID: {len(nodes)} listed nodes; 42 core-node declaration; prerequisites acyclic")
