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
scraped = 0
for entry in index.get('references', []):
    path = refs / entry['file']
    if not path.exists():
        errors.append(f"missing: {entry['file']}")
        continue
    data = json.loads(path.read_text())
    errors.extend(f"{entry['file']}: schema: {error.message}" for error in Draft202012Validator(schema).iter_errors(data))
    acquirer = data.get('acquirer', entry.get('acquirer'))
    if entry.get('type') == 'fixture':
        if acquirer == 'curated-reference-index':
            errors.append(f"{entry['file']}: rejected authored fixture acquirer curated-reference-index")
        if entry.get('note') != 'schema-valid example, not scraped':
            errors.append(f"{entry['file']}: fixture note must be 'schema-valid example, not scraped'")
        continue
    if acquirer == 'curated-reference-index':
        errors.append(f"{entry['file']}: rejected authored fixture acquirer curated-reference-index")
    if entry.get('type') != 'scraped':
        errors.append(f"{entry['file']}: missing explicit type fixture or scraped")
        continue
    if acquirer != 'spa-ripper':
        errors.append(f"{entry['file']}: scraped reference must have acquirer spa-ripper; got {acquirer!r}")
    scraped += 1
    routes = data.get('routes') or []
    sections = data.get('sections') or {}
    design_tokens = data.get('design_tokens') or {}
    if len(routes) < 5:
        errors.append(f"{entry['file']}: routes.length={len(routes)}; scraped references require at least 5 routes")
    if not sections:
        errors.append(f"{entry['file']}: sections is empty")
    if not design_tokens:
        errors.append(f"{entry['file']}: design_tokens is empty")
if errors:
    print('REFERENCES INVALID')
    print('\n'.join(errors))
    sys.exit(1)
print(f"REFERENCES VALID: {len(index.get('references', []))} indexed references; {scraped} scraped references; fixture entries excluded")
