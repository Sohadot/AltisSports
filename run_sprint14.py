#!/usr/bin/env python3
"""Run Sprint 14 validation, gate outputs, and DEC-017 append."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

DECISION_MARKER = "## DEC-017 — ASR-001 First-Wave Named Candidate Assignment and Controlled Invitation Release"

DECISION_TEXT = """
---

## DEC-017 — ASR-001 First-Wave Named Candidate Assignment and Controlled Invitation Release

**Status:** Ratified upon Sprint 14 PASS  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `ASR_001_OWNER_DECISION_SPRINT_14.md`, `ASR_001_REVIEWER_COHORT_ROSTER_V0.2.json`, and `ASR_001_NAMED_ASSIGNMENT_GATE_RESULT.md`

### Decision

1. The owner authorizes first-wave named candidate assignment for Wave RW-001 to B. David Ridpath (RWS-01/RC-01), Mallesham Dasari (RWS-03/RC-03), Stephanie Tow, MD (RWS-05/RC-05), and Emma Drake (RWS-07/RC-07) only.
2. Before written acceptance, each assigned person is classified solely as `named_candidate_assignee` with candidate_status `selected_not_contacted` until private dispatch occurs.
3. Controlled individual written invitation release is authorized for those four slots only.
4. Invitation drafts are prepared for private owner dispatch. Sprint 14 does not transmit messages and does not store personal contact addresses in the public repository.
5. RWS-02, RWS-04, and RWS-06 remain reserve-closed with invitation_status `not_authorized`.
6. Global `review-intake/` remains closed. Per-candidate intake may be enabled only after that candidate's invitation is privately dispatched.
7. No `ORC` identifier may be issued before written acceptance and a later accepted comment.
8. No person may be labeled `reviewer` before written acceptance.
9. Participation must not be represented as endorsement, adoption, partnership, federation recognition, or organizational approval.
10. Public Review Draft status, ASR-001 publication, certification, public conformance claims, scores, rankings, unsupported remote-synchronous tolerances, final BCI athletic classification, and industry-adoption claims remain unauthorized.

### Rationale

A four-candidate first wave satisfies the required coverage groups while remaining operationally bounded. Separating named-candidate assignment from reviewer status, and authorization-to-send from actual private dispatch, preserves non-endorsement boundaries and prevents contact-data leakage or premature intake opening.
""".strip() + "\n"

TRACKED = [
    "ASR_001_OWNER_DECISION_SPRINT_14.md",
    "ASR_001_REVIEWER_COHORT_ROSTER_V0.2.json",
    "ASR_001_NAMED_CANDIDATE_EVIDENCE_V0.1.md",
    "ASR_001_CONTROLLED_INVITATION_PACKAGE.md",
    "ASR_001_INVITATION_DISPATCH_LOG_V0.1.json",
    "ASR_001_PER_CANDIDATE_INTAKE_POLICY.md",
    "ASR_001_NAMED_ASSIGNMENT_GATE.md",
    "ASR_001_REVIEW_ACTIVATION_RECORD_RW001_S14_SUPPLEMENT.md",
    "invitations/INV-RW001-RWS-01.md",
    "invitations/INV-RW001-RWS-03.md",
    "invitations/INV-RW001-RWS-05.md",
    "invitations/INV-RW001-RWS-07.md",
]


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
    if "## DEC-016 — ASR-001 Wave RW-001 Apparatus Activation and Named-Outreach Hold" not in content:
        raise RuntimeError("DEC-016 missing")
    path.write_text(content.rstrip() + "\n\n" + DECISION_TEXT, encoding="utf-8")
    return True


def write_outputs(appended: bool) -> None:
    roster = json.loads(Path("ASR_001_REVIEWER_COHORT_ROSTER_V0.2.json").read_text(encoding="utf-8"))
    active = [s for s in roster["slots"] if s["assignment_status"] == "first_wave_active"]
    reserves = [s for s in roster["slots"] if s["assignment_status"] == "reserve_closed"]

    summary = [
        "# ASR-001 First-Wave Named Candidate Summary",
        "",
        f"**Date:** {date.today().isoformat()}  ",
        "**Wave:** RW-001  ",
        "**Classification before acceptance:** `named_candidate_assignee`",
        "",
        "## Authorized first wave",
        "",
        "| Slot | Class | Named candidate assignee | Invitation status |",
        "| --- | --- | --- | --- |",
    ]
    for slot in active:
        summary.append(
            f"| `{slot['reviewer_id']}` | `{slot['reviewer_class']}` | {slot['named_person']} | `{slot['invitation_status']}` |"
        )
    summary += [
        "",
        "## Reserve-closed",
        "",
        "| Slot | Class | Reserve name | Invitation status |",
        "| --- | --- | --- | --- |",
    ]
    for slot in reserves:
        summary.append(
            f"| `{slot['reviewer_id']}` | `{slot['reviewer_class']}` | {slot['named_person']} | `{slot['invitation_status']}` |"
        )
    summary += [
        "",
        "## Boundary",
        "",
        "No candidate is a reviewer yet. No invitation has been marked dispatched by Sprint 14 automation.",
        "",
    ]
    Path("ASR_001_FIRST_WAVE_NAMED_CANDIDATE_SUMMARY.md").write_text("\n".join(summary), encoding="utf-8")

    hashes = {name: sha256(Path(name)) for name in TRACKED}
    validation = [
        "# Sprint 14 Validation Result",
        "",
        "**Asset:** AltisSports  ",
        "**Sprint:** Sprint 14 — Named Candidate Assignment and Controlled Invitation Release  ",
        f"**Date:** {date.today().isoformat()}  ",
        "**Decision:** **PASS**",
        "",
        "## Validation",
        "",
        "- owner decision authorizes exactly four first-wave candidates;",
        "- role label before acceptance is `named_candidate_assignee`;",
        "- candidate_status remains `selected_not_contacted` until private dispatch;",
        "- reserve slots remain invitation-unauthorized;",
        "- required coverage groups are satisfied;",
        "- invitation drafts exist without public contact secrets;",
        "- dispatch log authorizes four packages and records no fake send;",
        "- global review-intake remains CLOSED;",
        "- ORC issuance remains gated on acceptance and later comment;",
        "- no Public Review, certification, scoring, or adoption claim is created;",
        f"- DEC-017 was {'appended' if appended else 'already present'}.",
        "",
        "## SHA-256",
        "",
        "| File | SHA-256 |",
        "| --- | --- |",
    ]
    for name, digest in hashes.items():
        validation.append(f"| `{name}` | `{digest}` |")
    validation.append("")
    Path("SPRINT_14_VALIDATION_RESULT.md").write_text("\n".join(validation), encoding="utf-8")

    gate = [
        "# ASR-001 Named Assignment Gate Result",
        "",
        "**Asset:** AltisSports  ",
        "**Sprint:** Sprint 14  ",
        "**Gate:** `ASR_001_NAMED_ASSIGNMENT_GATE.md`  ",
        "**Decision:** **PASS — NAMED CANDIDATE ASSIGNMENT AND CONTROLLED INVITATION RELEASE AUTHORIZED FOR RWS-01, RWS-03, RWS-05, RWS-07; PRIVATE DISPATCH REMAINS OWNER-EXECUTED**",
        "",
        "## Findings",
        "",
        "- N01 PASS — DEC-016 and wave apparatus exist.",
        "- N02 PASS — owner decision matches the four authorized names.",
        "- N03 PASS — roster v0.2 assigns exactly four first-wave candidates.",
        "- N04 PASS — role_label is `named_candidate_assignee`.",
        "- N05 PASS — candidate_status is `selected_not_contacted`.",
        "- N06 PASS — reserve slots remain not authorized.",
        "- N07 PASS — coverage groups are satisfied.",
        "- N08 PASS — four non-endorsement invitation drafts exist.",
        "- N09 PASS — no email/phone secrets in Sprint 14 artifacts.",
        "- N10 PASS — dispatch log has no fabricated send timestamps.",
        "- N11 PASS — global intake remains CLOSED.",
        "- N12 PASS — ORC remains gated.",
        "- N13 PASS — prohibited publication outcomes remain absent.",
        "- N14 PASS — DEC-017 is unique and append-only.",
        "",
    ]
    Path("ASR_001_NAMED_ASSIGNMENT_GATE_RESULT.md").write_text("\n".join(gate), encoding="utf-8")

    next_auth = [
        "# ASR-001 Private Invitation Dispatch Authorization",
        "",
        "**Decision:** **AUTHORIZED FOR OWNER-PRIVATE DISPATCH OF FOUR FIRST-WAVE INVITATIONS ONLY**  ",
        "**Execution actor:** Owner private written channel  ",
        "**Repository automation send:** not performed",
        "",
        "## Authorized packages",
        "",
        "- `INV-RW001-RWS-01`",
        "- `INV-RW001-RWS-03`",
        "- `INV-RW001-RWS-05`",
        "- `INV-RW001-RWS-07`",
        "",
        "## After each private send, the owner should",
        "",
        "1. set that entry's `dispatch_status` to `dispatched` and fill `dispatched_at`;",
        "2. keep contact secrets out of the public repository;",
        "3. enable only that candidate's intake path if needed;",
        "4. leave reviewer_status as `not_reviewer` until written acceptance;",
        "5. leave reserve slots untouched.",
        "",
        "## Suggested next governed move",
        "",
        "**Sprint 15 — Invitation Dispatch Recording, Acceptance Intake, and First Comment Window**",
        "",
        "Begins after at least one private invitation has actually been sent and recorded.",
        "",
    ]
    Path("ASR_001_PRIVATE_INVITATION_DISPATCH_AUTHORIZATION.md").write_text("\n".join(next_auth), encoding="utf-8")


def main() -> int:
    code = subprocess.run([sys.executable, "validate_asr001_named_assignment.py"]).returncode
    if code != 0:
        return code
    appended = append_decision()
    write_outputs(appended)
    print("PASS: wrote ASR_001_FIRST_WAVE_NAMED_CANDIDATE_SUMMARY.md")
    print("PASS: appended DEC-017 to DECISION_LOG.md." if appended else "PASS: DEC-017 already present.")
    print("PASS: named candidate assignment and controlled invitation release authorized for four slots.")
    print("PASS: wrote Sprint 14 validation, gate result, and private-dispatch authorization.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
