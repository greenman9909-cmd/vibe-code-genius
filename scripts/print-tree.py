#!/usr/bin/env python3
import json
from pathlib import Path
tree=json.loads((Path(__file__).resolve().parents[1]/'skill-tree.json').read_text())
for n in tree['nodes']: print('  '*n['tier']+f"{n['id']} {n['name']}")
