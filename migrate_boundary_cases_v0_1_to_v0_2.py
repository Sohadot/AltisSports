#!/usr/bin/env python3
"""Migrate the AltisSports BC-001–BC-010 dataset from schema v0.1 to v0.2.

The v0.1 source is never modified. The migration preserves sourced content,
renames governed concepts, creates an Operational Spatial Integration Profile,
and marks every inferred field for human review.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_VERSION = "1.0.0"

AGENCY_MODES: dict[str, list[str]] = {
    "BC-005": ["remote_performance"],
    "BC-010": ["design_engineering", "autonomous_execution"],
}

INTERFACE_TYPES: dict[str, list[str]] = {
    "BC-001": ["direct_bodily_action", "conventional_equipment"],
    "BC-002": ["controller_or_discrete_input"],
    "BC-003": ["vehicle_control"],
    "BC-004": ["direct_bodily_action", "adaptive_or_assistive_equipment"],
    "BC-005": ["remote_control"],
    "BC-006": ["controller_or_discrete_input"],
    "BC-007": ["direct_bodily_action", "tracked_xr_input"],
    "BC-008": ["direct_bodily_action", "resistance_equipment", "tracked_xr_input"],
    "BC-009": ["simulation_controls"],
    "BC-010": ["autonomous_agent"],
}

EMBODIED_DEMANDS: dict[str, list[str]] = {
    "BC-001": ["locomotion", "force", "balance", "endurance", "sensorimotor_coordination"],
    "BC-002": ["cognitive", "fine_motor"],
    "BC-003": ["vehicle_control", "endurance", "sensorimotor_coordination"],
    "BC-004": ["adaptive_bodily_performance", "locomotion", "force", "sensorimotor_coordination"],
    "BC-005": ["remote_control", "fine_motor", "sensorimotor_coordination"],
    "BC-006": ["cognitive", "fine_motor", "sensorimotor_coordination"],
    "BC-007": ["locomotion", "force", "balance", "endurance", "tracked_movement"],
    "BC-008": ["endurance", "force", "physiological_effort", "tracked_movement"],
    "BC-009": ["cognitive", "fine_motor", "sensorimotor_coordination"],
    "BC-010": ["none_live_human"],
}

ROLE_MAP = {
    "represent_only": "represent",
    "enable_performance": "enable",
    "constrain_performance": "constrain",
    "measure_performance": "measure",
    "compare_performance": "compare",
    "officiate_performance": "officiate",
}

ROLE_LAYERS = {
    "represent": ["L3", "L8"],
    "enable": ["L1", "L2", "L3"],
    "mediate": ["L2", "L3", "L5"],
    "constrain": ["L3", "L4"],
    "measure": ["L5", "L6"],
    "compare": ["L6"],
    "officiate": ["L4", "L5", "L7"],
}

CATEGORY_RELATION_MAP = {
    "spatial_athletic_system": "spatial_athletic_system",
    "partial_spatial_integration": "partial_spatial_integration",
    "computational_arena_without_athletic_embodiment_claim": "computational_contest",
    "not_spatial_sport": "outside_core_spatial_athletic_class",
    "unresolved": "unresolved",
}

CLASSIFIED_OBJECT_MAP = {
    "activity": "activity",
    "athletic_system": "athletic_system",
    "spatial_athletic_system": "spatial_athletic_system",
    "experience": "experience",
    "product": "product",
    "event": "event",
    "organization": "organization",
    "hybrid_unresolved": "hybrid_unresolved",
}


def _clone_dimension(block: dict[str, Any]) -> dict[str, Any]:
    result = {
        "status": block.get("status", "unknown"),
        "summary": block.get("summary", ""),
        "claim_class": block.get("claim_class", "C5"),
    }
    if "observables" in block:
        result["observables"] = copy.deepcopy(block["observables"])
    return result


def _significance(status: str) -> str:
    if status == "supported":
        return "constitutive"
    if status in {"partial", "disputed"}:
        return "supportive"
    if status == "absent":
        return "incidental"
    return "unknown"


def _human_skill_necessary(case_id: str, old_status: str) -> bool | None:
    if case_id == "BC-010":
        return False
    if old_status in {"supported", "partial"}:
        return True
    if old_status == "absent":
        return False
    return None


def _performance_window(case: dict[str, Any]) -> str:
    finding = case.get("provisional_finding", {}).get("summary", "")
    return (
        "The bounded contest or performance interval in which actions can "
        "materially change the evaluated result. Migrated from v0.1; review "
        f"against the case narrative. Prior finding: {finding}"
    )


def _spatial_functions(old: dict[str, Any]) -> list[dict[str, Any]]:
    functions: list[dict[str, Any]] = []
    overall_status = old.get("status", "unknown")
    summary = old.get("summary", "")
    roles = old.get("operational_roles", [])

    for old_role in roles:
        if old_role in {"none_observed", "unknown"}:
            continue
        role = ROLE_MAP.get(old_role)
        if not role:
            continue
        functions.append(
            {
                "role": role,
                "status": overall_status,
                "significance": _significance(overall_status),
                "mechanism": summary or f"Migrated from v0.1 operational role {old_role}.",
                "affected_layers": ROLE_LAYERS[role],
                "failure_effect": (
                    "Not independently specified in v0.1. Human review must state "
                    "what failure of this function changes."
                ),
                "evidence_refs": [],
                "uncertainty": (
                    "Role and significance were mechanically migrated from the "
                    "v0.1 status and require case-level review."
                ),
                "review_status": "migrated_inference_review_required",
            }
        )
    return functions


def migrate_case(case: dict[str, Any]) -> dict[str, Any]:
    case_id = case["case_id"]
    old_agency = case.get("human_agency", {})
    old_interface = case.get("embodied_interface", {})
    old_spatial = case.get("spatial_integration", {})
    old_invariants = case.get("candidate_invariants", {})
    old_layers = case.get("as3_layer_notes", {})
    old_finding = case.get("provisional_finding", {})
    old_classified = case.get("classified_object", {})

    primary = CLASSIFIED_OBJECT_MAP.get(old_classified.get("primary"), "hybrid_unresolved")
    secondary = [
        CLASSIFIED_OBJECT_MAP[value]
        for value in old_classified.get("secondary", [])
        if value in CLASSIFIED_OBJECT_MAP and CLASSIFIED_OBJECT_MAP[value] != "hybrid_unresolved"
    ]

    agency_modes = AGENCY_MODES.get(case_id, ["live_performance"])
    performance_agency = _clone_dimension(old_agency)
    performance_agency.update(
        {
            "agency_modes": agency_modes,
            "human_skill_causally_necessary": _human_skill_necessary(
                case_id, old_agency.get("status", "unknown")
            ),
            "performance_window": _performance_window(case),
            "migration_review_required": True,
        }
    )

    performance_interface = _clone_dimension(old_interface)
    performance_interface["interface_types"] = INTERFACE_TYPES.get(case_id, ["unknown"])

    embodied_performance = _clone_dimension(old_interface)
    embodied_performance["demand_types"] = EMBODIED_DEMANDS.get(case_id, ["unknown"])
    embodied_performance["summary"] = (
        f"{old_interface.get('summary', '')} "
        "Migrated as Embodied Performance; demand types are provisional."
    ).strip()

    functions = _spatial_functions(old_spatial)
    spatial_profile = {
        "overall_status": old_spatial.get("status", "unknown"),
        "summary": old_spatial.get("summary", ""),
        "functions": functions,
        "immersion_present": old_spatial.get("immersion_present"),
        "claim_class": old_spatial.get("claim_class", "C5"),
        "profile_status": "migrated_provisional",
        "no_function_observed": not functions,
    }

    consequence = _clone_dimension(case.get("consequence", {}))

    migrated = {
        "schema_version": "0.2",
        "case_id": case_id,
        "activity": case["activity"],
        "activity_aliases": copy.deepcopy(case.get("activity_aliases", [])),
        "corpus_refs": copy.deepcopy(case.get("corpus_refs", [])),
        "classified_object": {
            "primary": primary,
            "secondary": secondary,
            "notes": old_classified.get("notes", ""),
        },
        "performance_agency": performance_agency,
        "performance_interface": performance_interface,
        "embodied_performance": embodied_performance,
        "arena": _clone_dimension(case.get("arena", {})),
        "rules": _clone_dimension(case.get("rules", {})),
        "tracking": _clone_dimension(case.get("tracking", {})),
        "measurement": _clone_dimension(case.get("measurement", {})),
        "comparability": _clone_dimension(case.get("comparability", {})),
        "officiation": _clone_dimension(case.get("officiation", {})),
        "outcome_openness": _clone_dimension(case.get("outcome_openness", {})),
        "consequence_structure": consequence,
        "operational_spatial_integration_profile": spatial_profile,
        "as3_layer_notes": {
            "L1_performance_agency": old_layers.get("L1_human_agency", ""),
            "L2_performance_interface_embodied_demand": old_layers.get("L2_embodied_interface", ""),
            "L3_arena_spatial_state": old_layers.get("L3_arena_spatial_state", ""),
            "L4_constraint_rule_execution": old_layers.get("L4_constraint_rule_execution", ""),
            "L5_sensing_tracking": old_layers.get("L5_sensing_tracking", ""),
            "L6_measurement_comparability": old_layers.get("L6_measurement_comparability", ""),
            "L7_officiation_outcome": old_layers.get("L7_officiation_outcome", ""),
            "L8_presence_participation": old_layers.get("L8_presence_participation", ""),
            "L9_safety_accessibility": old_layers.get("L9_safety_accessibility", ""),
            "L10_governance_evidence": old_layers.get("L10_governance_evidence", ""),
        },
        "candidate_invariants": {
            "performance_agency": copy.deepcopy(
                old_invariants.get(
                    "human_agency",
                    {"status": old_agency.get("status", "unknown"), "notes": "Migrated from v0.1."},
                )
            ),
            "constraint_integrity": copy.deepcopy(
                old_invariants.get("constraint_integrity", {"status": "unknown", "notes": ""})
            ),
            "comparability": copy.deepcopy(
                old_invariants.get("comparability", {"status": "unknown", "notes": ""})
            ),
            "outcome_openness": copy.deepcopy(
                old_invariants.get("outcome_openness", {"status": "unknown", "notes": ""})
            ),
        },
        "evidence": copy.deepcopy(case.get("evidence", [])),
        "objections": copy.deepcopy(case.get("objections", [])),
        "what_would_change_judgment": copy.deepcopy(
            case.get("what_would_change_judgment", [])
        ),
        "provisional_finding": {
            "sport_contest_axis": old_finding.get("sport_axis", "unresolved"),
            "category_relation": CATEGORY_RELATION_MAP.get(
                old_finding.get("spatial_sport_axis"), "unresolved"
            ),
            "summary": old_finding.get("summary", ""),
            "claim_class": old_finding.get("claim_class", "C5"),
        },
        "confidence": case.get("confidence", "low"),
        "limitations": copy.deepcopy(case.get("limitations", [])),
        "access_date": case.get("access_date"),
        "revision": {
            "version": "0.2",
            "notes": (
                "Automated governed migration from schema v0.1. Semantic inferences "
                "remain review-required; the v0.1 source remains authoritative for "
                "the original Sprint 2 record."
            ),
        },
        "migration": {
            "source_schema_version": "0.1",
            "migration_script_version": SCRIPT_VERSION,
            "review_status": "automated_review_required",
            "notes": (
                "Terminology and field structure migrated under DEC-006/DEC-007. "
                "No case is treated as human-reviewed by this script."
            ),
        },
    }

    if "institutional_recognition" in case:
        migrated["institutional_recognition"] = copy.deepcopy(
            case["institutional_recognition"]
        )

    return migrated


def migrate_dataset(source: dict[str, Any]) -> dict[str, Any]:
    if source.get("schema_version") != "0.1":
        raise ValueError("Source dataset must declare schema_version 0.1.")
    cases = source.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ValueError("Source dataset must contain a non-empty cases array.")

    migrated_cases = [migrate_case(case) for case in cases]
    return {
        "dataset": "AltisSports Boundary Cases BC-001-010",
        "schema": "BOUNDARY_CASE_SCHEMA_V0.2.json",
        "schema_version": "0.2",
        "source_dataset": "boundary-cases-001-010.json",
        "source_schema_version": "0.1",
        "sprint": "Sprint 4 — Corpus Infrastructure and Second-Stratum Readiness",
        "status": "provisional_migrated_review_required",
        "license": {
            "identifier": "CC-BY-4.0",
            "notice": "See DATASET_LICENSE.md.",
        },
        "case_count": len(migrated_cases),
        "cases": migrated_cases,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source", default="boundary-cases-001-010.json", help="v0.1 dataset path"
    )
    parser.add_argument(
        "--output",
        default="boundary-cases-001-010.v0.2.json",
        help="v0.2 output path",
    )
    args = parser.parse_args()

    source_path = Path(args.source)
    output_path = Path(args.output)

    if source_path.resolve() == output_path.resolve():
        print("ERROR: source and output paths must differ.", file=sys.stderr)
        return 2
    if not source_path.exists():
        print(f"ERROR: source file not found: {source_path}", file=sys.stderr)
        return 2

    try:
        source = json.loads(source_path.read_text(encoding="utf-8"))
        migrated = migrate_dataset(source)
        output_path.write_text(
            json.dumps(migrated, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    except (OSError, json.JSONDecodeError, ValueError, KeyError, TypeError) as exc:
        print(f"ERROR: migration failed: {exc}", file=sys.stderr)
        return 1

    print(
        f"Migrated {migrated['case_count']} cases: "
        f"{source_path} -> {output_path}"
    )
    print("All migrated cases remain automated_review_required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
