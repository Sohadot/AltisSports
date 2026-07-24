# Sprint 7 Local Execution

Run from the repository root:

```powershell
python .\run_sprint7.py
```

Expected terminal result:

```text
PASS: wrote boundary-cases-001-010.reviewed.v0.3.json with 10 reviewed cases
PASS: wrote boundary-cases-011-020.reviewed.v0.3.json with 10 reviewed cases
PASS: wrote boundary-cases-001-020.v0.3.json with 20 cases
PASS: 20 human-reviewed v0.3 cases validate; corpus application and cross-case checks passed.
PASS: Sprint 7 corpus application and standardization-readiness gate completed.
```

Generated files:

- `boundary-cases-001-010.reviewed.v0.3.json`
- `boundary-cases-011-020.reviewed.v0.3.json`
- `boundary-cases-001-020.v0.3.json`
- `SPRINT_7_VALIDATION_RESULT.md`
- `STANDARDIZATION_READINESS_RESULT.md`
- `SPRINT_7_GATE_RESULT.md`

Source schemas and datasets are checked by hash before and after execution and are not overwritten.
