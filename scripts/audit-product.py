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


def parse_prereqs(value: str) -> list[str]:
    value = value.strip()
    if value in {"—", "none", "[none]", "[]"}:
        return []
    value = value.strip("[]")
    return [part.strip() for part in value.split(",") if part.strip()]


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
        else:
            text = skill.read_text(encoding="utf-8", errors="replace")
            header = "\n".join(text.splitlines()[:6])
            prereq_match = re.search(r"Prereqs:\s*([^\n]+?)\s+Parallel with:", header)
            input_match = re.search(r"Input:\s*([^\n]+?)\s+Output:", header)
            output_match = re.search(r"Output:\s*([^\n]+?)\s+Model:", header)
            model_match = re.search(r"Model:\s*([^\s]+)", header)
            budget_match = re.search(r"Budget:\s*(\d+)", header)
            expected_prereqs = node.get("prereqs", [])
            if prereq_match and parse_prereqs(prereq_match.group(1)) != expected_prereqs:
                errors.append(
                    f"node {nid}: skill header prereqs {parse_prereqs(prereq_match.group(1))!r} "
                    f"!= tree {expected_prereqs!r}"
                )
            if input_match and input_match.group(1).strip() != node.get("input", "").strip():
                errors.append(
                    f"node {nid}: skill header input {input_match.group(1).strip()!r} "
                    f"!= tree {node.get('input', '').strip()!r}"
                )
            if output_match and output_match.group(1).strip() != node.get("output", "").strip():
                errors.append(
                    f"node {nid}: skill header output {output_match.group(1).strip()!r} "
                    f"!= tree {node.get('output', '').strip()!r}"
                )
            if model_match and model_match.group(1).strip() != node.get("model"):
                errors.append(
                    f"node {nid}: skill header model {model_match.group(1).strip()!r} "
                    f"!= tree {node.get('model')!r}"
                )
            if budget_match and int(budget_match.group(1)) != int(node.get("max_response_tokens", 0)):
                errors.append(
                    f"node {nid}: skill header budget {budget_match.group(1)} "
                    f"!= tree {node.get('max_response_tokens')}"
                )

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

    # JSON-producing nodes require real JSON Schema constraints, not text-only heading metadata.
    for node in nodes:
        artifact = node.get("expected_artifact_path", "")
        if not artifact.endswith(".json"):
            continue
        schema_path = ROOT / node["artifact_schema"]
        if not schema_path.is_file():
            continue
        schema = load_json(schema_path)
        required = schema.get("required")
        if not isinstance(required, list) or not required:
            errors.append(
                f"node {node['id']}: JSON artifact {artifact} is bound to "
                f"{node['artifact_schema']} without non-empty JSON Schema required fields"
            )

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

        def scan_cardinality(value, path=""):
            if isinstance(value, dict):
                if isinstance(value.get("minItems"), int) and value["minItems"] > 1:
                    warnings.append(f"{title}: review minItems={value['minItems']} at {path or '<root>'}")
                if isinstance(value.get("minProperties"), int) and value["minProperties"] > 3:
                    warnings.append(f"{title}: review minProperties={value['minProperties']} at {path or '<root>'}")
                for key, child in value.items():
                    scan_cardinality(child, f"{path}.{key}" if path else key)
            elif isinstance(value, list):
                for index, child in enumerate(value):
                    scan_cardinality(child, f"{path}[{index}]")
        scan_cardinality(schema)

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
