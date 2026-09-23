#!/usr/bin/env python3
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

root = Path(__file__).resolve().parents[1]
refs = root / "references"
index = json.loads((refs / "index.json").read_text(encoding="utf-8"))

schemas = {
    "fixture": json.loads((root / "schema" / "structure.schema.json").read_text(encoding="utf-8")),
    "scraped": json.loads((root / "schema" / "structure.schema.json").read_text(encoding="utf-8")),
    "external-code-reference": json.loads((root / "schema" / "external-code-reference.schema.json").read_text(encoding="utf-8")),
}

errors = []
counts = {key: 0 for key in schemas}

for entry in index.get("references", []):
    rel = entry["file"]
    path = refs / rel
    if not path.exists():
        errors.append(f"missing: {rel}")
        continue

    entry_type = entry.get("type")
    if entry_type not in schemas:
        errors.append(f"{rel}: unsupported reference type {entry_type!r}")
        continue

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{rel}: invalid JSON: {exc}")
        continue

    validator = Draft202012Validator(schemas[entry_type])
    errors.extend(
        f"{rel}: schema: {error.message}"
        for error in validator.iter_errors(data)
    )
    counts[entry_type] += 1

    acquirer = data.get("acquirer", entry.get("acquirer"))

    if entry_type == "fixture":
        if acquirer == "curated-reference-index":
            errors.append(f"{rel}: rejected authored fixture acquirer curated-reference-index")
        if entry.get("note") != "schema-valid example, not scraped":
            errors.append(f"{rel}: fixture note must be 'schema-valid example, not scraped'")
        continue

    if entry_type == "external-code-reference":
        if entry.get("acquirer") != "spa-ripper":
            errors.append(f"{rel}: external code reference must preserve its SPA-Ripper provenance")
        if data.get("acquisition", {}).get("tool") != "spa-ripper":
            errors.append(f"{rel}: pinned code reference acquisition.tool must be spa-ripper")
        if "historical-pinned" not in entry.get("tags", []):
            errors.append(f"{rel}: external code reference must be labeled historical-pinned")
        continue

    if acquirer == "curated-reference-index":
        errors.append(f"{rel}: rejected authored fixture acquirer curated-reference-index")
    if acquirer != "spa-ripper":
        errors.append(f"{rel}: scraped reference must have acquirer spa-ripper; got {acquirer!r}")

    routes = data.get("routes") or []
    sections = data.get("sections") or {}
    design_tokens = data.get("design_tokens") or {}
    if len(routes) < 5:
        errors.append(f"{rel}: routes.length={len(routes)}; scraped references require at least 5 routes")
    if not sections:
        errors.append(f"{rel}: sections is empty")
    if not design_tokens:
        errors.append(f"{rel}: design_tokens is empty")

if errors:
    print("REFERENCES INVALID")
    print("\n".join(errors))
    sys.exit(1)

print(
    "REFERENCES VALID: "
    + ", ".join(f"{count} {kind}" for kind, count in counts.items())
)
