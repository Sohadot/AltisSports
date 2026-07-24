#!/usr/bin/env python3
"""Run Sprint 11 builds, internal trials, refinement gate, and decision append."""
from __future__ import annotations

import hashlib
import subprocess
import sys
from datetime import date
from pathlib import Path

DECISION_MARKER = "## DEC-014 — ASR-001 Internal Trial Refinement and Operator-Review Preparation Boundary"

DECISION_TEXT = """
---

## DEC-014 — ASR-001 Internal Trial Refinement and Operator-Review Preparation Boundary

**Status:** Ratified upon Sprint 11 PASS  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `ASR_001_INTERNAL_TRIAL_RESULTS.md`, `ASR_001_CLAUSE_FRICTION_REGISTER_V0.1.json`, and `ASR_001_REFINEMENT_RESULT.md`

### Decision

1. The seven Sprint 11 internal profile artifacts are accepted as the current implementation-trial baseline.
2. The ASR-001 Working Draft advances internally from v0.1 to v0.2 without changing the approved D01–D15 scope or any clause identifier.
3. Applicability and evidence sufficiency are separate states. An applicable clause may remain `not_evidenced`, `unknown`, or `partial` without becoming non-applicable or producing a score.
4. `ASR001-D03-C02` applies when agency modes, control regimes, or handoff are present, including autonomous contest execution after human design.
5. `ASR001-D04-C02` applies when embodied demand or intentional biological control is claimed, without settling athletic membership or establishing an embodiment threshold.
6. A JSON ASR-001 profile instance declares machine-readable distribution as present.
7. Clause records distinguish declarative, supporting-evidence, lifecycle, and distribution-manifest evidence requirements.
8. Profile correction and supersession are explicit and append-only; the rehabilitation revision pair is accepted as the lifecycle test.
9. Internal trials confirm the profile-only conformance boundary across autonomous, support, BCI, human–AI, participatory-audience, and remote-control configurations.
10. Preparation of an operator-review package is authorized. Outreach, external review execution, Public Review Draft status, ASR-001 publication, certification, public conformance claims, scores, rankings, unsupported technical tolerances, final BCI athletic classification, and claims of adoption remain unauthorized.

### Rationale

Internal implementation exposed representational and verification defects that syntax-only validation could not reveal. The bounded v0.2 refinement resolves those defects while preserving all identifiers, exclusions, uncertainty, and historical artifacts. The next useful step is to prepare a review package that lets relevant operators challenge the Working Draft without prematurely opening Public Review or claiming adoption.
""".strip() + "\n"

GENERATED_PROFILES = [
    "ASR_001_TRIAL_PROFILE_TRIAL_01_AUTONOMOUS_V0.2.json",
    "ASR_001_TRIAL_PROFILE_TRIAL_02_REHAB_V1_V0.2.json",
    "ASR_001_TRIAL_PROFILE_TRIAL_02_REHAB_V2_V0.2.json",
    "ASR_001_TRIAL_PROFILE_TRIAL_03_BCI_V0.2.json",
    "ASR_001_TRIAL_PROFILE_TRIAL_04_HUMAN_AI_V0.2.json",
    "ASR_001_TRIAL_PROFILE_TRIAL_05_AUDIENCE_V0.2.json",
    "ASR_001_TRIAL_PROFILE_TRIAL_06_DRONE_V0.2.json",
]

def run(command: list[str]) -> int:
    result = subprocess.run(command)
    return result.returncode

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
    if "## DEC-013 — ASR-001 Candidate Normative Core and Internal-Trial Boundary" not in content:
        raise RuntimeError("DEC-013 is missing; refusing to append DEC-014")
    path.write_text(content.rstrip() + "\n\n" + DECISION_TEXT, encoding="utf-8")
    return True

def write_outputs(appended: bool) -> None:
    tracked = [
        "ASR_001_WORKING_DRAFT_V0.2.md",
        "ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.2.json",
        "ASR_001_CLAUSE_TO_FIELD_MAP_V0.2.json",
        "ASR_001_PROFILE_MODEL_V0.2.json",
        "ASR_001_PROFILE_SCHEMA_V0.2.json",
        "ASR_001_CLAUSE_FRICTION_REGISTER_V0.1.json",
        "ASR_001_INTERNAL_TRIAL_RESULTS.md",
        "ASR_001_REFINEMENT_RESULT.md",
        *GENERATED_PROFILES,
    ]
    hashes = {name: sha256(Path(name)) for name in tracked}

    lines = [
        "# Sprint 11 Validation Result", "",
        "**Asset:** AltisSports  ",
        "**Sprint:** Sprint 11 — ASR-001 Internal Implementation Trials and Clause Refinement  ",
        f"**Date:** {date.today().isoformat()}  ",
        "**Decision:** **PASS**", "",
        "## Validation", "",
        "- internal implementation trials were authorized by Sprint 10;",
        "- seven profile artifacts validate against profile model v0.2;",
        "- six distinct configuration classes and one lifecycle revision pair are exercised;",
        "- every profile contains all thirty clause records;",
        "- applicability and evidence sufficiency remain separate;",
        "- autonomous agency regimes validate without a live human-performance claim;",
        "- BCI embodiment remains unresolved rather than certified;",
        "- participatory actors remain separate from Performance Agents;",
        "- remote craft control remains separate from remote synchronous competition;",
        "- correction and supersession links validate;",
        "- eight friction findings are dispositioned with no scope expansion;",
        "- no score, rank, certification, Public Review, publication, or adoption claim exists;",
        f"- DEC-014 was {'appended' if appended else 'already present'} in the decision log.", "",
        "## SHA-256", "",
        "| File | SHA-256 |",
        "| --- | --- |",
    ]
    for name, digest in hashes.items():
        lines.append(f"| `{name}` | `{digest}` |")
    lines += [
        "",
        "Sprint 11 PASS authorizes operator-review package preparation only.",
        ""
    ]
    Path("SPRINT_11_VALIDATION_RESULT.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )

    gate = """# ASR-001 Internal Implementation Trial Gate Result

**Asset:** AltisSports  
**Sprint:** Sprint 11  
**Gate:** `ASR_001_INTERNAL_TRIAL_GATE.md`  
**Decision:** **PASS — AUTHORIZE OPERATOR-REVIEW PACKAGE PREPARATION ONLY**

## Findings

- T01 PASS — internal trials were authorized.
- T02 PASS — autonomous, support, BCI, human–AI, participatory, and remote-control configurations are represented.
- T03 PASS — every trial applies all thirty clauses.
- T04 PASS — applicability and evidence states are independent.
- T05 PASS — autonomous agency regimes are representable without live human performance.
- T06 PASS — BCI biological control is disclosed while athletic membership remains unresolved.
- T07 PASS — rehabilitation remains a support configuration without clinical certification.
- T08 PASS — participatory actors remain separate from Performance Agents.
- T09 PASS — remote craft control is not misrepresented as remote synchronous competition.
- T10 PASS — correction and supersession validate across the rehabilitation profile pair.
- T11 PASS — evidence-requirement classes remove artificial duplication without weakening evidence integrity.
- T12 PASS — deterministic profile and trial validation pass.
- T13 PASS — clause identifiers and approved scope remain stable.
- T14 PASS — historical v0.1 and corpus artifacts remain unchanged.
- T15 PASS — prohibited publication, certification, scoring, ranking, tolerance, BCI, and adoption outcomes remain absent.

## Authorization Consequence

A written operator-review package can be prepared.

This gate does not authorize sending the package, conducting external review, opening Public Review, publishing ASR-001, certification, or public conformance claims.
"""
    Path("ASR_001_INTERNAL_TRIAL_GATE_RESULT.md").write_text(
        gate, encoding="utf-8"
    )

    authorization = """# ASR-001 Operator-Review Package Preparation Authorization

**Decision:** **AUTHORIZED FOR PACKAGE PREPARATION ONLY**  
**Effective condition:** Sprint 11 validation and internal-trial gate are PASS  
**Normative status:** ASR-001 remains unpublished

## Authorized Next Work

The next sprint can prepare:

- an operator brief explaining the profile-only purpose;
- a reviewer guide;
- role-specific question sets;
- a clause-comment template;
- an issue taxonomy;
- evidence and conflict-of-interest declarations;
- comment disposition and change-control procedures;
- a review corpus excerpt and synthetic examples;
- a review-readiness gate.

## Required Reviewer Classes

The package can be designed for more than one operator class, including:

- sport governance and integrity;
- competition operations;
- XR or spatial-system engineering;
- performance measurement;
- accessibility and adaptive sport;
- research methodology;
- evidence and data governance.

## Preparation Boundary

Package preparation does not authorize:

- contacting reviewers;
- sending invitations;
- conducting interviews or calls;
- opening a public comment channel;
- representing any person or organization as an adopter or endorser.

## Still Unauthorized

- external review execution;
- Public Review Draft status;
- ASR-001 publication;
- certification or certification marks;
- public product, sport, or category conformance claims;
- safety or clinical certification;
- scores, grades, maturity levels, or rankings;
- unsupported remote-synchronous tolerances;
- final BCI athletic classification;
- claims of federation recognition or industry adoption.

## Next Gate

The completed package requires a review-readiness gate before any operator outreach can be considered.
"""
    Path("ASR_001_OPERATOR_REVIEW_PACKAGE_PREPARATION_AUTHORIZATION.md").write_text(
        authorization, encoding="utf-8"
    )

def main() -> int:
    if run([sys.executable, "build_asr001_working_draft_v0_2.py"]) != 0:
        return 1
    if run([sys.executable, "build_asr001_internal_trials.py"]) != 0:
        return 1
    if run([sys.executable, "validate_asr001_internal_trials.py"]) != 0:
        return 1
    try:
        appended = append_decision()
        write_outputs(appended)
    except (OSError, RuntimeError) as exc:
        print(f"ERROR: Sprint 11 could not complete: {exc}", file=sys.stderr)
        return 2
    print(
        "PASS: "
        + (
            "appended DEC-014 to DECISION_LOG.md."
            if appended
            else "DEC-014 already present."
        )
    )
    print(
        "PASS: wrote Sprint 11 validation, trial gate result, "
        "and operator-review package preparation authorization."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
