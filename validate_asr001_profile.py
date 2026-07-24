#!/usr/bin/env python3
"""Validate an ASR-001 candidate profile instance without third-party packages."""
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

FLAG_KEYS = {
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

FLAG_STATES = {True, False, "unknown", "disputed", "not_evidenced"}
APPLICABILITY_STATES = {"applicable", "not_applicable", "unknown", "disputed", "not_evidenced"}
VERIFICATION_STATES = {
    "verified", "partially_verified", "not_verified",
    "not_applicable", "requires_human_review",
    "blocked_by_missing_evidence"
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

def expected_applicability(trigger_key: str | None, flags: dict[str, Any]) -> str:
    if trigger_key is None:
        return "applicable"
    value = flags.get(trigger_key)
    if value is True:
        return "applicable"
    if value is False:
        return "not_applicable"
    if value in {"unknown", "disputed", "not_evidenced"}:
        return value
    return "unknown"

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
        "subject_id", "license_notice"
    }
    if not isinstance(metadata, dict):
        errors.append("profile_metadata must be an object")
    else:
        missing_meta = sorted(required_meta - set(metadata))
        if missing_meta:
            errors.append(f"profile_metadata missing: {missing_meta}")
        if metadata.get("asr_working_draft_version") != "0.1":
            errors.append("asr_working_draft_version must be 0.1")
        if metadata.get("status") not in {"draft", "reviewed_draft", "superseded"}:
            errors.append("profile status must remain draft, reviewed_draft, or superseded")

    subject = profile["subject"]
    canonical = subject.get("canonical_subject") if isinstance(subject, dict) else None
    if not isinstance(canonical, dict):
        errors.append("subject.canonical_subject must be an object")
    else:
        for key in ["subject_id", "object_type", "name", "configuration", "version", "temporal_status"]:
            if not canonical.get(key):
                errors.append(f"canonical subject missing {key}")
        if metadata.get("subject_id") != canonical.get("subject_id"):
            errors.append("profile_metadata.subject_id must equal canonical subject_id")

    flags = profile["feature_flags"]
    if not isinstance(flags, dict):
        errors.append("feature_flags must be an object")
        flags = {}
    else:
        missing_flags = sorted(FLAG_KEYS - set(flags))
        extra_flags = sorted(set(flags) - FLAG_KEYS)
        if missing_flags:
            errors.append(f"missing feature flags: {missing_flags}")
        if extra_flags:
            errors.append(f"unexpected feature flags: {extra_flags}")
        for key, value in flags.items():
            if value not in FLAG_STATES:
                errors.append(f"invalid feature flag value for {key}: {value}")

    clauses = catalog.get("clauses")
    if not isinstance(clauses, list) or len(clauses) != 30:
        errors.append("normative catalog must contain 30 clauses")
        return errors
    expected = {item["clause_id"]: item for item in clauses}

    records = profile["clause_records"]
    if not isinstance(records, list) or len(records) != 30:
        errors.append("clause_records must contain exactly 30 records")
        return errors

    seen: set[str] = set()
    evidence_records = profile.get("evidence", {}).get("records", [])
    evidence_ids = {
        item.get("evidence_id")
        for item in evidence_records
        if isinstance(item, dict) and item.get("evidence_id")
    }

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

        applicability = record.get("applicability")
        if applicability not in APPLICABILITY_STATES:
            errors.append(f"{cid} invalid applicability: {applicability}")
        expected_state = expected_applicability(clause.get("trigger_key"), flags)
        if applicability != expected_state:
            errors.append(f"{cid} applicability is {applicability}; expected {expected_state}")

        verification = record.get("verification_status")
        if verification not in VERIFICATION_STATES:
            errors.append(f"{cid} invalid verification status: {verification}")

        disclosure = record.get("disclosure")
        if not isinstance(disclosure, str) or not disclosure.strip():
            errors.append(f"{cid} disclosure is empty")

        basis = record.get("applicability_basis")
        if not isinstance(basis, str) or not basis.strip():
            errors.append(f"{cid} applicability basis is empty")

        refs = record.get("evidence_refs")
        if not isinstance(refs, list):
            errors.append(f"{cid} evidence_refs must be an array")
            refs = []
        unknown_refs = sorted(set(refs) - evidence_ids)
        if unknown_refs:
            errors.append(f"{cid} references unknown evidence: {unknown_refs}")

        if applicability == "applicable":
            if not refs:
                errors.append(f"{cid} applicable clause requires evidence_refs")
            if verification == "not_applicable":
                errors.append(f"{cid} applicable clause cannot be verification not_applicable")
        elif applicability == "not_applicable":
            if refs:
                errors.append(f"{cid} not_applicable clause must not attach evidence")
            if verification != "not_applicable":
                errors.append(f"{cid} not_applicable clause needs verification_status not_applicable")
        elif verification == "verified":
            errors.append(f"{cid} unresolved applicability cannot be fully verified")

    if seen != set(expected):
        errors.append(f"clause record set mismatch; missing {sorted(set(expected) - seen)}")

    # Trigger-specific structural checks.
    if flags.get("human_performance_claimed") is True:
        if not profile.get("performance", {}).get("performance_window"):
            errors.append("human performance claim requires performance_window")
        if not profile.get("performance", {}).get("interface_channels"):
            errors.append("human performance claim requires interface_channels")
    if flags.get("agency_modes_or_handoff_present") is True:
        if not profile.get("performance", {}).get("agency_segments"):
            errors.append("agency handoff flag requires agency_segments")
    if flags.get("distributed_operation_claimed") is True:
        if not profile.get("arena", {}).get("distributed_relation"):
            errors.append("distributed operation flag requires distributed_relation")
    if flags.get("rules_or_constraints_present") is True:
        if not profile.get("constraints", {}).get("authoritative_sources"):
            errors.append("rules flag requires authoritative_sources")
    if flags.get("sensing_or_tracking_present") is True:
        if not profile.get("sensing", {}).get("observation_estimation_boundary"):
            errors.append("sensing flag requires observation_estimation_boundary")
    if flags.get("measurement_or_comparison_claimed") is True:
        if not profile.get("measurement", {}).get("metrics"):
            errors.append("measurement flag requires metrics")
    if flags.get("contest_or_outcome_present") is True:
        if not profile.get("outcome", {}).get("outcome_and_consequence"):
            errors.append("contest flag requires outcome_and_consequence")
    if flags.get("spatial_function_claimed") is True:
        if not profile.get("spatial_integration", {}).get("functions"):
            errors.append("spatial function flag requires functions")
    if flags.get("participatory_actor_present") is True:
        if not profile.get("actors", {}).get("participatory_relations"):
            errors.append("participatory actor flag requires participatory_relations")
    if flags.get("operational_responsibility_material") is True:
        if not profile.get("human_factors", {}).get("operational_responsibility"):
            errors.append("responsibility flag requires operational_responsibility")
    if flags.get("machine_readable_distribution_provided") is True:
        if not profile.get("distributions"):
            errors.append("distribution flag requires distributions")

    found_keys: set[str] = set()
    walk_keys(profile, found_keys)
    prohibited = sorted(PROHIBITED_KEYS & found_keys)
    if prohibited:
        errors.append(f"profile contains prohibited keys: {prohibited}")

    return errors

def main(argv: list[str]) -> int:
    if len(argv) not in {2, 3}:
        print(
            "Usage: python validate_asr001_profile.py PROFILE.json "
            "[ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.1.json]",
            file=sys.stderr
        )
        return 2
    profile_path = Path(argv[1])
    catalog_path = Path(argv[2]) if len(argv) == 3 else Path(
        "ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.1.json"
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
    print(f"PASS: {profile_path.name} validates against the ASR-001 candidate profile model.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
