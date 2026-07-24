# Sprint 10 Execution

## Purpose

Create the ASR-001 Candidate Normative Core and a clause-derived implementation profile model v0.1 for internal trial.

## Authored Files

- `ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.1.json`
- `ASR_001_PROFILE_MODEL_V0.1.json`
- `ASR_001_PROFILE_SCHEMA_V0.1.json`
- `ASR_001_SYNTHETIC_PROFILE_LOCAL_V0.1.json`
- `ASR_001_SYNTHETIC_PROFILE_DISTRIBUTED_V0.1.json`
- `ASR_001_CONFORMANCE_BOUNDARY_DRAFT.md`
- `ASR_001_NORMATIVE_CORE_GATE.md`
- `build_asr001_working_draft_v0_1.py`
- `validate_asr001_profile.py`
- `validate_asr001_working_draft_v0_1.py`
- `run_sprint10.py`
- `README.md`
- `SPRINT_10_EXECUTION.md`
- `SPRINT_10_MANIFEST.json`

## Generated Files

- `ASR_001_WORKING_DRAFT_V0.1.md`
- `ASR_001_CLAUSE_TO_FIELD_MAP_V0.1.json`
- `ASR_001_PROFILE_VALIDATION_RESULT.md`
- `SPRINT_10_VALIDATION_RESULT.md`
- `ASR_001_NORMATIVE_CORE_GATE_RESULT.md`
- `ASR_001_INTERNAL_IMPLEMENTATION_TRIAL_AUTHORIZATION.md`

The runner appends `DEC-013` to `DECISION_LOG.md`.

## Local Command

```powershell
python .\run_sprint10.py
```

## Expected Result

```text
PASS: wrote ASR_001_WORKING_DRAFT_V0.1.md
PASS: wrote ASR_001_CLAUSE_TO_FIELD_MAP_V0.1.json
PASS: ASR_001_SYNTHETIC_PROFILE_LOCAL_V0.1.json validates against the ASR-001 candidate profile model.
PASS: ASR_001_SYNTHETIC_PROFILE_DISTRIBUTED_V0.1.json validates against the ASR-001 candidate profile model.
PASS: ASR-001 Candidate Normative Core and implementation profile model v0.1 validate.
PASS: appended DEC-013 to DECISION_LOG.md.
PASS: wrote Sprint 10 validation, gate result, profile validation result, and internal-trial authorization.
```

## Commit Boundary

Commit only after every PASS appears.

Historical research schemas, data, scope documents, Sprint 9 catalog, and prior gate records remain unchanged.
