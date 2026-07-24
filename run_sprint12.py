#!/usr/bin/env python3
"""Run Sprint 12 package build, validation, decision append, and readiness outputs."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

DECISION_MARKER = "## DEC-015 — ASR-001 Operator Review Readiness and Owner-Activation Boundary"

DECISION_TEXT = """
---

## DEC-015 — ASR-001 Operator Review Readiness and Owner-Activation Boundary

**Status:** Ratified upon Sprint 12 PASS  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `ASR_001_OPERATOR_REVIEW_PACKAGE.md`, `ASR_001_REVIEW_BASELINE_MANIFEST.json`, and `ASR_001_OPERATOR_REVIEW_READINESS_RESULT.md`

### Decision

1. The ASR-001 Operator Review Package v0.1 is accepted as complete and review-ready.
2. The review baseline is ASR-001 Working Draft v0.2 together with its thirty-clause catalog, clause-to-field map, profile model, schema, internal-trial results, and frozen SHA-256 manifest.
3. The prepared package contains seven reviewer classes and forty-three questions: eight core questions and five role-specific questions for each class.
4. The permitted review mode is limited, asynchronous, and written only.
5. Calls, interviews, open public-comment channels, and implied endorsement or adoption are outside the permitted first-wave mode.
6. Public repository visibility does not activate review, create Public Review Draft status, invite unrestricted comment, or establish adoption.
7. Review comments are clause-addressable, conflict-disclosed, evidence-classified, and dispositioned through written change control.
8. Review participation does not constitute endorsement, adoption, partnership, federation recognition, certification, or approval of the category thesis.
9. No reviewer contact or invitation has occurred through Sprint 12.
10. A limited written review can begin only after the owner records an explicit activation decision, reviewer roster, class coverage, conflict-declaration identifiers, written channel, and frozen baseline.
11. The first-wave coverage design includes at least four reviewer classes: an operational class, a technical or measurement class, a human-impact or methodology class, and evidence/data governance.
12. Public Review Draft status, ASR-001 publication, certification, public conformance claims, scores, rankings, unsupported remote-synchronous tolerances, final BCI athletic classification, federation-recognition claims, and industry-adoption claims remain unauthorized.

### Rationale

The internal Working Draft now has sufficient structure, trial evidence, question coverage, comment intake, issue classification, conflict disclosure, and change control for a bounded operator review. Readiness does not justify automatic outreach. Owner activation is retained as a separate governance act so that reviewer selection, written-only mode, baseline integrity, and non-endorsement boundaries remain deliberate.
""".strip() + "\n"

TRACKED_FILES = [
    "ASR_001_OPERATOR_REVIEW_PACKAGE.md",
    "ASR_001_REVIEW_QUESTION_MATRIX.md",
    "ASR_001_REVIEW_PACKAGE_INDEX.json",
    "ASR_001_REVIEW_BASELINE_MANIFEST.json",
    "ASR_001_OPERATOR_REVIEW_BRIEF.md",
    "ASR_001_REVIEWER_GUIDE.md",
    "ASR_001_REVIEW_QUESTION_BANK_V0.1.json",
    "ASR_001_REVIEW_COMMENT_SCHEMA_V0.1.json",
    "ASR_001_COMMENT_DISPOSITION_PROCEDURE.md",
    "ASR_001_REVIEW_CHANGE_CONTROL.md",
    "ASR_001_OPERATOR_REVIEW_READINESS_GATE.md",
]

def run(command: list[str]) -> int:
    return subprocess.run(command).returncode

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()

def append_decision() -> bool:
    path = Path("DECISION_LOG.md")
    content = path.read_text(encoding="utf-8")
    if DECISION_MARKER in content:
        return False
    if "## DEC-014 — ASR-001 Internal Trial Refinement and Operator-Review Preparation Boundary" not in content:
        raise RuntimeError("DEC-014 is missing; refusing to append DEC-015")
    path.write_text(content.rstrip() + "\n\n" + DECISION_TEXT, encoding="utf-8")
    return True

def write_outputs(appended: bool) -> None:
    hashes = {name: sha256(Path(name)) for name in TRACKED_FILES}

    lines = [
        "# Sprint 12 Validation Result", "",
        "**Asset:** AltisSports  ",
        "**Sprint:** Sprint 12 — ASR-001 Operator Review Package and Review-Readiness Gate  ",
        f"**Date:** {date.today().isoformat()}  ",
        "**Decision:** **PASS**", "",
        "## Validation", "",
        "- Sprint 11 authorizes package preparation only;",
        "- the Working Draft v0.2 baseline is frozen through SHA-256;",
        "- seven reviewer classes are represented;",
        "- the question bank contains forty-three questions with D01–D15 coverage;",
        "- a clause-comment template and machine-readable schema are present;",
        "- issue taxonomy, evidence and conflict declaration, disposition, and change control are present;",
        "- selected trial profiles and research pressures are assigned without creating real-product claims;",
        "- the review mode is limited, asynchronous, and written only;",
        "- repository visibility is distinguished from Public Review status;",
        "- the invitation remains an inactive template;",
        "- no reviewer contact, invitation, public comment channel, endorsement, or adoption status exists;",
        f"- DEC-015 was {'appended' if appended else 'already present'} in the decision log.", "",
        "## SHA-256", "",
        "| File | SHA-256 |",
        "| --- | --- |",
    ]
    for name, digest in hashes.items():
        lines.append(f"| `{name}` | `{digest}` |")
    lines += [
        "",
        "Sprint 12 PASS makes the package ready. It does not activate review.",
        ""
    ]
    Path("SPRINT_12_VALIDATION_RESULT.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )

    readiness = """# ASR-001 Operator Review Readiness Result

**Asset:** AltisSports  
**Sprint:** Sprint 12  
**Gate:** `ASR_001_OPERATOR_REVIEW_READINESS_GATE.md`  
**Decision:** **PASS — PACKAGE READY; OWNER ACTIVATION REQUIRED FOR LIMITED WRITTEN OPERATOR REVIEW**

## Findings

- R01 PASS — package preparation was authorized.
- R02 PASS — the Working Draft and package source baseline are frozen.
- R03 PASS — the profile-only purpose and explicit non-purposes are visible.
- R04 PASS — seven reviewer classes have domain and trial assignments.
- R05 PASS — forty-three questions cover D01–D15.
- R06 PASS — comments are addressable to clauses, domains, fields, artifacts, and questions.
- R07 PASS — the permitted mode is asynchronous and written only.
- R08 PASS — issue types and non-numerical severity classes are defined.
- R09 PASS — human and machine-readable comment intake artifacts exist.
- R10 PASS — evidence, conflicts, compensation, attribution, and non-endorsement are declared.
- R11 PASS — dispositions, scope holds, version effects, and immutable history are governed.
- R12 PASS — sample profiles and research excerpts are bounded as synthetic or informative material.
- R13 PASS — repository visibility is distinguished from Public Review or open invitation.
- R14 PASS — Sprint 12 performs no outreach.
- R15 PASS — prohibited publication, certification, scoring, ranking, tolerance, BCI, recognition, and adoption outcomes remain absent.

## Readiness Consequence

The owner can prepare a reviewer roster and record an activation decision for a limited written review.

No review wave is active until that record is completed and approved.
"""
    Path("ASR_001_OPERATOR_REVIEW_READINESS_RESULT.md").write_text(
        readiness, encoding="utf-8"
    )

    authorization = """# ASR-001 Limited Written Operator Review Activation Authorization

**Decision:** **PACKAGE READY — EXPLICIT OWNER ACTIVATION REQUIRED**  
**Effective condition:** Sprint 12 validation and review-readiness gate are PASS  
**Current review state:** Not activated  
**Public Review status:** Not a Public Review Draft

## Authorized Preparation

The owner can now:

- select a limited reviewer cohort;
- assign reviewer classes, domains, questions, and trial profiles;
- request evidence and conflict declarations;
- define the written response channel;
- complete `ASR_001_REVIEW_ACTIVATION_RECORD_TEMPLATE.md`;
- record the review-wave dates and frozen baseline.

## Activation Condition

The first invitation can be sent only after the owner records:

- `ACTIVATE LIMITED WRITTEN REVIEW`;
- a reviewer roster;
- coverage of at least four reviewer classes, including the class-group conditions in the reviewer matrix;
- conflict-declaration identifiers or pending-declaration status;
- attribution preferences;
- the baseline manifest identifier;
- an asynchronous written channel;
- confirmation that no public comment channel is opened.

This authorization file does not itself activate the review.

## Permitted First-Wave Mode After Activation

- selected reviewers only;
- asynchronous written correspondence;
- clause-addressable comments;
- written responses and dispositions;
- no requirement for calls or interviews;
- no representation of participation as endorsement or adoption.

## Still Unauthorized

- open public comment;
- Public Review Draft status;
- ASR-001 publication;
- certification or certification marks;
- public product, sport, or category conformance claims;
- safety or clinical certification;
- scores, grades, maturity levels, or rankings;
- unsupported remote-synchronous tolerances;
- final BCI athletic classification;
- federation-recognition or industry-adoption claims.

## Next Governed Move

**Sprint 13 — Reviewer Cohort Selection and Limited Written Review Activation**

Sprint 13 requires an explicit owner decision before any invitation is sent.
"""
    Path(
        "ASR_001_LIMITED_WRITTEN_OPERATOR_REVIEW_ACTIVATION_AUTHORIZATION.md"
    ).write_text(authorization, encoding="utf-8")

def main() -> int:
    if run([sys.executable, "build_asr001_operator_review_package.py"]) != 0:
        return 1
    if run([sys.executable, "validate_asr001_operator_review_package.py"]) != 0:
        return 1
    try:
        appended = append_decision()
        write_outputs(appended)
    except (OSError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"ERROR: Sprint 12 could not complete: {exc}", file=sys.stderr)
        return 2
    print(
        "PASS: "
        + (
            "appended DEC-015 to DECISION_LOG.md."
            if appended
            else "DEC-015 already present."
        )
    )
    print(
        "PASS: wrote Sprint 12 validation, readiness result, "
        "and activation authorization."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
