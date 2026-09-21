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
    schema_path_str = sys.argv[2]
    schema_path = Path(schema_path_str)

    # Refuse placeholder schemas
    if not schema_path_str or str(schema_path).replace("\\", "/").endswith("node.schema.json"):
        print(f"FAIL: no valid artifact schema bound ({schema_path_str})")
        sys.exit(1)

    if not artifact_path.exists():
        print(f"FAIL: Artifact does not exist: {artifact_path}")
        sys.exit(1)

    if not schema_path.exists():
        print(f"FAIL: Schema does not exist: {schema_path}")
        sys.exit(1)

    # Minimum size check
    raw = artifact_path.read_text(encoding="utf-8")
    ext = artifact_path.suffix.lower()
    min_size = 500 if ext in [".md", ".ts", ".yaml", ".yml"] else 200
    if len(raw) < min_size:
        print(f"FAIL: artifact is only {len(raw)} bytes — too thin to be real")
        sys.exit(1)

    # Load schema
    try:
        schema_data = json.loads(schema_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"FAIL: Invalid JSON in schema {schema_path}: {e}")
        sys.exit(1)

    # Doc artifact checking
    if ext in [".md", ".ts", ".yaml", ".yml"]:
        required_headings = schema_data.get("required_headings", [])
        missing = [h for h in required_headings if h not in raw]
        if missing:
            print(f"FAIL: artifact missing required headings: {missing}")
            sys.exit(1)
        print(f"PASS: {artifact_path} conforms to {schema_path}")
        sys.exit(0)

    # JSON artifact validation
    try:
        artifact_data = json.loads(raw)
    except Exception as e:
        print(f"FAIL: Invalid JSON in artifact {artifact_path}: {e}")
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
