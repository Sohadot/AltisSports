# Sprint 4 Local Execution

**Target:** `main/root`  
**Working model:** local repository → GitHub Desktop commit → push  
**Commit message:** `Establish corpus schema v0.2 and second-stratum readiness`

## 1. Copy the Sprint 4 Inputs

Copy these files into the repository root:

- `BOUNDARY_CASE_SCHEMA_V0.2.json`
- `SCHEMA_MIGRATION_V0.1_TO_V0.2.md`
- `migrate_boundary_cases_v0_1_to_v0_2.py`
- `validate_boundary_cases.py`
- `run_sprint4.py`
- `DATASET_LICENSE.md`
- `SECOND_STRATUM_DESIGN.md`
- `DECISION_LOG.md` — replaces the current file by appending DEC-007
- `README.md` — replaces the current status page
- `SPRINT_4_EXECUTION.md`
- `SPRINT_4_MANIFEST.json`

Do not replace or edit:

- `BOUNDARY_CASE_SCHEMA.json`
- `boundary-cases-001-010.json`
- `BOUNDARY_CASE_METHOD.md`
- `BOUNDARY_CASES_001_010.md`
- `INVARIANCE_FINDINGS_V0.1.md`
- `SPRINT_2_GATE_RESULT.md`

## 2. Preflight

From PowerShell in the repository root:

```powershell
python --version
python -m py_compile `
  .\migrate_boundary_cases_v0_1_to_v0_2.py `
  .\validate_boundary_cases.py `
  .\run_sprint4.py
```

The scripts require Python 3.10 or later and use only the standard library.

Confirm that the historical files are tracked and clean:

```powershell
git status --short
git diff --exit-code -- `
  BOUNDARY_CASE_SCHEMA.json `
  boundary-cases-001-010.json `
  BOUNDARY_CASE_METHOD.md `
  BOUNDARY_CASES_001_010.md
```

The second command must return no diff.

## 3. Execute Sprint 4

```powershell
python .\run_sprint4.py
```

Expected terminal result:

```text
PASS: Sprint 4 generated boundary-cases-001-010.v0.2.json, SPRINT_4_VALIDATION_RESULT.md, and SPRINT_4_GATE_RESULT.md.
```

The runner will:

1. validate each historical case against schema v0.1;
2. hash the historical schema and dataset;
3. create `boundary-cases-001-010.v0.2.json`;
4. validate every migrated record against schema v0.2;
5. check case IDs, record count, evidence references, migration status, and prohibited scoring keys;
6. verify that the historical files remain byte-for-byte unchanged;
7. write the validation and gate records only after PASS.

## 4. Independent Validation

Run the validator again directly:

```powershell
python .\validate_boundary_cases.py `
  --schema .\BOUNDARY_CASE_SCHEMA_V0.2.json `
  --data .\boundary-cases-001-010.v0.2.json
```

Expected result:

```text
PASS: 10 cases validate against BOUNDARY_CASE_SCHEMA_V0.2.json; cross-record checks passed.
```

## 5. Historical-Integrity Check

```powershell
git diff --exit-code -- `
  BOUNDARY_CASE_SCHEMA.json `
  boundary-cases-001-010.json `
  BOUNDARY_CASE_METHOD.md `
  BOUNDARY_CASES_001_010.md `
  INVARIANCE_FINDINGS_V0.1.md `
  SPRINT_2_GATE_RESULT.md
```

This must return no diff.

Do not continue if any Sprint 2 file changed.

## 6. Expected Commit Scope

### Replaced

- `README.md`
- `DECISION_LOG.md`

### Added as authored infrastructure

- `BOUNDARY_CASE_SCHEMA_V0.2.json`
- `SCHEMA_MIGRATION_V0.1_TO_V0.2.md`
- `migrate_boundary_cases_v0_1_to_v0_2.py`
- `validate_boundary_cases.py`
- `run_sprint4.py`
- `DATASET_LICENSE.md`
- `SECOND_STRATUM_DESIGN.md`
- `SPRINT_4_EXECUTION.md`
- `SPRINT_4_MANIFEST.json`

### Generated after successful execution

- `boundary-cases-001-010.v0.2.json`
- `SPRINT_4_VALIDATION_RESULT.md`
- `SPRINT_4_GATE_RESULT.md`

## 7. Review Before Commit

Confirm:

```powershell
git status --short
git diff --stat
git diff -- README.md DECISION_LOG.md
```

Check that:

- DEC-001–DEC-006 remain unchanged;
- DEC-007 is appended once;
- README names Sprint 5 as the next move;
- generated records remain `automated_review_required`;
- no score, maturity level, certification, or conformance field was introduced;
- the validator result says PASS;
- the gate result says PASS FOR DECLARED SCOPE;
- `ASR-001` remains unauthorized.

## 8. Commit and Push

Commit only after every check passes:

```text
Establish corpus schema v0.2 and second-stratum readiness
```

Then push `main` to `origin/main`.

## 9. Failure Rule

If migration or validation fails:

- do not commit;
- retain the terminal error;
- inspect the first reported path;
- correct the migration, schema, or source inconsistency explicitly;
- rerun the complete Sprint 4 runner.

Do not weaken the schema merely to make invalid data pass.
