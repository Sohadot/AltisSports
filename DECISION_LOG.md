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

---

## DEC-008 — Second-Stratum Refinement Hold

**Status:** Ratified  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** BC-011–BC-020 and `SECOND_STRATUM_FINDINGS_V0.2.md`

### Decision

1. BC-011–BC-020 are accepted as the first **native v0.2** research stratum, distinct from migrated BC-001–BC-010 records.
2. Embodied Performance remains a channel-based profile. No minimum quantity, level, or universal threshold is authorized.
3. Fine-motor, balance, sensorimotor, adaptive, cognitive, and intentional physiological channels may be material evidence; none establishes Spatial Athletic System membership by itself.
4. `Spatial Athletic System`, `Spatial Athletic Contest`, and `Spatial Support System` remain separate objects; system membership may exist without mature contest governance.
5. Summary-level agency modes are insufficient for cases with time-varying control. A phase-level `agency_segments` design must be evaluated before normative agency attribution.
6. The remote-distributed hypothesis in BC-015 remains unresolved. Global availability, product aspiration, or co-located championship evidence may not be presented as proof of remote arena integrity.
7. Spectators who alter resources or constraints without executing the performance are participatory rule/resource actors, not Performance Agents by default.
8. Consequence remains a derived property. The second stratum does not restore it as an independent invariant.
9. Operational Spatial Integration remains qualitative and profile-based. No total score, maturity level, or binary certification badge is authorized.
10. `ASR-001` remains unauthorized. The next move is targeted boundary deepening and a schema v0.3 decision, not standard issuance.

### Rationale

The second stratum validates the main v0.2 separations while exposing two unresolved structures: agency that changes by phase and arenas distributed across physical locations. Preserving these uncertainties increases reference integrity and prevents a premature standard from encoding a convenient but incomplete theory.
---

## DEC-009 — Targeted Representation and Schema v0.3

**Status:** Ratified  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `SECOND_STRATUM_FINDINGS_V0.2.md`, `TARGETED_BOUNDARY_DEEPENING.md`

### Decision

1. `BOUNDARY_CASE_SCHEMA_V0.3.json` is authorized because v0.2 cannot faithfully represent phase-varying agency, distributed-arena relations, participatory rule/resource actors, or intentional biological control.
2. Phase-varying or regime-varying control must use `agency_segments`. A rule-permitted manual, semi-autonomous, or autonomous regime may not be presented as an observed transition without evidence.
3. Distributed-arena claims must state topology, shared computational state, synchronization, latency governance, calibration equivalence, officiation, safety responsibility, evidence, and uncertainty.
4. BC-015 remains a co-located Spatial Athletic Contest in the examined evidence. Geographically distributed synchronous Virtual Taekwondo is **not evidenced**, not declared impossible.
5. Intentional biological control may establish live Performance Agency when intentionality, task coupling, causal necessity, and incidental-signal exclusion are supported.
6. Intentional biological control does not by itself establish athletic embodiment or Spatial Athletic System membership. BC-018 remains unresolved on that relation.
7. A non-performing actor who changes a rule-authorized resource or constraint is a **Participatory Rule/Resource Actor** and does not become a Performance Agent or official by default.
8. v0.2 schemas and datasets remain immutable. v0.3 is a separate derivative with explicit migration and review status.
9. No score, spatiality level, embodiment level, maturity ladder, certification, conformance claim, or paid ranking is authorized.
10. `ASR-001` remains unauthorized. Schema v0.3 must first be validated and the targeted structures must survive further corpus use.

### Rationale

The second stratum did not primarily expose missing cases; it exposed missing representational relations. A reference system must record when control changes, how sites connect, how bodily-origin signals become task actions, and how external participants alter contest conditions without collapsing those distinctions into one label.
---

## DEC-010 — ASR-001 Scope Drafting Authorization

**Status:** Ratified upon Sprint 7 PASS  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** Reviewed BC-001–BC-020 v0.3 corpus and `CORPUS_APPLICATION_FINDINGS_V0.3.md`

### Decision

1. The human-reviewed BC-001–BC-020 v0.3 corpus is accepted as the current research baseline for scope definition.
2. Schema v0.3 is adequate for the current corpus. No schema v0.4 is authorized without a repeated representational failure.
3. AltisSports authorizes drafting the **scope only** of a candidate `ASR-001`.
4. The working subject is a **Spatial Athletic System Evidence Profile**: a minimum disclosure and evidence structure, not a category-certification system.
5. Scope drafting may use object lock, Performance Agency, Embodied Performance, AS³, Operational Spatial Integration functions, comparability, evidence, uncertainty, versioning, and governance.
6. Scope drafting must exclude total scores, maturity levels, vendor rankings, federation recognition, universal sport definitions, clinical efficacy, safety certification, final BCI membership, and unresearched remote-synchronous tolerances.
7. Normative requirements, conformance clauses, certification, and publication of `ASR-001` remain unauthorized.
8. The scope draft must follow `ASR_DRAFTING_GOVERNANCE.md` and pass a separate scope-approval gate.
9. Hosted CI and external review are not required to write the scope draft, but remain conditions before a normative public release can be considered.
10. Commercial participation may not alter evidence boundaries or buy favorable inclusion.

### Rationale

Twenty adversarial cases now provide enough conceptual and representational stability to define one bounded standardization problem. They do not provide enough evidence to issue technical tolerances or certify systems. Authorizing scope drafting captures the value of the research without converting research adequacy into premature normative authority.

---

## DEC-011 — ASR-001 Scope Approval and Requirements-Drafting Boundary

**Status:** Ratified upon Sprint 8 PASS  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `ASR_001_SCOPE_DRAFT.md`, `ASR_001_SCOPE_TRACEABILITY.md`, and the reviewed BC-001–BC-020 v0.3 corpus

### Decision

1. The scope of `ASR-001 — Spatial Athletic System Evidence Profile` is approved.
2. The profiled subject is one bounded, versioned system configuration. Findings about an activity, product, platform, event, organization, or deployment may not be silently generalized across objects.
3. The approved scope contains fifteen descriptive domains covering object identity, context, agency, interface, arena, rules, sensing, measurement, officiation, spatial functions, participation, safety/accessibility disclosure, evidence, governance, and machine-readable metadata.
4. ASR-001 is an evidence-profile project. It is not a universal sport definition, product-rating system, federation-recognition mechanism, safety or clinical certification, or category-ownership claim.
5. Any future conformance model is bounded to the evidence-profile document or machine-readable profile instance. It may not certify the underlying sport, system, product quality, safety, clinical efficacy, or market superiority.
6. Requirements drafting is authorized for a governed Working Draft only.
7. Every future candidate clause must map to an approved scope domain, a defined problem, evidence or governance dependency, applicability condition, verification approach, rationale, and affected exclusions or uncertainty.
8. The research corpus schema is not automatically the ASR-001 implementation schema. A separate implementation decision is required.
9. Publication as a standard, Public Review Draft status, certification, product or sport conformance claims, scoring, maturity levels, vendor rankings, and claims of industry adoption remain unauthorized.
10. External operator review and hosted validation remain conditions before a normative public release can be considered.

### Rationale

The approved scope converts twenty adversarial cases into one bounded standardization problem: how to disclose and support evidence about a spatial-athletic system configuration without converting documentation into product judgment or category certification. This is sufficient to begin a controlled Working Draft, but not to claim a standard, adoption, or conformance program.

---

## DEC-012 — ASR-001 Working Draft Architecture and Clause-Authoring Boundary

**Status:** Ratified upon Sprint 9 PASS  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `ASR_001_WORKING_DRAFT_ARCHITECTURE.md`, `ASR_001_CLAUSE_CATALOG_V0.1.json`, and `ASR_001_EVIDENCE_TO_CLAUSE_MAP.md`

### Decision

1. The ASR-001 Working Draft architecture is accepted as the governing structure for clause authoring.
2. Candidate requirement identifiers use the stable form `ASR001-DNN-CNN`, with every candidate mapped to one approved scope domain D01–D15.
3. The Sprint 9 baseline contains thirty candidate obligation records, exactly two for each approved domain.
4. Candidate records are not normative clauses. They define obligation intent, applicability, evidence, governance dependencies, verification, rationale, uncertainty, and exclusion guards.
5. Every future clause must retain traceability to its candidate record or record an explicit replacement decision.
6. Applicability is conditional and evidence-aware. A non-triggered clause is not a failed clause, and missing evidence does not become an underlying-system score.
7. Verification concerns the evidence-profile document or instance. It does not validate the underlying sport, product quality, safety, clinical efficacy, federation recognition, or market superiority.
8. The boundary-case research schema is not adopted as the ASR-001 implementation schema. A separate implementation-profile decision is required.
9. Candidate clause authoring is authorized for a governed non-public Working Draft only.
10. Publication, Public Review Draft status, certification, product or sport conformance claims, scores, levels, rankings, unsupported technical tolerances, final BCI athletic classification, and claims of industry adoption remain unauthorized.

### Rationale

The approved scope is now decomposed into uniquely identified, evidence-linked, conditionally applicable, and verifiable candidate obligations. This is enough to begin clause-level drafting without losing the exclusions and uncertainty that made the research credible. It is not enough to release a standard or conformance program.

---

## DEC-013 — ASR-001 Candidate Normative Core and Internal-Trial Boundary

**Status:** Ratified upon Sprint 10 PASS  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `ASR_001_WORKING_DRAFT_V0.1.md`, `ASR_001_NORMATIVE_CLAUSE_CATALOG_V0.1.json`, and `ASR_001_PROFILE_MODEL_V0.1.json`

### Decision

1. The ASR-001 Candidate Normative Core v0.1 is accepted as a non-public Working Draft.
2. The core contains exactly thirty clause-level candidate obligations using the stable identifiers authorized by DEC-012.
3. Candidate normative language is permitted only inside the governed Working Draft and does not establish publication, recognition, adoption, or a certification program.
4. Every clause retains its approved domain, applicability, evidence or governance dependency, verification approach, rationale, uncertainty handling, exclusion guards, and profile field path.
5. The candidate implementation profile model v0.1 is clause-derived and is distinct from the Boundary Case Schema.
6. Candidate profile validation checks the profile document or machine-readable instance only. It does not validate or certify the underlying sport, product, safety, clinical efficacy, quality, federation recognition, category membership, or market superiority.
7. Conditional applicability is explicit. A non-triggered clause is not a failure, and missing evidence is not converted into a zero, score, grade, or ranking.
8. Two synthetic profiles are accepted as deterministic structural fixtures. They are not market records and create no provider claims.
9. Internal implementation trials are authorized. Clause changes during those trials require recorded implementation evidence or a governance issue.
10. ASR-001 publication, Public Review Draft status, certification, public conformance claims, scores, maturity levels, vendor rankings, unsupported technical tolerances, final BCI athletic classification, and claims of industry adoption remain unauthorized.

### Rationale

The approved scope and candidate architecture now have clause-level expression and a separate operational profile model. Internal implementation is the next reliable test: it can expose clauses that are ambiguous, untestable, overbroad, duplicative, or poorly represented before any external review or publication posture is considered.

---

## DEC-014 — ASR-001 Internal Trial Refinement and Operator-Review Preparation Boundary

**Status:** Ratified upon Sprint 11 PASS  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `ASR_001_INTERNAL_TRIAL_RESULTS.md`, `ASR_001_CLAUSE_FRICTION_REGISTER_V0.1.json`, and `ASR_001_REFINEMENT_RESULT.md`

### Decision

1. The seven Sprint 11 internal profile artifacts are accepted as the current implementation-trial baseline.
2. The ASR-001 Working Draft advances internally from v0.1 to v0.2 without changing the approved D01–D15 scope or any clause identifier.
3. Applicability and evidence sufficiency are separate states. An applicable clause may remain `not_evidenced`, `unknown`, or `partial` without becoming non-applicable or producing a score.
4. `ASR001-D03-C02` applies when agency modes, control regimes, or handoff are present, including autonomous contest execution after human design.
5. `ASR001-D04-C02` applies when embodied demand or intentional biological control is claimed, without settling athletic membership or establishing an embodiment threshold.
6. A JSON ASR-001 profile instance declares machine-readable distribution as present.
7. Clause records distinguish declarative, supporting-evidence, lifecycle, and distribution-manifest evidence requirements.
8. Profile correction and supersession are explicit and append-only; the rehabilitation revision pair is accepted as the lifecycle test.
9. Internal trials confirm the profile-only conformance boundary across autonomous, support, BCI, human–AI, participatory-audience, and remote-control configurations.
10. Preparation of an operator-review package is authorized. Outreach, external review execution, Public Review Draft status, ASR-001 publication, certification, public conformance claims, scores, rankings, unsupported technical tolerances, final BCI athletic classification, and claims of adoption remain unauthorized.

### Rationale

Internal implementation exposed representational and verification defects that syntax-only validation could not reveal. The bounded v0.2 refinement resolves those defects while preserving all identifiers, exclusions, uncertainty, and historical artifacts. The next useful step is to prepare a review package that lets relevant operators challenge the Working Draft without prematurely opening Public Review or claiming adoption.

---

## DEC-015 — ASR-001 Operator Review Readiness and Owner-Activation Boundary

**Status:** Ratified upon Sprint 12 PASS  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `ASR_001_OPERATOR_REVIEW_PACKAGE.md`, `ASR_001_REVIEW_BASELINE_MANIFEST.json`, and `ASR_001_OPERATOR_REVIEW_READINESS_RESULT.md`

### Decision

1. The ASR-001 Operator Review Package v0.1 is accepted as complete and review-ready.
2. The review baseline is ASR-001 Working Draft v0.2 together with its thirty-clause catalog, clause-to-field map, profile model, schema, internal-trial results, and frozen SHA-256 manifest.
3. The prepared package contains seven reviewer classes and forty-three questions: eight core questions and five role-specific questions for each class.
4. The permitted review mode is limited, asynchronous, and written only.
5. Calls, interviews, open public-comment channels, and implied endorsement or adoption are outside the permitted first-wave mode.
6. Public repository visibility does not activate review, create Public Review Draft status, invite unrestricted comment, or establish adoption.
7. Review comments are clause-addressable, conflict-disclosed, evidence-classified, and dispositioned through written change control.
8. Review participation does not constitute endorsement, adoption, partnership, federation recognition, certification, or approval of the category thesis.
9. No reviewer contact or invitation has occurred through Sprint 12.
10. A limited written review can begin only after the owner records an explicit activation decision, reviewer roster, class coverage, conflict-declaration identifiers, written channel, and frozen baseline.
11. The first-wave coverage design includes at least four reviewer classes: an operational class, a technical or measurement class, a human-impact or methodology class, and evidence/data governance.
12. Public Review Draft status, ASR-001 publication, certification, public conformance claims, scores, rankings, unsupported remote-synchronous tolerances, final BCI athletic classification, federation-recognition claims, and industry-adoption claims remain unauthorized.

### Rationale

The internal Working Draft now has sufficient structure, trial evidence, question coverage, comment intake, issue classification, conflict disclosure, and change control for a bounded operator review. Readiness does not justify automatic outreach. Owner activation is retained as a separate governance act so that reviewer selection, written-only mode, baseline integrity, and non-endorsement boundaries remain deliberate.

---

## DEC-016 — ASR-001 Wave RW-001 Apparatus Activation and Named-Outreach Hold

**Status:** Ratified upon Sprint 13 PASS  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `ASR_001_REVIEW_ACTIVATION_RECORD_RW001.md`, `ASR_001_REVIEWER_COHORT_ROSTER_V0.1.json`, and `ASR_001_REVIEW_ACTIVATION_GATE_RESULT.md`

### Decision

1. Wave RW-001 limited-written-review apparatus is activated for preparation under ASR-001 Working Draft v0.2 and baseline manifest `ASR001-OPERATOR-REVIEW-BASELINE`.
2. The first-wave cohort is defined as seven role slots `RWS-01` through `RWS-07` covering RC-01 through RC-07 and satisfying the four required class groups.
3. Named persons are not assigned in Sprint 13. Fabricated personal identities are prohibited.
4. Conflict-declaration identifiers are reserved in pending status for each slot.
5. The written intake channel `review-intake/` is prepared and remains closed to external submission.
6. The issue-intake procedure is confirmed and remains disabled until invitation-linked enablement.
7. All invitation statuses remain `not_sent`. The invitation template remains prepared and inactive.
8. Named assignment and invitation sending remain held and require a separate owner outreach decision.
9. Public repository visibility still does not create Public Review Draft status or open comment rights.
10. Public Review Draft status, ASR-001 publication, certification, public conformance claims, scores, rankings, unsupported remote-synchronous tolerances, final BCI athletic classification, federation-recognition claims, and industry-adoption claims remain unauthorized.

### Rationale

Sprint 12 made the package review-ready. Sprint 13 converts readiness into a governed wave apparatus and class-covered cohort without collapsing preparation into outreach. Keeping named assignment and invitation sending under an explicit hold preserves non-endorsement boundaries and prevents identity fabrication or premature public comment.

---

## DEC-017 — ASR-001 First-Wave Named Candidate Assignment and Controlled Invitation Release

**Status:** Ratified upon Sprint 14 PASS  
**Version:** 1.0  
**Date:** 2026-07-24  
**Evidence basis:** `ASR_001_OWNER_DECISION_SPRINT_14.md`, `ASR_001_REVIEWER_COHORT_ROSTER_V0.2.json`, and `ASR_001_NAMED_ASSIGNMENT_GATE_RESULT.md`

### Decision

1. Four first-wave candidate assignments were authorized against RWS-01 (RC-01), RWS-03 (RC-03), RWS-05 (RC-05), and RWS-07 (RC-07). Candidate identities are maintained outside the public governance record under the reviewer privacy boundary (`REVIEWER_PRIVACY_BOUNDARY.md`). _(Names in this point are redacted as a public privacy projection per DEC-020; the substantive authorization recorded here is unchanged.)_
2. Before written acceptance, each assigned person is classified solely as `named_candidate_assignee` with candidate_status `selected_not_contacted` until private dispatch occurs.
3. Controlled individual written invitation release is authorized for those four slots only.
4. Invitation drafts are prepared for private owner dispatch. Sprint 14 does not transmit messages and does not store personal contact addresses in the public repository.
5. RWS-02, RWS-04, and RWS-06 remain reserve-closed with invitation_status `not_authorized`.
6. Global `review-intake/` remains closed. Per-candidate intake may be enabled only after that candidate's invitation is privately dispatched.
7. No `ORC` identifier may be issued before written acceptance and a later accepted comment.
8. No person may be labeled `reviewer` before written acceptance.
9. Participation must not be represented as endorsement, adoption, partnership, federation recognition, or organizational approval.
10. Public Review Draft status, ASR-001 publication, certification, public conformance claims, scores, rankings, unsupported remote-synchronous tolerances, final BCI athletic classification, and industry-adoption claims remain unauthorized.

### Rationale

A four-candidate first wave satisfies the required coverage groups while remaining operationally bounded. Separating named-candidate assignment from reviewer status, and authorization-to-send from actual private dispatch, preserves non-endorsement boundaries and prevents contact-data leakage or premature intake opening.

---

## DEC-018 — ASR-001 Operator-Review Baseline Correction 001

**Status:** Ratified
**Version:** 1.0
**Date:** 2026-08-14
**Evidence basis:** `ASR_001_REVIEW_BASELINE_CORRECTION_001.md`, `ASR_001_REVIEW_BASELINE_MANIFEST.json` (correction block), forensic reconstruction across commits `8564121` and `13e6590`

### Decision

1. `BLOCKER-OPREVIEW-BASELINE-001` is classified as **Case A — manifest metadata defect at creation**: five SHA-256 values in `ASR_001_REVIEW_BASELINE_MANIFEST.json` were wrong when the manifest was created in commit `8564121`; the baseline material itself never changed (each affected file has a single commit `13e6590` predating the manifest, and its committed content equals the current content).
2. The five erroneous hashes are corrected to their historically verified values (the hashes of the committed baseline material), retaining the superseded hashes in an auditable `correction` block. The logical baseline identity (`ASR001-OPERATOR-REVIEW-BASELINE`) and `created_date` are preserved; this is a metadata repair, not a new baseline.
3. No descriptive or normative content changed (`content_changed = false`). Correcting the baseline does **not** activate operator review: `review_status = prepared_not_activated` and `public_review_status = not_public_review` are unchanged.
4. `validate_asr001_operator_review_package.py` is promoted to `required = true` in the hosted validation gate with strict hash checking; the operator-review exclusion is removed.
5. `BLOCKER-OPREVIEW-BASELINE-001` is marked resolved. Its historical existence and resolution remain on the record in `CI_VALIDATION_MANIFEST.json` and this log; the record is not deleted.
6. `LICENSE-ASR-001`, ASR normative meaning, scope, profile semantics, review questions, Atlas architecture, publication/adoption/certification/conformance status, and evaluative permissions are unchanged by this decision.

### Rationale

Forensic reconstruction proved the stored hashes matched no committed state of the affected files, while the generator hashes real bytes deterministically. The truthful, minimal repair is therefore to correct the metadata to reflect the baseline material that was always intended — not to re-hash changed content (none changed) and not to fabricate a new baseline. Retaining the superseded hashes keeps the defect and its correction auditable, satisfying the rule that an active review baseline is never changed silently.

---

## DEC-019 — ASR-001 Licensing and Citability

**Status:** Ratified (owner-delegated)
**Version:** 1.0
**Date:** 2026-08-14
**Evidence basis:** `ASR_001_LICENSING_DECISION_V0.1.md`, `DATASET_LICENSE.md` §1/§1.1, `CITATION_REGISTRY_V0.1.json`

### Decision

1. The Altis-authored ASR normative clause text (candidate normative clause catalogs and clause-to-field maps of the ASR family) is licensed under **CC BY 4.0** by explicit extension of `DATASET_LICENSE.md` §1. This **resolves `LICENSE-ASR-001`**.
2. ASR clause identifiers remain **not externally citable** as canonical objects, now held by the explicit **`CITE-HOLD-ASR-001`**, because ASR is still an unpublished Working Draft (C5, provisional). The hold lifts only on a later ASR publication / public-review decision.
3. Licensing and canonical citability are decided as separate gates: the license grants reuse rights; it does not publish, ratify, or elevate ASR, and it does not change the externally-citable set (still 39 = 20 boundary cases + 19 AS³ elements).
4. No normative clause, scope, profile semantics, review question, or evidentiary meaning changed. `BLOCKER-OPREVIEW-BASELINE-001` remains resolved (DEC-018); no other blocker is affected. `LICENSE-ASR-001` remains on the record as resolved-and-superseded, not deleted.

### Rationale

Open licensing of the reference material strengthens, rather than weakens, reference sovereignty: it lets researchers, engineers, journalists, and AI systems reuse and cite the material while AltisSports remains the canonical origin of definitions, identifiers, versions, provenance, corrections, and claim scope. Tying canonical citability to publication keeps the published/unpublished distinction honest and mirrors the Atlas citation architecture (referenceable is not the same as registered-canonical).

---

## DEC-020 — Reviewer Privacy Boundary and Public Redaction Doctrine

**Status:** Ratified
**Version:** 1.0
**Date:** 2026-08-14
**Evidence basis:** `REVIEWER_PRIVACY_BOUNDARY.md`

### Decision

1. The **Reviewer Privacy Boundary** is adopted: the public repository records reviewer roles, slots (`RWS-*`), classes (`RC-*`), states, and process only. Candidate identity is not part of the public state.
2. **Three independent consents** are distinguished, none implying another: (a) review participation consent, (b) public-attribution consent, (c) correspondence-publication consent. A person may be a `reviewer` in the public record while identified only by slot; public-attribution consent does not authorize disclosure of correspondence.
3. **Public redaction is a projection, not a rewrite of history.** The current removal of candidate names from `README.md`, `DECISION_LOG.md` DEC-017, the owner decision, the cohort roster, the dispatch log, the controlled invitation package, and the first-wave summary — and the replacement of the four personalized invitations with an anonymous template — are **public privacy projections**. They do **not** change the substance of DEC-017 or the Sprint 14 authorization; the four slot assignments authorized then remain authorized now. The verbatim named authorization and candidate evidence are retained in a private record.
4. The **people-layer is separated** from the public logic: public code and validators operate on slots and states only and must run without any private names file.
5. **Git history is left unchanged.** Candidate names appeared publicly during Sprint 14, before this boundary was ratified. A deliberate history purge is reopened only on a named person's request, a legal or reputational trigger, or before AltisSports reaches a level of external distribution that materially increases the exposure of the old history.

### Rationale

Naming a real person publicly as a candidate for our review is information we create, and it can imply a relationship that has not yet been consented to. Recording process publicly while keeping identity and correspondence private protects both the individuals and the credibility of the reference, without erasing the historical governance record. Framing the redactions as projections under an explicit decision preserves the append-only integrity of this log.
