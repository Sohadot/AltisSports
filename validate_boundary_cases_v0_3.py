#!/usr/bin/env python3
"""Validate the AltisSports BC-011–BC-020 v0.3 derivative.

Uses the deterministic schema-node validator already checked into the
repository, then adds Sprint 6 cross-record and targeted-deepening checks.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from validate_boundary_cases import _walk_forbidden_keys, load_json, validate_node


def _validate_refs(
    refs: Any, evidence_count: int, path: str, errors: list[str]
) -> None:
    if not isinstance(refs, list):
        return
    for ref in refs:
        if not isinstance(ref, int) or isinstance(ref, bool):
            errors.append(f"{path}: evidence reference must be an integer")
        elif ref < 0 or ref >= evidence_count:
            errors.append(f"{path}: evidence index {ref} out of range")


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
        "access_date",
        "case_count",
        "cases",
    }
    for key in sorted(required_top - set(dataset)):
        errors.append(f"$: missing dataset property {key!r}")

    if dataset.get("schema") != "BOUNDARY_CASE_SCHEMA_V0.3.json":
        errors.append("$: schema must be BOUNDARY_CASE_SCHEMA_V0.3.json")
    if dataset.get("schema_version") != "0.3":
        errors.append("$: schema_version must be 0.3")
    if dataset.get("source_schema_version") != "0.2":
        errors.append("$: source_schema_version must be 0.2")
    if dataset.get("source_dataset") != "boundary-cases-011-020.v0.2.json":
        errors.append("$: source_dataset must identify the native v0.2 stratum")

    license_obj = dataset.get("license")
    if not isinstance(license_obj, dict) or license_obj.get("identifier") != "CC-BY-4.0":
        errors.append("$: license.identifier must remain CC-BY-4.0")

    cases = dataset.get("cases")
    if not isinstance(cases, list):
        errors.append("$: cases must be an array")
        return errors
    if dataset.get("case_count") != len(cases):
        errors.append("$: case_count does not match records")

    seen: set[str] = set()
    by_id: dict[str, dict[str, Any]] = {}

    for index, case in enumerate(cases):
        path = f"$.cases[{index}]"
        validate_node(case, schema, schema, path, errors)
        if not isinstance(case, dict):
            continue

        case_id = case.get("case_id")
        if isinstance(case_id, str):
            if case_id in seen:
                errors.append(f"{path}: duplicate case_id {case_id}")
            seen.add(case_id)
            by_id[case_id] = case

        evidence = case.get("evidence", [])
        evidence_count = len(evidence) if isinstance(evidence, list) else 0

        profile = case.get("operational_spatial_integration_profile", {})
        if isinstance(profile, dict):
            for i, function in enumerate(profile.get("functions", [])):
                if isinstance(function, dict):
                    _validate_refs(
                        function.get("evidence_refs"),
                        evidence_count,
                        f"{path}.operational_spatial_integration_profile.functions[{i}].evidence_refs",
                        errors,
                    )

        for i, segment in enumerate(case.get("agency_segments", [])):
            if isinstance(segment, dict):
                _validate_refs(
                    segment.get("evidence_refs"),
                    evidence_count,
                    f"{path}.agency_segments[{i}].evidence_refs",
                    errors,
                )

        relation = case.get("distributed_arena_relation")
        if isinstance(relation, dict):
            _validate_refs(
                relation.get("evidence_refs"),
                evidence_count,
                f"{path}.distributed_arena_relation.evidence_refs",
                errors,
            )

        for i, relation_item in enumerate(case.get("participatory_actor_relations", [])):
            if isinstance(relation_item, dict):
                _validate_refs(
                    relation_item.get("evidence_refs"),
                    evidence_count,
                    f"{path}.participatory_actor_relations[{i}].evidence_refs",
                    errors,
                )

        biological = case.get("intentional_biological_control")
        if isinstance(biological, dict):
            _validate_refs(
                biological.get("evidence_refs"),
                evidence_count,
                f"{path}.intentional_biological_control.evidence_refs",
                errors,
            )

        _walk_forbidden_keys(case, path, errors)

    expected = {f"BC-{number:03d}" for number in range(11, 21)}
    if seen != expected:
        errors.append(f"$: expected exactly BC-011–BC-020, got {sorted(seen)}")

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    bc15 = by_id.get("BC-015", {})
    dar15 = bc15.get("distributed_arena_relation", {})
    require(
        isinstance(dar15, dict) and dar15.get("status") == "not_evidenced",
        "BC-015: remote-distributed relation must remain not_evidenced",
    )
    require(
        isinstance(dar15, dict) and dar15.get("topology") == "co_located_multi_station",
        "BC-015: examined topology must be co_located_multi_station",
    )

    for case_id in ("BC-017", "BC-019"):
        segments = by_id.get(case_id, {}).get("agency_segments", [])
        require(
            isinstance(segments, list) and len(segments) >= 3,
            f"{case_id}: at least three phase/regime agency segments required",
        )

    bc18 = by_id.get("BC-018", {})
    biological = bc18.get("intentional_biological_control")
    require(
        isinstance(biological, dict) and biological.get("status") == "supported",
        "BC-018: intentional biological control profile must be supported",
    )
    require(
        isinstance(biological, dict)
        and biological.get("athletic_embodiment_relation") == "unresolved",
        "BC-018: athletic embodiment relation must remain unresolved",
    )

    bc20 = by_id.get("BC-020", {})
    actors = bc20.get("participatory_actor_relations", [])
    require(
        isinstance(actors, list) and len(actors) >= 1,
        "BC-020: participatory actor relation required",
    )
    if isinstance(actors, list) and actors:
        require(
            actors[0].get("performance_agency_relation") == "indirect_no_execution",
            "BC-020: spectator relation must not become direct Performance Agency",
        )

    for case_id, case in by_id.items():
        migration = case.get("migration", {})
        expected_review = (
            "human_reviewed_v0_3"
            if case_id in {"BC-015", "BC-017", "BC-018", "BC-019", "BC-020"}
            else "structural_migration_reviewed"
        )
        require(
            isinstance(migration, dict)
            and migration.get("review_status") == expected_review,
            f"{case_id}: incorrect migration review status",
        )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--schema", default="BOUNDARY_CASE_SCHEMA_V0.3.json")
    parser.add_argument("--data", default="boundary-cases-011-020.v0.3.json")
    args = parser.parse_args()

    try:
        schema = load_json(Path(args.schema))
        dataset = load_json(Path(args.data))
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
        "PASS: 10 v0.3 derivative cases validate; targeted agency, arena, "
        "biological-control, and participatory-actor checks passed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
