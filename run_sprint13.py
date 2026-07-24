#!/usr/bin/env python3
"""Run Sprint 13 validation, coverage report, gate outputs, and DEC-016 append."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

DECISION_MARKER = "## DEC-016 — ASR-001 Wave RW-001 Apparatus Activation and Named-Outreach Hold"

DECISION_TEXT = """
---

## DEC-016 — ASR-001 Wave RW-001 Apparatus Activation and Named-Outreach Hold

**Status:** Ratified upon Sprint 13 PASS  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `ASR_001_REVIEW_ACTIVATION_RECORD_RW001.md`, `ASR_001_REVIEWER_COHORT_ROSTER_V0.1.json`, and `ASR_001_REVIEW_ACTIVATION_GATE_RESULT.md`

### Decision

1. Wave RW-001 limited-written-review apparatus is activated for preparation under ASR-001 Working Draft v0.2 and baseline manifest `ASR001-OPERATOR-REVIEW-BASELINE`.
2. The first-wave cohort is defined as seven role slots `RWS-01` through `RWS-07` covering RC-01 through RC-07 and satisfying the four required class groups.
3. Named persons are not assigned in Sprint 13. Fabricated personal identities are prohibited.
4. Conflict-declaration identifiers are reserved in pending status for each slot.
5. The written intake channel `review-intake/` is prepared and remains closed to external submission.
6. The issue-intake procedure is confirmed and remains disabled until invitation-linked enablement.
7. All invitation statuses remain `not_sent`. The invitation template remains prepared and inactive.
8. Named assignment and invitation sending remain held and require a separate owner outreach decision.
9. Public repository visibility still does not create Public Review Draft status or open comment rights.
10. Public Review Draft status, ASR-001 publication, certification, public conformance claims, scores, rankings, unsupported remote-synchronous tolerances, final BCI athletic classification, federation-recognition claims, and industry-adoption claims remain unauthorized.

### Rationale

Sprint 12 made the package review-ready. Sprint 13 converts readiness into a governed wave apparatus and class-covered cohort without collapsing preparation into outreach. Keeping named assignment and invitation sending under an explicit hold preserves non-endorsement boundaries and prevents identity fabrication or premature public comment.
""".strip() + "\n"

TRACKED = [
    "ASR_001_REVIEWER_SELECTION_CRITERIA.md",
    "ASR_001_REVIEWER_COHORT_ROSTER_V0.1.json",
    "ASR_001_REVIEW_WAVE_RW001_PLAN.md",
    "ASR_001_REVIEW_ACTIVATION_RECORD_RW001.md",
    "ASR_001_WRITTEN_INTAKE_CHANNEL.md",
    "ASR_001_ISSUE_INTAKE_PROCEDURE.md",
    "ASR_001_REVIEW_ACTIVATION_GATE.md",
    "ASR_001_REVIEW_BASELINE_MANIFEST.json",
    "ASR_001_REVIEW_INVITATION_TEMPLATE.md",
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
    if "## DEC-015 — ASR-001 Operator Review Readiness and Owner-Activation Boundary" not in content:
        raise RuntimeError("DEC-015 is missing; refusing to append DEC-016")
    path.write_text(content.rstrip() + "\n\n" + DECISION_TEXT, encoding="utf-8")
    return True


def write_coverage_report(roster: dict) -> None:
    lines = [
        "# ASR-001 Review Cohort Coverage Report",
        "",
        f"**Roster ID:** `{roster['roster_id']}`  ",
        f"**Wave:** `{roster['review_wave_id']}`  ",
        f"**Date:** {date.today().isoformat()}  ",
        "**Outreach status:** held  ",
        "",
        "## Slots",
        "",
        "| Reviewer ID | Class | Invitation | Named person | Conflict status |",
        "| --- | --- | --- | --- | --- |",
    ]
    for slot in roster["slots"]:
        lines.append(
            f"| `{slot['reviewer_id']}` | `{slot['reviewer_class']}` | `{slot['invitation_status']}` | "
            f"{'none' if slot['named_person'] is None else slot['named_person']} | `{slot['conflict_declaration_status']}` |"
        )
    lines += [
        "",
        "## Required Groups",
        "",
        "- operational: RC-01 and RC-02 present",
        "- technical/measurement: RC-03 and RC-04 present",
        "- human-impact/methodology: RC-05 and RC-06 present",
        "- evidence/data governance: RC-07 present",
        "",
        "## Boundary",
        "",
        "Coverage confirms design completeness. It is not a quorum, vote, endorsement count, or authorization to send invitations.",
        "",
    ]
    Path("ASR_001_REVIEW_COHORT_COVERAGE_REPORT.md").write_text("\n".join(lines), encoding="utf-8")


def write_outputs(appended: bool) -> None:
    hashes = {name: sha256(Path(name)) for name in TRACKED}
    roster = json.loads(Path("ASR_001_REVIEWER_COHORT_ROSTER_V0.1.json").read_text(encoding="utf-8"))
    write_coverage_report(roster)

    validation = [
        "# Sprint 13 Validation Result",
        "",
        "**Asset:** AltisSports  ",
        "**Sprint:** Sprint 13 — Reviewer Cohort Selection and Limited Written Review Activation  ",
        f"**Date:** {date.today().isoformat()}  ",
        "**Decision:** **PASS**",
        "",
        "## Validation",
        "",
        "- Sprint 12 readiness and DEC-015 are present;",
        "- owner continuation of Sprint 13 is recorded in selection criteria;",
        "- seven role slots cover RC-01 through RC-07;",
        "- required class groups are satisfied;",
        "- no named persons are fabricated;",
        "- all invitation statuses remain `not_sent`;",
        "- conflict declarations remain pending by reserved identifiers;",
        "- activation record activates apparatus while holding outreach;",
        "- written intake channel is prepared and closed;",
        "- issue intake procedure is confirmed and closed;",
        "- invitation template remains prepared and not sent;",
        "- no Public Review, certification, scoring, or adoption status is created;",
        f"- DEC-016 was {'appended' if appended else 'already present'} in the decision log.",
        "",
        "## SHA-256",
        "",
        "| File | SHA-256 |",
        "| --- | --- |",
    ]
    for name, digest in hashes.items():
        validation.append(f"| `{name}` | `{digest}` |")
    validation.append("")
    Path("SPRINT_13_VALIDATION_RESULT.md").write_text("\n".join(validation), encoding="utf-8")

    gate = [
        "# ASR-001 Review Activation Gate Result",
        "",
        "**Asset:** AltisSports  ",
        "**Sprint:** Sprint 13  ",
        "**Gate:** `ASR_001_REVIEW_ACTIVATION_GATE.md`  ",
        "**Decision:** **PASS — WAVE APPARATUS ACTIVATED; NAMED OUTREACH AND INVITATION SENDING REMAIN HELD**",
        "",
        "## Findings",
        "",
        "- A01 PASS — Sprint 12 readiness and DEC-015 are present.",
        "- A02 PASS — owner continuation under strict governance is documented.",
        "- A03 PASS — selection criteria prohibit fabricated identities.",
        "- A04 PASS — cohort covers required class groups with seven designed classes.",
        "- A05 PASS — every slot remains `not_sent`.",
        "- A06 PASS — every named_person is null.",
        "- A07 PASS — pending conflict-declaration identifiers exist.",
        "- A08 PASS — baseline manifest ID is frozen.",
        "- A09 PASS — written intake is prepared and externally closed.",
        "- A10 PASS — issue intake procedure exists and is closed.",
        "- A11 PASS — invitation template remains prepared-not-sent.",
        "- A12 PASS — prohibited publication and certification outcomes remain absent.",
        "- A13 PASS — outreach hold is explicit.",
        "- A14 PASS — DEC-016 is unique and append-only.",
        "",
        "## Consequence",
        "",
        "Wave RW-001 apparatus is ready for owner-controlled named assignment.",
        "",
        "No invitation may be sent until a separate outreach authorization records named assignees and sending approval.",
        "",
    ]
    Path("ASR_001_REVIEW_ACTIVATION_GATE_RESULT.md").write_text("\n".join(gate), encoding="utf-8")

    auth = [
        "# ASR-001 Named Outreach and Invitation-Sending Authorization Boundary",
        "",
        "**Decision:** **NOT AUTHORIZED BY SPRINT 13**  ",
        "**Wave apparatus status:** Activated for preparation  ",
        "**Named outreach status:** Held  ",
        "**Invitation sending status:** Held",
        "",
        "## What Sprint 13 Authorized",
        "",
        "- role-slot cohort RW-001;",
        "- class coverage confirmation;",
        "- activation record for the review apparatus;",
        "- closed written intake preparation;",
        "- issue-intake procedure confirmation.",
        "",
        "## What Remains Owner-Controlled Next",
        "",
        "A later sprint may begin only after an explicit owner decision that:",
        "",
        "1. assigns named persons to one or more slots without fabricating identity;",
        "2. records attribution preferences;",
        "3. advances conflict declarations from pending to requested/received as appropriate;",
        "4. authorizes invitation sending for those named assignees;",
        "5. fills review opening and closing dates before send;",
        "6. keeps the channel written, limited, and non-public;",
        "7. continues to prohibit Public Review, publication, certification, scoring, and adoption claims.",
        "",
        "## Suggested Next Governed Move",
        "",
        "**Sprint 14 — Named Reviewer Assignment and Controlled Invitation Release**",
        "",
        "Only if the owner explicitly authorizes named assignment and sending.",
        "",
    ]
    Path("ASR_001_NAMED_OUTREACH_HOLD.md").write_text("\n".join(auth), encoding="utf-8")


def main() -> int:
    code = subprocess.run([sys.executable, "validate_asr001_review_activation.py"]).returncode
    if code != 0:
        return code
    appended = append_decision()
    write_outputs(appended)
    print("PASS: wrote ASR_001_REVIEW_COHORT_COVERAGE_REPORT.md")
    print("PASS: appended DEC-016 to DECISION_LOG.md." if appended else "PASS: DEC-016 already present.")
    print("PASS: Wave RW-001 apparatus activated; named outreach and invitation sending remain held.")
    print("PASS: wrote Sprint 13 validation, activation gate result, and named-outreach hold.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
