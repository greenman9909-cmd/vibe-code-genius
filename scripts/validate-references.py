#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

root = Path(__file__).resolve().parents[1]
refs = root / 'references'
index = json.loads((refs / 'index.json').read_text())
schema = json.loads((root / 'schema' / 'structure.schema.json').read_text())
errors = []
for entry in index.get('references', []):
    path = refs / entry['file']
    if not path.exists():
        errors.append(f"missing: {entry['file']}")
        continue
    data = json.loads(path.read_text())
    errors.extend(f"{entry['file']}: {error.message}" for error in Draft202012Validator(schema).iter_errors(data))
if errors:
    print('REFERENCES INVALID')
    print('\n'.join(errors))
    sys.exit(1)
print(f"REFERENCES VALID: {len(index.get('references', []))} indexed structure.json files")
