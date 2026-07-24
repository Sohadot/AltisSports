#!/usr/bin/env python3
"""Build BOUNDARY_CASE_SCHEMA_V0.3.json from the checked-in v0.2 schema.

The script performs a deterministic additive schema evolution. It does not
modify BOUNDARY_CASE_SCHEMA_V0.2.json.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any


def _append_unique(items: list[Any], value: Any) -> None:
    if value not in items:
        items.append(value)


def build_schema(source: dict[str, Any]) -> dict[str, Any]:
    schema = copy.deepcopy(source)

    schema["$id"] = "https://altissports.com/schemas/boundary-case-v0.3.json"
    schema["title"] = "AltisSports Boundary Case Record v0.3"
    schema["description"] = (
        "Machine-readable schema for evidence-linked Spatial Sport boundary cases, "
        "including phase-level agency, distributed-arena relations, participatory "
        "actors, and intentional biological control. Not a scoring or certification standard."
    )

    schema["properties"]["schema_version"]["const"] = "0.3"
    schema["properties"]["revision"]["properties"]["version"]["const"] = "0.3"

    required = schema["required"]
    for field in (
        "agency_segments",
        "distributed_arena_relation",
        "participatory_actor_relations",
        "intentional_biological_control",
    ):
        _append_unique(required, field)

    interface_enum = (
        schema["properties"]["performance_interface"]["properties"]["interface_types"]
        ["items"]["enum"]
    )
    _append_unique(interface_enum, "intentional_biological_control")

    demand_enum = (
        schema["properties"]["embodied_performance"]["properties"]["demand_types"]
        ["items"]["enum"]
    )
    _append_unique(demand_enum, "intentional_biosignal_control")

    profile_status = (
        schema["properties"]["operational_spatial_integration_profile"]["properties"]
        ["profile_status"]["enum"]
    )
    _append_unique(profile_status, "carried_forward_v0_3")
    _append_unique(profile_status, "human_reviewed_v0_3")

    function_review = schema["$defs"]["spatial_function"]["properties"]["review_status"]["enum"]
    _append_unique(function_review, "carried_forward_v0_3")
    _append_unique(function_review, "human_reviewed_v0_3")

    migration_source = schema["properties"]["migration"]["properties"]["source_schema_version"]["enum"]
    _append_unique(migration_source, "0.2")

    migration_review = schema["properties"]["migration"]["properties"]["review_status"]["enum"]
    _append_unique(migration_review, "structural_migration_reviewed")
    _append_unique(migration_review, "human_reviewed_v0_3")

    schema["$defs"]["agency_segment"] = {
        "type": "object",
        "additionalProperties": False,
        "required": [
            "segment_id",
            "phase_or_regime",
            "segment_basis",
            "boundary_description",
            "active_agents",
            "agency_modes",
            "primary_control",
            "transition_trigger",
            "allowed_assistance",
            "causal_attribution",
            "evidence_refs",
            "uncertainty",
            "review_status",
        ],
        "properties": {
            "segment_id": {"type": "string", "pattern": "^AS-[0-9]{3}-[0-9]{2}$"},
            "phase_or_regime": {"type": "string", "minLength": 1},
            "segment_basis": {
                "type": "string",
                "enum": [
                    "observed_phase",
                    "declared_rule_regime",
                    "inferred_phase",
                    "unknown",
                ],
            },
            "boundary_description": {"type": "string", "minLength": 1},
            "active_agents": {
                "type": "array",
                "minItems": 1,
                "items": {"type": "string", "minLength": 1},
            },
            "agency_modes": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "type": "string",
                    "enum": [
                        "live_performance",
                        "remote_performance",
                        "assisted_performance",
                        "design_engineering",
                        "autonomous_execution",
                        "agency_handoff",
                        "unknown",
                    ],
                },
            },
            "primary_control": {
                "type": "string",
                "enum": [
                    "human_pilot",
                    "human_team",
                    "human_intention_decoder_mediated",
                    "shared_or_variable",
                    "automated_system",
                    "external_participants",
                    "unknown",
                ],
            },
            "transition_trigger": {"type": "string"},
            "allowed_assistance": {"type": "string"},
            "causal_attribution": {"type": "string"},
            "evidence_refs": {
                "type": "array",
                "items": {"type": "integer"},
            },
            "uncertainty": {"type": "string"},
            "review_status": {
                "type": "string",
                "enum": ["human_reviewed_v0_3", "review_required"],
            },
        },
    }

    schema["$defs"]["distributed_arena_relation"] = {
        "type": "object",
        "additionalProperties": False,
        "required": [
            "status",
            "topology",
            "physical_site_relation",
            "shared_computational_state",
            "synchronization_mechanism",
            "latency_governance",
            "calibration_equivalence",
            "officiation_relation",
            "safety_relation",
            "evidence_refs",
            "uncertainty",
            "review_status",
        ],
        "properties": {
            "status": {
                "type": "string",
                "enum": [
                    "supported",
                    "partial",
                    "not_evidenced",
                    "not_applicable",
                    "disputed",
                    "unknown",
                ],
            },
            "topology": {
                "type": "string",
                "enum": [
                    "co_located_single_site",
                    "co_located_multi_station",
                    "remote_synchronous",
                    "multi_hub_synchronous",
                    "remote_asynchronous",
                    "remote_supervision_physical_arena",
                    "hybrid",
                    "unknown",
                    "not_applicable",
                ],
            },
            "physical_site_relation": {"type": "string"},
            "shared_computational_state": {
                "type": "string",
                "enum": [
                    "supported",
                    "partial",
                    "absent",
                    "not_applicable",
                    "unknown",
                ],
            },
            "synchronization_mechanism": {"type": "string"},
            "latency_governance": {"type": "string"},
            "calibration_equivalence": {"type": "string"},
            "officiation_relation": {"type": "string"},
            "safety_relation": {"type": "string"},
            "evidence_refs": {
                "type": "array",
                "items": {"type": "integer"},
            },
            "uncertainty": {"type": "string"},
            "review_status": {
                "type": "string",
                "enum": ["human_reviewed_v0_3", "review_required"],
            },
        },
    }

    schema["$defs"]["participatory_actor_relation"] = {
        "type": "object",
        "additionalProperties": False,
        "required": [
            "relation_id",
            "actor_type",
            "relation_type",
            "action_window",
            "mechanism",
            "performance_agency_relation",
            "rule_authority_relation",
            "resource_or_constraint_effect",
            "evidence_refs",
            "uncertainty",
            "review_status",
        ],
        "properties": {
            "relation_id": {"type": "string", "pattern": "^PAR-[0-9]{3}-[0-9]{2}$"},
            "actor_type": {
                "type": "string",
                "enum": [
                    "spectator_public",
                    "crowd",
                    "coach",
                    "team_engineer",
                    "operator",
                    "external_public",
                    "team_member_nonperformer",
                    "unknown",
                ],
            },
            "relation_type": {
                "type": "string",
                "enum": [
                    "resource_allocator",
                    "constraint_modifier",
                    "information_supplier",
                    "vote_actor",
                    "trigger_actor",
                    "supervisor",
                    "other",
                ],
            },
            "action_window": {"type": "string"},
            "mechanism": {"type": "string"},
            "performance_agency_relation": {
                "type": "string",
                "enum": [
                    "none",
                    "indirect_no_execution",
                    "shared",
                    "disputed",
                    "unknown",
                ],
            },
            "rule_authority_relation": {
                "type": "string",
                "enum": [
                    "none",
                    "participatory",
                    "officiating",
                    "disputed",
                    "unknown",
                ],
            },
            "resource_or_constraint_effect": {"type": "string"},
            "evidence_refs": {
                "type": "array",
                "items": {"type": "integer"},
            },
            "uncertainty": {"type": "string"},
            "review_status": {
                "type": "string",
                "enum": ["human_reviewed_v0_3", "review_required"],
            },
        },
    }

    schema["$defs"]["intentional_biological_control"] = {
        "type": ["object", "null"],
        "additionalProperties": False,
        "required": [
            "status",
            "signal_origin",
            "intentional_generation",
            "task_coupling",
            "decoder_mediation",
            "human_skill_causally_necessary",
            "trainability_or_control_evidence",
            "incidental_signal_exclusion",
            "athletic_embodiment_relation",
            "summary",
            "evidence_refs",
            "uncertainty",
            "review_status",
        ],
        "properties": {
            "status": {
                "type": "string",
                "enum": ["supported", "partial", "disputed", "unknown", "not_applicable"],
            },
            "signal_origin": {
                "type": "string",
                "enum": [
                    "brain_activity",
                    "muscle_activity",
                    "neural_activity",
                    "other_physiological_signal",
                    "unknown",
                ],
            },
            "intentional_generation": {
                "type": "string",
                "enum": ["supported", "partial", "disputed", "unknown"],
            },
            "task_coupling": {
                "type": "string",
                "enum": ["incidental", "supportive", "constitutive", "unknown"],
            },
            "decoder_mediation": {
                "type": "string",
                "enum": ["absent", "supportive", "constitutive", "unknown"],
            },
            "human_skill_causally_necessary": {"type": ["boolean", "null"]},
            "trainability_or_control_evidence": {
                "type": "string",
                "enum": ["supported", "partial", "absent", "unknown"],
            },
            "incidental_signal_exclusion": {
                "type": "string",
                "enum": ["supported", "partial", "disputed", "unknown"],
            },
            "athletic_embodiment_relation": {
                "type": "string",
                "enum": ["supported", "outside_scope", "disputed", "unresolved"],
            },
            "summary": {"type": "string"},
            "evidence_refs": {
                "type": "array",
                "items": {"type": "integer"},
            },
            "uncertainty": {"type": "string"},
            "review_status": {
                "type": "string",
                "enum": ["human_reviewed_v0_3", "review_required"],
            },
        },
    }

    schema["properties"]["agency_segments"] = {
        "type": "array",
        "items": {"$ref": "#/$defs/agency_segment"},
    }
    schema["properties"]["distributed_arena_relation"] = {
        "$ref": "#/$defs/distributed_arena_relation"
    }
    schema["properties"]["participatory_actor_relations"] = {
        "type": "array",
        "items": {"$ref": "#/$defs/participatory_actor_relation"},
    }
    schema["properties"]["intentional_biological_control"] = {
        "$ref": "#/$defs/intentional_biological_control"
    }

    return schema


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="BOUNDARY_CASE_SCHEMA_V0.2.json")
    parser.add_argument("--output", default="BOUNDARY_CASE_SCHEMA_V0.3.json")
    args = parser.parse_args()

    source_path = Path(args.source)
    output_path = Path(args.output)
    if not source_path.exists():
        print(f"ERROR: file not found: {source_path}")
        return 2

    source = json.loads(source_path.read_text(encoding="utf-8"))
    result = build_schema(source)
    output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
