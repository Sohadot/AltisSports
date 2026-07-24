# Boundary Case Method

**Asset:** AltisSports  
**Sprint:** Sprint 2 — Boundary Case Validation  
**Version:** 0.1  
**Status:** Provisional Research Method — Not a Standard  
**Depends on:** `CATEGORY_THESIS.md`, `ONTOLOGY.md`, `AS3_STACK.md`, `FIRST_PRINCIPLES.md`, `SOURCE_AND_CLAIM_POLICY.md`, `QUALITY_GATE.md`, `BOUNDARY_CASES_CORPUS.md`

## 1. Purpose

This method governs how AltisSports tests the Spatial Sport category thesis, candidate invariants, and the provisional AS³ architecture against stratified boundary cases.

The purpose is correction, not confirmation. A case that destabilizes the theory is retained and documented.

## 2. Unit of Classification

Every case must state what object is being classified. The ontology distinguishes:

| Object | Question answered |
| --- | --- |
| **Activity** | What structured actions occur under constraints? |
| **Athletic System** | Through what arrangement is performance enabled, constrained, measured, and interpreted? |
| **Spatial Athletic System** | Does computationally mediated space play an operational role? |
| **Experience** | What does a particular participant or spectator encounter? |
| **Product** | What implementation provides experiences or system functions? |
| **Event / Contest** | What specific competitive instance is under review? |
| **Organization / Governance** | Who sets, enforces, or certifies rules and eligibility? |

### Binding Rule

A finding about a **product** must not be silently generalized to an **activity**, and a finding about an **activity** must not be silently treated as a finding about **Spatial Sport**.

When multiple objects are entangled (for example: a VR boxing product that can be used as training, fitness, or competition), the case must classify each object separately or declare the entanglement unresolved.

## 3. Dual Evaluation Axes

Each case is evaluated on two independent axes:

1. **Sport / athletic-contest axis** — Does the case satisfy candidate invariants for athletic contest under the First Principles framework?
2. **Spatial-integration axis** — Does computationally mediated space operationally enable, constrain, measure, compare, or officiate performance?

A case may be:

- sport-like / sport-recognized **without** being Spatial Sport;
- spatially integrated **without** being sport;
- both;
- neither;
- unresolved pending evidence.

## 4. Evidence Discipline

### 4.1 Accepted Evidence

Evidence must conform to `SOURCE_AND_CLAIM_POLICY.md`. Preferred sources, in order:

1. laws, regulations, and official records;
2. standards and formal sporting codes;
3. peer-reviewed research;
4. first-party technical documentation;
5. official federation, league, or company announcements;
6. reputable research with disclosed methodology;
7. high-quality professional reporting.

### 4.2 Non-Evidence

The following are discovery aids only and are insufficient as sole support for material findings:

- social posts;
- marketing slogans;
- AI-generated summaries without inspectable sources;
- brand use of “sport,” “athletic,” “immersive,” or “spatial.”

### 4.3 Fact vs Interpretation

Every material statement in a case record must carry a claim class:

- **C1** Directly Documented Fact
- **C2** Multi-Source Factual Synthesis
- **C3** Attributed External Claim
- **C4** Altis Analytical Interpretation
- **C5** Provisional Category Proposition
- **C6** Commercial or Forecast Claim

Analytical judgments about Spatial Sport membership are typically **C4** or **C5**. Institutional recognition of an activity as “sport” is typically **C1** or **C3**, depending on the source, and does not automatically settle Altis classification.

## 5. Anti-Confirmation Controls

To prevent desired conclusions from driving the analysis:

1. **Stratified sampling first.** Sprint 2 uses a fixed antagonistic sample (BC-001–BC-010). Cases are not added or dropped to protect the thesis.
2. **Separate axes.** Sport recognition and spatial integration are scored independently before any combined judgment.
3. **Explicit falsifiers.** Each case states what evidence would reverse or weaken the provisional finding.
4. **Unknown allowed.** Fields may be `unknown`, `disputed`, or `not_applicable`. Unknown must never be encoded as false.
5. **No total score.** AS³ layers are inspected; they are not averaged into a maturity or spatiality score.
6. **Disconfirming cases privileged.** If a case exposes a missing distinction, the method requires documenting the gap before inventing a salvage interpretation.
7. **Object lock.** Reclassification of the unit of analysis mid-case is prohibited unless recorded as a correction with reason.

## 6. Analysis Procedure

For each case:

1. Lock the classified object(s).
2. Record institutional recognition status with sources (if any).
3. Map observable structure to AS³ layers L1–L10.
4. Test candidate invariants: Human Agency, Constraint Integrity, Comparability, Outcome Openness, Consequence.
5. Assess operational spatial integration (not immersion, branding, or 3D graphics alone).
6. Separate documented facts from Altis interpretation.
7. State provisional findings on both axes.
8. Record confidence, disputes, and falsifiers.
9. Feed invariant-level lessons into `INVARIANCE_FINDINGS_V0.1.md` rather than forcing immediate thesis rewrite inside the case file.

## 7. Recording Disagreement and Uncertainty

Use the following statuses:

| Status | Meaning |
| --- | --- |
| `supported` | Observable evidence supports the property for the classified object. |
| `partial` | Property holds in some configurations or layers only. |
| `absent` | Property is not present in the classified object as described. |
| `disputed` | Credible readings conflict; no forced resolution. |
| `unknown` | Evidence insufficient. |
| `not_applicable` | Property does not apply to this object type. |

Confidence is recorded on a three-point scale: `low`, `medium`, `high`. Confidence concerns the quality of the case reading, not the commercial importance of the activity.

Unresolved disputes remain visible. Sprint 2 does not require unanimous closure.

## 8. Schema Binding

Machine-readable case records must validate against `BOUNDARY_CASE_SCHEMA.json`.

Human-readable analysis in `BOUNDARY_CASES_001_010.md` is authoritative for reasoning. The JSON export is authoritative for field structure, controlled values, and downstream atlas/API use.

Where the two conflict, correct the export and record the correction.

## 9. Revision Trigger

Revise this method if:

- cases cannot be compared because object types remain ambiguous;
- claim classes are routinely collapsed;
- the method systematically protects the thesis from counterexamples;
- schema fields cannot capture a recurring distinction required by the cases;
- AS³ layers cannot be mapped to observable evidence.

## 10. Explicit Non-Goals of Sprint 2

This method does not authorize:

- issuance of ASR-001;
- an S-Scale or any total spatiality score;
- product scoring tools;
- SEO page production;
- market vendor classification;
- monetized assessments.

Those depend on surviving boundary-case correction.
