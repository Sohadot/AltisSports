#!/usr/bin/env python3
"""Validate an AltisSports boundary-case dataset with no third-party packages.

This validator implements the JSON Schema features used by
BOUNDARY_CASE_SCHEMA_V0.2.json and adds cross-record integrity checks.
It is intentionally narrow and deterministic; it is not a general-purpose
replacement for a complete JSON Schema implementation.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

FORBIDDEN_KEYS = {
    "total_score",
    "spatiality_score",
    "spatiality_level",
    "maturity_level",
    "certification_status",
}


def _type_matches(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "null":
        return value is None
    return False


def _resolve_ref(root_schema: dict[str, Any], ref: str) -> dict[str, Any]:
    if not ref.startswith("#/"):
        raise ValueError(f"Only internal references are supported: {ref}")
    node: Any = root_schema
    for part in ref[2:].split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        node = node[part]
    if not isinstance(node, dict):
        raise ValueError(f"Reference does not resolve to an object schema: {ref}")
    return node


def _validate_format(value: Any, fmt: str, path: str, errors: list[str]) -> None:
    if fmt == "date" and isinstance(value, str):
        try:
            date.fromisoformat(value)
        except ValueError:
            errors.append(f"{path}: expected ISO date YYYY-MM-DD, got {value!r}")


def validate_node(
    value: Any,
    schema: dict[str, Any],
    root_schema: dict[str, Any],
    path: str,
    errors: list[str],
) -> None:
    if "$ref" in schema:
        validate_node(value, _resolve_ref(root_schema, schema["$ref"]), root_schema, path, errors)
        return

    if "allOf" in schema:
        for index, sub in enumerate(schema["allOf"]):
            validate_node(value, sub, root_schema, f"{path}.allOf[{index}]", errors)

    expected = schema.get("type")
    if expected is not None:
        expected_types = expected if isinstance(expected, list) else [expected]
        if not any(_type_matches(value, item) for item in expected_types):
            errors.append(f"{path}: expected type {expected_types}, got {type(value).__name__}")
            return

    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: expected constant {schema['const']!r}, got {value!r}")

    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: value {value!r} is not in allowed enum")

    if isinstance(value, str):
        if "minLength" in schema and len(value) < schema["minLength"]:
            errors.append(f"{path}: string shorter than minLength {schema['minLength']}")
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append(f"{path}: value {value!r} does not match {schema['pattern']!r}")
        if "format" in schema:
            _validate_format(value, schema["format"], path, errors)

    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            errors.append(f"{path}: array has {len(value)} items; minimum is {schema['minItems']}")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(value):
                validate_node(item, item_schema, root_schema, f"{path}[{index}]", errors)

    if isinstance(value, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in value:
                errors.append(f"{path}: missing required property {key!r}")

        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in properties:
                    errors.append(f"{path}: unexpected property {key!r}")

        for key, sub_schema in properties.items():
            if key in value:
                validate_node(value[key], sub_schema, root_schema, f"{path}.{key}", errors)


def _walk_forbidden_keys(value: Any, path: str, errors: list[str]) -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            if key in FORBIDDEN_KEYS:
                errors.append(f"{path}: prohibited scoring/certification key {key!r}")
            _walk_forbidden_keys(item, f"{path}.{key}", errors)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _walk_forbidden_keys(item, f"{path}[{index}]", errors)


def validate_dataset(dataset: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    required_top = {
        "dataset",
        "schema",
        "schema_version",
        "source_dataset",
        "source_schema_version",
        "sprint",
        "status",
        "license",
        "case_count",
        "cases",
    }
    missing = sorted(required_top - set(dataset))
    for key in missing:
        errors.append(f"$: missing dataset property {key!r}")

    if dataset.get("schema") != "BOUNDARY_CASE_SCHEMA_V0.2.json":
        errors.append("$: schema must be BOUNDARY_CASE_SCHEMA_V0.2.json")
    if dataset.get("schema_version") != "0.2":
        errors.append("$: schema_version must be 0.2")
    if dataset.get("source_schema_version") != "0.1":
        errors.append("$: source_schema_version must be 0.1")

    license_obj = dataset.get("license")
    if not isinstance(license_obj, dict) or license_obj.get("identifier") != "CC-BY-4.0":
        errors.append("$: license.identifier must be CC-BY-4.0")

    cases = dataset.get("cases")
    if not isinstance(cases, list):
        errors.append("$: cases must be an array")
        return errors

    if dataset.get("case_count") != len(cases):
        errors.append(
            f"$: case_count {dataset.get('case_count')!r} does not match {len(cases)} records"
        )

    seen_ids: set[str] = set()
    for index, case in enumerate(cases):
        case_path = f"$.cases[{index}]"
        validate_node(case, schema, schema, case_path, errors)
        if not isinstance(case, dict):
            continue

        case_id = case.get("case_id")
        if case_id in seen_ids:
            errors.append(f"{case_path}: duplicate case_id {case_id!r}")
        if isinstance(case_id, str):
            seen_ids.add(case_id)

        evidence = case.get("evidence", [])
        profile = case.get("operational_spatial_integration_profile", {})
        functions = profile.get("functions", []) if isinstance(profile, dict) else []
        for f_index, function in enumerate(functions):
            refs = function.get("evidence_refs", []) if isinstance(function, dict) else []
            for ref in refs:
                if ref < 0 or ref >= len(evidence):
                    errors.append(
                        f"{case_path}.operational_spatial_integration_profile.functions"
                        f"[{f_index}].evidence_refs: index {ref} out of range"
                    )

        migration = case.get("migration", {})
        profile_status = profile.get("profile_status") if isinstance(profile, dict) else None
        if migration.get("review_status") == "automated_review_required":
            if profile_status != "migrated_provisional":
                errors.append(
                    f"{case_path}: automated migration must retain "
                    "operational profile_status migrated_provisional"
                )

        _walk_forbidden_keys(case, case_path, errors)

    expected_ids = [f"BC-{number:03d}" for number in range(1, 11)]
    if sorted(seen_ids) != expected_ids:
        errors.append(
            "$: BC-001–BC-010 dataset must contain exactly the ten expected case identifiers"
        )

    return errors


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--schema", default="BOUNDARY_CASE_SCHEMA_V0.2.json")
    parser.add_argument("--data", default="boundary-cases-001-010.v0.2.json")
    args = parser.parse_args()

    schema_path = Path(args.schema)
    data_path = Path(args.data)
    for path in (schema_path, data_path):
        if not path.exists():
            print(f"ERROR: file not found: {path}", file=sys.stderr)
            return 2

    try:
        schema = load_json(schema_path)
        dataset = load_json(data_path)
        errors = validate_dataset(dataset, schema)
    except (OSError, json.JSONDecodeError, ValueError, KeyError) as exc:
        print(f"ERROR: validation could not run: {exc}", file=sys.stderr)
        return 2

    if errors:
        print(f"FAIL: {len(errors)} validation error(s)")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"PASS: {dataset['case_count']} cases validate against "
        f"{schema_path.name}; cross-record checks passed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
