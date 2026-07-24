#!/usr/bin/env python3
"""Validate native v0.2 BC-011–BC-020 records against the repository schema."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from typing import Any

from validate_boundary_cases import validate_node, _walk_forbidden_keys, load_json


def validate_native_dataset(dataset: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required_top = {"dataset","schema","schema_version","source_dataset","source_schema_version","sprint","status","license","case_count","cases"}
    for key in sorted(required_top - set(dataset)):
        errors.append(f"$: missing dataset property {key!r}")
    if dataset.get("schema") != "BOUNDARY_CASE_SCHEMA_V0.2.json":
        errors.append("$: schema must be BOUNDARY_CASE_SCHEMA_V0.2.json")
    if dataset.get("schema_version") != "0.2":
        errors.append("$: schema_version must be 0.2")
    if dataset.get("source_schema_version") != "native":
        errors.append("$: source_schema_version must be native")
    license_obj = dataset.get("license")
    if not isinstance(license_obj, dict) or license_obj.get("identifier") != "CC-BY-4.0":
        errors.append("$: license.identifier must be CC-BY-4.0")
    cases = dataset.get("cases")
    if not isinstance(cases, list):
        return errors + ["$: cases must be an array"]
    if dataset.get("case_count") != len(cases):
        errors.append(f"$: case_count does not match {len(cases)} records")
    seen: set[str] = set()
    for index, record in enumerate(cases):
        path = f"$.cases[{index}]"
        validate_node(record, schema, schema, path, errors)
        if not isinstance(record, dict):
            continue
        cid = record.get("case_id")
        if cid in seen:
            errors.append(f"{path}: duplicate case_id {cid!r}")
        if isinstance(cid, str):
            seen.add(cid)
        evidence = record.get("evidence", [])
        if not isinstance(evidence, list) or len(evidence) < 2:
            errors.append(f"{path}: native second-stratum case requires at least two evidence records")
        profile = record.get("operational_spatial_integration_profile", {})
        if isinstance(profile, dict):
            if profile.get("profile_status") != "native_v0_2":
                errors.append(f"{path}: profile_status must be native_v0_2")
            for f_index, function in enumerate(profile.get("functions", [])):
                for ref in function.get("evidence_refs", []):
                    if not isinstance(ref, int) or ref < 0 or ref >= len(evidence):
                        errors.append(f"{path}.functions[{f_index}]: evidence ref {ref!r} out of range")
        migration = record.get("migration", {})
        if migration.get("source_schema_version") != "native" or migration.get("review_status") != "native_v0_2":
            errors.append(f"{path}: migration must identify a native v0.2 record")
        if record.get("performance_agency", {}).get("migration_review_required") is not False:
            errors.append(f"{path}: native performance_agency must not require migration review")
        _walk_forbidden_keys(record, path, errors)
    expected = {f"BC-{n:03d}" for n in range(11, 21)}
    if seen != expected:
        errors.append("$: dataset must contain exactly BC-011–BC-020")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--schema', default='BOUNDARY_CASE_SCHEMA_V0.2.json')
    parser.add_argument('--data', default='boundary-cases-011-020.v0.2.json')
    args = parser.parse_args()
    try:
        schema = load_json(Path(args.schema))
        dataset = load_json(Path(args.data))
        errors = validate_native_dataset(dataset, schema)
    except (OSError, json.JSONDecodeError, ValueError, KeyError) as exc:
        print(f"ERROR: validation could not run: {exc}", file=sys.stderr)
        return 2
    if errors:
        print(f"FAIL: {len(errors)} validation error(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS: {dataset['case_count']} native v0.2 cases validate; BC-011–BC-020 integrity checks passed.")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
