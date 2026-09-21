#!/usr/bin/env python3
import hashlib, json, sys
from pathlib import Path
node=sys.argv[1] if len(sys.argv)>1 else 'unknown'; payload=sys.stdin.read(); h=hashlib.sha256(payload.encode()).hexdigest()[:12]; out=Path('tests/failures')/f'{node}-{h}'; out.mkdir(parents=True,exist_ok=True); (out/'reproduction.json').write_text(payload or '{}'); (out/'expected.txt').write_text(''); (out/'actual.txt').write_text(''); print(out)
