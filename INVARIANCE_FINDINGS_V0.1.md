# Invariance Findings v0.1

**Asset:** AltisSports  
**Sprint:** Sprint 2 — Boundary Case Validation  
**Version:** 0.1  
**Status:** Provisional Theory Correction Notes — Not a Standard  
**Based on:** `BOUNDARY_CASES_001_010.md`, `boundary-cases-001-010.json`  
**Depends on:** `FIRST_PRINCIPLES.md`, `CATEGORY_THESIS.md`, `ONTOLOGY.md`, `AS3_STACK.md`

## 1. Purpose

This document extracts what the stratified sample teaches about candidate invariants and AS³. It does not re-narrate each case. It records what survives, what fails, and what must be redesigned before ASR-001.

## 2. Method Reminder

Findings are **C5 provisional category propositions** unless marked otherwise. A finding is retained when multiple antagonistic cases converge; a single elegant case is not enough.

## 3. Core Findings

### F1 — Human Agency is insufficient; Performance Agency is required

**Claim:** The candidate invariant “Human Agency” must be narrowed to **Performance Agency**: meaningful in-contest influence by a human performer through skill executed during the contest window.

| Evidence | Lesson |
| --- | --- |
| BC-010 Autonomous robots | Humans design and engineer agents, yet lack live performance agency during play. Design agency ≠ athletic agency. |
| BC-005 Drone racing | Remote control still counts as performance agency if skill is exercised in-match. |
| BC-003 Formula One | Mediation does not cancel performance agency when the human remains the required in-contest controller. |

**Implication:** Replace or subtype L1 / invariant wording:

- **Performance Agency** (necessary for athletic contest)
- **Design / Engineering Agency** (pre-contest; insufficient alone)
- optional later: **Assisted Agency** (human performance with real-time assistance under declared constraints)

### F2 — Embodiment is not necessary for all sport; it is candidate-necessary for Spatial Athletic Sport

**Claim:** Gross motor embodiment is not a necessary condition for *sport as such*. It is a leading candidate condition for membership in **Spatial Athletic Sport**.

| Evidence | Lesson |
| --- | --- |
| BC-002 Chess | IOC-recognized sport federation activity with minimal locomotor embodiment. |
| BC-006 Tactical shooter | Computational contest with high skill and weak athletic embodiment. |
| BC-008 Virtual cycling | Embodied physiological interface + computational arena — strong Spatial Athletic candidate. |
| BC-007 VR boxing | Embodiment present; sport status still depends on governance/comparability. |

**Implication:** Keep two axes permanently:

1. sport / athletic-contest axis  
2. spatial-athletic-integration axis  

Do not smuggle embodiment into the general sport definition merely to protect Spatial Sport branding.

### F3 — Consequence is usually derivative, not an independent invariant

**Claim:** In this sample, Consequence almost always follows from contest structure (ranking, elimination, stakes) plus Outcome Openness and Constraint Integrity. It rarely adds independent discriminatory power.

| Evidence | Lesson |
| --- | --- |
| BC-001–BC-006 | Where contest structure exists, consequence appears. |
| BC-007 / BC-009 | Weak or variable consequence tracks weak contest governance more than a separate metaphysical property. |
| Physical exertion | Important for many athletic forms, but chess shows exertion is not universal for sport recognition. |

**Implication:** Demote Consequence from candidate invariant to **derived contest property** unless a later sample finds a case with open outcomes and constraints but no non-trivial consequence inside the activity structure.

### F4 — Activity, athletic system, product, and training system must stay separated

**Claim:** Object collapse is the most frequent classification error risk in spatial-adjacent domains.

| Evidence | Lesson |
| --- | --- |
| BC-007 VR boxing | Product/experience hybrid; “boxing” the sport must not be inferred. |
| BC-009 Flight sim | Training network ≠ skill contest ≠ sport. |
| BC-008 Virtual cycling | Same stack can support training and championship; classification depends on event system, not scenery. |

**Implication:** Ontology classification discipline is not optional metadata. ASR and Atlas records must lock `classified_object` before judgment.

### F5 — Operational Space is graded, not binary

**Claim:** “Operational Space” should be modeled as a multi-degree condition, not a yes/no badge.

Observed degrees in the sample:

1. **None / representational only** — BC-001 default; BC-002 digital board as state machine representation.
2. **Measurement/officiation assist** — optional VAR-like layers; telemetry in F1.
3. **Remote sensing channel into physical arena** — BC-005 FPV.
4. **Computational contest arena without athletic embodiment claim** — BC-006, typical BC-009.
5. **Unified embodied–computational performance coupling** — BC-008; partial BC-007.

**Implication:** Category Thesis language (“operationally integrated”) survives, but needs an explicit degree vocabulary before any standard. No total score; profile fields instead.

### F6 — Computational arena ≠ Spatial Athletic Sport

**Claim:** A decisive computational map/space is not sufficient for Spatial Athletic Sport.

BC-006 demonstrates the split:

- computational space can constrain, measure, and officiate;
- without an athletic/performance interface of the kind AS³ L2 targets, the correct class may be **computational contest** (sibling), not Spatial Athletic Sport.

**Implication:** Category Thesis should explicitly reject “any game with a 3D map” and also reject the subtler error “any competitive computational arena.”

### F7 — Mediation is not Spatiality

**Claim:** Vehicle, prosthesis, or ECU mediation preserves or reshapes embodiment; it does not by itself create Spatial Sport.

| Evidence | Lesson |
| --- | --- |
| BC-003 F1 | Deep computation + physical arena ≠ Spatial Athletic System. |
| BC-004 Para Athletics | Assistive interfaces support agency and comparability; they are not computational arenas. |

**Implication:** AS³ L2 must distinguish:

- adaptive/assistive interfaces;
- vehicle mediation;
- remote control interfaces;
- tracked embodied XR interfaces.

### F8 — Comparability is often engineered, not ambient

**Claim:** In spatial and hybrid systems, comparability frequently appears as an active integrity project (standardized trainers, patch locks, latency rules), not as a natural given.

BC-008’s trainer standardization is positive evidence of sport-like integrity work and simultaneous evidence that Spatial Athletic Systems fail easily without it.

**Implication:** L6 should treat missing comparability controls as unresolved evidence, not automatic negative scoring (already aligned with Tool Gate philosophy).

## 4. Candidate Invariant Status After Sprint 2

| Candidate | Status after BC-001–010 | Action |
| --- | --- | --- |
| Human Agency | Needs rewrite | Replace with Performance Agency (+ agency subtypes) |
| Constraint Integrity | Survives | Keep; require inspectability for code/geometry rules |
| Comparability | Survives, sharpened | Emphasize engineered conditions in hybrid systems |
| Outcome Openness | Survives | Keep |
| Consequence | Weak as independent invariant | Demote to derived property pending further tests |
| Operational Spatial Integration | Survives as category differentiator | Convert to graded profile, not binary label |
| Embodiment | Not universal for sport | Scope to Spatial Athletic Sport / athletic subclass |

## 5. AS³ Correction Notes

### Surviving structure

The failure chain remains useful:

> human action → interface → arena → rule → sensing → measurement → decision → participation → safety → governance

### Gaps / overlaps exposed

1. **L1 underspecified** — must encode Performance Agency vs Design Agency.
2. **L2 underspecified** — mediation types and body variation (BC-004) need first-class vocabulary.
3. **L3/L5/L6/L7 entanglement** — “operational space” spans multiple layers; needs a cross-layer condition object rather than stuffing everything into L3.
4. **L8 vs immersion** — presence/immersion can be high while spatial-athletic integration is low or contested (BC-007 marketing risk).
5. **No layer for classified object lock** — object type is methodological precondition; keep in method/ontology, not as an AS³ layer.
6. **No total score** — confirmed again: averaging layers would hide BC-006 vs BC-008 differences.

### Provisional AS³ revision candidates (not yet applied)

- Add agency subtypes under L1.
- Add interface typology under L2.
- Add cross-layer `OperationalSpatialIntegrationProfile` with graded roles: enable / constrain / measure / compare / officiate.
- Clarify that L8 presence is not evidence of Spatial Sport.

## 6. Category Thesis Pressure Points

The working definition largely survives if clarified as follows:

> Spatial Sport concerns athletic systems in which **human performance agency** is operationally integrated with computationally mediated space through interaction, constraint, measurement, comparison, or officiation.

Required clarifications before ASR-001:

1. Athletic ≠ every skilled competition.
2. Operational integration is graded.
3. Computational contest arenas without athletic interfaces are adjacent, not automatic members.
4. Training/simulation products are not sports by scenery or branding.
5. Institutional recognition is evidence about organizations, not automatic Altis class membership.

## 7. What This Sample Does *Not* Settle

- Threshold values for “enough” embodiment.
- Whether drone racing is in or out of Spatial Athletic Sport.
- A final esports ontology.
- Transfer-of-training claims for VR/sim products.
- Any S-Scale or readiness index.
- Market vendor rankings.

## 8. Recommended Theory Edits (next governed revision)

Priority order:

1. Update `FIRST_PRINCIPLES.md` candidate invariants (Performance Agency; demote Consequence).
2. Patch `CATEGORY_THESIS.md` with graded operational space + computational-contest exclusion.
3. Patch `ONTOLOGY.md` with agency subtypes and explicit sibling class hooks for computational contests.
4. Patch `AS3_STACK.md` L1/L2 and cross-layer spatial profile.
5. Only then draft ASR-001 scope.

Do **not** silently rewrite theory inside marketing copy or tools.

## 9. Falsifiers for These Findings

Revise F1–F8 if later strata show, for example:

- autonomous spectacles that institutions and athletes treat as sport without live human performance agency, with coherent integrity rationale;
- non-embodied computational contests that are indistinguishable in failure modes from embodied spatial athletic systems;
- consequence as an independent discriminator after contest structure is controlled for;
- binary operational-space labeling that outperforms graded profiles in predictive or governance use.

## 10. One-Sentence Verdict

Sprint 2 confirms that Altis should center **performance agency + graded operational spatial integration**, refuse to equate computational arenas with Spatial Athletic Sport, and treat embodiment as category-scoped rather than universal for sport.
