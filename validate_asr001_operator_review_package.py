#!/usr/bin/env python3
"""Validate the ASR-001 Sprint 12 operator-review package."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

AUTHORED_FILES = [
    "ASR_001_OPERATOR_REVIEW_BRIEF.md",
    "ASR_001_REVIEWER_GUIDE.md",
    "ASR_001_REVIEWER_CLASS_MATRIX.md",
    "ASR_001_REVIEW_QUESTION_BANK_V0.1.json",
    "ASR_001_CLAUSE_COMMENT_TEMPLATE.md",
    "ASR_001_REVIEW_COMMENT_SCHEMA_V0.1.json",
    "ASR_001_REVIEW_ISSUE_TAXONOMY.md",
    "ASR_001_REVIEWER_EVIDENCE_AND_CONFLICT_DECLARATION.md",
    "ASR_001_COMMENT_DISPOSITION_PROCEDURE.md",
    "ASR_001_REVIEW_CHANGE_CONTROL.md",
    "ASR_001_REVIEW_SAMPLE_SET.md",
    "ASR_001_REVIEW_EVIDENCE_EXCERPT.md",
    "ASR_001_REVIEW_INVITATION_TEMPLATE.md",
    "ASR_001_REVIEW_ACTIVATION_RECORD_TEMPLATE.md",
    "ASR_001_OPERATOR_REVIEW_READINESS_GATE.md",
    "build_asr001_operator_review_package.py",
    "validate_asr001_operator_review_package.py",
    "run_sprint12.py",
    "README.md",
    "SPRINT_12_EXECUTION.md",
    "SPRINT_12_MANIFEST.json",
]

GENERATED_FILES = [
    "ASR_001_OPERATOR_REVIEW_PACKAGE.md",
    "ASR_001_REVIEW_QUESTION_MATRIX.md",
    "ASR_001_REVIEW_PACKAGE_INDEX.json",
    "ASR_001_REVIEW_BASELINE_MANIFEST.json",
]

REPOSITORY_DEPENDENCIES = [
    "ASR_001_OPERATOR_REVIEW_PACKAGE_PREPARATION_AUTHORIZATION.md",
    "ASR_001_INTERNAL_TRIAL_GATE_RESULT.md",
    "ASR_001_WORKING_DRAFT_V0.2.md",
    "ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.2.json",
    "ASR_001_CLAUSE_TO_FIELD_MAP_V0.2.json",
    "ASR_001_PROFILE_MODEL_V0.2.json",
    "ASR_001_PROFILE_SCHEMA_V0.2.json",
    "ASR_001_INTERNAL_TRIAL_RESULTS.md",
    "ASR_001_CLAUSE_FRICTION_REGISTER_V0.1.json",
    "ASR_001_INTERNAL_TRIAL_INDEX_V0.2.json",
    "boundary-cases-001-020.v0.3.json",
    "DECISION_LOG.md",
]

REVIEWER_CLASSES = {
    "RC-01","RC-02","RC-03","RC-04","RC-05","RC-06","RC-07"
}
EXPECTED_DOMAINS = {f"D{i:02d}" for i in range(1, 16)}
PROHIBITED_JSON_KEYS = {
    "total_score","spatiality_score","maturity_level","quality_grade",
    "vendor_rank","product_rank","certification_status","certification_mark",
    "endorsement_status","adoption_status"
}

def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()

def walk_keys(value: Any, keys: set[str]) -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            keys.add(key)
            walk_keys(item, keys)
    elif isinstance(value, list):
        for item in value:
            walk_keys(item, keys)

def taxonomy_types(text: str) -> set[str]:
    return set(re.findall(r"\| `([a-z0-9_]+)` \|", text))

def validate() -> list[str]:
    errors: list[str] = []
    for name in AUTHORED_FILES + GENERATED_FILES + REPOSITORY_DEPENDENCIES:
        if not Path(name).exists():
            errors.append(f"missing required file: {name}")
    if errors:
        return errors

    authorization = Path(
        "ASR_001_OPERATOR_REVIEW_PACKAGE_PREPARATION_AUTHORIZATION.md"
    ).read_text(encoding="utf-8")
    if "AUTHORIZED FOR PACKAGE PREPARATION ONLY" not in authorization:
        errors.append("Sprint 11 package-preparation authorization is missing")
    for phrase in [
        "contacting reviewers",
        "sending invitations",
        "opening a public comment channel"
    ]:
        if phrase not in authorization:
            errors.append(f"preparation boundary missing phrase: {phrase}")

    prior_gate = Path("ASR_001_INTERNAL_TRIAL_GATE_RESULT.md").read_text(
        encoding="utf-8"
    )
    if "PASS — AUTHORIZE OPERATOR-REVIEW PACKAGE PREPARATION ONLY" not in prior_gate:
        errors.append("Sprint 11 readiness decision is missing")

    decision_log = Path("DECISION_LOG.md").read_text(encoding="utf-8")
    if "DEC-014 — ASR-001 Internal Trial Refinement and Operator-Review Preparation Boundary" not in decision_log:
        errors.append("DEC-014 is missing")

    trial_results = Path("ASR_001_INTERNAL_TRIAL_RESULTS.md").read_text(
        encoding="utf-8"
    )
    for phrase in [
        "seven profile artifacts",
        "unresolved blocking friction: **0**",
        "does not authorize sending that package"
    ]:
        if phrase not in trial_results:
            errors.append(f"internal trial result missing: {phrase}")

    working = Path("ASR_001_WORKING_DRAFT_V0.2.md").read_text(encoding="utf-8")
    if working.count("**Candidate clause:**") != 30:
        errors.append("Working Draft v0.2 must contain exactly 30 candidate clauses")
    if "ASR-001 remains unpublished" not in working:
        errors.append("Working Draft publication hold is missing")

    bank = load_json(Path("ASR_001_REVIEW_QUESTION_BANK_V0.1.json"))
    questions = bank.get("questions")
    if not isinstance(questions, list) or len(questions) != 43:
        errors.append("question bank must contain exactly 43 questions")
        questions = []
    if bank.get("question_count") != len(questions):
        errors.append("question_count does not match questions")
    if bank.get("status") != "prepared_not_activated":
        errors.append("question bank status must remain prepared_not_activated")

    question_ids: set[str] = set()
    audience_counts: Counter[str] = Counter()
    domain_coverage: set[str] = set()
    issue_types_used: set[str] = set()
    for item in questions:
        qid = item.get("question_id")
        if not isinstance(qid, str) or not qid:
            errors.append("question lacks question_id")
            continue
        if qid in question_ids:
            errors.append(f"duplicate question id: {qid}")
        question_ids.add(qid)
        audience = item.get("audience")
        if audience not in REVIEWER_CLASSES | {"all"}:
            errors.append(f"{qid} invalid audience: {audience}")
        audience_counts[audience] += 1
        domains = set(item.get("target_domains", []))
        if not domains.issubset(EXPECTED_DOMAINS):
            errors.append(f"{qid} contains invalid target domain")
        domain_coverage.update(domains)
        issue_types_used.update(item.get("expected_issue_types", []))
        if item.get("criticality") not in {"blocking","major","minor","editorial","observation"}:
            errors.append(f"{qid} invalid criticality")
        if not item.get("question"):
            errors.append(f"{qid} has empty question")

    if audience_counts["all"] != 8:
        errors.append("question bank must contain exactly 8 core questions")
    for class_id in REVIEWER_CLASSES:
        if audience_counts[class_id] != 5:
            errors.append(
                f"{class_id} must contain exactly 5 role-specific questions"
            )
    if domain_coverage != EXPECTED_DOMAINS:
        errors.append(
            f"question domain coverage mismatch: {sorted(domain_coverage)}"
        )

    taxonomy = Path("ASR_001_REVIEW_ISSUE_TAXONOMY.md").read_text(
        encoding="utf-8"
    )
    defined_types = taxonomy_types(taxonomy)
    missing_types = sorted(issue_types_used - defined_types)
    if missing_types:
        errors.append(f"question bank uses undefined issue types: {missing_types}")
    for severity in ["blocking","major","minor","editorial","observation"]:
        if f"`{severity}`" not in taxonomy:
            errors.append(f"issue taxonomy missing severity {severity}")
    if "Severity is not a score" not in taxonomy:
        errors.append("taxonomy does not reject score interpretation")

    class_matrix = Path("ASR_001_REVIEWER_CLASS_MATRIX.md").read_text(
        encoding="utf-8"
    )
    for class_id in REVIEWER_CLASSES:
        if class_id not in class_matrix:
            errors.append(f"class matrix missing {class_id}")
    for phrase in [
        "at least four reviewer classes",
        "This is a coverage condition, not a quorum, vote, or adoption threshold"
    ]:
        if phrase not in class_matrix:
            errors.append(f"class matrix missing coverage boundary: {phrase}")

    brief = Path("ASR_001_OPERATOR_REVIEW_BRIEF.md").read_text(
        encoding="utf-8"
    )
    for phrase in [
        "Package prepared; review not activated",
        "written review only",
        "Repository visibility does not by itself",
        "Reviewers are not asked to endorse"
    ]:
        if phrase not in brief:
            errors.append(f"operator brief missing: {phrase}")

    guide = Path("ASR_001_REVIEWER_GUIDE.md").read_text(encoding="utf-8")
    for phrase in [
        "Written and asynchronous after activation",
        "not a Public Review Draft",
        "Participation does not constitute"
    ]:
        if phrase not in guide:
            errors.append(f"reviewer guide missing: {phrase}")

    invitation = Path("ASR_001_REVIEW_INVITATION_TEMPLATE.md").read_text(
        encoding="utf-8"
    )
    if "**Status:** Prepared template — not sent" not in invitation:
        errors.append("invitation template is not visibly inactive")
    if "[Name]" not in invitation or "[Written contact channel]" not in invitation:
        errors.append("invitation template appears personalized or active")
    if "This template remains inactive until the owner" not in invitation:
        errors.append("invitation activation boundary is missing")

    activation = Path(
        "ASR_001_REVIEW_ACTIVATION_RECORD_TEMPLATE.md"
    ).read_text(encoding="utf-8")
    for phrase in [
        "Template only — no review wave is active",
        "ACTIVATE LIMITED WRITTEN REVIEW",
        "no public comment channel is opened"
    ]:
        if phrase not in activation:
            errors.append(f"activation record template missing: {phrase}")

    comment_schema = load_json(Path("ASR_001_REVIEW_COMMENT_SCHEMA_V0.1.json"))
    reviewer_enum = (
        comment_schema.get("properties", {})
        .get("reviewer", {})
        .get("properties", {})
        .get("reviewer_class", {})
        .get("enum", [])
    )
    if set(reviewer_enum) != REVIEWER_CLASSES:
        errors.append("comment schema reviewer classes are incomplete")
    confirmations = (
        comment_schema.get("properties", {})
        .get("confirmations", {})
        .get("properties", {})
    )
    if confirmations.get("not_endorsement", {}).get("const") is not True:
        errors.append("comment schema must require non-endorsement confirmation")
    scope_impact = (
        comment_schema.get("properties", {})
        .get("proposed_disposition", {})
        .get("properties", {})
        .get("scope_impact", {})
        .get("enum", [])
    )
    if "potential_expansion_requires_hold" not in scope_impact:
        errors.append("comment schema lacks scope-expansion hold state")

    disposition = Path("ASR_001_COMMENT_DISPOSITION_PROCEDURE.md").read_text(
        encoding="utf-8"
    )
    for phrase in [
        "A blocking issue cannot be closed as `no change`",
        "No Voting",
        "Scope Expansion Hold"
    ]:
        if phrase not in disposition:
            errors.append(f"disposition procedure missing: {phrase}")

    change_control = Path("ASR_001_REVIEW_CHANGE_CONTROL.md").read_text(
        encoding="utf-8"
    )
    for phrase in [
        "Frozen Baseline",
        "Review Wave Isolation",
        "No Adoption Claim"
    ]:
        if phrase not in change_control:
            errors.append(f"change control missing: {phrase}")

    package = Path("ASR_001_OPERATOR_REVIEW_PACKAGE.md").read_text(
        encoding="utf-8"
    )
    for phrase in [
        "Prepared; owner activation required",
        "Not a Public Review Draft",
        "eight core questions and five role-specific questions",
        "publicly visible repository"
    ]:
        if phrase not in package:
            errors.append(f"assembled package missing: {phrase}")

    matrix = Path("ASR_001_REVIEW_QUESTION_MATRIX.md").read_text(
        encoding="utf-8"
    )
    for qid in question_ids:
        if qid not in matrix:
            errors.append(f"question matrix missing {qid}")

    index = load_json(Path("ASR_001_REVIEW_PACKAGE_INDEX.json"))
    if index.get("public_review") is not False:
        errors.append("package index must keep public_review=false")
    if index.get("outreach_performed") is not False:
        errors.append("package index must keep outreach_performed=false")
    if index.get("review_mode") != "limited_asynchronous_written_only":
        errors.append("package index review mode is incorrect")
    if index.get("status") != "ready_subject_to_gate_owner_activation_required":
        errors.append("package index status is incorrect")

    baseline = load_json(Path("ASR_001_REVIEW_BASELINE_MANIFEST.json"))
    if baseline.get("review_status") != "prepared_not_activated":
        errors.append("baseline manifest review status is incorrect")
    if baseline.get("public_review_status") != "not_public_review":
        errors.append("baseline manifest public review status is incorrect")
    entries = baseline.get("files", [])
    if baseline.get("file_count") != len(entries):
        errors.append("baseline manifest file_count mismatch")
    for entry in entries:
        path = Path(entry.get("path", ""))
        if not path.exists():
            errors.append(f"baseline manifest references missing file: {path}")
            continue
        if entry.get("sha256") != sha256(path):
            errors.append(f"baseline hash mismatch: {path}")

    friction = load_json(Path("ASR_001_CLAUSE_FRICTION_REGISTER_V0.1.json"))
    if friction.get("status") != "dispositioned":
        errors.append("Sprint 11 friction register is not dispositioned")
    items = friction.get("items", [])
    if len(items) != 8:
        errors.append("Sprint 11 friction register must contain 8 items")
    if any(item.get("scope_effect") != "none" for item in items):
        errors.append("Sprint 11 friction register contains scope expansion")

    corpus = load_json(Path("boundary-cases-001-020.v0.3.json"))
    if corpus.get("case_count") != 20 or len(corpus.get("cases", [])) != 20:
        errors.append("research corpus must remain 20 cases")

    gate = Path("ASR_001_OPERATOR_REVIEW_READINESS_GATE.md").read_text(
        encoding="utf-8"
    )
    if "PASS — PACKAGE READY; OWNER ACTIVATION REQUIRED FOR LIMITED WRITTEN OPERATOR REVIEW" not in gate:
        errors.append("Sprint 12 gate decision is missing")
    if "A PASS does not send the package" not in gate:
        errors.append("Sprint 12 gate does not preserve no-outreach boundary")

    all_json = [bank, comment_schema, index, baseline]
    found_keys: set[str] = set()
    for data in all_json:
        walk_keys(data, found_keys)
    prohibited = sorted(PROHIBITED_JSON_KEYS & found_keys)
    if prohibited:
        errors.append(f"package JSON contains prohibited status keys: {prohibited}")

    return errors

def main() -> int:
    try:
        errors = validate()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: package validation could not run: {exc}", file=sys.stderr)
        return 2
    if errors:
        print(f"FAIL: {len(errors)} operator-review package error(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: ASR-001 operator-review package is complete and review-ready subject to owner activation.")
    print("PASS: no outreach, Public Review, publication, certification, or adoption status is created.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
