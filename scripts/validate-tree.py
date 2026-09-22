#!/usr/bin/env python3
import json, sys
from pathlib import Path

root=Path(__file__).resolve().parents[1]
tree=json.loads((root/'skill-tree.json').read_text())
nodes=tree['nodes']
ids=[n['id'] for n in nodes]
idset=set(ids)
errors=[]

if len(ids) != len(idset):
    errors.append('duplicate node id detected')
if tree.get('node_count') != len(nodes):
    errors.append(f"node_count says {tree.get('node_count')} but {len(nodes)} nodes are listed")

declared_files=set()
for n in nodes:
    skill=root/n['skill_file']
    declared_files.add(n['skill_file'])
    if not skill.exists():
        errors.append(f"missing file: {n['skill_file']}")
    for p in n['prereqs']:
        if p not in idset:
            errors.append(f"{n['id']} references missing prerequisite {p}")

actual_files={
    str(p.relative_to(root)).replace('\\','/')
    for p in (root/'nodes').rglob('*.md')
}
for orphan in sorted(actual_files-declared_files):
    errors.append(f"unregistered node file: {orphan}")
for missing in sorted(declared_files-actual_files):
    errors.append(f"declared node file missing: {missing}")

remaining=set(idset)
while remaining:
    ready={n['id'] for n in nodes if n['id'] in remaining and not (set(n['prereqs']) & remaining)}
    if not ready:
        errors.append('cycle detected: '+','.join(sorted(remaining)))
        break
    remaining-=ready

if errors:
    print('TREE INVALID')
    print('\n'.join(errors))
    sys.exit(1)
print(f"TREE VALID: {len(nodes)} listed nodes; {tree.get('declared_node_count')} core-node declaration; prerequisites acyclic; no orphan node files")
