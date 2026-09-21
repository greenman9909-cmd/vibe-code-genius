#!/usr/bin/env python3
import json, sys
from pathlib import Path
path=Path(sys.argv[2] if len(sys.argv)>2 else '.artifacts/session/session.json')
if sys.argv[1]=='write': path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(json.loads(sys.stdin.read()),indent=2)+'\n')
elif sys.argv[1]=='read': print(path.read_text())
elif sys.argv[1]=='list': print('\n'.join(str(p) for p in Path('.artifacts').glob('**/session.json')))
