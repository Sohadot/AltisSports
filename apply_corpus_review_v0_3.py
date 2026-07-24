#!/usr/bin/env python3
"""Apply human-reviewed v0.3 corpus patches without overwriting source datasets."""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def apply_common_review(case: dict[str, Any], patch: dict[str, Any], source_version: str) -> None:
    case["schema_version"] = "0.3"

    performance = case["performance_agency"]
    for key in ("performance_window", "agency_modes", "human_skill_causally_necessary"):
        if key in patch:
            performance[key] = copy.deepcopy(patch[key])
    if "migration_review_required" in performance:
        performance["migration_review_required"] = False

    for field in (
        "agency_segments",
        "distributed_arena_relation",
        "participatory_actor_relations",
        "intentional_biological_control",
    ):
        if field not in patch:
            raise ValueError(f"{case['case_id']}: patch missing {field}")
        case[field] = copy.deepcopy(patch[field])

    profile = case["operational_spatial_integration_profile"]
    profile["profile_status"] = "human_reviewed_v0_3"
    for function in profile.get("functions", []):
        function["review_status"] = "human_reviewed_v0_3"

    case["revision"] = {
        "version": "0.3",
        "notes": (
            "Sprint 7 human review applied schema v0.3 across the case. "
            "Earlier datasets remain unchanged."
        ),
    }
    case["migration"] = {
        "source_schema_version": source_version,
        "migration_script_version": "1.0.0",
        "review_status": "human_reviewed_v0_3",
        "notes": (
            "Human-reviewed v0.3 derivative. Core case findings were checked "
            "against the existing human narrative; v0.3 relation fields were "
            "authored explicitly rather than inferred as scores."
        ),
    }


def review_first(source: dict[str, Any], patches: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(source)
    result.update({
        "dataset": "AltisSports Boundary Cases BC-001-010 reviewed v0.3",
        "schema": "BOUNDARY_CASE_SCHEMA_V0.3.json",
        "schema_version": "0.3",
        "source_dataset": "boundary-cases-001-010.v0.2.json",
        "source_schema_version": "0.2",
        "sprint": "Sprint 7 — v0.3 Corpus Application and Standardization-Readiness Gate",
        "status": "human_reviewed_v0_3",
        "access_date": patches.get("access_date", result.get("access_date")),
    })
    patch_cases = patches["cases"]
    seen: set[str] = set()
    for case in result["cases"]:
        case_id = case["case_id"]
        if case_id not in patch_cases:
            raise ValueError(f"First stratum missing patch for {case_id}")
        apply_common_review(case, patch_cases[case_id], "0.2")
        seen.add(case_id)
    expected = {f"BC-{n:03d}" for n in range(1, 11)}
    if seen != expected:
        raise ValueError(f"First stratum IDs mismatch: {sorted(seen)}")
    result["case_count"] = len(result["cases"])
    return result


def review_second(source: dict[str, Any], patches: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(source)
    result.update({
        "dataset": "AltisSports Boundary Cases BC-011-020 reviewed v0.3",
        "schema": "BOUNDARY_CASE_SCHEMA_V0.3.json",
        "schema_version": "0.3",
        "source_dataset": "boundary-cases-011-020.v0.3.json",
        "source_schema_version": "0.3",
        "sprint": "Sprint 7 — v0.3 Corpus Application and Standardization-Readiness Gate",
        "status": "fully_human_reviewed_v0_3",
        "access_date": patches.get("access_date", result.get("access_date")),
    })
    patch_cases = patches["cases"]
    seen: set[str] = set()
    for case in result["cases"]:
        case_id = case["case_id"]
        if case_id in patch_cases:
            apply_common_review(case, patch_cases[case_id], "0.2")
            seen.add(case_id)
        else:
            # Motivating Sprint 6 cases already contain human-authored v0.3 fields.
            case["schema_version"] = "0.3"
            profile = case["operational_spatial_integration_profile"]
            profile["profile_status"] = "human_reviewed_v0_3"
            for function in profile.get("functions", []):
                function["review_status"] = "human_reviewed_v0_3"
            case["revision"] = {
                "version": "0.3",
                "notes": (
                    "Sprint 6 targeted v0.3 relations retained and rechecked "
                    "during Sprint 7 corpus application."
                ),
            }
            case["migration"]["review_status"] = "human_reviewed_v0_3"
            case["migration"]["notes"] = (
                "Targeted Sprint 6 fields and carried-forward v0.2 semantics "
                "were rechecked in the Sprint 7 corpus application."
            )
    expected_patched = {"BC-011", "BC-012", "BC-013", "BC-014", "BC-016"}
    if seen != expected_patched:
        raise ValueError(f"Second stratum application IDs mismatch: {sorted(seen)}")
    result["case_count"] = len(result["cases"])
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--first-source", default="boundary-cases-001-010.v0.2.json")
    parser.add_argument("--second-source", default="boundary-cases-011-020.v0.3.json")
    parser.add_argument("--first-patches", default="FIRST_STRATUM_REVIEW_PATCHES_V0.3.json")
    parser.add_argument("--second-patches", default="SECOND_STRATUM_APPLICATION_PATCHES_V0.3.json")
    parser.add_argument("--first-output", default="boundary-cases-001-010.reviewed.v0.3.json")
    parser.add_argument("--second-output", default="boundary-cases-011-020.reviewed.v0.3.json")
    args = parser.parse_args()

    paths = [Path(args.first_source), Path(args.second_source), Path(args.first_patches), Path(args.second_patches)]
    for path in paths:
        if not path.exists():
            print(f"ERROR: file not found: {path}")
            return 2
    try:
        first = review_first(load(paths[0]), load(paths[2]))
        second = review_second(load(paths[1]), load(paths[3]))
        Path(args.first_output).write_text(json.dumps(first, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        Path(args.second_output).write_text(json.dumps(second, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        print(f"ERROR: corpus review failed: {exc}")
        return 2
    print(f"PASS: wrote {args.first_output} with {first['case_count']} reviewed cases")
    print(f"PASS: wrote {args.second_output} with {second['case_count']} reviewed cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
