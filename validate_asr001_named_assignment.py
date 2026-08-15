#!/usr/bin/env python3
"""Validate Sprint 14 first-wave assignment as public process — slots and states,
never people.

Under REVIEWER_PRIVACY_BOUNDARY.md the public record holds roles, slots, states,
and process only. This validator therefore asks "are exactly four slots
authorized, in the correct states, with candidate identity kept private?" — not
"are these four named people present?". Candidate identity must be absent from
the public tree.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"\+\d{6,}|\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b")

ACTIVE = {"RWS-01", "RWS-03", "RWS-05", "RWS-07"}
RESERVE = {"RWS-02", "RWS-04", "RWS-06"}
FIRST_WAVE_CLASSES = {"RC-01", "RC-03", "RC-05", "RC-07"}

IDENTITY_FIELDS = ("named_person", "public_affiliation", "named_candidate_assignee")
# Personalized, identity-bearing files that must NOT exist in the public tree.
FORBIDDEN_PUBLIC_FILES = [
    Path("ASR_001_NAMED_CANDIDATE_EVIDENCE_V0.1.md"),
    Path("invitations/INV-RW001-RWS-01.md"),
    Path("invitations/INV-RW001-RWS-03.md"),
    Path("invitations/INV-RW001-RWS-05.md"),
    Path("invitations/INV-RW001-RWS-07.md"),
]
TEMPLATE = Path("invitations/INV-RW001-TEMPLATE.md")

SCAN_PATHS = [
    Path("ASR_001_OWNER_DECISION_SPRINT_14.md"),
    Path("ASR_001_REVIEWER_COHORT_ROSTER_V0.2.json"),
    Path("ASR_001_CONTROLLED_INVITATION_PACKAGE.md"),
    Path("ASR_001_INVITATION_DISPATCH_LOG_V0.1.json"),
    Path("ASR_001_PER_CANDIDATE_INTAKE_POLICY.md"),
    Path("ASR_001_NAMED_ASSIGNMENT_GATE.md"),
    Path("ASR_001_REVIEW_ACTIVATION_RECORD_RW001_S14_SUPPLEMENT.md"),
    Path("ASR_001_FIRST_WAVE_NAMED_CANDIDATE_SUMMARY.md"),
    TEMPLATE,
]


def fail(msg: str) -> int:
    print(f"ERROR: {msg}", file=sys.stderr)
    return 2


def main() -> int:
    # Privacy boundary must be published.
    boundary = Path("REVIEWER_PRIVACY_BOUNDARY.md")
    if not boundary.exists():
        return fail("REVIEWER_PRIVACY_BOUNDARY.md is required")
    btext = boundary.read_text(encoding="utf-8")
    for needle in ("Review participation consent", "Public attribution consent",
                   "Correspondence-publication consent"):
        if needle not in btext:
            return fail(f"privacy boundary must distinguish {needle}")

    # No identity-bearing personal files may exist in the public tree.
    for path in FORBIDDEN_PUBLIC_FILES:
        if path.exists():
            return fail(f"identity-bearing file must not be public: {path}")

    decision_log = Path("DECISION_LOG.md").read_text(encoding="utf-8")
    if "## DEC-016 — ASR-001 Wave RW-001 Apparatus Activation and Named-Outreach Hold" not in decision_log:
        return fail("DEC-016 required")

    owner = Path("ASR_001_OWNER_DECISION_SPRINT_14.md").read_text(encoding="utf-8")
    for slot in ACTIVE:
        if slot not in owner:
            return fail(f"owner decision must reference slot {slot}")
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

    for slot in by_id.values():
        for f in ("named_person", "public_affiliation"):
            if slot.get(f) is not None:
                return fail(f"{slot['reviewer_id']} must not carry {f} in the public record")

    # Authorization is frozen; the per-slot lifecycle is state-transition-aware so
    # a legitimate first dispatch / acceptance does not break the gate. Legal
    # lifecycle values and their cross-field invariants (per the per-candidate
    # intake policy) are enforced, not a single frozen snapshot.
    ROLE = {"named_candidate_assignee", "reviewer"}
    CAND = {"selected_not_contacted", "invited_awaiting_acceptance", "accepted"}
    INV = {"prepared_authorized_awaiting_private_dispatch", "dispatched"}
    INTAKE = {"closed_until_invitation_dispatched", "enabled_for_candidate"}
    for slot_id in ACTIVE:
        slot = by_id[slot_id]
        if slot.get("role_label") not in ROLE:
            return fail(f"{slot_id} role_label invalid: {slot.get('role_label')!r}")
        if slot.get("candidate_status") not in CAND:
            return fail(f"{slot_id} candidate_status invalid: {slot.get('candidate_status')!r}")
        if slot.get("invitation_status") not in INV:
            return fail(f"{slot_id} invitation_status invalid: {slot.get('invitation_status')!r}")
        if slot.get("intake_enablement") not in INTAKE:
            return fail(f"{slot_id} intake_enablement invalid: {slot.get('intake_enablement')!r}")
        # invariants: no reviewer before acceptance; pre-dispatch snapshot is coherent.
        if slot.get("role_label") == "reviewer" and slot.get("candidate_status") != "accepted":
            return fail(f"{slot_id} cannot be reviewer before written acceptance")
        if slot.get("invitation_status") == "prepared_authorized_awaiting_private_dispatch":
            if slot.get("candidate_status") != "selected_not_contacted":
                return fail(f"{slot_id} pre-dispatch candidate_status must be selected_not_contacted")
            if slot.get("intake_enablement") != "closed_until_invitation_dispatched":
                return fail(f"{slot_id} pre-dispatch intake must be closed")
            if slot.get("role_label") != "named_candidate_assignee":
                return fail(f"{slot_id} pre-dispatch role must be named_candidate_assignee")

    for slot_id in RESERVE:
        slot = by_id[slot_id]
        if slot.get("candidate_status") != "reserve_candidate_not_assigned":
            return fail(f"{slot_id} must remain reserve_candidate_not_assigned")
        if slot.get("invitation_status") != "not_authorized":
            return fail(f"{slot_id} invitation must be not_authorized")

    if {by_id[s]["reviewer_class"] for s in ACTIVE} != FIRST_WAVE_CLASSES:
        return fail("first-wave class coverage incorrect")

    # Public invitations are one anonymous template, not personalized letters.
    if not TEMPLATE.exists():
        return fail("anonymous invitation template is required")
    tpl = TEMPLATE.read_text(encoding="utf-8")
    if "named candidate assignee" not in tpl.lower():
        return fail("template must preserve named candidate assignee language")
    if "does not imply endorsement" not in tpl.lower() and "not imply endorsement" not in tpl.lower():
        return fail("template must carry non-endorsement language")
    if "separate" not in tpl.lower() or "public attribution" not in tpl.lower():
        return fail("template must state that participation is not public-attribution consent")

    # Dispatch log — a legal state machine, not a frozen snapshot. A slot may
    # advance awaiting_private_dispatch -> dispatched (with a real timestamp),
    # then to reviewer only after written acceptance. This lets the first real
    # dispatch land without breaking the gate, while still forbidding illegal
    # states (dispatched without a timestamp, reviewer before acceptance, etc.).
    log = json.loads(Path("ASR_001_INVITATION_DISPATCH_LOG_V0.1.json").read_text(encoding="utf-8"))
    if len(log.get("entries") or []) != 4:
        return fail("dispatch log must contain four authorized entries")
    for entry in log["entries"]:
        if entry.get("named_candidate_assignee") is not None:
            return fail("dispatch log must not carry candidate identity")
        if entry.get("slot") not in ACTIVE:
            return fail("dispatch log entry has an unexpected slot")
        if entry.get("authorization_status") != "authorized":
            return fail(f"{entry.get('slot')} must remain authorized")
        ds = entry.get("dispatch_status")
        at = entry.get("dispatched_at")
        intake = entry.get("intake_enabled")
        acc = entry.get("acceptance_status")
        rev = entry.get("reviewer_status")
        if ds not in {"awaiting_private_dispatch", "dispatched"}:
            return fail(f"{entry.get('slot')} dispatch_status invalid: {ds!r}")
        if acc not in {"not_accepted", "accepted"}:
            return fail(f"{entry.get('slot')} acceptance_status invalid: {acc!r}")
        if rev not in {"not_reviewer", "reviewer"}:
            return fail(f"{entry.get('slot')} reviewer_status invalid: {rev!r}")
        if ds == "awaiting_private_dispatch":
            if at is not None:
                return fail(f"{entry.get('slot')} dispatched_at must be null before send")
            if intake is not False or acc != "not_accepted" or rev != "not_reviewer":
                return fail(f"{entry.get('slot')} pre-dispatch state incoherent")
        else:  # dispatched
            if not (isinstance(at, str) and at.strip()):
                return fail(f"{entry.get('slot')} dispatched requires a real dispatched_at timestamp")
        if acc == "accepted" and ds != "dispatched":
            return fail(f"{entry.get('slot')} cannot be accepted before dispatch")
        if rev == "reviewer" and not (ds == "dispatched" and acc == "accepted"):
            return fail(f"{entry.get('slot')} cannot be reviewer before dispatch and written acceptance")

    # Cross-file invariant: the same RWS-* cannot tell two public stories.
    # Per ASR_001_PER_CANDIDATE_INTAKE_POLICY.md, awaiting_private_dispatch
    # matches the pre-send roster snapshot; dispatched + not_accepted matches
    # invited_awaiting_acceptance; accepted/reviewer appears only after
    # dispatch and written acceptance.
    by_slot_entry = {}
    for entry in log["entries"]:
        slot_id = entry.get("slot")
        if slot_id in by_slot_entry:
            return fail(f"dispatch log has duplicate entry for {slot_id}")
        by_slot_entry[slot_id] = entry
    if set(by_slot_entry) != ACTIVE:
        return fail("dispatch log must contain exactly the four authorized slots")

    for slot_id in ACTIVE:
        slot = by_id[slot_id]
        entry = by_slot_entry[slot_id]
        if slot.get("invitation_package_id") != entry.get("invitation_package_id"):
            return fail(f"{slot_id} invitation_package_id mismatch between roster and dispatch log")
        ds = entry.get("dispatch_status")
        acc = entry.get("acceptance_status")
        rev = entry.get("reviewer_status")
        inv = slot.get("invitation_status")
        cand = slot.get("candidate_status")
        role = slot.get("role_label")
        if ds == "awaiting_private_dispatch":
            if inv != "prepared_authorized_awaiting_private_dispatch":
                return fail(f"{slot_id} awaiting_private_dispatch requires pre-dispatch invitation_status")
            if cand != "selected_not_contacted":
                return fail(f"{slot_id} awaiting_private_dispatch requires selected_not_contacted")
            if role != "named_candidate_assignee":
                return fail(f"{slot_id} awaiting_private_dispatch requires named_candidate_assignee")
        elif ds == "dispatched" and acc == "not_accepted":
            if inv != "dispatched":
                return fail(f"{slot_id} dispatched + not_accepted requires invitation_status dispatched")
            if cand != "invited_awaiting_acceptance":
                return fail(f"{slot_id} dispatched + not_accepted must match invited_awaiting_acceptance")
            if role != "named_candidate_assignee":
                return fail(f"{slot_id} dispatched + not_accepted cannot be reviewer")
        else:
            # dispatched + accepted (illegal pre-dispatch acceptance is already rejected above)
            if ds != "dispatched" or acc != "accepted":
                return fail(f"{slot_id} accepted/reviewer requires dispatch and written acceptance")
            if inv != "dispatched":
                return fail(f"{slot_id} accepted/reviewer requires invitation_status dispatched")
            if cand != "accepted":
                return fail(f"{slot_id} written acceptance must appear as candidate_status accepted")
            if role != "reviewer" or rev != "reviewer":
                return fail(f"{slot_id} written acceptance must appear as reviewer on roster and dispatch log")

    intake = Path("review-intake/README.md").read_text(encoding="utf-8")
    if "CLOSED" not in intake:
        return fail("global review-intake must remain CLOSED")

    policy = Path("ASR_001_PER_CANDIDATE_INTAKE_POLICY.md").read_text(encoding="utf-8")
    if "ORC" not in policy or "written acceptance" not in policy.lower():
        return fail("intake policy must gate ORC on acceptance")

    # No contact data, and no residual identity fields, in the public files.
    for path in SCAN_PATHS:
        text = path.read_text(encoding="utf-8")
        if EMAIL_RE.search(text):
            return fail(f"email address found in {path}")
        if PHONE_RE.search(text):
            return fail(f"phone-like number found in {path}")
    for name in ("named_person", "public_affiliation"):
        for path in [Path("ASR_001_REVIEWER_COHORT_ROSTER_V0.2.json"),
                     Path("ASR_001_INVITATION_DISPATCH_LOG_V0.1.json")]:
            if f'"{name}"' in path.read_text(encoding="utf-8"):
                return fail(f"{path} still carries identity field {name}")

    print("PASS: Sprint 14 first-wave assignment validates as public process "
          "(four authorized slots, correct states, candidate identity kept private).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
