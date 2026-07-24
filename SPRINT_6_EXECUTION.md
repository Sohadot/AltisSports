# Sprint 6 Execution

**Target:** repository root on `main`

## 1. Place the authored files

Extract the Sprint 6 package into the repository root.

The package replaces:

- `FIRST_PRINCIPLES.md`
- `ONTOLOGY.md`
- `AS3_STACK.md`
- `DECISION_LOG.md`
- `README.md`

It adds the remaining Sprint 6 files.

Do not modify or delete v0.1 or v0.2 schemas and datasets.

## 2. Run

From the repository root:

```powershell
python .\run_sprint6.py
```

Expected terminal output:

```text
PASS: wrote BOUNDARY_CASE_SCHEMA_V0.3.json
PASS: wrote boundary-cases-011-020.v0.3.json with 10 cases
PASS: 10 v0.3 derivative cases validate; targeted agency, arena, biological-control, and participatory-actor checks passed.
PASS: Sprint 6 generated and validated schema v0.3 and the targeted derivative.
```

## 3. Generated files

The runner creates:

- `BOUNDARY_CASE_SCHEMA_V0.3.json`
- `boundary-cases-011-020.v0.3.json`
- `SPRINT_6_VALIDATION_RESULT.md`
- `SPRINT_6_GATE_RESULT.md`

## 4. Commit

Review the diff and confirm that v0.1 and v0.2 historical files are unchanged.

Suggested commit message:

```text
Deepen boundary relations and establish schema v0.3
```
