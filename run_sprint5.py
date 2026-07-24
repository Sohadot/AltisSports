#!/usr/bin/env python3
"""Run Sprint 5 validation and write a deterministic result record."""
from __future__ import annotations
import hashlib, subprocess, sys
from datetime import date
from pathlib import Path

FILES = [
    Path('BOUNDARY_CASE_SCHEMA_V0.2.json'),
    Path('BOUNDARY_CASES_011_020.md'),
    Path('boundary-cases-011-020.v0.2.json'),
    Path('SECOND_STRATUM_FINDINGS_V0.2.md'),
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    missing = [str(p) for p in FILES if not p.exists()]
    if missing:
        print('ERROR: missing required files: ' + ', '.join(missing), file=sys.stderr)
        return 2
    proc = subprocess.run([sys.executable, 'validate_second_stratum.py'], text=True, capture_output=True)
    print(proc.stdout, end='')
    if proc.stderr:
        print(proc.stderr, end='', file=sys.stderr)
    if proc.returncode != 0:
        return proc.returncode
    result = [
        '# Sprint 5 Validation Result','',
        '**Asset:** AltisSports  ',
        '**Sprint:** Sprint 5 — Second Antagonistic Stratum BC-011–BC-020  ',
        f'**Date:** {date.today().isoformat()}  ',
        '**Decision:** **PASS**','',
        '## Validation','',
        '- Ten native v0.2 records validate against `BOUNDARY_CASE_SCHEMA_V0.2.json`.','- Case identifiers are exactly BC-011–BC-020.','- Every record has at least two evidence records.','- Spatial Function evidence references are in range.','- Native records are not marked as migrated.','- Prohibited scoring and certification keys are absent.','',
        '## SHA-256','', '| File | SHA-256 |','| --- | --- |']
    for p in FILES:
        result.append(f'| `{p}` | `{sha(p)}` |')
    result += ['', 'Validation is structural and deterministic. It does not convert provisional analytical findings into a standard or certification.', '']
    Path('SPRINT_5_VALIDATION_RESULT.md').write_text('\n'.join(result), encoding='utf-8')
    print('PASS: wrote SPRINT_5_VALIDATION_RESULT.md')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
