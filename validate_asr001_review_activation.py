#!/usr/bin/env python3
"""Validate Sprint 13 cohort selection and activation apparatus under outreach hold."""
from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED = [
    Path("ASR_001_REVIEWER_SELECTION_CRITERIA.md"),
    Path("ASR_001_REVIEWER_COHORT_ROSTER_V0.1.json"),
    Path("ASR_001_REVIEW_WAVE_RW001_PLAN.md"),
    Path("ASR_001_REVIEW_ACTIVATION_RECORD_RW001.md"),
    Path("ASR_001_WRITTEN_INTAKE_CHANNEL.md"),
    Path("ASR_001_ISSUE_INTAKE_PROCEDURE.md"),
    Path("ASR_001_REVIEW_ACTIVATION_GATE.md"),
    Path("ASR_001_REVIEW_INVITATION_TEMPLATE.md"),
    Path("ASR_001_REVIEW_BASELINE_MANIFEST.json"),
    Path("ASR_001_LIMITED_WRITTEN_OPERATOR_REVIEW_ACTIVATION_AUTHORIZATION.md"),
    Path("review-intake/README.md"),
]

REQUIRED_CLASSES = {"RC-01", "RC-02", "RC-03", "RC-04", "RC-05", "RC-06", "RC-07"}


def fail(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 2


def main() -> int:
    missing = [str(path) for path in REQUIRED if not path.exists()]
    if missing:
        return fail("missing required files: " + ", ".join(missing))

    decision = Path("DECISION_LOG.md").read_text(encoding="utf-8")
    if "## DEC-015 — ASR-001 Operator Review Readiness and Owner-Activation Boundary" not in decision:
        return fail("DEC-015 is required before Sprint 13 validation")

    roster = json.loads(Path("ASR_001_REVIEWER_COHORT_ROSTER_V0.1.json").read_text(encoding="utf-8"))
    if roster.get("outreach_status") != "held":
        return fail("roster outreach_status must be held")
    if roster.get("invitation_sending_authorized") is not False:
        return fail("invitation_sending_authorized must be false")
    if roster.get("public_review") is not False:
        return fail("public_review must be false")
    if roster.get("baseline_manifest_id") != "ASR001-OPERATOR-REVIEW-BASELINE":
        return fail("baseline_manifest_id mismatch")

    slots = roster.get("slots") or []
    if len(slots) != 7:
        return fail("expected exactly seven cohort slots")

    classes = set()
    for slot in slots:
        classes.add(slot.get("reviewer_class"))
        if slot.get("named_person") is not None:
            return fail(f"{slot.get('reviewer_id')} must not invent a named_person")
        if slot.get("invitation_status") != "not_sent":
            return fail(f"{slot.get('reviewer_id')} invitation_status must be not_sent")
        if not str(slot.get("conflict_declaration_id", "")).endswith("PENDING"):
            return fail(f"{slot.get('reviewer_id')} conflict declaration must remain pending")
        if slot.get("conflict_declaration_status") != "pending_request":
            return fail(f"{slot.get('reviewer_id')} conflict status must be pending_request")

    if classes != REQUIRED_CLASSES:
        return fail(f"class coverage incomplete: {sorted(classes)}")

    # Required group coverage
    if not (("RC-01" in classes or "RC-02" in classes)
            and ("RC-03" in classes or "RC-04" in classes)
            and ("RC-05" in classes or "RC-06" in classes)
            and ("RC-07" in classes)):
        return fail("required class-group coverage failed")

    activation = Path("ASR_001_REVIEW_ACTIVATION_RECORD_RW001.md").read_text(encoding="utf-8")
    for needle in [
        "ACTIVATE LIMITED WRITTEN REVIEW APPARATUS",
        "INVITATION_SENDING_HELD",
        "NAMED_ASSIGNMENT_HELD",
        "ASR001-OPERATOR-REVIEW-BASELINE",
        "not sent",
    ]:
        if needle not in activation:
            return fail(f"activation record missing required marker: {needle}")

    invitation = Path("ASR_001_REVIEW_INVITATION_TEMPLATE.md").read_text(encoding="utf-8")
    if "Prepared template" not in invitation or "not sent" not in invitation.lower():
        return fail("invitation template must remain prepared and not sent")

    intake_readme = Path("review-intake/README.md").read_text(encoding="utf-8")
    if "CLOSED" not in intake_readme:
        return fail("review-intake must declare CLOSED status")

    criteria = Path("ASR_001_REVIEWER_SELECTION_CRITERIA.md").read_text(encoding="utf-8")
    if "No fabricated identity" not in criteria and "no fabricated" not in criteria.lower():
        return fail("selection criteria must prohibit fabricated identity")

    print("PASS: Sprint 13 cohort roster, activation apparatus, and outreach hold validate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
