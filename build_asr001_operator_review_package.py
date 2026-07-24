#!/usr/bin/env python3
"""Build the ASR-001 operator-review package, question matrix, index, and frozen baseline."""
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any

QUESTION_BANK = Path("ASR_001_REVIEW_QUESTION_BANK_V0.1.json")

BASELINE_FILES = [
    "ASR_001_WORKING_DRAFT_V0.2.md",
    "ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.2.json",
    "ASR_001_CLAUSE_TO_FIELD_MAP_V0.2.json",
    "ASR_001_PROFILE_MODEL_V0.2.json",
    "ASR_001_PROFILE_SCHEMA_V0.2.json",
    "ASR_001_INTERNAL_TRIAL_RESULTS.md",
    "ASR_001_CLAUSE_FRICTION_REGISTER_V0.1.json",
    "ASR_001_INTERNAL_TRIAL_INDEX_V0.2.json",
]

PACKAGE_SOURCE_FILES = [
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
]

REVIEWER_CLASS_NAMES = {
    "RC-01": "Sport governance and integrity",
    "RC-02": "Competition operations",
    "RC-03": "XR and spatial-system engineering",
    "RC-04": "Performance measurement",
    "RC-05": "Accessibility and adaptive sport",
    "RC-06": "Research methodology",
    "RC-07": "Evidence and data governance",
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

def build_question_matrix(bank: dict[str, Any]) -> None:
    questions = bank["questions"]
    lines = [
        "# ASR-001 Operator Review Question Matrix",
        "",
        "**Version:** 0.1  ",
        "**Status:** Prepared; review not activated  ",
        f"**Question count:** {len(questions)}",
        "",
        "## Core Questions",
        "",
        "| ID | Question | Domains | Issue types | Response | Criticality |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in questions:
        if item["audience"] != "all":
            continue
        text = item["question"].replace("|", "\\|")
        lines.append(
            f"| `{item['question_id']}` | {text} | "
            f"{', '.join(item['target_domains'])} | "
            f"{', '.join(item['expected_issue_types'])} | "
            f"`{item['response_type']}` | `{item['criticality']}` |"
        )

    for class_id, class_name in REVIEWER_CLASS_NAMES.items():
        lines += [
            "",
            f"## {class_id} — {class_name}",
            "",
            "| ID | Question | Domains | Clauses | Issue types | Criticality |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
        for item in questions:
            if item["audience"] != class_id:
                continue
            text = item["question"].replace("|", "\\|")
            clauses = ", ".join(item["target_clauses"]) or "cross-domain"
            lines.append(
                f"| `{item['question_id']}` | {text} | "
                f"{', '.join(item['target_domains'])} | {clauses} | "
                f"{', '.join(item['expected_issue_types'])} | "
                f"`{item['criticality']}` |"
            )

    lines += [
        "",
        "## Interpretation",
        "",
        "Criticality organizes review attention. It is not a numerical score, vote, reviewer rank, or adoption threshold.",
        "",
    ]
    Path("ASR_001_REVIEW_QUESTION_MATRIX.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )

def build_baseline_manifest() -> dict[str, Any]:
    entries = []
    for name in BASELINE_FILES + PACKAGE_SOURCE_FILES:
        path = Path(name)
        entries.append({
            "path": name,
            "sha256": sha256(path),
            "role": "working_draft_baseline" if name in BASELINE_FILES else "review_package_source",
        })
    manifest = {
        "manifest_id": "ASR001-OPERATOR-REVIEW-BASELINE",
        "version": "0.1",
        "created_date": date.today().isoformat(),
        "working_draft": "ASR-001 v0.2",
        "review_status": "prepared_not_activated",
        "public_review_status": "not_public_review",
        "file_count": len(entries),
        "files": entries,
        "interpretation": (
            "Hashes freeze the review reference. Repository visibility does not activate "
            "review or create Public Review Draft status."
        ),
    }
    Path("ASR_001_REVIEW_BASELINE_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )
    return manifest

def build_package_index(bank: dict[str, Any], baseline: dict[str, Any]) -> None:
    audience_counts = Counter(item["audience"] for item in bank["questions"])
    domains = sorted({
        domain
        for item in bank["questions"]
        for domain in item["target_domains"]
    })
    index = {
        "package_id": "ASR001-OPERATOR-REVIEW-PACKAGE",
        "version": "0.1",
        "status": "ready_subject_to_gate_owner_activation_required",
        "working_draft_baseline": "ASR-001 v0.2",
        "review_mode": "limited_asynchronous_written_only",
        "public_review": False,
        "outreach_performed": False,
        "reviewer_classes": [
            {"class_id": key, "name": value}
            for key, value in REVIEWER_CLASS_NAMES.items()
        ],
        "question_summary": {
            "total": bank["question_count"],
            "core": audience_counts["all"],
            "per_class": {
                key: audience_counts[key] for key in REVIEWER_CLASS_NAMES
            },
            "domain_coverage": domains,
        },
        "package_documents": PACKAGE_SOURCE_FILES + [
            "ASR_001_REVIEW_QUESTION_MATRIX.md",
            "ASR_001_REVIEW_BASELINE_MANIFEST.json",
            "ASR_001_OPERATOR_REVIEW_PACKAGE.md",
        ],
        "baseline_manifest": baseline["manifest_id"],
        "activation_condition": (
            "Explicit owner decision after reviewer roster, coverage, conflict declarations, "
            "and written-only channel are documented."
        ),
        "prohibited_claims": [
            "endorsement", "adoption", "partnership", "federation_recognition",
            "certification", "public_conformance", "safety_approval",
            "clinical_validation", "score", "ranking", "industry_adoption"
        ],
    }
    Path("ASR_001_REVIEW_PACKAGE_INDEX.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )

def build_package_document(bank: dict[str, Any]) -> None:
    audience_counts = Counter(item["audience"] for item in bank["questions"])
    lines = [
        "# ASR-001 Operator Review Package",
        "",
        "**Package version:** 0.1  ",
        "**Working Draft baseline:** ASR-001 v0.2  ",
        "**Status:** Prepared; owner activation required  ",
        "**Review mode after activation:** Limited, asynchronous, written only  ",
        "**Public Review status:** Not a Public Review Draft",
        "",
        "## 1. Package Purpose",
        "",
        "This package prepares a multidisciplinary operator review of the ASR-001 evidence-profile Working Draft.",
        "",
        "It does not contact reviewers, open public comment, publish ASR-001, or establish certification or conformance for an underlying system.",
        "",
        "## 2. Review Sequence",
        "",
        "1. Read the operator brief and reviewer guide.",
        "2. Complete the conflict and evidence declaration.",
        "3. Review assigned domains, clauses, and profile fields.",
        "4. Inspect assigned internal trial profiles.",
        "5. Answer eight core questions and five role-specific questions.",
        "6. Submit material issues through the clause comment template or schema.",
        "7. Receive a written disposition after issue intake is authorized.",
        "",
        "## 3. Reviewer Classes",
        "",
    ]
    for class_id, name in REVIEWER_CLASS_NAMES.items():
        lines.append(
            f"- `{class_id}` — {name}: {audience_counts[class_id]} role-specific questions."
        )
    lines += [
        "",
        "## 4. Question Coverage",
        "",
        f"- total questions: **{bank['question_count']}**",
        f"- core questions: **{audience_counts['all']}**",
        "- role-specific questions: **5 per reviewer class**",
        "- domain coverage: **D01–D15**",
        "",
        "See `ASR_001_REVIEW_QUESTION_MATRIX.md`.",
        "",
        "## 5. Comment and Issue Controls",
        "",
        "- `ASR_001_CLAUSE_COMMENT_TEMPLATE.md`",
        "- `ASR_001_REVIEW_COMMENT_SCHEMA_V0.1.json`",
        "- `ASR_001_REVIEW_ISSUE_TAXONOMY.md`",
        "- `ASR_001_COMMENT_DISPOSITION_PROCEDURE.md`",
        "- `ASR_001_REVIEW_CHANGE_CONTROL.md`",
        "",
        "Comments are clause-addressable, evidence-classified, conflict-disclosed, and dispositioned without voting or reviewer ranking.",
        "",
        "## 6. Evidence and Trial Material",
        "",
        "- `ASR_001_REVIEW_SAMPLE_SET.md`",
        "- `ASR_001_REVIEW_EVIDENCE_EXCERPT.md`",
        "- `ASR_001_INTERNAL_TRIAL_RESULTS.md`",
        "",
        "Trial profiles are case-derived synthetic fixtures and are not real-provider conformance records.",
        "",
        "## 7. Baseline Integrity",
        "",
        "`ASR_001_REVIEW_BASELINE_MANIFEST.json` freezes the Working Draft and package source files through SHA-256.",
        "",
        "The active review baseline cannot be changed silently.",
        "",
        "## 8. Activation Boundary",
        "",
        "The package is not active merely because it exists in a publicly visible repository.",
        "",
        "Limited written review begins only after the owner records:",
        "",
        "- the reviewer roster;",
        "- class coverage;",
        "- conflict declarations;",
        "- attribution preferences;",
        "- the frozen baseline identifier;",
        "- the written response channel;",
        "- an explicit activation decision recorded through `ASR_001_REVIEW_ACTIVATION_RECORD_TEMPLATE.md`.",
        "",
        "## 9. Prohibited Interpretations",
        "",
        "Review participation does not mean endorsement, adoption, certification, partnership, recognition, or approval.",
        "",
        "Package readiness does not mean Public Review Draft status.",
        "",
    ]
    Path("ASR_001_OPERATOR_REVIEW_PACKAGE.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )

def main() -> int:
    bank = load_json(QUESTION_BANK)
    build_question_matrix(bank)
    baseline = build_baseline_manifest()
    build_package_document(bank)
    build_package_index(bank, baseline)
    print("PASS: wrote ASR_001_REVIEW_QUESTION_MATRIX.md")
    print("PASS: wrote ASR_001_REVIEW_BASELINE_MANIFEST.json")
    print("PASS: wrote ASR_001_OPERATOR_REVIEW_PACKAGE.md")
    print("PASS: wrote ASR_001_REVIEW_PACKAGE_INDEX.json")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
