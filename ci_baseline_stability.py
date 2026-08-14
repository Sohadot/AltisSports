#!/usr/bin/env python3
"""Identifier-stability gate across revisions.

Runs validate_citation_registry.py --baseline against the Citation Registry
as it existed at the correct base revision, catching dropped stable IDs
(without a tombstone), semantic repointing, and source_key/kind drift.

Base resolution is event-aware (never a blind HEAD^):

  - pull_request: merge-base of HEAD and the PR base ref;
  - push:        the event 'before' SHA, when valid (not a branch creation);
  - otherwise (workflow_dispatch / local): HEAD's first parent, if any.

When no legitimate baseline registry exists — the first governed version, a
branch creation, or a base revision that predates the registry — the check
prints an explicit first-baseline notice and passes WITHOUT fabricating a
baseline. Standard library only; exit 0 on pass or legitimate first-baseline,
1 on a stability break.
"""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REGISTRY = "CITATION_REGISTRY_V0.1.json"
ZERO = "0" * 40


def git(*args):
    proc = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def rev_ok(ref):
    code, _, _ = git("rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}")
    return code == 0


def resolve_base():
    event = os.environ.get("GITHUB_EVENT_NAME", "")
    if event == "pull_request":
        base_ref = os.environ.get("GITHUB_BASE_REF", "")
        for cand in (f"origin/{base_ref}", base_ref):
            if base_ref and rev_ok(cand):
                code, mb, _ = git("merge-base", "HEAD", cand)
                if code == 0 and mb:
                    return mb, f"merge-base with {cand}"
        return None, f"pull_request base ref unavailable ({base_ref!r})"
    if event == "push":
        before = os.environ.get("GITHUB_EVENT_BEFORE", "") or os.environ.get("GITHUB_SHA_BEFORE", "")
        if before and before != ZERO and rev_ok(before):
            return before, "push event 'before' SHA"
        return None, "push with no valid 'before' SHA (branch creation or first push)"
    # local / workflow_dispatch
    if rev_ok("HEAD~1"):
        return "HEAD~1", "HEAD first parent (local/dispatch)"
    return None, "no parent commit"


def registry_at(rev):
    code, out, _ = git("show", f"{rev}:{REGISTRY}")
    if code != 0:
        return None
    return out


def main():
    base, how = resolve_base()
    if base is None:
        print(f"baseline unavailable — first governed registry version ({how}).")
        sys.exit(0)

    content = registry_at(base)
    if content is None:
        print(f"baseline unavailable — {REGISTRY} not present at base {base[:12]} ({how}); "
              "treating as first governed registry version.")
        sys.exit(0)

    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as tf:
        tf.write(content)
        baseline_path = tf.name
    try:
        print(f"baseline: {REGISTRY} at {base[:12]} ({how})")
        proc = subprocess.run(
            [sys.executable, "validate_citation_registry.py", "--baseline", baseline_path],
            cwd=ROOT, capture_output=True, text=True,
        )
        if proc.stdout.strip():
            print(proc.stdout.rstrip())
        if proc.stderr.strip():
            print("[stderr]", proc.stderr.rstrip())
        sys.exit(proc.returncode)
    finally:
        os.unlink(baseline_path)


if __name__ == "__main__":
    main()
