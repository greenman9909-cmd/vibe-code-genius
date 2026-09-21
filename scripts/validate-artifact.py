#!/usr/bin/env python3
import sys
import json
from pathlib import Path
from jsonschema import Draft202012Validator

def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <artifact_path> <schema_path>")
        sys.exit(1)

    artifact_path = Path(sys.argv[1])
    schema_path = Path(sys.argv[2])

    if not artifact_path.exists():
        print(f"FAIL: Artifact does not exist: {artifact_path}")
        sys.exit(1)

    if not schema_path.exists():
        print(f"FAIL: Schema does not exist: {schema_path}")
        sys.exit(1)

    if artifact_path.suffix.lower() != ".json":
        print(f"SKIP: Non-JSON artifact {artifact_path}")
        sys.exit(0)

    try:
        artifact_data = json.loads(artifact_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"FAIL: Invalid JSON in artifact {artifact_path}: {e}")
        sys.exit(1)

    try:
        schema_data = json.loads(schema_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"FAIL: Invalid JSON in schema {schema_path}: {e}")
        sys.exit(1)

    validator = Draft202012Validator(schema_data)
    errors = list(validator.iter_errors(artifact_data))
    if errors:
        print(f"FAIL: Schema validation failed for {artifact_path} against {schema_path}:")
        for err in errors:
            print(f"  - {err.message} (path: {'/'.join(str(p) for p in err.absolute_path)})")
        sys.exit(1)

    print(f"PASS: {artifact_path} conforms to {schema_path}")
    sys.exit(0)

if __name__ == "__main__":
    main()
