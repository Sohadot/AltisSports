#!/usr/bin/env python3
"""Run Sprint 10 build, validation, decision append, and gate outputs."""
from __future__ import annotations

import hashlib
import subprocess
import sys
from datetime import date
from pathlib import Path

DECISION_MARKER = "## DEC-013 — ASR-001 Candidate Normative Core and Internal-Trial Boundary"

DECISION_TEXT = """
---

## DEC-013 — ASR-001 Candidate Normative Core and Internal-Trial Boundary

**Status:** Ratified upon Sprint 10 PASS  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `ASR_001_WORKING_DRAFT_V0.1.md`, `ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.1.json`, and `ASR_001_PROFILE_MODEL_V0.1.json`

### Decision

1. The ASR-001 Candidate Normative Core v0.1 is accepted as a non-public Working Draft.
2. The core contains exactly thirty clause-level candidate obligations using the stable identifiers authorized by DEC-012.
3. Candidate normative language is permitted only inside the governed Working Draft and does not establish publication, recognition, adoption, or a certification program.
4. Every clause retains its approved domain, applicability, evidence or governance dependency, verification approach, rationale, uncertainty handling, exclusion guards, and profile field path.
5. The candidate implementation profile model v0.1 is clause-derived and is distinct from the Boundary Case Schema.
6. Candidate profile validation checks the profile document or machine-readable instance only. It does not validate or certify the underlying sport, product, safety, clinical efficacy, quality, federation recognition, category membership, or market superiority.
7. Conditional applicability is explicit. A non-triggered clause is not a failure, and missing evidence is not converted into a zero, score, grade, or ranking.
8. Two synthetic profiles are accepted as deterministic structural fixtures. They are not market records and create no provider claims.
9. Internal implementation trials are authorized. Clause changes during those trials require recorded implementation evidence or a governance issue.
10. ASR-001 publication, Public Review Draft status, certification, public conformance claims, scores, maturity levels, vendor rankings, unsupported technical tolerances, final BCI athletic classification, and claims of industry adoption remain unauthorized.

### Rationale

The approved scope and candidate architecture now have clause-level expression and a separate operational profile model. Internal implementation is the next reliable test: it can expose clauses that are ambiguous, untestable, overbroad, duplicative, or poorly represented before any external review or publication posture is considered.
""".strip() + "\n"

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
    if "## DEC-012 — ASR-001 Working Draft Architecture and Clause-Authoring Boundary" not in content:
        raise RuntimeError("DEC-012 is missing; refusing to append DEC-013")
    path.write_text(content.rstrip() + "\n\n" + DECISION_TEXT, encoding="utf-8")
    return True

def run(command: list[str]) -> int:
    result = subprocess.run(command)
    return result.returncode

def write_outputs(appended: bool) -> None:
    tracked = [
        "ASR_001_WORKING_DRAFT_V0.1.md",
        "ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.1.json",
        "ASR_001_CLAUSE_TO_FIELD_MAP_V0.1.json",
        "ASR_001_PROFILE_MODEL_V0.1.json",
        "ASR_001_PROFILE_SCHEMA_V0.1.json",
        "ASR_001_SYNTHETIC_PROFILE_LOCAL_V0.1.json",
        "ASR_001_SYNTHETIC_PROFILE_DISTRIBUTED_V0.1.json",
        "ASR_001_CONFORMANCE_BOUNDARY_DRAFT.md"
    ]
    hashes = {name: sha256(Path(name)) for name in tracked}

    profile_result = """# ASR-001 Candidate Profile Validation Result

**Working Draft version:** 0.1  
**Decision:** **PASS**

## Fixtures

- `ASR_001_SYNTHETIC_PROFILE_LOCAL_V0.1.json` — PASS
- `ASR_001_SYNTHETIC_PROFILE_DISTRIBUTED_V0.1.json` — PASS

## Checks

- exactly thirty clause records are present in each profile;
- unconditional clauses are applicable;
- conditional clauses follow feature triggers;
- applicable clauses link to evidence records;
- non-applicable clauses do not attach evidence;
- profile and subject identifiers agree;
- distributed, performance, measurement, contest, spatial-function, actor, responsibility, and distribution triggers are structurally checked;
- prohibited score, grade, ranking, and certification keys are absent.

The fixtures are synthetic. PASS does not establish a real product claim or external conformance.
"""
    Path("ASR_001_PROFILE_VALIDATION_RESULT.md").write_text(profile_result, encoding="utf-8")

    lines = [
        "# Sprint 10 Validation Result", "",
        "**Asset:** AltisSports  ",
        "**Sprint:** Sprint 10 — ASR-001 Candidate Normative Core and Implementation Profile Model v0.1  ",
        f"**Date:** {date.today().isoformat()}  ",
        "**Decision:** **PASS**", "",
        "## Validation", "",
        "- the Sprint 9 clause-authoring authorization is present;",
        "- thirty stable clauses are rendered in the Candidate Normative Core;",
        "- D01–D15 each retain exactly two clauses;",
        "- every clause retains applicability, verification, traceability, rationale, uncertainty, exclusions, and a field path;",
        "- the implementation model is distinct from the Boundary Case Schema;",
        "- both synthetic fixtures pass deterministic profile validation;",
        "- candidate conformance remains profile-only;",
        "- no score, grade, ranking, certification, public-review, or adoption claim exists;",
        f"- DEC-013 was {'appended' if appended else 'already present'} in the decision log.", "",
        "## SHA-256", "",
        "| File | SHA-256 |",
        "| --- | --- |",
    ]
    for name, digest in hashes.items():
        lines.append(f"| `{name}` | `{digest}` |")
    lines += ["", "Sprint 10 PASS authorizes internal implementation trials only.", ""]
    Path("SPRINT_10_VALIDATION_RESULT.md").write_text("\n".join(lines), encoding="utf-8")

    gate_result = """# ASR-001 Candidate Normative Core Gate Result

**Asset:** AltisSports  
**Sprint:** Sprint 10  
**Gate:** `ASR_001_NORMATIVE_CORE_GATE.md`  
**Decision:** **PASS — AUTHORIZE INTERNAL IMPLEMENTATION TRIALS ONLY**

## Findings

- N01 PASS — clause authoring was authorized.
- N02 PASS — exactly thirty stable clauses exist.
- N03 PASS — every clause remains within the approved scope.
- N04 PASS — candidate normative language is explicit and the draft remains unpublished.
- N05 PASS — applicability triggers and states are explicit.
- N06 PASS — verification statements are preserved.
- N07 PASS — every clause maps to a profile field.
- N08 PASS — the profile model is clause-derived and separate from the research schema.
- N09 PASS — local and distributed synthetic profiles validate.
- N10 PASS — deterministic validation checks trigger logic, evidence references, clause coverage, and prohibited keys.
- N11 PASS — conformance remains profile-only.
- N12 PASS — excluded scores, rankings, certifications, tolerances, and status claims remain absent.
- N13 PASS — historical artifacts are not rewritten.
- N14 PASS — ASR-001 remains a non-public Working Draft.

## Authorization Consequence

Internal implementation trials can apply the model to additional bounded configurations and record clause friction.

Public Review, publication, certification, and external conformance claims remain unauthorized.
"""
    Path("ASR_001_NORMATIVE_CORE_GATE_RESULT.md").write_text(gate_result, encoding="utf-8")

    authorization = """# ASR-001 Internal Implementation Trial Authorization

**Decision:** **AUTHORIZED FOR INTERNAL IMPLEMENTATION TRIALS ONLY**  
**Effective condition:** Sprint 10 validation and Candidate Normative Core gate are PASS  
**Normative status:** ASR-001 remains unpublished

## Authorized Next Work

The next sprint can:

- create bounded trial profiles for distinct configuration classes;
- apply all thirty clauses and applicability triggers;
- record ambiguity, duplication, untestable language, missing fields, and verification burden;
- propose clause clarification, narrowing, merging, or conditionality changes;
- test correction and supersession;
- test the profile model independently of the research corpus schema;
- prepare an operator-review package only if the trial gate passes.

## Trial Requirements

Each trial records:

- the bounded subject and configuration;
- evidence sources;
- triggered and non-triggered clauses;
- validation result;
- human-review issues;
- clause-level friction;
- proposed disposition;
- effect on scope and exclusions.

## Still Unauthorized

- ASR-001 publication;
- Public Review Draft status;
- certification or certification marks;
- public product, sport, or category conformance claims;
- safety or clinical certification;
- scores, grades, maturity levels, or rankings;
- unsupported remote-synchronous tolerances;
- final BCI athletic classification;
- claims of federation recognition or industry adoption.

## Next Gate

Internal trials require a separate implementation-trial gate before any operator-review or public-review posture is considered.
"""
    Path("ASR_001_INTERNAL_IMPLEMENTATION_TRIAL_AUTHORIZATION.md").write_text(
        authorization, encoding="utf-8"
    )

def main() -> int:
    if run([sys.executable, "build_asr001_working_draft_v0_1.py"]) != 0:
        return 1
    profiles = [
        "ASR_001_SYNTHETIC_PROFILE_LOCAL_V0.1.json",
        "ASR_001_SYNTHETIC_PROFILE_DISTRIBUTED_V0.1.json"
    ]
    for profile in profiles:
        if run([sys.executable, "validate_asr001_profile.py", profile]) != 0:
            return 1
    if run([sys.executable, "validate_asr001_working_draft_v0_1.py"]) != 0:
        return 1
    try:
        appended = append_decision()
        write_outputs(appended)
    except (OSError, RuntimeError) as exc:
        print(f"ERROR: Sprint 10 could not complete: {exc}", file=sys.stderr)
        return 2
    print("PASS: " + ("appended DEC-013 to DECISION_LOG.md." if appended else "DEC-013 already present."))
    print("PASS: wrote Sprint 10 validation, gate result, profile validation result, and internal-trial authorization.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
