#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise RuntimeError(f"{path.relative_to(ROOT)}: invalid JSON: {exc}") from exc


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    tree = load_json(ROOT / "skill-tree.json")
    nodes = tree.get("nodes", [])
    ids = {n.get("id") for n in nodes}

    if tree.get("node_count") != len(nodes):
        errors.append(f"skill-tree node_count={tree.get('node_count')} but contains {len(nodes)} nodes")

    # Validate every node object against the node schema.
    node_schema = load_json(ROOT / "schema" / "node.schema.json")
    node_validator = Draft202012Validator(node_schema)
    for node in nodes:
        for err in node_validator.iter_errors(node):
            where = "/".join(str(p) for p in err.absolute_path)
            errors.append(f"node {node.get('id')}: node schema: {err.message} ({where})")

    # Validate graph references and output ownership.
    owned: dict[str, list[str]] = {}
    for node in nodes:
        nid = node["id"]
        for key in ("prereqs", "parallel_with", "consumers"):
            for other in node.get(key, []):
                if other not in ids:
                    errors.append(f"node {nid}: {key} references unknown node {other}")

        skill = ROOT / node["skill_file"]
        if not skill.is_file():
            errors.append(f"node {nid}: missing skill file {node['skill_file']}")

        schema_rel = node.get("artifact_schema")
        if not schema_rel:
            errors.append(f"node {nid}: missing artifact_schema")
        elif not (ROOT / schema_rel).is_file():
            errors.append(f"node {nid}: missing artifact schema file {schema_rel}")

        output = node.get("expected_artifact_path")
        if not output:
            errors.append(f"node {nid}: missing expected_artifact_path")
        else:
            owned.setdefault(output, []).append(nid)

    for path, owners in sorted(owned.items()):
        required_owners = [n for n in nodes if n["id"] in owners and not n.get("optional", False)]
        if len(required_owners) > 1:
            errors.append(f"artifact {path} has multiple required producers: {', '.join(owners)}")

    # Artifact schemas must actually reject incomplete JSON artifacts.
    schema_dir = ROOT / "schema"
    for schema_path in sorted(schema_dir.glob("*.schema.json")):
        schema = load_json(schema_path)
        title = schema_path.name
        if schema.get("type") == "object":
            required = schema.get("required")
            headings = schema.get("required_headings")
            if required == []:
                errors.append(f"{title}: required is empty; schema is vacuous")
            if not required and not headings and title != "node.schema.json":
                errors.append(f"{title}: object schema has no required fields or required_headings")
            status = schema.get("properties", {}).get("status")
            if status and status.get("type") == "string" and "enum" not in status:
                warnings.append(f"{title}: status is unconstrained")

    # Source-of-truth docs must not advertise stale node counts.
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    stale_patterns = [
        r"\b61 node files\b",
        r"\breal 61-node\b",
    ]
    for pat in stale_patterns:
        if re.search(pat, readme, flags=re.I):
            errors.append(f"README.md contains stale node-count wording matching {pat!r}")

    # A product-complete tree must include core CI gates.
    validate = (ROOT / ".github" / "workflows" / "validate.yml").read_text(encoding="utf-8")
    for required_cmd in (
        "python scripts/validate-tree.py",
        "python scripts/validate-structure.py",
        "python scripts/audit-product.py",
        "python scripts/validate-references.py",
    ):
        if required_cmd not in validate:
            errors.append(f"validate workflow missing: {required_cmd}")

    print(f"product audit: {len(nodes)} nodes, {len(list(schema_dir.glob('*.schema.json')))} schemas")
    for warning in warnings:
        print("WARN:", warning)
    if errors:
        print("PRODUCT AUDIT FAILED")
        for err in errors:
            print("-", err)
        return 1
    print("PRODUCT AUDIT PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
