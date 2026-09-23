#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

from vibe_code_genius.validation import validate_artifact_file


def main():
    parser = argparse.ArgumentParser(description="Validate build artifacts against schemas.")
    parser.add_argument("--node", default=None, help="Node ID (e.g. 01, 07g)")
    parser.add_argument("--artifact", default=None, help="Path to the declared artifact")
    parser.add_argument("--schema", default=None, help="Path to the schema file")
    parser.add_argument("positional", nargs="*", help="Positional fallback: <artifact> <schema>")
    args = parser.parse_args()

    node_id = args.node or "unknown"
    artifact_str = args.artifact or (args.positional[0] if len(args.positional) >= 1 else None)
    schema_str = args.schema or (args.positional[1] if len(args.positional) >= 2 else None)

    if not artifact_str or not schema_str:
        print("Usage: scripts/validate-artifact.py --node <id> --artifact <declared_path> --schema <schema_path>")
        return 1

    artifact_path = Path(artifact_str)
    if not artifact_path.exists():
        for prefix in (Path("first-build"), Path("verify")):
            candidate = prefix / artifact_str
            if candidate.exists():
                artifact_path = candidate
                break

    errors = validate_artifact_file(artifact_path, Path(schema_str))
    if errors:
        print(f"FAIL: node {node_id} artifact {artifact_path} does not conform to {schema_str}:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"PASS: node {node_id} artifact {artifact_path} conforms to {schema_str}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
