# Second Stratum Findings v0.2

**Asset:** AltisSports  
**Sprint:** Sprint 5 — Second Antagonistic Stratum BC-011–BC-020  
**Status:** Provisional Cross-Case Findings — Not a Standard  
**Evidence base:** `BOUNDARY_CASES_011_020.md`, `boundary-cases-011-020.v0.2.json`

## 1. Executive Finding

The v0.2 architecture largely survives the second stratum, but two areas require targeted refinement before any ASR scope draft: **time-varying agency handoff** and **distributed-arena relations**.

The stratum does not justify a total score, an embodiment threshold, certification, or ASR-001.

## 2. Findings

### F9 — Embodied Performance must remain channel-based, not locomotion-based

BC-011 and BC-012 show that fine motor control, balance, posture, and sensorimotor precision can be decisive with little locomotion or overt exertion. BC-018 adds an intentional physiological and cognitive channel with minimal conventional movement.

**Decision pressure:** retain demand channels and reject a single quantity called “amount of embodiment.” No minimum threshold is yet defensible.

### F10 — Physical spatial skill is not Operational Spatial Integration

Competitive shooting and cue sports depend heavily on physical geometry and spatial reasoning but remain outside the core computational Spatial Athletic class by default.

**Decision pressure:** public language must explicitly distinguish *spatial skill* from the governed term *Operational Spatial Integration*.

### F11 — System membership and contest maturity remain separable

BC-013 supports provisional Spatial Athletic Contest membership despite unsettled general sport recognition. BC-014 strongly supports Spatial Athletic System membership but lacks enough public governance and comparability evidence for a mature contest classification.

**Decision pressure:** preserve `spatial_athletic_system` and `spatial_athletic_contest` as distinct objects. Do not solve the distinction with a maturity score.

### F12 — Spatial Support System survives as a necessary sibling class

BC-016 is embodied, tracked, interactive, and clinically consequential without an open contest. The support-system class prevents therapeutic products from being mislabeled as sport.

**Decision pressure:** retain the class and require clinical claims to remain separated from category classification.

### F13 — Agency Handoff needs phase-level representation

BC-017 permits manual, semi-autonomous, and autonomous exoskeleton modes. BC-019 combines pre-run engineering, human supervision, and autonomous robot execution. One list of agency modes cannot show when control changed, what triggered the change, or which component caused the result.

**Required next design:** evaluate an optional `agency_segments` structure containing phase, time or task boundary, active agent, allowed assistance, evidence, and causal attribution.

### F14 — Alternative biological control keeps the embodiment boundary open

BC-018 demonstrates live human Performance Agency through brain activity, but v0.2 cannot yet determine whether intentional physiological control is sufficient Embodied Performance for Spatial Athletic System membership.

**Decision pressure:** do not equate embodiment with visible movement, and do not declare every biological signal athletic embodiment. A targeted principle is required.

### F15 — The fixed remote-distributed hypothesis remains unproven

BC-015 strongly supports co-located Virtual Taekwondo as a Spatial Athletic Contest. The available primary sources do not establish competitors in different physical sites sharing one governed match with documented latency, calibration, safety, and officiation controls.

**Consequence:** Sprint 5 must record this as an evidence gap, not infer remote validity from global distribution or product aspiration.

### F16 — Spectator intervention is not automatically Performance Agency

Under Formula E FANBOOST, spectators allocated an optional resource while drivers retained execution and deployment decisions. Spectators became **participatory rule/resource actors**, not athletes, officials, or performance agents.

**Required next design:** add a role relation for external participants who alter resources or constraints without performing.

### F17 — Consequence remains derived

Every contest case generated consequence through its contest structure. BC-016 generated clinical consequence without contest consequence. No case restored Consequence as an independent invariant.

### F18 — Qualitative Spatial Functions remain useful

The profile distinguished:

- physical spatial skill without computational integration (BC-011/012);
- embodied computational contest (BC-013/015);
- strong system integration with weak public contest governance (BC-014);
- support-system integration (BC-016);
- assistance without computational arena membership (BC-017);
- physiological control of a computational arena (BC-018);
- autonomous spatial engineering contest (BC-019);
- digital spectator intervention without Spatiality (BC-020).

No averaging was required.

## 3. Status of v0.2 Propositions

| Proposition | Status after BC-011–BC-020 |
| --- | --- |
| Performance Agency | Survives; needs phase-level handoff representation |
| Constraint Integrity | Survives |
| Comparability | Survives as engineered and object-specific |
| Outcome Openness | Survives |
| Consequence Structure | Remains derived |
| Embodied Performance | Survives as channel profile; no threshold |
| Operational Spatial Integration Profile | Survives; distributed-arena relation needs refinement |
| Spatial Support System | Strongly supported |
| Computational Contest | Useful but pressured by BCI boundary |
| Spatial Athletic System / Contest separation | Strongly supported |

## 4. What This Stratum Does Not Settle

- a minimum embodiment threshold;
- remote distributed martial-competition integrity;
- final BCI category membership;
- a normative agency-attribution method;
- a general spectator-participation taxonomy;
- any score, maturity level, conformance claim, or certification.

## 5. Required Next Move

The next sprint should be **Targeted Boundary Deepening and Schema v0.3 Decision**, focused on:

1. BC-015 remote distributed evidence;
2. BC-018 intentional physiological embodiment;
3. BC-017/019 phase-level agency segments;
4. BC-020 participatory rule/resource actors;
5. whether a `distributed_arena_relation` field is required.

`ASR-001` remains on hold.
