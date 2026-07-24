#!/usr/bin/env python3
"""Validate the reviewed 20-case v0.3 corpus and Sprint 7 application claims."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from validate_boundary_cases import _walk_forbidden_keys, load_json, validate_node


def validate_refs(refs: Any, evidence_count: int, path: str, errors: list[str]) -> None:
    if not isinstance(refs, list):
        errors.append(f"{path}: evidence_refs must be an array")
        return
    for ref in refs:
        if not isinstance(ref, int) or isinstance(ref, bool):
            errors.append(f"{path}: evidence reference must be an integer")
        elif ref < 0 or ref >= evidence_count:
            errors.append(f"{path}: evidence index {ref} out of range")


def validate_case_relations(case: dict[str, Any], errors: list[str]) -> None:
    case_id = case.get("case_id", "<unknown>")
    base = f"{case_id}"
    evidence_count = len(case.get("evidence", []))

    if case.get("migration", {}).get("review_status") != "human_reviewed_v0_3":
        errors.append(f"{base}: migration review_status must be human_reviewed_v0_3")
    if case.get("operational_spatial_integration_profile", {}).get("profile_status") != "human_reviewed_v0_3":
        errors.append(f"{base}: profile_status must be human_reviewed_v0_3")

    for index, segment in enumerate(case.get("agency_segments", [])):
        if segment.get("review_status") != "human_reviewed_v0_3":
            errors.append(f"{base}.agency_segments[{index}]: not human reviewed")
        validate_refs(segment.get("evidence_refs"), evidence_count, f"{base}.agency_segments[{index}]", errors)

    relation = case.get("distributed_arena_relation", {})
    if relation.get("review_status") != "human_reviewed_v0_3":
        errors.append(f"{base}.distributed_arena_relation: not human reviewed")
    validate_refs(relation.get("evidence_refs"), evidence_count, f"{base}.distributed_arena_relation", errors)

    for index, actor in enumerate(case.get("participatory_actor_relations", [])):
        if actor.get("review_status") != "human_reviewed_v0_3":
            errors.append(f"{base}.participatory_actor_relations[{index}]: not human reviewed")
        validate_refs(actor.get("evidence_refs"), evidence_count, f"{base}.participatory_actor_relations[{index}]", errors)

    biological = case.get("intentional_biological_control")
    if isinstance(biological, dict):
        if biological.get("review_status") != "human_reviewed_v0_3":
            errors.append(f"{base}.intentional_biological_control: not human reviewed")
        validate_refs(biological.get("evidence_refs"), evidence_count, f"{base}.intentional_biological_control", errors)


def validate_dataset(dataset: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    cases = dataset.get("cases")
    if not isinstance(cases, list):
        return ["$: cases must be an array"]
    if dataset.get("schema") != "BOUNDARY_CASE_SCHEMA_V0.3.json":
        errors.append("$: wrong schema name")
    if dataset.get("schema_version") != "0.3":
        errors.append("$: schema_version must be 0.3")
    if dataset.get("case_count") != len(cases):
        errors.append("$: case_count mismatch")
    if dataset.get("license", {}).get("identifier") != "CC-BY-4.0":
        errors.append("$: license.identifier must be CC-BY-4.0")

    seen: set[str] = set()
    for index, case in enumerate(cases):
        path = f"$.cases[{index}]"
        validate_node(case, schema, schema, path, errors)
        if not isinstance(case, dict):
            continue
        case_id = case.get("case_id")
        if case_id in seen:
            errors.append(f"{path}: duplicate case_id {case_id}")
        if isinstance(case_id, str):
            seen.add(case_id)
        validate_case_relations(case, errors)
        _walk_forbidden_keys(case, path, errors)

    expected = {f"BC-{n:03d}" for n in range(1, 21)}
    if seen != expected:
        errors.append(f"$: expected BC-001–BC-020, got {sorted(seen)}")

    by_id = {case["case_id"]: case for case in cases if isinstance(case, dict) and "case_id" in case}

    if by_id["BC-005"]["distributed_arena_relation"]["topology"] != "remote_supervision_physical_arena":
        errors.append("BC-005: remote-control arena relation not applied")
    if by_id["BC-008"]["distributed_arena_relation"]["topology"] != "remote_synchronous":
        errors.append("BC-008: remote-synchronous arena relation not applied")
    bc10 = by_id["BC-010"]["agency_segments"]
    if len(bc10) < 2 or not any(s.get("primary_control") == "automated_system" for s in bc10):
        errors.append("BC-010: design-to-autonomous agency segmentation missing")
    if by_id["BC-013"]["distributed_arena_relation"]["topology"] != "remote_synchronous":
        errors.append("BC-013: v0.3 field not applied outside motivating cases")
    if by_id["BC-014"]["distributed_arena_relation"]["topology"] != "co_located_single_site":
        errors.append("BC-014: free-roam co-location relation missing")
    if not by_id["BC-016"]["participatory_actor_relations"]:
        errors.append("BC-016: supervisor relation missing")
    if by_id["BC-018"]["intentional_biological_control"] is None:
        errors.append("BC-018: intentional biological control lost")
    if by_id["BC-018"]["provisional_finding"]["category_relation"] != "unresolved":
        errors.append("BC-018: category uncertainty was improperly closed")
    if not by_id["BC-020"]["participatory_actor_relations"]:
        errors.append("BC-020: participatory actor relation lost")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--schema", default="BOUNDARY_CASE_SCHEMA_V0.3.json")
    parser.add_argument("--data", default="boundary-cases-001-020.v0.3.json")
    args = parser.parse_args()
    try:
        schema = load_json(Path(args.schema))
        dataset = load_json(Path(args.data))
        errors = validate_dataset(dataset, schema)
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        print(f"ERROR: validation could not run: {exc}", file=sys.stderr)
        return 2
    if errors:
        print(f"FAIL: {len(errors)} validation error(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: 20 human-reviewed v0.3 cases validate; corpus application and cross-case checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
