# ASR-001 Review Baseline Correction 001

**Correction ID:** ASR-001-REVIEW-BASELINE-CORRECTION-001
**Blocker:** BLOCKER-OPREVIEW-BASELINE-001
**Status:** Owner Decision — Ratified
**Correction date:** 2026-08-14
**Affects:** `ASR_001_REVIEW_BASELINE_MANIFEST.json` (metadata only)

## 1. Summary

The operator-review baseline manifest recorded five SHA-256 values that never
matched the committed content of the files they name. Forensic reconstruction
shows the recorded hashes were wrong **at manifest creation** (a metadata
defect), not the result of any later change to the baseline material. The
baseline material itself is unchanged and is the intended review material. This
correction repairs only the erroneous metadata; it changes no descriptive or
normative content, and it does not activate review.

## 2. Forensic Reconstruction

- Manifest created in commit `8564121` (`Prepare ASR-001 operator review package and readiness gate`).
- Each affected file has exactly **one** commit in history, `13e6590`
  (`Complete ASR-001 internal trials and refine Working Draft v0.2`), which
  **precedes** `8564121`. The files have not changed since.
- Therefore the only committed content of each file is the `13e6590` content,
  whose hash equals the current hash. The manifest's stored hash equals neither.

Three-state comparison (all five files):

| Path | Manifest hash (stored) | Hash @ `8564121` | Current hash | Manifest == committed? | @8564121 == current? |
| --- | --- | --- | --- | --- | --- |
| `ASR_001_WORKING_DRAFT_V0.2.md` | `f85fced6…9cb2` | `4083a542…9caf` | `4083a542…9caf` | no | yes |
| `ASR_001_CLAUSE_TO_FIELD_MAP_V0.2.json` | `540c16e0…de13` | `e7290e5f…b0df` | `e7290e5f…b0df` | no | yes |
| `ASR_001_INTERNAL_TRIAL_RESULTS.md` | `90c18d73…518e` | `88ae1ad9…c706` | `88ae1ad9…c706` | no | yes |
| `ASR_001_CLAUSE_FRICTION_REGISTER_V0.1.json` | `7087c2ab…b5ea` | `adf8b5a3…470a` | `adf8b5a3…470a` | no | yes |
| `ASR_001_INTERNAL_TRIAL_INDEX_V0.2.json` | `42a88a16…b19f` | `42e587a0…6c40` | `42e587a0…6c40` | no | yes |

The full 64-hex values are recorded in the manifest's `correction` block
(`superseded_sha256` and `corrected_sha256`).

## 3. First-Divergence Commit

For every affected file the "first divergence" is at manifest creation
(`8564121`): the stored hash corresponds to no committed state of the file. The
generator `build_asr001_operator_review_package.py` hashes real file bytes
deterministically, so the manifest was serialized from a transient, uncommitted
working-tree state of these five files that was never itself committed; the
committed content that landed in `8564121` (identical to `13e6590`) was not
re-hashed before commit.

## 4. Classification

**Case A — Manifest metadata defect at creation.**

- Not Case B (post-baseline file mutation): the files never changed after the
  baseline; each has a single commit predating it.
- Not Case D (generator defect): the generator hashes actual bytes and is
  deterministic; re-running it over the current files yields exactly the
  corrected hashes.
- Not Case C (ambiguous): it is provable that the stored hashes matched no
  committed state and that the content is stable.

## 5. Disposition

Correct the five stored hashes to their historically verified correct values
(the hash of the committed baseline content, which equals both the `8564121`
content and the current content), in a versioned, auditable way:

- the erroneous hashes are retained in the manifest `correction` block as
  `superseded_sha256`, so the defect remains on the record;
- the logical baseline identity (`manifest_id = ASR001-OPERATOR-REVIEW-BASELINE`)
  is **preserved** — the reviewer inspects the same material that was always
  intended; this is a metadata repair, not a new baseline;
- `created_date` and all other 18 correct hashes are left unchanged.

This is the minimal and most truthful repair: it makes the manifest tell the
truth about the baseline material, without rewriting the material or the
creation date.

## 6. What Did / Did Not Change

- **Changed:** five stored SHA-256 metadata values in the baseline manifest, plus
  an added `correction` audit block.
- **Not changed:** any Working Draft, clause, profile, trial, friction-register,
  or corpus content; the baseline material bytes; the `created_date`; the
  baseline identity; review activation.

`content_changed = false`. `baseline_material_unchanged = true`.
`baseline_identity_preserved = true` (no new baseline version).

## 7. Review Status (unchanged)

`review_status = prepared_not_activated` and `public_review_status =
not_public_review` are unchanged. Baseline integrity being valid does **not**
mean review was activated, reviewers participated, or ASR-001 gained any
external recognition. Correcting the baseline does not activate operator review.

## 8. Owner Decision

The owner ratifies the Case A correction above: repair the historical truth of
the baseline metadata; do not present changed content as unchanged (none was),
and do not create a new baseline. `BLOCKER-OPREVIEW-BASELINE-001` is resolved by
this correction. Its historical existence and resolution remain on the record in
`CI_VALIDATION_MANIFEST.json` and `DECISION_LOG.md` (DEC-018).

## 9. Downstream Validation Effect

`validate_asr001_operator_review_package.py` passes with strict hash checking
(no exclusion). The validator is promoted to `required = true` in the hosted
gate, and the operator-review exclusion is removed from the CI manifest.
