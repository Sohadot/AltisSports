#!/usr/bin/env python3
"""Validate Sprint 8 ASR-001 scope artifacts without third-party packages."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

REQUIRED_FILES = [
    'ASR_001_SCOPE_DRAFT.md','ASR_001_SCOPE_MODEL.json','ASR_001_SCOPE_TRACEABILITY.md',
    'ASR_001_DEFERRED_ISSUES.md','ASR_001_SCOPE_GATE.md',
    'ASR_001_SCOPE_DRAFTING_AUTHORIZATION.md','ASR_DRAFTING_GOVERNANCE.md',
    'STANDARDIZATION_READINESS_RESULT.md','CORPUS_APPLICATION_FINDINGS_V0.3.md',
    'boundary-cases-001-020.v0.3.json','SOURCE_AND_CLAIM_POLICY.md','QUALITY_GATE.md',
    'FIRST_PRINCIPLES.md','ONTOLOGY.md','AS3_STACK.md','DECISION_LOG.md'
]

REQUIRED_HEADINGS = [
    '## 1. Scope Statement','## 2. Problem Being Addressed',
    '## 3. Profile Subject and Object Lock','## 4. Intended Users',
    '## 5. Intended Uses','## 7. In-Scope Profile Domains',
    '## 8. Evidence and Claim Boundary','## 9. Uncertainty and State Representation',
    '## 10. Future Conformance Boundary','## 11. Explicit Exclusions',
    '## 12. Dependencies','## 13. Relationship to the Boundary Corpus',
    '## 16. Scope Verdict'
]

REQUIRED_EXCLUSIONS = {
    'universal_sport_definition','minimum_embodiment_threshold','total_score',
    'spatiality_level','maturity_level','vendor_ranking','product_ranking',
    'automatic_category_certification','federation_recognition','safety_certification',
    'clinical_efficacy_requirements','remote_synchronous_technical_tolerances',
    'final_bci_athletic_membership','causal_attribution_scoring',
    'paid_favorable_classification'
}

FORBIDDEN_SCOPE_TOKENS = ['MUST','MUST NOT','SHOULD','SHOULD NOT','MAY','SHALL','SHALL NOT']
FORBIDDEN_MODEL_KEYS = {'total_score','spatiality_score','maturity_level_value','certification_status'}

def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(value, dict):
        raise ValueError(f'{path} must contain an object')
    return value

def walk_keys(value: Any, found: set[str]) -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            found.add(key)
            walk_keys(item, found)
    elif isinstance(value, list):
        for item in value:
            walk_keys(item, found)

def validate() -> list[str]:
    errors: list[str] = []
    for name in REQUIRED_FILES:
        if not Path(name).exists():
            errors.append(f'missing required file: {name}')
    if errors:
        return errors

    scope = Path('ASR_001_SCOPE_DRAFT.md').read_text(encoding='utf-8')
    for heading in REQUIRED_HEADINGS:
        if heading not in scope:
            errors.append(f'scope draft missing heading: {heading}')
    for token in FORBIDDEN_SCOPE_TOKENS:
        if re.search(rf'\b{re.escape(token)}\b', scope):
            errors.append(f'scope draft contains prohibited normative token: {token}')

    domain_ids = re.findall(r'^### (D\d{2}) — ', scope, flags=re.MULTILINE)
    expected_domains = [f'D{i:02d}' for i in range(1, 16)]
    if domain_ids != expected_domains:
        errors.append(f'scope domains must be exactly D01-D15 in order; got {domain_ids}')

    model = load_json(Path('ASR_001_SCOPE_MODEL.json'))
    if model.get('asr_id') != 'ASR-001':
        errors.append('scope model asr_id must be ASR-001')
    if model.get('working_title') != 'Spatial Athletic System Evidence Profile':
        errors.append('scope model title mismatch')
    if model.get('normative_status') != 'descriptive_scope_only_no_standard_issued':
        errors.append('scope model normative status is not scope-only')

    model_domains = [item.get('id') for item in model.get('in_scope_domains', []) if isinstance(item, dict)]
    if model_domains != expected_domains:
        errors.append('scope model domains must be exactly D01-D15')

    exclusions = set(model.get('excluded_outcomes', []))
    missing_exclusions = sorted(REQUIRED_EXCLUSIONS - exclusions)
    if missing_exclusions:
        errors.append(f'scope model missing required exclusions: {missing_exclusions}')

    boundary = model.get('future_conformance_boundary', {})
    if boundary.get('profile_document_or_instance_only') is not True:
        errors.append('future conformance boundary must be profile-only')
    for key in ['underlying_system_certification','sport_certification',
                'product_quality_endorsement','safety_or_clinical_certification']:
        if boundary.get(key) is not False:
            errors.append(f'future conformance boundary must keep {key}=false')

    found_keys: set[str] = set()
    walk_keys(model, found_keys)
    prohibited = sorted(FORBIDDEN_MODEL_KEYS & found_keys)
    if prohibited:
        errors.append(f'scope model contains prohibited keys: {prohibited}')

    traceability = Path('ASR_001_SCOPE_TRACEABILITY.md').read_text(encoding='utf-8')
    for domain_id in expected_domains:
        if domain_id not in traceability:
            errors.append(f'traceability map missing {domain_id}')

    deferred = Path('ASR_001_DEFERRED_ISSUES.md').read_text(encoding='utf-8')
    deferred_ids = set(re.findall(r'\| (DI-\d{3}) \|', deferred))
    if len(deferred_ids) < 12:
        errors.append('deferred issues register must contain at least 12 distinct issues')

    corpus = load_json(Path('boundary-cases-001-020.v0.3.json'))
    cases = corpus.get('cases')
    if not isinstance(cases, list) or len(cases) != 20 or corpus.get('case_count') != 20:
        errors.append('current corpus must contain 20 cases')
    else:
        ids = sorted(case.get('case_id') for case in cases if isinstance(case, dict))
        expected_ids = [f'BC-{i:03d}' for i in range(1, 21)]
        if ids != expected_ids:
            errors.append('current corpus identifiers must be exactly BC-001 through BC-020')

    readiness = Path('STANDARDIZATION_READINESS_RESULT.md').read_text(encoding='utf-8')
    if 'AUTHORIZE SCOPE DRAFTING ONLY' not in readiness:
        errors.append('standardization readiness does not authorize scope drafting')
    authorization = Path('ASR_001_SCOPE_DRAFTING_AUTHORIZATION.md').read_text(encoding='utf-8')
    if 'AUTHORIZED FOR SCOPE DRAFTING ONLY' not in authorization:
        errors.append('scope drafting authorization is absent')
    decision_log = Path('DECISION_LOG.md').read_text(encoding='utf-8')
    if 'DEC-010 — ASR-001 Scope Drafting Authorization' not in decision_log:
        errors.append('DECISION_LOG.md does not contain DEC-010')
    return errors

def main() -> int:
    try:
        errors = validate()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f'ERROR: validation could not run: {exc}', file=sys.stderr)
        return 2
    if errors:
        print(f'FAIL: {len(errors)} validation error(s)')
        for error in errors:
            print(f'- {error}')
        return 1
    print('PASS: ASR-001 scope artifacts validate against the Sprint 8 gate.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
