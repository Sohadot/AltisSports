# ASR-001 Clause Refinement v0.1 to v0.2

**Status:** Controlled Working Draft refinement  
**Scope impact:** None  
**Clause identifiers:** Preserved

## 1. Summary

Sprint 11 preserves all thirty clause identifiers and the approved D01–D15 scope.

Three clauses receive applicability or interpretation clarification. No clause is added, removed, merged, split, or renumbered.

## 2. Clause Changes

### ASR001-D03-C02 — Agency modes and segments

**v0.1 issue:** The metadata classified the clause as `when_human_performance_claimed`, even though autonomous contests can contain meaningful agency regime changes between design, preparation, and contest execution without live human Performance Agency.

**v0.2 disposition:** Applicability becomes `when_feature_present`, triggered by `agency_modes_or_handoff_present`.

**Scope effect:** None. The clause still documents agency regimes; it does not create causal-attribution scoring.

### ASR001-D04-C02 — Embodied demand and intentional biological control

**v0.1 issue:** The applicability metadata presumed a human-performance claim even when a support configuration or disputed BCI case needs to disclose biological control or embodied demand without settled category membership.

**v0.2 disposition:** Applicability becomes `when_feature_present`, triggered by `embodiment_or_biological_control_claimed`.

**Scope effect:** None. No embodiment threshold or BCI membership decision is introduced.

### ASR001-D15-C02 — Machine-readable distribution

**v0.1 issue:** A JSON implementation profile could theoretically mark machine-readable distribution absent, even though the instance itself is a machine-readable distribution.

**v0.2 disposition:** The clause remains conditional at the document-family level, but the JSON profile schema fixes the trigger to `present`.

**Scope effect:** None. Human-readable-only profiles remain possible outside the JSON implementation model.

## 3. Evidence Requirement Metadata

Every clause now identifies one evidence-requirement class.

This does not weaken evidence integrity. It prevents profile metadata, lifecycle declarations, and absence-of-correction states from requiring artificial external evidence records.

## 4. Unchanged Boundaries

v0.2 does not authorize:

- ASR-001 publication;
- public conformance;
- certification;
- scores or rankings;
- safety or clinical approval;
- remote technical tolerances;
- final BCI athletic classification;
- category ownership or industry adoption.
