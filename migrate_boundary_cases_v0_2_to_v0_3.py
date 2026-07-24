#!/usr/bin/env python3
"""Create boundary-cases-011-020.v0.3.json from the native v0.2 stratum.

The v0.2 dataset is never overwritten. New semantic fields are populated only
from TARGETED_DEEPENING_PATCHES_V0.3.json; all other records receive explicit
unassessed/default structures.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any


TARGET_IDS = {"BC-015", "BC-017", "BC-018", "BC-019", "BC-020"}


def default_distributed_relation() -> dict[str, Any]:
    return {
        "status": "unknown",
        "topology": "unknown",
        "physical_site_relation": "Not assessed in Sprint 6 targeted deepening.",
        "shared_computational_state": "unknown",
        "synchronization_mechanism": "Not assessed.",
        "latency_governance": "Not assessed.",
        "calibration_equivalence": "Not assessed.",
        "officiation_relation": "Not assessed.",
        "safety_relation": "Not assessed.",
        "evidence_refs": [],
        "uncertainty": "The field is structurally present but was outside the targeted Sprint 6 review.",
        "review_status": "review_required",
    }


def migrate_dataset(
    source: dict[str, Any], patch_document: dict[str, Any]
) -> dict[str, Any]:
    result = copy.deepcopy(source)
    result["dataset"] = "AltisSports Boundary Cases BC-011-020 v0.3"
    result["schema"] = "BOUNDARY_CASE_SCHEMA_V0.3.json"
    result["schema_version"] = "0.3"
    result["source_dataset"] = "boundary-cases-011-020.v0.2.json"
    result["source_schema_version"] = "0.2"
    result["sprint"] = "Sprint 6 — Targeted Boundary Deepening and Schema v0.3 Decision"
    result["status"] = "targeted_human_reviewed_derivative"
    result["access_date"] = patch_document.get("access_date", result.get("access_date"))

    patches = patch_document.get("cases", {})
    seen: set[str] = set()

    for case in result["cases"]:
        case_id = case["case_id"]
        case["schema_version"] = "0.3"
        case.setdefault("agency_segments", [])
        case.setdefault("distributed_arena_relation", default_distributed_relation())
        case.setdefault("participatory_actor_relations", [])
        case.setdefault("intentional_biological_control", None)

        profile = case.get("operational_spatial_integration_profile", {})
        if isinstance(profile, dict):
            profile["profile_status"] = "carried_forward_v0_3"
            for function in profile.get("functions", []):
                if isinstance(function, dict):
                    function["review_status"] = "carried_forward_v0_3"

        case["revision"] = {
            "version": "0.3",
            "notes": (
                "Derived from native v0.2. Sprint 6 adds targeted structures for "
                "agency segmentation, distributed arenas, participatory actors, "
                "and intentional biological control without rewriting v0.2."
            ),
        }

        if case_id in patches:
            patch = patches[case_id]
            seen.add(case_id)
            for evidence in patch.get("append_evidence", []):
                case.setdefault("evidence", []).append(evidence)
            for field in (
                "agency_segments",
                "distributed_arena_relation",
                "participatory_actor_relations",
                "intentional_biological_control",
            ):
                if field in patch:
                    case[field] = copy.deepcopy(patch[field])

            if case_id == "BC-018":
                interface_types = case["performance_interface"].setdefault("interface_types", [])
                if "intentional_biological_control" not in interface_types:
                    interface_types.append("intentional_biological_control")
                demand_types = case["embodied_performance"].setdefault("demand_types", [])
                if "intentional_biosignal_control" not in demand_types:
                    demand_types.append("intentional_biosignal_control")

            case["migration"] = {
                "source_schema_version": "0.2",
                "migration_script_version": "1.0.0",
                "review_status": "human_reviewed_v0_3",
                "notes": (
                    "v0.2 record carried forward and targeted Sprint 6 fields "
                    "were human-authored from the cited evidence."
                ),
            }
        else:
            case["migration"] = {
                "source_schema_version": "0.2",
                "migration_script_version": "1.0.0",
                "review_status": "structural_migration_reviewed",
                "notes": (
                    "v0.2 semantics carried forward. New v0.3 fields remain empty "
                    "or explicitly unassessed because the case was outside Sprint 6 scope."
                ),
            }

    missing = TARGET_IDS - seen
    unexpected = seen - TARGET_IDS
    if missing:
        raise ValueError(f"Missing targeted patches: {sorted(missing)}")
    if unexpected:
        raise ValueError(f"Unexpected targeted patches: {sorted(unexpected)}")

    result["case_count"] = len(result["cases"])
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="boundary-cases-011-020.v0.2.json")
    parser.add_argument("--patches", default="TARGETED_DEEPENING_PATCHES_V0.3.json")
    parser.add_argument("--output", default="boundary-cases-011-020.v0.3.json")
    args = parser.parse_args()

    source_path = Path(args.source)
    patch_path = Path(args.patches)
    output_path = Path(args.output)

    for path in (source_path, patch_path):
        if not path.exists():
            print(f"ERROR: file not found: {path}")
            return 2

    try:
        source = json.loads(source_path.read_text(encoding="utf-8"))
        patches = json.loads(patch_path.read_text(encoding="utf-8"))
        result = migrate_dataset(source, patches)
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        print(f"ERROR: migration failed: {exc}")
        return 2

    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"PASS: wrote {output_path} with {result['case_count']} cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
