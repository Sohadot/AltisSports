# AltisSports Decision Log

This log records foundational decisions that govern the asset. Decisions are append-only unless formally superseded by a later decision.

---

## DEC-001 — Category and Measurement Doctrine

**Status:** Ratified  
**Version:** 1.0  
**Date:** 2026-07-24

### Decision

1. **Spatial Sport** is the public, descriptive name of the field in which AltisSports operates.
2. AltisSports does not claim exclusive ownership of the descriptive category term.
3. Defensible intellectual authority will be built through ontology, standards, reference models, datasets, evidence structures, and operational methods.
4. The standards family will use the name **Altis Spatial Reference (ASR)** and sequential identifiers such as `ASR-001`.
5. The system architecture may use the name **Altis Spatial Sport Stack (AS³)**.
6. No scale, score, profile, level, or classification hierarchy may be fixed before the theoretical and empirical structure justifying it exists.
7. Measurement must be derived from theory and evidence; it must not be imposed for branding convenience.

### Rationale

A descriptive category term preserves discoverability and market legibility. Proprietary value is created through the governed language and infrastructure used to define and evaluate the category.

---

## DEC-002 — Invariance Research Doctrine

**Status:** Ratified  
**Version:** 1.0  
**Date:** 2026-07-24

### Decision

1. AltisSports will investigate which properties must remain invariant for an activity to remain classifiable as sport when its arena or medium changes.
2. Early invariants are treated as candidate hypotheses, not settled truths.
3. Candidate invariants must be tested against ordinary, disputed, and boundary cases.
4. No invariant becomes normative merely because it is conceptually elegant.
5. Contradictory cases must be documented rather than excluded to protect the theory.
6. The Boundary Cases Corpus is a mandatory precondition for formal standards.

### Rationale

The project must derive its theory through disciplined comparison rather than declare a closed doctrine before testing.

---

## DEC-003 — Authority–Revenue Separation

**Status:** Ratified  
**Version:** 1.0  
**Date:** 2026-07-24

### Decision

1. Foundational definitions, methods, high-level ontology, and public reference material should remain openly accessible.
2. Revenue may be generated from structured intelligence, expanded datasets, professional reports, assessments, licensed integrations, APIs, and institutional services.
3. Payment may not purchase favorable classification, suppress criticism, alter evidence thresholds, or bypass methodology.
4. Sponsored or paid participation must be visibly distinguished from independent editorial judgment.
5. Monetization must strengthen the reference layer rather than compromise it.

### Rationale

Public authority creates demand; structured intelligence captures value.

---

## DEC-004 — Interface Embodiment Doctrine

**Status:** Ratified  
**Version:** 1.0  
**Date:** 2026-07-24

### Decision

1. The interface must embody the asset thesis rather than decorate it.
2. The visual system must express the arena as a governed spatial system connecting body, rules, measurement, presence, and integrity.
3. No movement, three-dimensional scene, visual layer, or interaction is permitted without a defined explanatory function.
4. Accessibility, performance, semantic HTML, crawlability, mobile reliability, and progressive enhancement are non-negotiable.
5. The site must remain understandable and useful when scripts, animation, or advanced graphics are unavailable.
6. The interface must not resemble a generic gaming, casino, metaverse, or juvenile entertainment product.

### Rationale

Concept precedes performance; performance precedes beauty.

---

## DEC-005 — No Premature Standardization

**Status:** Ratified  
**Version:** 1.0  
**Date:** 2026-07-24

### Decision

AltisSports may publish research questions, candidate models, and provisional classifications during the foundation phase, but may not present them as settled standards until:

- the relevant terms are defined;
- boundary cases have been tested;
- evidence and claim rules are operational;
- the scope and exclusions are explicit;
- versioning and revision procedures exist.

### Rationale

Premature certainty would weaken trust and make later correction look like failure rather than disciplined refinement.

---

## DEC-006 — Evidence-Driven Theory Revision

**Status:** Ratified  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `INVARIANCE_FINDINGS_V0.1.md`, BC-001–BC-010

### Decision

1. **Performance Agency** replaces **Human Agency** as the candidate contest invariant. Human contribution outside the performance window is not sufficient by itself.
2. Live, remote, and assisted Performance Agency may preserve human performance; Design or Engineering Agency and Autonomous Execution must be distinguished from it.
3. Embodied Performance is not a universal condition for all sport. It remains a candidate-defining property of the provisional Spatial Athletic System class.
4. Consequence is demoted from an independent candidate invariant to a derived **Consequence Structure**, pending contrary evidence.
5. Operational Spatial Integration must be represented through a multi-dimensional evidence profile rather than a binary badge, total score, or maturity level.
6. A computational arena, visual immersion, telemetry, or mediation is not sufficient by itself to establish Spatial Athletic System membership.
7. The classified object must be locked before judgment. Activity, contest, system, product, experience, event, organization, and support system may not be silently collapsed.
8. Sprint 2 method and schema artifacts remain immutable historical records of the v0.1 test. They will not be rewritten retroactively to conceal terminology correction.
9. Any migration from `human_agency` to `performance_agency` in machine-readable records must occur through a new schema version with an explicit migration record.
10. `ASR-001` remains unauthorized until the revised theory is tested against additional antagonistic cases and the evidence infrastructure conditions are satisfied.

### Rationale

The first boundary stratum showed that design contribution can exist without live athletic performance, embodiment cannot define every recognized sport, consequence adds little independent discrimination, and operational space appears through multiple roles. A reference system gains authority by preserving the evidence trail of correction rather than rewriting its history.

---

## DEC-007 — Corpus Schema Evolution and Open Dataset Licensing

**Status:** Ratified  
**Version:** 1.0  
**Date:** 2026-07-24  
**Applies to:** Boundary-case schemas, datasets, migrations, and validation artifacts

### Decision

1. `BOUNDARY_CASE_SCHEMA.json` and `boundary-cases-001-010.json` remain immutable historical v0.1 artifacts.
2. Theory-driven schema change must use a new versioned schema and a separate derived dataset rather than overwrite the historical record.
3. Every schema migration must publish its field mapping, assumptions, review requirements, and executable migration path.
4. Automated migration may establish structural compatibility but may not present inferred semantic fields as human-reviewed findings.
5. The v0.2 corpus must remain profile-based and must not introduce total scores, maturity levels, spatiality levels, certification, or conformance claims.
6. Dataset validation must be deterministic, locally executable, and blocking: a failed migration or validation result may not be committed as a completed sprint.
7. Original AltisSports boundary-case data, schema descriptions, controlled vocabularies, and Altis-authored analytical text are released under **CC BY 4.0**, subject to the exclusions in `DATASET_LICENSE.md`.
8. Citations, external documents, trademarks, logos, and other third-party materials are not relicensed merely because they appear in or are linked from an AltisSports record.
9. BC-011–BC-020 must be authored natively against schema v0.2; migrated BC-001–BC-010 records must retain visible migration status.
10. `ASR-001` remains unauthorized after corpus infrastructure completion; a second evidence stratum and a separate standardization gate are still required.

### Rationale

A reference dataset must evolve without erasing the conditions under which earlier findings were produced. Versioned schemas, explicit migrations, deterministic validation, and clear reuse rights convert conceptual correction into durable public infrastructure while preserving attribution, uncertainty, and third-party boundaries.
