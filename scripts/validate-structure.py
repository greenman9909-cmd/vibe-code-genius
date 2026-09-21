#!/usr/bin/env python3
import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator
root=Path(__file__).resolve().parents[1]; path=Path(sys.argv[1]) if len(sys.argv)>1 else root/'tests/inputs/structure.json'
data=json.loads(path.read_text()); schema=json.loads((root/'schema/structure.schema.json').read_text()); errors=list(Draft202012Validator(schema).iter_errors(data))
if errors:
    print('INVALID STRUCTURE'); [print(e.message) for e in errors]; sys.exit(1)
print('VALID STRUCTURE')
