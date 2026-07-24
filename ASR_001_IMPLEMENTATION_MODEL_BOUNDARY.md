# ASR-001 Implementation Model Boundary

**Version:** 0.1  
**Status:** Working Draft boundary decision

## 1. Research Schema Is Not the Standard Schema

`BOUNDARY_CASE_SCHEMA_V0.3.json` describes research cases.

It contains fields needed to test category theory, corpus migration, and boundary analysis. It is not automatically the correct representation for operational ASR-001 evidence profiles.

## 2. Future Implementation Model

A future implementation model can include:

- a canonical profile identifier;
- profile subject and configuration;
- clause applicability;
- disclosures;
- evidence records;
- uncertainty states;
- correction history;
- extensions;
- machine-readable validation.

The field design occurs only after candidate clauses have stabilized.

## 3. Prohibited Carry-Over

The implementation model does not inherit from the research schema merely because a field exists there.

In particular, it does not automatically inherit:

- research-only migration metadata;
- boundary-case provisional findings;
- case confidence as product confidence;
- corpus classification labels as certification states;
- analytical notes not needed for an operational profile.

## 4. Extension Boundary

A future extension mechanism preserves:

- the ASR namespace;
- extension owner;
- extension identifier;
- version;
- semantics;
- compatibility impact.

Extensions cannot redefine a core field silently.

## 5. Validation Boundary

Machine validation can test structure and deterministic logic.

Human review remains necessary for:

- object lock;
- claim interpretation;
- evidence relevance;
- contested classification;
- causal attribution;
- safety and accessibility context.

## 6. Decision Point

No ASR-001 implementation schema is authorized by Sprint 9.

The next clause-authoring sprint can define candidate fields only where a candidate clause requires them.
