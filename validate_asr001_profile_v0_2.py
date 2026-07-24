#!/usr/bin/env python3
"""Validate one ASR-001 candidate profile v0.2."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

REQUIRED_TOP_LEVEL = {
    "profile_metadata", "subject", "operating_context",
    "system_roles_and_dependencies", "feature_flags",
    "performance", "arena", "constraints", "sensing",
    "measurement", "outcome", "spatial_integration",
    "actors", "human_factors", "evidence", "governance",
    "distributions", "clause_records"
}
FEATURE_KEYS = {
    "human_performance_claimed",
    "agency_modes_or_handoff_present",
    "embodiment_or_biological_control_claimed",
    "distributed_operation_claimed",
    "rules_or_constraints_present",
    "sensing_or_tracking_present",
    "measurement_or_comparison_claimed",
    "contest_or_outcome_present",
    "spatial_function_claimed",
    "participatory_actor_present",
    "operational_responsibility_material",
    "machine_readable_distribution_provided",
}
FEATURE_STATES = {"present", "absent", "unknown", "disputed"}
APPLICABILITY_STATES = {"applicable", "not_applicable", "unknown", "disputed"}
EVIDENCE_STATES = {
    "supported", "partial", "absent", "unknown",
    "not_evidenced", "not_applicable"
}
VERIFICATION_STATES = {
    "verified", "partially_verified", "not_verified",
    "not_applicable", "requires_human_review",
    "blocked_by_missing_evidence"
}
EVIDENCE_REQUIREMENTS = {
    "declaration_required",
    "supporting_evidence_or_unresolved_state",
    "lifecycle_record_required",
    "declaration_or_manifest_required"
}
PROHIBITED_KEYS = {
    "total_score", "spatiality_score", "maturity_level",
    "quality_grade", "vendor_rank", "product_rank",
    "certification_status", "certification_mark"
}

def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain an object")
    return data

def walk_keys(value: Any, found: set[str]) -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            found.add(key)
            walk_keys(item, found)
    elif isinstance(value, list):
        for item in value:
            walk_keys(item, found)

def path_exists(root: dict[str, Any], dotted: str) -> bool:
    value: Any = root
    for part in dotted.split("."):
        if not isinstance(value, dict) or part not in value:
            return False
        value = value[part]
    return True

def expected_applicability(trigger_key: str | None, flags: dict[str, Any]) -> str:
    if trigger_key is None:
        return "applicable"
    state = flags[trigger_key]
    return {
        "present": "applicable",
        "absent": "not_applicable",
        "unknown": "unknown",
        "disputed": "disputed",
    }[state]

def validate_profile(profile_path: Path, catalog_path: Path) -> list[str]:
    errors: list[str] = []
    profile = load_json(profile_path)
    catalog = load_json(catalog_path)

    missing_top = sorted(REQUIRED_TOP_LEVEL - set(profile))
    extra_top = sorted(set(profile) - REQUIRED_TOP_LEVEL)
    if missing_top:
        errors.append(f"missing top-level fields: {missing_top}")
    if extra_top:
        errors.append(f"unexpected top-level fields: {extra_top}")
    if errors:
        return errors

    metadata = profile["profile_metadata"]
    required_meta = {
        "profile_id", "profile_version", "status", "created_date",
        "revised_date", "language", "asr_working_draft_version",
        "subject_id", "license_notice", "supersedes_profile_id",
        "superseded_by_profile_id"
    }
    if not isinstance(metadata, dict):
        errors.append("profile_metadata must be an object")
    else:
        missing = sorted(required_meta - set(metadata))
        if missing:
            errors.append(f"profile_metadata missing: {missing}")
        if metadata.get("asr_working_draft_version") != "0.2":
            errors.append("asr_working_draft_version must be 0.2")
        if metadata.get("status") not in {"draft", "reviewed_draft", "superseded"}:
            errors.append("profile status is invalid")

    subject = profile["subject"]
    canonical = subject.get("canonical_subject") if isinstance(subject, dict) else None
    if not isinstance(canonical, dict):
        errors.append("subject.canonical_subject must be an object")
    else:
        for key in [
            "subject_id", "object_type", "name",
            "configuration", "version", "temporal_status"
        ]:
            if not canonical.get(key):
                errors.append(f"canonical subject missing {key}")
        if metadata.get("subject_id") != canonical.get("subject_id"):
            errors.append("metadata and canonical subject identifiers differ")

    flags = profile["feature_flags"]
    if not isinstance(flags, dict):
        errors.append("feature_flags must be an object")
        flags = {}
    else:
        missing = sorted(FEATURE_KEYS - set(flags))
        extra = sorted(set(flags) - FEATURE_KEYS)
        if missing:
            errors.append(f"missing feature flags: {missing}")
        if extra:
            errors.append(f"unexpected feature flags: {extra}")
        for key, value in flags.items():
            if value not in FEATURE_STATES:
                errors.append(f"invalid feature state {key}={value}")
        if flags.get("machine_readable_distribution_provided") != "present":
            errors.append(
                "JSON profile requires machine_readable_distribution_provided=present"
            )

    clauses = catalog.get("clauses")
    if not isinstance(clauses, list) or len(clauses) != 30:
        errors.append("v0.2 clause catalog must contain exactly 30 clauses")
        return errors
    expected = {item["clause_id"]: item for item in clauses}

    records = profile["clause_records"]
    if not isinstance(records, list) or len(records) != 30:
        errors.append("clause_records must contain exactly 30 records")
        return errors

    evidence_records = profile.get("evidence", {}).get("records", [])
    evidence_ids = {
        item.get("evidence_id")
        for item in evidence_records
        if isinstance(item, dict) and item.get("evidence_id")
    }
    seen: set[str] = set()

    for index, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            errors.append(f"clause record #{index} is not an object")
            continue
        cid = record.get("clause_id")
        if cid not in expected:
            errors.append(f"unknown clause id: {cid}")
            continue
        if cid in seen:
            errors.append(f"duplicate clause id: {cid}")
        seen.add(cid)
        clause = expected[cid]

        if record.get("field_path") != clause.get("profile_field_path"):
            errors.append(f"{cid} field path mismatch")
        elif not path_exists(profile, record["field_path"]):
            errors.append(f"{cid} field path does not exist in profile")

        requirement = record.get("evidence_requirement")
        if requirement not in EVIDENCE_REQUIREMENTS:
            errors.append(f"{cid} invalid evidence requirement")
        if requirement != clause.get("evidence_requirement"):
            errors.append(f"{cid} evidence requirement differs from catalog")

        applicability = record.get("applicability")
        if applicability not in APPLICABILITY_STATES:
            errors.append(f"{cid} invalid applicability: {applicability}")
            continue
        expected_state = expected_applicability(clause.get("trigger_key"), flags)
        if applicability != expected_state:
            errors.append(
                f"{cid} applicability is {applicability}; expected {expected_state}"
            )

        evidence_state = record.get("evidence_state")
        if evidence_state not in EVIDENCE_STATES:
            errors.append(f"{cid} invalid evidence state: {evidence_state}")

        refs = record.get("evidence_refs")
        if not isinstance(refs, list):
            errors.append(f"{cid} evidence_refs must be an array")
            refs = []
        unknown_refs = sorted(set(refs) - evidence_ids)
        if unknown_refs:
            errors.append(f"{cid} references unknown evidence: {unknown_refs}")

        verification = record.get("verification_status")
        if verification not in VERIFICATION_STATES:
            errors.append(f"{cid} invalid verification status: {verification}")

        if not isinstance(record.get("applicability_basis"), str) or not record["applicability_basis"].strip():
            errors.append(f"{cid} lacks applicability basis")
        if not isinstance(record.get("disclosure"), str) or not record["disclosure"].strip():
            errors.append(f"{cid} lacks disclosure")
        if not isinstance(record.get("friction_notes"), list):
            errors.append(f"{cid} friction_notes must be an array")

        if applicability == "not_applicable":
            if evidence_state != "not_applicable":
                errors.append(f"{cid} not-applicable clause needs evidence_state not_applicable")
            if refs:
                errors.append(f"{cid} not-applicable clause must not attach evidence")
            if verification != "not_applicable":
                errors.append(f"{cid} not-applicable clause needs not_applicable verification")
        elif applicability in {"unknown", "disputed"}:
            if evidence_state not in {"partial", "unknown", "not_evidenced"}:
                errors.append(f"{cid} unresolved applicability has invalid evidence state")
            if verification not in {
                "requires_human_review", "blocked_by_missing_evidence",
                "partially_verified"
            }:
                errors.append(f"{cid} unresolved applicability has invalid verification")
        else:
            if evidence_state == "not_applicable":
                errors.append(f"{cid} applicable clause cannot have not_applicable evidence")
            if evidence_state == "supported" and verification not in {
                "verified", "requires_human_review"
            }:
                errors.append(f"{cid} supported evidence has invalid verification")
            if evidence_state == "partial" and verification not in {
                "partially_verified", "requires_human_review"
            }:
                errors.append(f"{cid} partial evidence has invalid verification")
            if evidence_state in {"unknown", "not_evidenced", "absent"} and verification not in {
                "blocked_by_missing_evidence", "requires_human_review"
            }:
                errors.append(f"{cid} unresolved evidence has invalid verification")

            if requirement == "supporting_evidence_or_unresolved_state":
                if evidence_state in {"supported", "partial"} and not refs:
                    errors.append(f"{cid} supported or partial evidence requires references")
                if evidence_state in {"unknown", "not_evidenced", "absent"} and refs:
                    errors.append(f"{cid} unresolved evidence should not attach supporting refs")
            elif requirement in {
                "declaration_required",
                "lifecycle_record_required",
                "declaration_or_manifest_required"
            }:
                if evidence_state == "supported" and not refs:
                    errors.append(f"{cid} supported declaration or lifecycle state needs a record")

    if seen != set(expected):
        errors.append(f"clause record set mismatch; missing {sorted(set(expected) - seen)}")

    # Triggered structural checks.
    if flags.get("human_performance_claimed") == "present":
        if not profile.get("performance", {}).get("performance_window"):
            errors.append("human performance requires performance_window")
        if not profile.get("performance", {}).get("interface_channels"):
            errors.append("human performance requires interface_channels")
    if flags.get("agency_modes_or_handoff_present") == "present":
        if not profile.get("performance", {}).get("agency_segments"):
            errors.append("agency mode or handoff requires agency_segments")
    if flags.get("distributed_operation_claimed") == "present":
        if not profile.get("arena", {}).get("distributed_relation"):
            errors.append("distributed operation requires distributed_relation")
    if flags.get("rules_or_constraints_present") == "present":
        if not profile.get("constraints", {}).get("authoritative_sources"):
            errors.append("rules or constraints require authoritative_sources")
    if flags.get("sensing_or_tracking_present") == "present":
        if not profile.get("sensing", {}).get("observation_estimation_boundary"):
            errors.append("sensing requires observation_estimation_boundary")
    if flags.get("measurement_or_comparison_claimed") == "present":
        if not profile.get("measurement", {}).get("metrics"):
            errors.append("measurement claim requires metrics")
    if flags.get("contest_or_outcome_present") == "present":
        if not profile.get("outcome", {}).get("outcome_and_consequence"):
            errors.append("contest or outcome requires outcome_and_consequence")
    if flags.get("spatial_function_claimed") == "present":
        if not profile.get("spatial_integration", {}).get("functions"):
            errors.append("spatial function claim requires functions")
    if flags.get("participatory_actor_present") == "present":
        if not profile.get("actors", {}).get("participatory_relations"):
            errors.append("participatory actor requires participatory_relations")
    if flags.get("operational_responsibility_material") == "present":
        if not profile.get("human_factors", {}).get("operational_responsibility"):
            errors.append("responsibility flag requires operational_responsibility")
    if not profile.get("distributions"):
        errors.append("JSON profile requires at least one distribution")

    corrections = profile.get("governance", {}).get(
        "corrections_and_supersession", []
    )
    if metadata.get("supersedes_profile_id") and not corrections:
        errors.append("superseding profile requires a correction record")
    for correction in corrections:
        refs = correction.get("evidence_refs", [])
        if not set(refs).issubset(evidence_ids):
            errors.append("correction references unknown evidence")
        if not correction.get("affected_clause_ids"):
            errors.append("correction requires affected_clause_ids")
        if not correction.get("affected_field_paths"):
            errors.append("correction requires affected_field_paths")

    found_keys: set[str] = set()
    walk_keys(profile, found_keys)
    prohibited = sorted(PROHIBITED_KEYS & found_keys)
    if prohibited:
        errors.append(f"profile contains prohibited keys: {prohibited}")

    return errors

def main(argv: list[str]) -> int:
    if len(argv) not in {2, 3}:
        print(
            "Usage: python validate_asr001_profile_v0_2.py PROFILE.json "
            "[ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.2.json]",
            file=sys.stderr
        )
        return 2
    profile_path = Path(argv[1])
    catalog_path = (
        Path(argv[2])
        if len(argv) == 3
        else Path("ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.2.json")
    )
    try:
        errors = validate_profile(profile_path, catalog_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: validation could not run: {exc}", file=sys.stderr)
        return 2
    if errors:
        print(f"FAIL: {profile_path.name}: {len(errors)} error(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS: {profile_path.name} validates against ASR-001 profile model v0.2.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
