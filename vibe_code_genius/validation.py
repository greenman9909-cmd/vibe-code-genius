from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


TEXT_SUFFIXES = {".md", ".ts", ".tsx", ".js", ".jsx", ".css", ".html", ".yaml", ".yml"}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_artifact_file(artifact_path: Path, schema_path: Path) -> list[str]:
    errors: list[str] = []

    if not artifact_path.exists():
        return [f"missing artifact: {artifact_path}"]
    if not schema_path.exists():
        return [f"missing schema: {schema_path}"]
    if schema_path.name == "node.schema.json":
        return ["node.schema.json is metadata schema, not an artifact schema"]

    try:
        raw = artifact_path.read_text(encoding="utf-8")
    except Exception as exc:
        return [f"could not read artifact: {exc}"]

    try:
        schema = load_json(schema_path)
    except Exception as exc:
        return [f"invalid schema JSON: {exc}"]

    suffix = artifact_path.suffix.lower()
    if suffix in TEXT_SUFFIXES:
        if not raw.strip():
            errors.append("artifact is empty")

        required_snippets = schema.get("required_headings") or schema.get("x-required-snippets") or []
        for snippet in required_snippets:
            if snippet not in raw:
                errors.append(f"missing required text/snippet: {snippet}")

        min_bytes = schema.get("x-min-bytes")
        if isinstance(min_bytes, int) and len(raw.encode("utf-8")) < min_bytes:
            errors.append(f"artifact too thin: {len(raw.encode('utf-8'))} bytes < {min_bytes}")

        forbidden = schema.get("x-forbidden-snippets") or []
        for snippet in forbidden:
            if snippet in raw:
                errors.append(f"forbidden placeholder/snippet present: {snippet}")

        return errors

    try:
        data = json.loads(raw)
    except Exception as exc:
        return [f"invalid JSON: {exc}"]

    for err in Draft202012Validator(schema).iter_errors(data):
        where = "/".join(str(p) for p in err.absolute_path)
        errors.append(f"{err.message}" + (f" at {where}" if where else ""))

    return errors
