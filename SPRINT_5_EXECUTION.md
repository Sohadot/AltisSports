# Sprint 5 Local Execution

## 1. Copy

Place every file from this package in the repository root. Existing `README.md` and `DECISION_LOG.md` are replaced; Sprint 1–4 research files remain untouched.

The included `.gitignore` prevents Python bytecode from appearing in GitHub Desktop.

## 2. Run

From the repository root:

```powershell
python .un_sprint5.py
```

Expected terminal output:

```text
PASS: 10 native v0.2 cases validate; BC-011–BC-020 integrity checks passed.
PASS: wrote SPRINT_5_VALIDATION_RESULT.md
```

## 3. Review

Confirm:

- `boundary-cases-011-020.v0.2.json` contains 10 records;
- `SPRINT_5_VALIDATION_RESULT.md` was generated;
- no `__pycache__/` or `*.pyc` file is staged;
- Sprint 1–4 artifacts are not modified except `README.md` and append-only `DECISION_LOG.md` replacement;
- `ASR-001` remains unauthorized.

## 4. Commit

```text
Complete native v0.2 second boundary stratum
```

Then push `main` to `origin/main`.
