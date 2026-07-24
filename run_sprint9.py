#!/usr/bin/env python3
"""Run Sprint 9 map generation, validation, decision append, and gate outputs."""
from __future__ import annotations

import hashlib
import subprocess
import sys
from datetime import date
from pathlib import Path

DECISION_MARKER = "## DEC-012 — ASR-001 Working Draft Architecture and Clause-Authoring Boundary"

DECISION_TEXT = """
---

## DEC-012 — ASR-001 Working Draft Architecture and Clause-Authoring Boundary

**Status:** Ratified upon Sprint 9 PASS  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `ASR_001_WORKING_DRAFT_ARCHITECTURE.md`, `ASR_001_CLAUSE_CATALOG_V0.1.json`, and `ASR_001_EVIDENCE_TO_CLAUSE_MAP.md`

### Decision

1. The ASR-001 Working Draft architecture is accepted as the governing structure for clause authoring.
2. Candidate requirement identifiers use the stable form `ASR001-DNN-CNN`, with every candidate mapped to one approved scope domain D01–D15.
3. The Sprint 9 baseline contains thirty candidate obligation records, exactly two for each approved domain.
4. Candidate records are not normative clauses. They define obligation intent, applicability, evidence, governance dependencies, verification, rationale, uncertainty, and exclusion guards.
5. Every future clause must retain traceability to its candidate record or record an explicit replacement decision.
6. Applicability is conditional and evidence-aware. A non-triggered clause is not a failed clause, and missing evidence does not become an underlying-system score.
7. Verification concerns the evidence-profile document or instance. It does not validate the underlying sport, product quality, safety, clinical efficacy, federation recognition, or market superiority.
8. The boundary-case research schema is not adopted as the ASR-001 implementation schema. A separate implementation-profile decision is required.
9. Candidate clause authoring is authorized for a governed non-public Working Draft only.
10. Publication, Public Review Draft status, certification, product or sport conformance claims, scores, levels, rankings, unsupported technical tolerances, final BCI athletic classification, and claims of industry adoption remain unauthorized.

### Rationale

The approved scope is now decomposed into uniquely identified, evidence-linked, conditionally applicable, and verifiable candidate obligations. This is enough to begin clause-level drafting without losing the exclusions and uncertainty that made the research credible. It is not enough to release a standard or conformance program.
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
    if "## DEC-011 — ASR-001 Scope Approval and Requirements-Drafting Boundary" not in content:
        raise RuntimeError("DEC-011 is missing; refusing to append DEC-012")
    path.write_text(content.rstrip() + "\n\n" + DECISION_TEXT, encoding="utf-8")
    return True

def write_outputs(appended: bool) -> None:
    tracked = [
        "ASR_001_WORKING_DRAFT_ARCHITECTURE.md",
        "ASR_001_CLAUSE_CATALOG_V0.1.json",
        "ASR_001_EVIDENCE_TO_CLAUSE_MAP.md",
        "ASR_001_CLAUSE_COVERAGE_REPORT.md",
        "ASR_001_APPLICABILITY_MODEL.md",
        "ASR_001_VERIFICATION_MODEL_DRAFT.md",
        "ASR_001_IMPLEMENTATION_MODEL_BOUNDARY.md",
    ]
    hashes = {name: sha256(Path(name)) for name in tracked}

    lines = [
        "# Sprint 9 Validation Result", "",
        "**Asset:** AltisSports  ",
        "**Sprint:** Sprint 9 — ASR-001 Working Draft Architecture and Evidence-to-Clause Mapping  ",
        f"**Date:** {date.today().isoformat()}  ",
        "**Decision:** **PASS**", "",
        "## Validation", "",
        "- the approved D01–D15 scope is preserved;",
        "- 30 unique candidate clauses exist;",
        "- every domain has exactly two candidate clauses;",
        "- every candidate declares applicability, evidence or governance dependencies, verification, rationale, uncertainty, and exclusion guards;",
        "- evidence-to-clause and coverage reports were generated deterministically;",
        "- the research corpus schema remains separate from the future implementation model;",
        "- examples remain informative;",
        "- no candidate has been finalized as normative prose;",
        "- no score, maturity ladder, certification, vendor ranking, or public-release claim exists;",
        f"- DEC-012 was {'appended' if appended else 'already present'} in the decision log.", "",
        "## SHA-256", "",
        "| File | SHA-256 |",
        "| --- | --- |",
    ]
    for name, digest in hashes.items():
        lines.append(f"| `{name}` | `{digest}` |")
    lines += ["", "Validation approves the Working Draft architecture, not ASR-001 publication.", ""]
    Path("SPRINT_9_VALIDATION_RESULT.md").write_text("\n".join(lines), encoding="utf-8")

    gate = """# ASR-001 Working Draft Architecture Gate Result

**Asset:** AltisSports  
**Sprint:** Sprint 9  
**Gate:** `ASR_001_WORKING_DRAFT_GATE.md`  
**Decision:** **PASS — AUTHORIZE CANDIDATE CLAUSE AUTHORING ONLY**

## Findings

- W01 PASS — the approved scope and exclusions are preserved.
- W02 PASS — all candidate identifiers are unique and domain-aligned.
- W03 PASS — D01–D15 each contain exactly two candidates.
- W04 PASS — every candidate maps to cases or governance dependencies.
- W05 PASS — applicability classes and conditions are explicit.
- W06 PASS — verification modes are explicit.
- W07 PASS — rationale and uncertainty handling are present.
- W08 PASS — exclusion guards prevent scores, rankings, and certification.
- W09 PASS — the research schema is not adopted as the implementation schema.
- W10 PASS — examples remain informative.
- W11 PASS — the artifact remains a non-public Working Draft architecture.
- W12 PASS — deferred issues remain unresolved and visible.

## Authorization Consequence

Clause-level Working Draft text can be authored from the candidate catalog.

This does not authorize publication, Public Review, certification, conformance claims, or industry-adoption claims.
"""
    Path("ASR_001_WORKING_DRAFT_GATE_RESULT.md").write_text(gate, encoding="utf-8")

    authorization = """# ASR-001 Candidate Clause Authoring Authorization

**Decision:** **AUTHORIZED FOR NON-PUBLIC WORKING-DRAFT CLAUSE AUTHORING ONLY**  
**Effective condition:** Sprint 9 validation and Working Draft architecture gate are PASS  
**Normative status:** ASR-001 remains unpublished

## Authorized Next Work

The next sprint can:

- convert candidate obligation intents into clause-level Working Draft text;
- distinguish unconditional and conditional clauses;
- define candidate verification statements;
- derive a candidate operational profile model from clauses;
- preserve evidence-to-clause traceability;
- create informative examples separated from clauses.

## Drafting Conditions

Every clause remains connected to:

- its stable clause identifier;
- one approved domain;
- applicability;
- evidence or governance dependency;
- verification;
- rationale;
- uncertainty handling;
- exclusion guards.

## Still Unauthorized

- ASR-001 publication;
- Public Review Draft status;
- certification or certification marks;
- product, sport, or category conformance claims;
- safety or clinical certification;
- scores, maturity levels, or rankings;
- unsupported technical tolerances;
- final BCI athletic classification;
- claims of federation recognition or industry adoption.

## Next Gate

The candidate normative core and implementation profile model require a separate Working Draft gate.
"""
    Path("ASR_001_CLAUSE_AUTHORING_AUTHORIZATION.md").write_text(authorization, encoding="utf-8")

def main() -> int:
    build = subprocess.run([sys.executable, "build_asr001_clause_map.py"])
    if build.returncode != 0:
        return build.returncode
    validation = subprocess.run([sys.executable, "validate_asr001_working_architecture.py"])
    if validation.returncode != 0:
        return validation.returncode
    try:
        appended = append_decision()
        write_outputs(appended)
    except (OSError, RuntimeError) as exc:
        print(f"ERROR: Sprint 9 could not complete: {exc}", file=sys.stderr)
        return 2
    print("PASS: " + ("appended DEC-012 to DECISION_LOG.md." if appended else "DEC-012 already present."))
    print("PASS: wrote Sprint 9 validation, Working Draft gate result, and clause-authoring authorization.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
