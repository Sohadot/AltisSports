#!/usr/bin/env python3
"""Validate Sprint 14 named-candidate assignment and controlled invitation authorization."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"\+\d{6,}|\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b")

ACTIVE = {"RWS-01", "RWS-03", "RWS-05", "RWS-07"}
RESERVE = {"RWS-02", "RWS-04", "RWS-06"}
EXPECTED_NAMES = {
    "RWS-01": "B. David Ridpath",
    "RWS-03": "Mallesham Dasari",
    "RWS-05": "Stephanie Tow, MD",
    "RWS-07": "Emma Drake",
}
INVITE_FILES = {
    "RWS-01": Path("invitations/INV-RW001-RWS-01.md"),
    "RWS-03": Path("invitations/INV-RW001-RWS-03.md"),
    "RWS-05": Path("invitations/INV-RW001-RWS-05.md"),
    "RWS-07": Path("invitations/INV-RW001-RWS-07.md"),
}

SCAN_PATHS = [
    Path("ASR_001_OWNER_DECISION_SPRINT_14.md"),
    Path("ASR_001_REVIEWER_COHORT_ROSTER_V0.2.json"),
    Path("ASR_001_NAMED_CANDIDATE_EVIDENCE_V0.1.md"),
    Path("ASR_001_CONTROLLED_INVITATION_PACKAGE.md"),
    Path("ASR_001_INVITATION_DISPATCH_LOG_V0.1.json"),
    Path("ASR_001_PER_CANDIDATE_INTAKE_POLICY.md"),
    Path("ASR_001_NAMED_ASSIGNMENT_GATE.md"),
    Path("ASR_001_REVIEW_ACTIVATION_RECORD_RW001_S14_SUPPLEMENT.md"),
    *INVITE_FILES.values(),
]


def fail(msg: str) -> int:
    print(f"ERROR: {msg}", file=sys.stderr)
    return 2


def main() -> int:
    decision_log = Path("DECISION_LOG.md").read_text(encoding="utf-8")
    if "## DEC-016 — ASR-001 Wave RW-001 Apparatus Activation and Named-Outreach Hold" not in decision_log:
        return fail("DEC-016 required")

    owner = Path("ASR_001_OWNER_DECISION_SPRINT_14.md").read_text(encoding="utf-8")
    for name in EXPECTED_NAMES.values():
        if name.split(",")[0] not in owner and name not in owner:
            return fail(f"owner decision missing {name}")
    if "لا يصبح أي منهم مراجعًا قبل القبول الكتابي" not in owner:
        return fail("owner decision missing Arabic non-reviewer-before-acceptance clause")

    roster = json.loads(Path("ASR_001_REVIEWER_COHORT_ROSTER_V0.2.json").read_text(encoding="utf-8"))
    if roster.get("invitation_sending_authorized") is not True:
        return fail("invitation_sending_authorized must be true for controlled release")
    if set(roster.get("invitation_sending_authorized_slots") or []) != ACTIVE:
        return fail("authorized slots must be exactly first-wave four")
    if roster.get("public_review") is not False:
        return fail("public_review must remain false")

    by_id = {s["reviewer_id"]: s for s in roster["slots"]}
    if set(by_id) != ACTIVE | RESERVE:
        return fail("roster must contain seven slots")

    for slot_id, name in EXPECTED_NAMES.items():
        slot = by_id[slot_id]
        if slot.get("role_label") != "named_candidate_assignee":
            return fail(f"{slot_id} must be named_candidate_assignee")
        if slot.get("candidate_status") != "selected_not_contacted":
            return fail(f"{slot_id} candidate_status must be selected_not_contacted")
        if slot.get("named_person") != name:
            return fail(f"{slot_id} named_person mismatch")
        if slot.get("invitation_status") != "prepared_authorized_awaiting_private_dispatch":
            return fail(f"{slot_id} invitation_status invalid")
        if slot.get("intake_enablement") != "closed_until_invitation_dispatched":
            return fail(f"{slot_id} intake_enablement invalid")

    for slot_id in RESERVE:
        slot = by_id[slot_id]
        if slot.get("candidate_status") != "reserve_candidate_not_assigned":
            return fail(f"{slot_id} must remain reserve_candidate_not_assigned")
        if slot.get("invitation_status") != "not_authorized":
            return fail(f"{slot_id} invitation must be not_authorized")

    first_wave_classes = {by_id[s]["reviewer_class"] for s in ACTIVE}
    if first_wave_classes != {"RC-01", "RC-03", "RC-05", "RC-07"}:
        return fail("first-wave class coverage incorrect")

    for slot_id, path in INVITE_FILES.items():
        text = path.read_text(encoding="utf-8")
        if EXPECTED_NAMES[slot_id] not in text:
            return fail(f"{path} missing candidate name")
        if "not endorsement" not in text.lower() and "does not imply endorsement" not in text.lower():
            return fail(f"{path} missing non-endorsement language")
        if "named candidate assignee" not in text.lower():
            return fail(f"{path} must preserve named candidate assignee language")

    log = json.loads(Path("ASR_001_INVITATION_DISPATCH_LOG_V0.1.json").read_text(encoding="utf-8"))
    if len(log.get("entries") or []) != 4:
        return fail("dispatch log must contain four authorized entries")
    for entry in log["entries"]:
        if entry.get("dispatch_status") != "awaiting_private_dispatch":
            return fail("no invitation may be marked dispatched in Sprint 14 automation")
        if entry.get("dispatched_at") is not None:
            return fail("dispatched_at must remain null until owner private send")
        if entry.get("reviewer_status") != "not_reviewer":
            return fail("reviewer_status must remain not_reviewer")
        if entry.get("intake_enabled") is not False:
            return fail("intake_enabled must remain false")

    intake = Path("review-intake/README.md").read_text(encoding="utf-8")
    if "CLOSED" not in intake:
        return fail("global review-intake must remain CLOSED")

    policy = Path("ASR_001_PER_CANDIDATE_INTAKE_POLICY.md").read_text(encoding="utf-8")
    if "ORC" not in policy or "written acceptance" not in policy.lower():
        return fail("intake policy must gate ORC on acceptance")

    for path in SCAN_PATHS:
        text = path.read_text(encoding="utf-8")
        if EMAIL_RE.search(text):
            return fail(f"email address found in {path}")
        if PHONE_RE.search(text):
            return fail(f"phone-like number found in {path}")

    print("PASS: Sprint 14 named-candidate assignment and controlled invitation authorization validate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
