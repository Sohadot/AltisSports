# AR-001 — AS³ Evidence Matrix

**Asset:** AltisSports  
**Case:** Applied Reference 001 — Evidence Lock  
**Frozen object:** WT Virtual Taekwondo contest configuration (Rules v4.0 / co-located FOP) — see `AR-001_OBJECT_LOCK.md`  
**Access date:** 2026-08-27  
**Status:** Internal inspection record — not a scorecard, not certification, not a category verdict

Layers remain inspection layers. Status words mean evidence state, not pass/fail. Source IDs refer to `AR-001_SOURCE_REGISTER.json`.

---

## How to read a layer

Each layer records:

- **Question being inspected**
- **Directly documented evidence** (prefer C1)
- **Provider or institutional claim** (C3/C6 unless independently verified)
- **Altis analytical interpretation** (C4)
- **Current status** (`documented` / `partial` / `attributed` / `not_evidenced` / `unknown`)
- **Evidence gaps**
- **Unresolved condition**
- **Evidence that would change the interpretation**
- **Source references**
- **Claim class of the Altis interpretation**

---

## L1 — Performance Agency

**Question being inspected:** Who or what performs during the round, and is live human skill causally necessary to the result?

**Directly documented evidence:**  
Athletes must be present on their mats, calibrated, and execute kicks (and blocking/stun-building actions) during a live round. Round start is `Shi-jak`; outcomes are knockout, remaining HP, disqualification, or draw-resolution statistics produced from that round. If an athlete is absent when called, the opponent wins. Manipulating PC, headset, controllers, or trackers to disturb the outcome is a prohibited act. (`SRC-001`)

**Provider or institutional claim:**  
Players use their body as the controller; physical movements control avatars. (`SRC-007`, `SRC-016`)

**Altis interpretation:**  
For the frozen contest object, live human Performance Agency is evidenced. Design of AXIS/VTKD is not in-performance agency. Game Master, Referee, and Technical Operators are officiating/operating agents, not performers. No public evidence of autonomous fighting during the round. Optional GM “force a faction’s victory” exists in older patch notes as an operator control (`SRC-008` v1.2.10); that is an officiation/override channel, not performer agency, and whether it is enabled in WT tournament mode is unknown.

**Current status:** documented for live human agency in the performance window; unknown for undeclared automation inside hit detection.

**Evidence gaps:** No public description of any assisted aiming, auto-block, or animation-driven scoring that would replace the athlete’s movement.

**Unresolved condition:** Whether any closed-source smoothing, IK, or “Full Body IK” (`SRC-008` v1.2.15) adds non-performed limb motion that can score.

**Evidence that would change the interpretation:** Software specification showing scored events generated without corresponding tracked athlete motion; or a documented auto-pilot / NPC opponent used in WT-recognised matches.

**Source references:** SRC-001, SRC-007, SRC-008, SRC-016  
**Claim class:** C4 (agency necessity); C1 for presence/start/stop procedures

---

## L2 — Performance Interface and Embodied Demand

**Question being inspected:** How does human skill enter the system, and what bodily demand is constitutive rather than scenic?

**Directly documented evidence:**  
Required interface for a court: VR headsets with controllers; AXIS nodes worn on spine, thighs, and shins (five nodes per player in manuals/site assessment); T-pose / in-game calibration; 4 m × 4 m play area; kicking to head/body; blocking with arms; possible knee involvement in older manual text. Damage depends on strike acceleration. Matches are 60-second high-intensity rounds, best-of-3, with 1-minute rest. Physical hitting of the opponent is prohibited. (`SRC-001`, `SRC-005`, `SRC-006`, `SRC-007`, `SRC-010`)

**Provider or institutional claim:**  
“Full-body motion tracking”; “every movement, speed, and force of kicks and punches precisely captured”; “strength and age no longer influence the outcome”; non-contact format reduces injury fear. (`SRC-016`, `SRC-017`)

**Altis interpretation:**  
The evidenced competition interface is **tracked XR input**, not a camera-only system and not a conventional gamepad fighter. Constitutive channels:

1. **Leg/trunk kicking channel** — AXIS nodes on spine/thighs/shins plus computational hit detection. Strongly evidenced as embodied.
2. **Head/view channel** — VR headset pose (and possibly IK). Evidenced as worn equipment; contribution to scoring vs orientation is only partly specified.
3. **Arm/block channel** — WT rules locate shields on avatar forearms; v1.3.0 patch improves one- and two-arm blocking. Required AXIS set does **not** include arm nodes (optional pairing is mentioned). Arm blocking is therefore likely controller- and/or IK-mediated. This is an interface split, not a full-body sensor suit.

Embodied demand (balance, repeated kicking, spatial timing, headset mass, cybersickness risk) is a reasoned inference from the documented interface. No public physiological study is attached to the frozen object. Provider claims that strength and age do not influence outcomes conflict with acceleration-based damage and with age categories in the rules.

**Current status:** partial (interface documented; “full-body” overstated; embodiment profile qualitative)

**Evidence gaps:** Which sensor is authoritative for forearm block; whether punches are tracked by controllers or inferred; quantitative workload/heart-rate/cybersickness data.

**Unresolved condition:** How much of scored blocking is controller pose versus body IK versus optional extra AXIS nodes.

**Evidence that would change the interpretation:** Official node map for scoring channels; biomechanical or physiological measurement under competition rules; a WT para/classification manual.

**Source references:** SRC-001, SRC-005, SRC-006, SRC-007, SRC-008, SRC-010, SRC-016, SRC-017  
**Claim class:** C4

---

## L3 — Arena and Spatial State

**Question being inspected:** What physical, computational, and unified arenas exist, and is computationally mediated space constitutive?

**Directly documented evidence:**  
Physical FOP: WT-approved elastic non-slip mats, 4 m × 4 m per player, ≥ 2 m apart, start marks, safety perimeter, operator/coach/spectator displays at specified distances. Computational arena: shared Game Room; avatars; virtual start points (yellow circle in VR); in-game boundary that TOs may set; automatic break when avatars are close for 2 seconds; optional shrinking Boundary Damage zone in software. Players occupy separate physical mats and share one virtual sparring space. Headsets must join the GM room on the same local Wi-Fi. Maximum two courts in current manuals. (`SRC-001`, `SRC-005`, `SRC-007`, `SRC-009`, `SRC-010`)

**Provider or institutional claim:**  
Players are transported to a virtual arena; realistic sparring in a digital realm. (`SRC-016`)

**Altis interpretation:**  
For the frozen object, computationally mediated space is **constitutive**, not merely representational scenery. Failure of shared match state, calibration alignment, or avatar proximity logic changes whether a round can proceed. The physical mats are also constitutive: they bound real movement, safety, and calibration. This is a **unified arena**: two local physical stations coupled to one computational contest state.

It is **not** evidenced as a geographically distributed remote arena. Global events and internet uplinks do not establish that topology (`AS3_STACK.md` §3 L3; `TARGETED_BOUNDARY_DEEPENING.md`).

**Current status:** documented for co-located unified arena; `not_evidenced` for remote distributed arena

**Evidence gaps:** Exact virtual court dimensions vs physical 4 m × 4 m; whether Boundary Damage is used in WT events; synchronisation protocol and tick rate.

**Unresolved condition:** Whether the computational geometry is a faithful metric space or a gameplay abstraction with non-linear mapping from physical displacement.

**Evidence that would change the interpretation:** Published virtual-world metric and mapping; documented WAN match between separate physical sites with latency governance; event outlines requiring or forbidding Boundary Damage.

**Source references:** SRC-001, SRC-005, SRC-007, SRC-009, SRC-010, SRC-016  
**Claim class:** C4 (constitutive unified arena); C1 for physical FOP specifications

---

## L4 — Constraint and Rule Execution

**Question being inspected:** Where do rules reside, and how do they become operative—text, humans, equipment, sensors, geometry, or code?

**Directly documented evidence:**  
WT Rules v4.0 are the written sporting code for WT-promoted/recognised events. Human execution: Referee warnings/DQ, TD final technical decisions, GM start/timeout/resume, TOs spotting unnatural movement (≥ 3 seconds) and equipment failure. Code execution: HP damage, stun, automatic break, draw criteria “determined by the game”, in-game commands. Geometry execution: virtual proximity break; optional shrinking boundary; physical play-area leaving as a prohibited act. Versioning: rules editions v1–v4; VTKD patches including v1.3.0 after Rules v4.0. (`SRC-001`, `SRC-003`, `SRC-008`)

**Provider or institutional claim:**  
Rule books are updated when there are in-game updates or new features. (`SRC-004`)

**Altis interpretation:**  
Rule execution is **hybrid**. Several decisive constraints are software-enforced (HP, stun trigger, automatic break, draw order). Several are human-enforced (prohibited physical contact, unsportsmanlike conduct, inspection, disconnection winner after 20 seconds). Calibration is a human-checked precondition for a valid start.

**Material text/code divergence after 11 April 2026** (must remain visible):

| Topic | Rules v4.0 | VTKD v1.3.0 (provider) |
| --- | --- | --- |
| Stun activation | next successful **strike** after 500 stun points | punches no longer **trigger** stun; next successful **kick** activates |
| Groin kicks | not specified as illegal-scoring exclusion | damage no longer counted from illegal groin kicks |
| Surface Calibration | not in WT text | introduced in 1.2.34, withdrawn in 1.3.0 as unstable |
| GM-Timeout on equipment power-off | disconnection policy is TD/Referee procedure | automatic GM-Timeout in software |
| Boundary Damage | not in WT Articles 1–6 | toggleable software setting |

This is not a finding that events are invalid. It is a finding that **declared rules and implemented rules can diverge**, which L4 is required to inspect.

**Current status:** partial (hybrid execution documented; version lock between rules and build not public)

**Evidence gaps:** Which VTKD build is mandatory at WT events; whether Boundary Damage is on; Tournament Mode flag vs public match.

**Unresolved condition:** Authoritative hierarchy when patch notes and WT articles disagree.

**Evidence that would change the interpretation:** Event outline locking software version to Rules v4.0; WT circular reconciling stun/groin/boundary; inspectable build identifier on official results.

**Source references:** SRC-001, SRC-003, SRC-004, SRC-007, SRC-008  
**Claim class:** C4

---

## L5 — Sensing, Tracking, and State Estimation

**Question being inspected:** What does the motion-tracking system actually observe, and how do calibration, drift, and loss affect valid state?

**Directly documented evidence:**  
AXIS wireless nodes on spine, thighs, shins; magnetometer calibration against Earth’s magnetic field and local interference; in-game T-pose calibration with controllers; dongle on the headset as motion-tracking receiver; 2.4 GHz AXIS radio with channel isolation; site assessment forbids metal structures and electrical cabling in the FOP; standing drift ≳ 10° is unacceptable in site assessment; Surface Calibration failed at many event sites due to magnetic variation across mats (later withdrawn); TOs raise a hand for unnatural avatar movement ≥ 3 seconds or equipment failure; GM-Timeout if headset, controller, dongle, or node disconnects/powers off. (`SRC-001`, `SRC-005`, `SRC-006`, `SRC-008`, `SRC-009`, `SRC-010`)

**Provider or institutional claim:**  
Occlusion-proof, stable, accurate full-body tracking without external setup. (`SRC-017`)

**Altis interpretation:**  
Sensing is constitutive. The public evidence describes **IMU / magnetometer wearable tracking plus headset tracking**, not an optical volume. That makes magnetic environment, strap stability, and calibration **part of contest integrity**, not setup trivia. “Full-body” is a provider phrase; the documented VTKD competition node map is five body nodes plus HMD (and controllers). Direct vs estimated state is not separated in public docs: IK and smoothing are acknowledged in patch history. Confidence scores are not published. Occlusion-proof is an attributed claim; IMU systems can avoid optical occlusion while still drifting.

**Current status:** partial (what is worn and how it fails is documented; accuracy, sampling, and estimator internals are not)

**Evidence gaps:** Sensor model, rates, fusion algorithm, per-joint error, how kick acceleration is derived, headset vs AXIS fusion.

**Unresolved condition:** How much scored limb motion is estimated rather than measured.

**Evidence that would change the interpretation:** Technical specification with error budgets; independent tracking validation; disclosure of IK contribution to scored hits.

**Source references:** SRC-001, SRC-005, SRC-006, SRC-008, SRC-009, SRC-010, SRC-017, SRC-018  
**Claim class:** C4

---

## L6 — Measurement and Comparability

**Question being inspected:** How do observations become metrics, and under what conditions is comparison valid?

**Directly documented evidence:**  
Metrics: HP (0–1000), stun points (0–500), damage bands Low/Medium/High from acceleration, head vs body (head deals more; mechanics page: double), headshot count, total kicks, last hit, optional Boundary Damage HP drain. Common equipment class: AXIS + listed PICO models + VTKD clients. Calibration required each match/round. Age categories exist; mixed-gender categories exist; no weight classes in Rules v4.0. (`SRC-001`, `SRC-007`)

**Provider or institutional claim:**  
Accurate scoring; level playing field; technique and strategy not physical attributes. (`SRC-004`, `SRC-016`)

**Altis interpretation:**  
Comparability is **engineered and incomplete**. Shared rules and a specified equipment class support comparison **among athletes on the same co-located stack after accepted calibration**. Missing public controls: acceleration thresholds, software-version lock, headset firmware lock, AXIS firmware lock, magnetic-environment pass/fail tied to results, latency envelope even locally. Accessibility adaptations are not specified as measurement conditions. Remote comparison is not evidenced. Provider “physical attributes no longer matter” is not established: acceleration scoring preserves a physical performance component.

**Current status:** partial

**Evidence gaps:** Formula, units of acceleration, uncertainty, official equipment homologation list with versions, whether character models affect hurtboxes.

**Unresolved condition:** Whether two calibrated athletes on different mats at the same event are metrically equivalent within a stated tolerance.

**Evidence that would change the interpretation:** Published metric specification and version lock; homologation document; independent repeatability study; documented cross-site protocol.

**Source references:** SRC-001, SRC-004, SRC-005, SRC-007, SRC-008, SRC-016  
**Claim class:** C4

---

## L7 — Officiation and Outcome

**Question being inspected:** How do rule-relevant events become decisions, and who can correct them?

**Directly documented evidence:**  
Software computes HP, stun, KO, and draw criteria. Referee declares the match winner, issues warnings/DQ, stops/resumes, determines disconnection cause and resumption using game state, consults GM/TOs. GM creates room, starts/stops, requests referee timeout on glitches. TOs flag tracking/equipment faults. TD is ultimate technical decision-maker and approves results before they are official. Coach technical timeout once per match; TD decides. Recoverable game state is restored; unrecoverable: restart if <20 s, else leading player **may** be declared winner regardless of HP margin. Injury stoppages use remaining HP or prior-round result as specified. Appeals path beyond on-mat consultation and Extraordinary Sanctions Committee is not a video-review system like WT kyorugi IVR in this text. (`SRC-001`)

**Provider or institutional claim:**  
Real-time motion tracking and accurate scoring. (`SRC-004`)

**Altis interpretation:**  
Outcome is **hybrid and only partly contestable**. Many scoring events appear non-reviewable except via timeout/equipment swap. The post-20-second disconnection rule is discretionary (“may”), which is Outcome Openness in one sense (human judgement) and reproducibility risk in another. Older GM “force victory” control (`SRC-008`) would, if enabled, be an override of performance-dependent outcome; its tournament status is unknown. Results require TD officialisation.

**Current status:** documented for role split; partial for contestability/reproducibility

**Evidence gaps:** Whether scored hits can be reviewed; logging of hits available to coaches; use of force-win in sanctioned events; protest procedure specific to VTKD scoring errors.

**Unresolved condition:** Reproducibility of a round from logs.

**Evidence that would change the interpretation:** Published protest/IVR-equivalent for VTKD; mandatory match logs; prohibition of GM force-win in tournament mode.

**Source references:** SRC-001, SRC-004, SRC-008  
**Claim class:** C4

---

## L8 — Presence and Participation

**Question being inspected:** Who perceives, communicates, and can affect the system without being the performer?

**Directly documented evidence:**  
Roles: two athletes, one coach each, Referee, GM, two TOs, TD, Referee Chairman, OMD, Game Operations Manager (official technology provider), spectators via required displays, optional spectator PC client. Athletes see opponent health in VR; GM sees both avatars and health. Information is asymmetric by design. Coach may spend one technical timeout. Spectators are not described as resource-modifying participatory actors. Hijab allowed. Mixed and age categories structure who may meet whom. (`SRC-001`, `SRC-005`, `SRC-007`)

**Provider or institutional claim:**  
Inclusive event promoting diversity; reaches new audiences. (`SRC-001` Art. 1.1, `SRC-013`)

**Altis interpretation:**  
Presence and immersion are evidenced and **must not** be treated as Spatial Athletic System membership (`AS3_STACK.md` L8). Coaches are participatory only through the timeout card and ordinary coaching, not as performance agents. Remote spectators joining a room are described for local display, not as distributed athletes. Harassment/access beyond prohibited unsportsmanlike acts and spectator altercations is not specified.

**Current status:** documented for co-located role set; `not_evidenced` for remote athlete participation

**Evidence gaps:** Broadcast delay vs live FOP; whether spectator client can leak round state; accessibility of VR view for visually impaired officials/spectators.

**Unresolved condition:** None that changes the frozen topology.

**Evidence that would change the interpretation:** Documented remote competitor role; spectator-to-constraint mechanism.

**Source references:** SRC-001, SRC-005, SRC-007, SRC-013  
**Claim class:** C4

---

## L9 — Safety, Accessibility, and Human Limits

**Question being inspected:** What physical, cognitive, and access conditions of participation are actually evidenced?

**Directly documented evidence:**  
Non-contact virtual striking; physical hitting is prohibited. Medical doctor, nurse, paramedics on venue; injury timeout 1–2 minutes. Mats non-slip; operator distances for athlete safety; play area and VR boundary; leaving designated play area prohibited. Headset/controller/node handling by TOs between rounds. Site assessment: interference, drift, no metal/cabling. Anti-doping applies. Minimum age 13 (year-based). Hijab allowed. Mixed-gender categories exist. Cybersickness, headset impact, strap failure, and collision with displays/staff are not quantified. (`SRC-001`, `SRC-010`)

**Provider or institutional claim:**  
Inclusive; breaks physical barriers; strength/age/gender limits removed; reduces injury apprehension; para pathway mentioned as WT ambition in Art. 1.1 (Olympic and Paralympic). (`SRC-001`, `SRC-013`, `SRC-016`)

**Altis interpretation:**  
Safety design is **real but local and conventional**: medical cover, mats, non-contact rule, equipment inspection. XR-specific risks (cybersickness, disorientation, cable-less collision, magnetic-site failure inducing wild avatar motion) are operationally acknowledged in tracking manuals more than in the sporting code. Accessibility: removal of weight classes and existence of mixed categories are documented format choices, **not** evidence that the system is accessible to arbitrary bodies. VR/AXIS donning, 4 m movement, kicking acceleration, and visual HUD are barriers that remain. No WT Virtual Taekwondo classification or adaptive-equipment rule was found. Provider inclusion claims are C3/C6 until evidenced.

**Current status:** partial for safety procedures; `not_evidenced` for systematic accessibility/para competition rules

**Evidence gaps:** Cybersickness protocol; adaptive interface; vision/hearing/mobility variants; child safeguarding beyond U-14 category existence.

**Unresolved condition:** Whether “inclusive” refers to format mixing or to evidenced access for disabled athletes.

**Evidence that would change the interpretation:** WT para VTKD classification; published incident/cybersickness data; adaptive-equipment homologation.

**Source references:** SRC-001, SRC-010, SRC-013, SRC-016  
**Claim class:** C4

---

## L10 — Governance, Evidence, and Change

**Question being inspected:** Who owns the contest, how do versions change, and what can an external inspector actually see?

**Directly documented evidence:**  
WT is the sporting authority; rules apply to WT-promoted/recognised events; statutes, dispute, medical, anti-doping incorporated. Official technology provider: Refract Technologies Pte Ltd / Virtual TKD Pte. Ltd. Game Operations Manager is a provider representative appointed by TD (WT President for World Championships). Software is downloaded from a VTKD portal behind operator accounts. Patch notes and manuals are public; source code, damage tables, and mandatory build IDs are not. Commercial relationship between WT and provider is institutional, not independently audited here. (`SRC-001`, `SRC-003`, `SRC-005`, `SRC-012`)

**Provider or institutional claim:**  
Endorsed by WT; highest standards of Taekwondo excellence. (`SRC-004`)

**Altis interpretation:**  
Governance is **stronger than a community VR title** because a recognised IF wrote a rulebook and stages championships. External inspectability is **limited**: scoring internals are closed; rules and software can move on different clocks (v4.0 in April, v1.3.0 in August). That is exactly the L10 condition AS³ exists to record. No Altis commercial relationship with WT or Refract is claimed in this dossier.

**Current status:** documented for authority and provider identity; partial for change-control and inspectability

**Evidence gaps:** Contractual homologation; which build was used at Chuncheon 2026 / Roma 2026; correction log for scoring defects; data-rights for athlete motion captures.

**Unresolved condition:** Whether WT or the provider is authoritative when implemented stun/boundary behaviour differs from Articles 5.x.

**Evidence that would change the interpretation:** Public software–rules version matrix; WT technical circulars; open scoring specification; disclosed data policy.

**Source references:** SRC-001, SRC-003, SRC-004, SRC-005, SRC-008, SRC-012  
**Claim class:** C4

---

## Cross-layer: Operational Spatial Integration Profile

Not an 11th layer and not a score (`AS3_STACK.md` §4). Qualitative record for the frozen object only.

| Spatial function | Status | Significance | Mechanism (short) | Failure effect | Uncertainty |
| --- | --- | --- | --- | --- | --- |
| represent | documented | constitutive | Avatars, HP, stun, virtual start points | Desync or wrong avatar invalidates contest state | Mapping fidelity unknown |
| enable | documented | constitutive | AXIS + HMD convert live movement to action | Tracking loss / GM-Timeout stops valid action | IK contribution unknown |
| mediate | documented | constitutive | Headset, straps, dongle, local network | Equipment failure or radio interference | Controller vs AXIS split for arms |
| constrain | documented | constitutive | Rules + code + virtual proximity + physical mats | Patch/rule divergence changes the contest | Boundary Damage use unknown |
| measure | partial | constitutive | Acceleration → damage bands; counts for draws | Calibration/sensing error changes outcome | Formula unpublished |
| compare | partial | supportive | Shared rules/equipment at one venue | Uncontrolled calibration, version, or magnetics weaken fairness | Remote comparison not evidenced |
| officiate | documented | supportive | Software scores; humans stop, DQ, restore, officialise | Operator/system failure may restart or award by lead | Discretion after 20 s disconnect |

Immersion is present and is **not** treated as a membership criterion.

---

## Cross-layer conditions (AS³ §5)

| Condition | Record for frozen object |
| --- | --- |
| Integrity | Trustworthy only within co-located, calibrated, version-unspecified stack; known public divergences between Rules v4.0 and VTKD v1.3.0. |
| Agency handoff | Stable live-athlete regime during rounds; no evidenced in-round autonomy. Handoffs are officiation/timeouts, not performer control modes. Agency segments remain empty (consistent with BC-015). |
| Distributed arena relation | `not_evidenced`. Topology: `co_located_multi_station`. |
| Participatory actor relation | Coach technical-timeout card is a limited constraint/process trigger. Not converted into Performance Agency. |
| Intentional biological control | `null` / not applicable. IMU tracking of limb motion is not a decoded biosignal control path. |
| Comparability | Engineered, object-specific, incomplete. |
| Accessibility | Format claims exist; systematic accessibility design not evidenced. |
| Security and privacy | Portal accounts, local logs (home-button logging in older patches), motion data: policy not inspected in depth. Prohibited acts include input tampering. |
