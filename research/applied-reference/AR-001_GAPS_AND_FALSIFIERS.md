# AR-001 — Gaps and Falsifiers

**Asset:** AltisSports  
**Case:** Applied Reference 001 — Evidence Lock  
**Frozen object:** WT Virtual Taekwondo contest configuration (Rules v4.0 / co-located FOP)  
**Access date:** 2026-08-27  
**Status:** Internal research — tests assumptions; does not close them with scores

This file records what was tested rather than assumed. Unknown remains unknown.

---

## 1. Hard-part tests

### 1.1 Is bodily movement causally connected to in-game competitive action?

**Test, not assumption.**  
**Result:** **Supported as documented mechanism, not as independently measured causality.**  
WT Rules v4.0 tie HP damage to kick acceleration in valid zones. Manuals state physical movement controls avatars. Prohibited acts include faking inputs on PC/headset/controllers/trackers, which only makes sense if those channels can affect outcome.  
**Documented vs inferred:** The existence of a movement→avatar→score pipeline is documented (C1/C3). The absence of hidden auto-scoring is inferred (C4) from official roles watching “unnatural movement,” not from a published causal audit.  
**Falsifier:** A WT-recognised match in which scored hits occur without corresponding tracked athlete motion, or an official spec of animation-driven scoring.

### 1.2 What does the motion-tracking system observe?

**Result:** **Partially documented.**  
Observed: five AXIS nodes per player (spine, thighs, shins/calves), headset with AXIS dongle, PICO controllers, magnetometer and in-game T-pose calibration.  
Not observed in public evidence: raw IMU streams, fusion graph, whether fists/forearms are measured or inverse-kinematic.  
**Documented vs inferred:** Node placement is documented. “Full-body capture” is a provider claim (C3). Arm-block sensing is inferred as controller/IK-dominant because arm nodes are not required.  
**Falsifier:** Official scoring-channel sensor map; optical ground-truth study.

### 1.3 How does calibration affect valid competition state?

**Result:** **Constitutive and operationally fragile.**  
Rules: GM must ensure calibration before start and between rounds; Referee signals proper calibration before TOs leave the mat. Manuals: magnetometer calibration; in-game calibration; offset > 1 foot unacceptable (1.2.34). Site assessment: drift > ~10° unacceptable. Patch 1.3.0: Surface Calibration withdrawn because event-site magnetic environments caused inaccurate leg tracking. Calibration disabled after countdown starts.  
**Documented vs inferred:** Calibration as a validity gate is documented. A numeric relationship between residual error and HP error is unknown.  
**Falsifier:** Homologation that a match may start without in-game calibration; or a published error-to-score transfer function.

### 1.4 Is computational space constitutive or merely representational?

**Result:** **Constitutive for the frozen contest object.**  
Shared Game Room, avatar positions, virtual proximity break, HP/stun as contest state, in-game commands, and inability to continue when match state is unrecoverable are not decorative overlays on a physical kyorugi bout. Physical mats remain constitutive for safety and tracking volume.  
**Documented vs inferred:** Constitutive status is an Altis interpretation (C4) from documented failure effects, using `CATEGORY_THESIS.md` §6 and `AS3_STACK.md` §4.  
**Falsifier:** Evidence that WT-recognised VTKD matches can be decided without shared computational state (e.g. purely physical judging of kicks).

### 1.5 Where does rule execution occur: software, human official, or both?

**Result:** **Both, with documented seams.**  
Software: damage, stun, automatic break, draw order, some timeouts.  
Human: inspection, warnings, DQ, physical-contact prohibition, disconnection winner after 20 s, injury, TD officialisation.  
**Documented vs inferred:** Hybrid split is documented. Which authority wins when v1.3.0 stun behaviour disagrees with Article 5.3.1 is unresolved.  
**Falsifier:** WT circular stating software is merely illustrative; or an event outline that software is sole referee.

### 1.6 How is scoring / outcome generated?

**Result:** **Described qualitatively, not quantitatively.**  
Pipeline: tracked strike → zone (head/body) → acceleration band → HP and/or stun; blocks negate damage; KO at 0 HP; else remaining HP; else headshots / kick-efficiency / last hit. Referee still declares the winner.  
**Documented vs inferred:** Qualitative pipeline is documented. Exact thresholds, hurtboxes, minimum inter-hit interval (a past patch mentioned minimum damage interval), and character-model effects are unknown.  
**Falsifier:** Open damage table; or evidence that officials override per-hit scores in ordinary play.

### 1.7 What happens when tracking or network state fails?

**Result:** **Procedures exist; they are not a latency specification.**  
Rules: timeout; technical timeout with equipment swap; round reset if issue in first 10 s of a coach timeout; disconnection recoverable restore vs restart (<20 s) vs possible award to leader (>20 s). Software v1.3.0: automatic GM-Timeout on headset/controller/dongle/node disconnect. Known issues in patch notes include missing disconnect indicators.  
**Documented vs inferred:** Procedures are documented. Fairness of awarding the leader “regardless of HP margin” is a governance choice, not a measured integrity bound.  
**Falsifier:** Public WAN latency budget and remediation; or event results showing matches continued with known tracking loss.

### 1.8 Do competitors share one physical venue, or can they compete remotely?

**Result:** **Examined public competition configuration is co-located.**  
Rules describe one FOP, two mats, officials walking onto mats, displays for spectators. Manuals: same Wi-Fi as Game Master; dedicated local router; max two courts. Championship announcements name a venue (Singapore OCBC Arena; Chuncheon; Foro Italico).  
**Documented vs inferred:** Co-location of examined events is documented. Possibility of other modes is not denied; it is `not_evidenced`.  
**Falsifier:** WT event outline or results proving two athletes in different physical sites in one live match under these rules.

### 1.9 Is geographically distributed synchronous competition actually evidenced?

**Result:** **`not_evidenced`.**  
This restates BC-015 / Sprint 6 without upgrading it. Internet at the court (25 Mbps) supports local clients and presumably licensing/server processes. It is not evidence of distributed opponents. Game-room join architecture is compatible with remote play in the abstract; operator instructions require same-network headsets and a shared physical FOP. Provider text: home play is an aim “down the line”; present operation is dojangs/distributors.  
**Falsifier:** Same as 1.8, plus latency, calibration-equivalence, and cross-site safety/officiation documents.

### 1.10 What is documented versus inferred?

| Claim | Status |
| --- | --- |
| WT published Rules v4.0 on 11 April 2026 | documented |
| May 30, 2025 is still the latest edition | **false**; superseded |
| AXIS + PICO + GM software used in WT VTKD | documented |
| Five nodes per player on trunk and legs | documented in manuals |
| Full-body optical mocap | not documented |
| Damage = f(acceleration) | documented qualitatively |
| Damage formula and thresholds | unknown |
| Co-located FOP | documented |
| Remote synchronous WT matches | not_evidenced |
| Inclusive / strength-irrelevant | attributed; partly contradicted by acceleration scoring and age categories |
| Computational arena constitutive | Altis interpretation (C4) |
| VTKD v1.3.0 used at all 2026 WT events | unknown |

### 1.11 What accessibility / inclusion claims are actually evidenced?

**Evidenced as format facts:** mixed-gender categories exist; no weight classes in Rules v4.0; hijab allowed; non-contact rule; age bands including Over 35 and U-14; refugee invitation discretion.  
**Not evidenced:** para classification, adaptive equipment, sensory-impairment pathways, measured reduction of injury, independence from strength/speed.  
**Institutional ambition:** Art. 1.1 aims at Olympic and Paralympic inclusion. That is C6/C3 trajectory, not present access evidence.

### 1.12 What cannot be established from public evidence?

- Numerical sensing accuracy and scoring formula  
- Mandatory software build per event  
- Authoritative resolution of rules/patch conflicts  
- Remote distributed contest integrity  
- Independent verification of “occlusion-proof” / “accurate scoring”  
- Athlete motion-data rights  
- Whether Boundary Damage is on in WT competition  
- Physiological load and cybersickness incidence  
- Reproducibility from logs  

---

## 2. Major evidence gaps (priority)

1. **Closed scoring specification** — acceleration bands, head multiplier in rules vs “double” in mechanics, hurtboxes, illegal-kick list completeness.  
2. **Rules v4.0 vs VTKD v1.3.0 clock skew** — stun trigger, groin damage, calibration method, GM-Timeout, Boundary Damage.  
3. **No public event–build lock** — cannot prove which implementation a named 2026 competition used.  
4. **Tracking estimator internals** — IK, smoothing, controller vs AXIS for arms.  
5. **Comparability controls** — firmware, magnetics pass criteria tied to results, local latency envelope.  
6. **Distributed-arena evidence still absent** — unchanged from BC-015.  
7. **Accessibility over-claim vs format fact** — inclusion language exceeds documented accommodations.  
8. **WT PDF discoverability** — current v4.0 lives on a UUID upload path linked from the provider archive, not the older human-readable `att_file` name used for v3.0.

---

## 3. Falsifiers for the frozen object lock itself

Change the object lock if any of the following is evidenced:

- A later WT rulebook than Version 4.0 governs WT-recognised VTKD.  
- WT-recognised matches are routinely geographically distributed.  
- WT disclaims the VTKD software and officiates kicks by other means.  
- The official stack is no longer AXIS + listed VR headsets.  
- Practice/home VTKD without GM/FOP is declared the same object as championships.

---

## 4. Falsifiers inherited from BC-015 (not silently closed)

BC-015 `what_would_change_judgment`:

> Published remote match rules, latency budgets, calibration procedures, and evidence of competitors in different physical sites sharing one match.

AR-001 searched current sources through 2026-08-27. That package was **not** found. The Sprint 6 `not_evidenced` status is therefore **retained**, not upgraded and not converted into impossibility.

---

## 5. Non-gaps (so they are not re-litigated as missing)

These are often assumed to be unknown; they are not:

- There is a current WT sporting code (v4.0), not only marketing.  
- Officials, calibration, FOP geometry, disconnection, and hybrid scoring are written down.  
- The technology provider is named by WT.  
- Co-located championships have been staged.  
- Software change is publicly patched, including failure-driven calibration withdrawal.

The question for publication is whether this documented core is enough to demonstrate AS³ inspection utility despite the gaps in §2.
