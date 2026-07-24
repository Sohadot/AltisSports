#!/usr/bin/env python3
"""Validate Sprint 10 Candidate Normative Core and implementation model."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any

AUTHORED_FILES = [
    "ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.1.json",
    "ASR_001_PROFILE_MODEL_V0.1.json",
    "ASR_001_PROFILE_SCHEMA_V0.1.json",
    "ASR_001_SYNTHETIC_PROFILE_LOCAL_V0.1.json",
    "ASR_001_SYNTHETIC_PROFILE_DISTRIBUTED_V0.1.json",
    "ASR_001_CONFORMANCE_BOUNDARY_DRAFT.md",
    "ASR_001_NORMATIVE_CORE_GATE.md",
    "build_asr001_working_draft_v0_1.py",
    "validate_asr001_profile.py",
    "validate_asr001_working_draft_v0_1.py",
    "run_sprint10.py",
]

GENERATED_FILES = [
    "ASR_001_WORKING_DRAFT_V0.1.md",
    "ASR_001_CLAUSE_TO_FIELD_MAP_V0.1.json",
]

REPOSITORY_DEPENDENCIES = [
    "ASR_001_CLAUSE_CATALOG_V0.1.json",
    "ASR_001_CLAUSE_AUTHORING_AUTHORIZATION.md",
    "ASR_001_WORKING_DRAFT_GATE_RESULT.md",
    "ASR_001_SCOPE_DRAFT.md",
    "ASR_001_SCOPE_MODEL.json",
    "ASR_001_DEFERRED_ISSUES.md",
    "ASR_DRAFTING_GOVERNANCE.md",
    "boundary-cases-001-020.v0.3.json",
    "DECISION_LOG.md",
]

PROHIBITED_MODEL_KEYS = {
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

def validate() -> list[str]:
    errors: list[str] = []
    for name in AUTHORED_FILES + GENERATED_FILES + REPOSITORY_DEPENDENCIES:
        if not Path(name).exists():
            errors.append(f"missing required file: {name}")
    if errors:
        return errors

    authorization = Path("ASR_001_CLAUSE_AUTHORING_AUTHORIZATION.md").read_text(encoding="utf-8")
    if "AUTHORIZED FOR NON-PUBLIC WORKING-DRAFT CLAUSE AUTHORING ONLY" not in authorization:
        errors.append("candidate clause authoring is not authorized")

    prior_gate = Path("ASR_001_WORKING_DRAFT_GATE_RESULT.md").read_text(encoding="utf-8")
    if "PASS — AUTHORIZE CANDIDATE CLAUSE AUTHORING ONLY" not in prior_gate:
        errors.append("Sprint 9 Working Draft gate authorization is missing")

    decision_log = Path("DECISION_LOG.md").read_text(encoding="utf-8")
    if "DEC-012 — ASR-001 Working Draft Architecture and Clause-Authoring Boundary" not in decision_log:
        errors.append("DEC-012 is missing")

    source = load_json(Path("ASR_001_CLAUSE_CATALOG_V0.1.json"))
    norm = load_json(Path("ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.1.json"))
    source_ids = [item["clause_id"] for item in source.get("candidate_clauses", [])]
    clauses = norm.get("clauses")
    if not isinstance(clauses, list) or len(clauses) != 30:
        errors.append("normative catalog must contain exactly 30 clauses")
        return errors
    norm_ids = [item.get("clause_id") for item in clauses]
    if norm_ids != source_ids:
        errors.append("normative catalog clause order or identifiers diverge from Sprint 9 source catalog")
    if norm.get("status") != "candidate_normative_non_public":
        errors.append("normative catalog status must be candidate_normative_non_public")
    if norm.get("publication_status") != "unpublished":
        errors.append("normative catalog publication status must remain unpublished")
    if norm.get("conformance_boundary") != "profile_document_or_instance_only":
        errors.append("normative catalog conformance boundary must remain profile-only")

    counts = Counter()
    paths: set[str] = set()
    for item in clauses:
        cid = item.get("clause_id", "")
        match = re.fullmatch(r"ASR001-(D(?:0[1-9]|1[0-5]))-C(?:0[1-9]|[1-9][0-9])", cid)
        if not match:
            errors.append(f"invalid clause id: {cid}")
            continue
        counts[match.group(1)] += 1
        text = item.get("normative_text", "")
        if " MUST " not in f" {text} ":
            errors.append(f"{cid} lacks candidate MUST language")
        if any(token in text for token in ["certifies the product", "certifies the sport", "industry approved"]):
            errors.append(f"{cid} contains prohibited external-status language")
        if item.get("drafting_status") != "candidate_normative_working_draft":
            errors.append(f"{cid} drafting status mismatch")
        field_path = item.get("profile_field_path")
        if not isinstance(field_path, str) or not field_path:
            errors.append(f"{cid} lacks profile_field_path")
        elif field_path in paths:
            errors.append(f"duplicate field path: {field_path}")
        else:
            paths.add(field_path)
        if not item.get("verification_statement"):
            errors.append(f"{cid} lacks verification statement")
        if not item.get("exclusions_guarded"):
            errors.append(f"{cid} lacks exclusion guards")

    expected_domains = {f"D{i:02d}" for i in range(1, 16)}
    if set(counts) != expected_domains:
        errors.append(f"domain coverage mismatch: {sorted(counts)}")
    for domain in expected_domains:
        if counts[domain] != 2:
            errors.append(f"{domain} must contain exactly two clauses")

    working = Path("ASR_001_WORKING_DRAFT_V0.1.md").read_text(encoding="utf-8")
    if "**Status:** Candidate Normative Core — unpublished" not in working:
        errors.append("Working Draft publication hold is not visible")
    for cid in norm_ids:
        if cid not in working:
            errors.append(f"Working Draft missing {cid}")
    if working.count("**Candidate clause:**") != 30:
        errors.append("Working Draft must render exactly 30 candidate clauses")
    for phrase in [
        "It does not certify the underlying sport",
        "ASR-001 remains unpublished"
    ]:
        if phrase not in working:
            errors.append(f"Working Draft missing boundary phrase: {phrase}")

    field_map = load_json(Path("ASR_001_CLAUSE_TO_FIELD_MAP_V0.1.json"))
    mappings = field_map.get("mappings")
    if not isinstance(mappings, list) or len(mappings) != 30:
        errors.append("clause-to-field map must contain 30 mappings")
    else:
        mapped_ids = [item.get("clause_id") for item in mappings]
        if mapped_ids != norm_ids:
            errors.append("clause-to-field map IDs diverge from normative catalog")

    model = load_json(Path("ASR_001_PROFILE_MODEL_V0.1.json"))
    boundary = model.get("conformance_boundary", {})
    if boundary.get("profile_document_or_instance_only") is not True:
        errors.append("profile model must preserve profile-only conformance")
    for key in [
        "underlying_system_certification", "sport_certification",
        "product_quality_endorsement", "safety_or_clinical_certification"
    ]:
        if boundary.get(key) is not False:
            errors.append(f"profile model must keep {key}=false")
    if model.get("publication_status") != "unpublished":
        errors.append("profile model publication status must remain unpublished")

    schema = load_json(Path("ASR_001_PROFILE_SCHEMA_V0.1.json"))
    if schema.get("description") != "Non-public Working Draft schema. Validation concerns the profile instance only.":
        errors.append("profile schema description does not preserve candidate boundary")
    records_schema = (
        schema.get("properties", {})
        .get("clause_records", {})
    )
    if records_schema.get("minItems") != 30 or records_schema.get("maxItems") != 30:
        errors.append("profile schema must require exactly 30 clause records")

    found_keys: set[str] = set()
    walk_keys(model, found_keys)
    walk_keys(schema, found_keys)
    prohibited = sorted(PROHIBITED_MODEL_KEYS & found_keys)
    if prohibited:
        errors.append(f"candidate model contains prohibited keys: {prohibited}")

    conformance = Path("ASR_001_CONFORMANCE_BOUNDARY_DRAFT.md").read_text(encoding="utf-8")
    for phrase in [
        "Candidate conformance applies only to",
        "No certification body, mark, badge, register, public claim, or commercial certification service is authorized."
    ]:
        if phrase not in conformance:
            errors.append(f"conformance boundary missing: {phrase}")

    corpus = load_json(Path("boundary-cases-001-020.v0.3.json"))
    if corpus.get("case_count") != 20 or len(corpus.get("cases", [])) != 20:
        errors.append("current research corpus must remain twenty cases")

    for profile_name in [
        "ASR_001_SYNTHETIC_PROFILE_LOCAL_V0.1.json",
        "ASR_001_SYNTHETIC_PROFILE_DISTRIBUTED_V0.1.json"
    ]:
        result = subprocess.run(
            [sys.executable, "validate_asr001_profile.py", profile_name],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            errors.append(f"{profile_name} failed profile validation: {result.stdout}{result.stderr}")

    return errors

def main() -> int:
    try:
        errors = validate()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: validation could not run: {exc}", file=sys.stderr)
        return 2
    if errors:
        print(f"FAIL: {len(errors)} validation error(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: ASR-001 Candidate Normative Core and implementation profile model v0.1 validate.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
