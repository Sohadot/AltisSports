#!/usr/bin/env python3
# Run Sprint 8 validation, append DEC-011, and write gate records.
from __future__ import annotations

import hashlib
import subprocess
import sys
from datetime import date
from pathlib import Path

DECISION_MARKER = '## DEC-011 — ASR-001 Scope Approval and Requirements-Drafting Boundary'

DECISION_TEXT = r'''
---

## DEC-011 — ASR-001 Scope Approval and Requirements-Drafting Boundary

**Status:** Ratified upon Sprint 8 PASS  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `ASR_001_SCOPE_DRAFT.md`, `ASR_001_SCOPE_TRACEABILITY.md`, and the reviewed BC-001–BC-020 v0.3 corpus

### Decision

1. The scope of `ASR-001 — Spatial Athletic System Evidence Profile` is approved.
2. The profiled subject is one bounded, versioned system configuration. Findings about an activity, product, platform, event, organization, or deployment may not be silently generalized across objects.
3. The approved scope contains fifteen descriptive domains covering object identity, context, agency, interface, arena, rules, sensing, measurement, officiation, spatial functions, participation, safety/accessibility disclosure, evidence, governance, and machine-readable metadata.
4. ASR-001 is an evidence-profile project. It is not a universal sport definition, product-rating system, federation-recognition mechanism, safety or clinical certification, or category-ownership claim.
5. Any future conformance model is bounded to the evidence-profile document or machine-readable profile instance. It may not certify the underlying sport, system, product quality, safety, clinical efficacy, or market superiority.
6. Requirements drafting is authorized for a governed Working Draft only.
7. Every future candidate clause must map to an approved scope domain, a defined problem, evidence or governance dependency, applicability condition, verification approach, rationale, and affected exclusions or uncertainty.
8. The research corpus schema is not automatically the ASR-001 implementation schema. A separate implementation decision is required.
9. Publication as a standard, Public Review Draft status, certification, product or sport conformance claims, scoring, maturity levels, vendor rankings, and claims of industry adoption remain unauthorized.
10. External operator review and hosted validation remain conditions before a normative public release can be considered.

### Rationale

The approved scope converts twenty adversarial cases into one bounded standardization problem: how to disclose and support evidence about a spatial-athletic system configuration without converting documentation into product judgment or category certification. This is sufficient to begin a controlled Working Draft, but not to claim a standard, adoption, or conformance program.
'''.strip() + '\n'

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as fh:
        for chunk in iter(lambda: fh.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()

def append_decision() -> bool:
    path = Path('DECISION_LOG.md')
    content = path.read_text(encoding='utf-8')
    if DECISION_MARKER in content:
        return False
    if '## DEC-010 — ASR-001 Scope Drafting Authorization' not in content:
        raise RuntimeError('DEC-010 is missing; refusing to append DEC-011')
    path.write_text(content.rstrip() + '\n\n' + DECISION_TEXT, encoding='utf-8')
    return True

def write_results(decision_appended: bool) -> None:
    tracked = ['ASR_001_SCOPE_DRAFT.md','ASR_001_SCOPE_MODEL.json',
               'ASR_001_SCOPE_TRACEABILITY.md','ASR_001_DEFERRED_ISSUES.md',
               'ASR_001_SCOPE_GATE.md','boundary-cases-001-020.v0.3.json']
    hashes = {name: sha256(Path(name)) for name in tracked}
    lines = [
        '# Sprint 8 Validation Result','',
        '**Asset:** AltisSports  ',
        '**Sprint:** Sprint 8 — ASR-001 Scope Draft and Scope-Approval Gate  ',
        f'**Date:** {date.today().isoformat()}  ',
        '**Decision:** **PASS**','',
        '## Validation','',
        '- the scope subject is bounded to one versioned system configuration;',
        '- fifteen scope domains are present in the document and machine model;',
        '- every required exclusion is preserved;',
        '- future conformance is bounded to the profile document or instance;',
        '- the scope draft contains no prohibited normative requirement keywords;',
        '- the traceability map covers D01–D15;',
        '- the deferred register preserves requirements and review questions;',
        '- the current evidence corpus contains BC-001–BC-020;',
        '- no score, maturity ladder, ranking, certification, or category-ownership mechanism exists;',
        f"- DEC-011 was {'appended' if decision_appended else 'already present'} in the append-only decision log.",'',
        '## SHA-256','',
        '| File | SHA-256 |','| --- | --- |'
    ]
    for name, digest in hashes.items():
        lines.append(f'| `{name}` | `{digest}` |')
    lines += ['', 'Validation approves the scope artifact. It does not publish ASR-001 or certify an implementation.', '']
    Path('SPRINT_8_VALIDATION_RESULT.md').write_text('\n'.join(lines), encoding='utf-8')

    gate = '''# ASR-001 Scope Gate Result

**Asset:** AltisSports  
**Sprint:** Sprint 8 — ASR-001 Scope Draft and Scope-Approval Gate  
**Gate:** `ASR_001_SCOPE_GATE.md`  
**Decision:** **APPROVE SCOPE — AUTHORIZE REQUIREMENTS DRAFTING ONLY**

## Gate Findings

- G01 PASS — the subject matches the DEC-010 authorization.
- G02 PASS — one bounded, versioned system configuration is the profile subject.
- G03 PASS — the problem is disclosure and evidence traceability, not universal sport definition.
- G04 PASS — institutional, technical, research, procurement, and machine-readable uses are identified.
- G05 PASS — D01–D15 are traced to corpus findings and governing documents.
- G06 PASS — all required exclusions remain explicit.
- G07 PASS — possible future conformance is limited to the profile document or instance.
- G08 PASS — uncertainty states remain qualitative and visible.
- G09 PASS — no normative clauses occur in the scope draft.
- G10 PASS — no score, maturity ladder, ranking, or certification mechanism exists.
- G11 PASS — dependencies are explicit and the research schema is not silently adopted as an implementation schema.
- G12 PASS — unresolved requirements and review questions remain in the deferred register.

## Approved Boundary

The approved ASR-001 scope is an evidence and disclosure profile for one bounded spatial-athletic system configuration.

Scope approval does not establish system quality, category membership, safety, clinical efficacy, federation recognition, or market rank.

## Authorization Consequence

A governed Working Draft can now be developed. Publication, Public Review Draft status, certification, scoring, product or sport conformance, and adoption claims remain unauthorized.
'''
    Path('ASR_001_SCOPE_GATE_RESULT.md').write_text(gate, encoding='utf-8')

    authorization = '''# ASR-001 Requirements-Drafting Authorization

**Decision:** **AUTHORIZED FOR GOVERNED WORKING-DRAFT REQUIREMENTS ONLY**  
**Effective condition:** Sprint 8 validation and scope gate are PASS  
**Normative status:** No standard is issued

## Authorized Next Work

The next sprint can develop:

- the ASR-001 Working Draft architecture;
- evidence-to-clause traceability;
- candidate profile obligations and conditional applicability;
- informative examples separated from clauses;
- a candidate implementation-model boundary;
- a draft profile-validation approach.

## Clause Boundary

Every candidate clause is connected to:

- an approved scope domain D01–D15;
- a defined disclosure or evidence problem;
- corpus evidence or a declared governance dependency;
- the profiled object and applicability condition;
- a verification approach;
- rationale;
- affected exclusions and uncertainty.

## Still Unauthorized

This authorization does not permit:

- publication of ASR-001 as a standard;
- Public Review Draft status;
- certification or a certification mark;
- product, sport, or category conformance claims;
- safety or clinical certification;
- scores, levels, rankings, or paid favorable classification;
- unsupported remote-synchronous technical tolerances;
- final BCI athletic classification;
- claims of federation recognition or industry adoption.

## Next Gate

A Working Draft gate is required before any Public Review Draft or external conformance claim can be considered.
'''
    Path('ASR_001_REQUIREMENTS_DRAFTING_AUTHORIZATION.md').write_text(authorization, encoding='utf-8')

def main() -> int:
    result = subprocess.run([sys.executable, 'validate_asr001_scope.py'])
    if result.returncode != 0:
        return result.returncode
    try:
        appended = append_decision()
        write_results(appended)
    except (OSError, RuntimeError) as exc:
        print(f'ERROR: Sprint 8 could not complete: {exc}', file=sys.stderr)
        return 2
    print("PASS: " + ("appended DEC-011 to DECISION_LOG.md." if appended else "DEC-011 already present."))
    print('PASS: wrote Sprint 8 validation, scope-gate result, and requirements-drafting authorization.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
