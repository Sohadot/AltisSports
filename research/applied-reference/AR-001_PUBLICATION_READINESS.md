# AR-001 — Publication Readiness

**Asset:** AltisSports  
**Case:** Applied Reference 001 — Evidence Lock  
**Frozen object:** WT Virtual Taekwondo contest configuration (Rules v4.0 / co-located FOP)  
**Access date:** 2026-08-27  
**Status:** Internal gate only — does not publish `/applied/`

This file answers one question: whether existing BC-015 evidence plus current authoritative sources are sufficient to support the first public AltisSports Applied Reference Case **without writing the result in advance**.

---

## Verdict

**READY_WITH_EXPLICIT_GAPS**

---

## Why this verdict

### Why not `NOT_READY`

`NOT_READY` would apply if the object could not be locked, if current rules could not be retrieved, if inspection collapsed into marketing, or if most AS³ layers had no public mechanism to inspect.

That is not the case:

- The object can be locked as a **WT-governed co-located contest configuration** under **Rules Version 4.0 (11 April 2026)**, distinct from the VTKD product, from named events, and from a remote-distributed hypothesis.
- A later edition than May 30, 2025 **does exist** and was read in full as WT PDF Version 4.0. No later public rulebook was found.
- All ten AS³ layers have inspectable questions, documented evidence or attributed claims, and named unknowns.
- The architecture can already show something a taxonomy or press release cannot: **where human movement, wearable sensing, computational arena, hybrid officiation, and versioned software actually meet**, and where they part.

That is enough to demonstrate reference *use*, provided the public page refuses scores, certification, and silent object slides.

### Why not `READY`

`READY` would require that a public case could state the current contest configuration without a material “unknown” on the joints that make AS³ distinctive.

Those joints are still open:

- scoring formula and acceleration thresholds are unpublished;
- VTKD v1.3.0 (21 August 2026) post-dates Rules v4.0 and diverges on stun activation, groin-kick damage, calibration method, and optional Boundary Damage;
- no public lock of software build to a named WT event;
- remote distributed competition remains `not_evidenced`;
- accessibility/inclusion claims exceed documented accommodations;
- tracking internals (IK, arm channel, error budget) are closed.

Publishing as if those were settled would reproduce the failure mode this lock exists to prevent: a handsome page that later unravels.

`READY_WITH_EXPLICIT_GAPS` means: **publish later only if the public page makes the object lock and the gaps structurally visible**, not as footnotes after a triumphant narrative.

---

## What a later public page would be allowed to do

If a subsequent sprint builds `/applied/ar-001/` or `/applied/virtual-taekwondo/`, it may:

- inspect the frozen object through AS³;
- cite WT Rules v4.0 and current VTKD operator documents with temporal status;
- show hybrid rule execution and unified co-located arena;
- keep BC-015’s C5 category finding attributed to the corpus, not re-issued as a new Altis verdict;
- state remote topology as `not_evidenced`;
- display claim classes.

It may not:

- score, certify, or pass/fail the system;
- treat May 2025 as current;
- treat VTKD marketing as independent fact;
- treat internet-connected courts as remote matches;
- overwrite BC-015;
- imply ASR-001 status change.

Recommended public title (from the research brief, still not built):

> Applied Reference 001 — Virtual Taekwondo  
> Inspecting a computational athletic arena through the Altis Spatial Sport Stack.

Sovereign path `/applied/ar-001/` is preferable to a product-slug path if the page must survive VTKD rebranding. That is a later information-architecture decision, not part of Evidence Lock.

---

## Evidence-based summary for the gate

| Criterion | Result |
| --- | --- |
| Object lock explicit | Yes — `AR-001_OBJECT_LOCK.md` |
| Current primary rules retrieved | Yes — WT Rules v4.0, 11 April 2026 |
| May 2025 checked, not assumed current | Yes — superseded Version 3.0 |
| BC-015 preserved, not silently improved | Yes |
| Provider claims separated from fact | Yes |
| Unknown remains unknown | Yes |
| AS³ used as inspection, not scoring | Yes |
| Hard parts tested | Yes — `AR-001_GAPS_AND_FALSIFIERS.md` |
| Enough to show architecture-in-use vs theory-only | Yes, if gaps stay visible |
| Enough for an evaluative or completeness claim | No |

---

## Quality-gate check (Evidence Lock only)

This is not a public-web-page gate (`QUALITY_GATE.md` §2). It is the research publication test in `SOURCE_AND_CLAIM_POLICY.md` §11 applied to internal artefacts.

| Check | Result |
| --- | --- |
| Object lock is explicit | Pass |
| No product claim became independent fact | Pass — C3 retained for VTKD marketing |
| No historical source silently treated as current | Pass — v3.0, 1.2.34, 2023–2024 events marked historical/superseded |
| Material statements map to evidence or declared Altis interpretation | Pass |
| Unknown remains unknown | Pass |
| AS³ not converted into scoring | Pass |
| Existing BC-015 not silently overwritten | Pass |
| No ASR-001 status changes | Pass |
| No public website files changed | Pass (this sprint created only `research/applied-reference/` files) |
| New governance created | Not required; no contradiction forced a decision |

---

## Validation results

1. **Edition check:** VTKD archive + WT PDF title page agree that the current public edition is Version 4.0, 11 April 2026. The research brief’s May 30, 2025 starting PDF is Version 3.0 and is superseded.  
2. **Corpus check:** BC-015 in `boundary-cases-001-020.v0.3.json` and `boundary-cases-011-020.reviewed.v0.3.json` match on object notes, claim classes, and `distributed_arena_relation.status = not_evidenced`. Atlas `ATL-D-015` preserves the same.  
3. **New since BC-015 access 2026-07-24:** VTKD v1.3.0 / User Manual 1.3.0 / Game Mechanics 1.3.0 (21 August 2026); Network Setup page fully extracted; WT v4.0 PDF body extracted rather than archive notes only.  
4. **Contradiction found, not papered over:** Rules v4.0 Article 5.3.1 vs VTKD v1.3.0 stun activation; Surface Calibration withdrawn; Boundary Damage software-only. Recorded as L4/L10 gaps, not “fixed” into a single story.  
5. **Remote hypothesis:** Re-tested; still `not_evidenced`.  
6. **Out of scope confirmed:** No `docs/applied/` created; ASR-001, Category Thesis, and AS³ files not modified.

---

## If the next sprint proceeds

Build the public case only from these five artefacts plus the locked object. Do not widen to a product review, a 20-page SEO cluster, or a remote-sport claim. The first public Applied Reference earns its keep by making the human–computational seam inspectable—and by leaving closed software and absent remote evidence **closed and absent**.
