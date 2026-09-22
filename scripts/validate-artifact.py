#!/usr/bin/env python3
import sys
import argparse
import json
from pathlib import Path
from jsonschema import Draft202012Validator

def main():
    parser = argparse.ArgumentParser(description="Validate build artifacts against schemas.")
    parser.add_argument("--node", default=None, help="Node ID (e.g. 01, 07g)")
    parser.add_argument("--artifact", default=None, help="Path to the declared artifact")
    parser.add_argument("--schema", default=None, help="Path to the schema file")
    parser.add_argument("positional", nargs="*", help="Positional fallback: <artifact> <schema>")

    args = parser.parse_args()

    node_id = args.node or "unknown"
    artifact_str = args.artifact
    schema_str = args.schema

    if not artifact_str and len(args.positional) >= 1:
        artifact_str = args.positional[0]
    if not schema_str and len(args.positional) >= 2:
        schema_str = args.positional[1]

    if not artifact_str or not schema_str:
        print("Usage: scripts/validate-artifact.py --node <id> --artifact <declared_path> --schema <schema_path>")
        sys.exit(1)

    # Resolve artifact path
    artifact_path = Path(artifact_str)
    if not artifact_path.exists():
        if (Path("first-build") / artifact_str).exists():
            artifact_path = Path("first-build") / artifact_str
        elif (Path("verify") / artifact_str).exists():
            artifact_path = Path("verify") / artifact_str

    if not artifact_path.exists():
        print(f"FAIL: node {node_id} did not produce its declared artifact at {artifact_str}")
        sys.exit(1)

    # Refuse placeholder schemas
    if not schema_str or str(schema_str).replace("\\", "/").endswith("node.schema.json"):
        print(f"FAIL: no valid artifact schema bound ({schema_str})")
        sys.exit(1)

    schema_path = Path(schema_str)
    if not schema_path.exists():
        print(f"FAIL: Schema does not exist: {schema_path}")
        sys.exit(1)

    # Read artifact content
    try:
        raw = artifact_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"FAIL: could not read artifact {artifact_path}: {e}")
        sys.exit(1)

    # Load schema
    try:
        schema_data = json.loads(schema_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"FAIL: Invalid JSON in schema {schema_path}: {e}")
        sys.exit(1)

    ext = artifact_path.suffix.lower()

    # Doc / text artifact validation
    if ext in [".md", ".ts", ".tsx", ".yaml", ".yml"]:
        required = schema_data.get("required_headings") or schema_data.get("required") or []
        missing = [h for h in required if h not in raw]
        if missing:
            print(f"FAIL: artifact missing required fields/headings: {missing}")
            sys.exit(1)

        min_size = 500
        if len(raw) < min_size:
            print(f"FAIL: artifact too thin ({len(raw)} bytes, minimum is {min_size})")
            sys.exit(1)

        print(f"PASS: node {node_id} artifact {artifact_path} conforms to {schema_path}")
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

    # Minimum size check for JSON
    min_size = 200
    if len(raw) < min_size:
        print(f"FAIL: artifact too thin ({len(raw)} bytes, minimum is {min_size})")
        sys.exit(1)

    print(f"PASS: node {node_id} artifact {artifact_path} conforms to {schema_path}")
    sys.exit(0)

if __name__ == "__main__":
    main()
