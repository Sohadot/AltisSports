#!/usr/bin/env python3
"""Validate ASR-001 Sprint 9 Working Draft architecture."""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

PACKAGE_FILES = [
    "ASR_001_WORKING_DRAFT_ARCHITECTURE.md",
    "ASR_001_CLAUSE_CATALOG_V0.1.json",
    "ASR_001_APPLICABILITY_MODEL.md",
    "ASR_001_VERIFICATION_MODEL_DRAFT.md",
    "ASR_001_IMPLEMENTATION_MODEL_BOUNDARY.md",
    "ASR_001_INFORMATIVE_EXAMPLES_BOUNDARY.md",
    "ASR_001_WORKING_DRAFT_GATE.md",
    "ASR_001_EVIDENCE_TO_CLAUSE_MAP.md",
    "ASR_001_CLAUSE_COVERAGE_REPORT.md",
]

REPOSITORY_DEPENDENCIES = [
    "ASR_001_SCOPE_DRAFT.md",
    "ASR_001_SCOPE_MODEL.json",
    "ASR_001_SCOPE_GATE_RESULT.md",
    "ASR_001_REQUIREMENTS_DRAFTING_AUTHORIZATION.md",
    "ASR_001_DEFERRED_ISSUES.md",
    "ASR_DRAFTING_GOVERNANCE.md",
    "boundary-cases-001-020.v0.3.json",
    "DECISION_LOG.md",
]

VALID_APPLICABILITY = {
    "always", "when_feature_present", "when_claim_made",
    "when_measurement_or_comparison_claimed", "when_contest_or_outcome_present",
    "when_distributed_operation_claimed", "when_human_performance_claimed",
    "when_machine_readable_distribution_provided",
}

VALID_VERIFICATION = {
    "document_presence", "field_presence", "cross_reference_integrity",
    "evidence_traceability", "controlled_vocabulary", "conditional_logic",
    "temporal_consistency", "human_review", "machine_validation",
}

REQUIRED_CLAUSE_FIELDS = {
    "clause_id", "domain_id", "domain_name", "title",
    "candidate_obligation_intent", "clause_family", "applicability_class",
    "applicability_condition", "problem_addressed", "evidence_case_refs",
    "governance_dependencies", "verification_modes", "rationale",
    "uncertainty_handling", "exclusions_guarded", "drafting_status",
}

NORMATIVE_TOKENS = ["MUST", "MUST NOT", "SHOULD", "SHOULD NOT", "SHALL", "SHALL NOT"]

def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value

def validate() -> list[str]:
    errors: list[str] = []
    for name in PACKAGE_FILES + REPOSITORY_DEPENDENCIES:
        if not Path(name).exists():
            errors.append(f"missing required file: {name}")
    if errors:
        return errors

    authorization = Path("ASR_001_REQUIREMENTS_DRAFTING_AUTHORIZATION.md").read_text(encoding="utf-8")
    if "AUTHORIZED FOR GOVERNED WORKING-DRAFT REQUIREMENTS ONLY" not in authorization:
        errors.append("requirements-drafting authorization is missing")

    scope_gate = Path("ASR_001_SCOPE_GATE_RESULT.md").read_text(encoding="utf-8")
    if "APPROVE SCOPE — AUTHORIZE REQUIREMENTS DRAFTING ONLY" not in scope_gate:
        errors.append("scope gate approval is missing")

    decision_log = Path("DECISION_LOG.md").read_text(encoding="utf-8")
    if "DEC-011 — ASR-001 Scope Approval and Requirements-Drafting Boundary" not in decision_log:
        errors.append("DEC-011 is missing from DECISION_LOG.md")

    architecture = Path("ASR_001_WORKING_DRAFT_ARCHITECTURE.md").read_text(encoding="utf-8")
    for domain in [f"D{i:02d}" for i in range(1, 16)]:
        if domain not in architecture:
            errors.append(f"architecture missing domain {domain}")
    if "It cannot convert profile conformance into" not in architecture:
        errors.append("architecture does not preserve profile-only conformance boundary")

    implementation = Path("ASR_001_IMPLEMENTATION_MODEL_BOUNDARY.md").read_text(encoding="utf-8")
    if "No ASR-001 implementation schema is authorized by Sprint 9." not in implementation:
        errors.append("implementation-schema hold is missing")

    data = load_json(Path("ASR_001_CLAUSE_CATALOG_V0.1.json"))
    clauses = data.get("candidate_clauses")
    if not isinstance(clauses, list):
        return errors + ["candidate_clauses must be a list"]
    if data.get("status") != "candidate_not_yet_normative":
        errors.append("catalog status must remain candidate_not_yet_normative")
    if data.get("candidate_clause_count") != 30 or len(clauses) != 30:
        errors.append("catalog must contain exactly 30 candidate clauses")

    seen: set[str] = set()
    counts: Counter[str] = Counter()
    pattern = re.compile(r"^ASR001-(D(?:0[1-9]|1[0-5]))-C(0[1-9]|[1-9][0-9])$")
    for index, item in enumerate(clauses, start=1):
        if not isinstance(item, dict):
            errors.append(f"clause #{index} is not an object")
            continue
        missing = REQUIRED_CLAUSE_FIELDS - set(item)
        if missing:
            errors.append(f"clause #{index} missing fields: {sorted(missing)}")
            continue
        clause_id = item["clause_id"]
        match = pattern.fullmatch(clause_id)
        if not match:
            errors.append(f"invalid clause identifier: {clause_id}")
            continue
        domain = match.group(1)
        if item["domain_id"] != domain:
            errors.append(f"{clause_id} domain mismatch")
        if clause_id in seen:
            errors.append(f"duplicate clause identifier: {clause_id}")
        seen.add(clause_id)
        counts[domain] += 1

        if item["drafting_status"] != "candidate_not_yet_normative":
            errors.append(f"{clause_id} has invalid drafting status")
        if item["applicability_class"] not in VALID_APPLICABILITY:
            errors.append(f"{clause_id} has invalid applicability class")
        modes = item["verification_modes"]
        if not isinstance(modes, list) or not modes:
            errors.append(f"{clause_id} needs verification modes")
        elif not set(modes).issubset(VALID_VERIFICATION):
            errors.append(f"{clause_id} has invalid verification mode")
        if not item["evidence_case_refs"] and not item["governance_dependencies"]:
            errors.append(f"{clause_id} lacks evidence and governance dependencies")
        for case in item["evidence_case_refs"]:
            if not re.fullmatch(r"BC-(?:00[1-9]|01[0-9]|020)", case):
                errors.append(f"{clause_id} has invalid case ref {case}")
        intent = item["candidate_obligation_intent"]
        for token in NORMATIVE_TOKENS:
            if re.search(rf"\b{re.escape(token)}\b", intent):
                errors.append(f"{clause_id} prematurely uses normative token {token}")
        for key in [
            "title", "candidate_obligation_intent", "applicability_condition",
            "problem_addressed", "rationale", "uncertainty_handling"
        ]:
            if not isinstance(item[key], str) or not item[key].strip():
                errors.append(f"{clause_id} has empty {key}")

    expected_domains = {f"D{i:02d}" for i in range(1, 16)}
    if set(counts) != expected_domains:
        errors.append(f"catalog domain coverage mismatch: {sorted(counts)}")
    for domain in expected_domains:
        if counts[domain] != 2:
            errors.append(f"{domain} must have exactly 2 candidate clauses; got {counts[domain]}")

    map_text = Path("ASR_001_EVIDENCE_TO_CLAUSE_MAP.md").read_text(encoding="utf-8")
    for clause_id in seen:
        if clause_id not in map_text:
            errors.append(f"evidence map missing {clause_id}")

    coverage = Path("ASR_001_CLAUSE_COVERAGE_REPORT.md").read_text(encoding="utf-8")
    if "candidate clauses: **30**" not in coverage:
        errors.append("coverage report does not confirm 30 clauses")
    if "approved domains covered: **15**" not in coverage:
        errors.append("coverage report does not confirm 15 domains")

    corpus = load_json(Path("boundary-cases-001-020.v0.3.json"))
    if corpus.get("case_count") != 20 or len(corpus.get("cases", [])) != 20:
        errors.append("current corpus must contain 20 cases")

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
    print("PASS: ASR-001 Working Draft architecture and 30 candidate clauses validate.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
