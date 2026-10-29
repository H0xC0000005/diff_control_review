# Information-gap review directions and proposed default plan

Date: 2026-10-05. Status: **Detailed discussion record; review ordering agreed,
observer C subsequently approved; no new physical extension adopted.**
Current ordering reference: [consolidated brief plan](rm9_next_review_brief_plan.md).
Earlier provisional wording below records the discussion chronology; the brief
plan supersedes its pending status for the source-first ordering only.
The accepted flow closed UG4-R. R1 delivered its C/A/P observer proposal;
the user subsequently approved C and authorized continuation. The bounded R2/R3
and R5 audit is now at [UG5](../../reporting/rm9_70_observer_c_findings_and_disposition_gate.md).
Earlier pending-observer/route and no-execution wording below is chronological
history, superseded by the [approval](../../discussion/rm9_observer_c_approval_and_continuation.md).
No changed physics, successor or RM9 closure is adopted.
Parent: [current UG4 gate](../../reporting/rm9_50_separate_resource_findings_and_observer_gate.md).
Inputs: [aggregate-flow explanation](rm9_lane_contrast_and_aggregate_flow_explained.pdf),
[adopted kernel](rm9_separate_resource_and_observer_audit.pdf),
[RM8 information ladder](../rm8_predecessor_and_information_map.md) and
[deferred extensions](rm9_deferred_lane_interaction_extensions.md).

## User clarification and purpose

The user wants a default plan to discuss and revise before further execution.
They explicitly reject adding more than two mainline lanes by default merely
to defeat mass/flow reconstruction. Task and model admission must be method-first:
source-supported traffic mechanisms and control questions determine the model,
rather than preserving project progress or an existing formulation at all costs.

The target is a **decision-relevant state that remains unresolved by the entire
admitted aggregate history**. Mass and flow remain observed channels; the plan
does not try to make those measurements unavailable. A contrast revealed by
them is not hidden information. A failure of one mass-only closure is different
from a limitation of every method using the strong aggregate observer.

Accepted planning guardrails from this instruction:

- Keep two mainline lanes as the default baseline. More lanes need an independent
  traffic-domain reason and separate adoption, not an information-rank workaround.
- Do not force equal lane parameters, remove independent speed, weaken history,
  introduce private forcing or tune a service penalty to create a positive pair.
- Preserve a sufficient/negative/unresolved result as a valid review outcome.
- Reuse current findings as evidence and rejection criteria, not an admission
  constraint on a genuinely different source-supported task.

This request approves drafting and discussion, not execution of an extension,
adoption of UG4, a revised physical law, numerical runs or a successor sprint.

## Core question, model-chain function and gap

**Problem statement:** Which physically justified single-ramp task, if any, has
state unavailable to the complete aggregate observer that changes useful common
meter actions and provides consequential gradient information?

**Assumed chain:** source-supported geometry/demand/merge mechanism → conserved
state and declared aggregate measurements/history → common feasible meter action
→ traffic evolution → final departures and complete affected-population time.
Additional state is admitted only where evidence says it can affect this chain.

**Core gap:** current free-flow two-lane states are reconstructible under exact
aligned mass/flow and distinct known mobilities. Flow clipping prevents that
particular inverse but has not established equality of speed and full history.
The current speed/support contract and ramp geometry/balances are incomplete.
No reviewed work yet supplies our complete matched-history/useful-action/gradient
bridge. A real merge-control effect and a genuinely hidden control-relevant
state are separate evidence claims.

## Four candidate directions

### IG-D1 — source-led audit of the present two-lane finite-receiving task

**Task/model formulation:** Retain one finite-storage ramp, a common bounded
open-loop rate schedule, two mainline lanes and the adopted lateral-first CTM
kernel. Review source-supported traffic regimes around a merge: ordinary
free flow, active downstream receiving, queues and transients. Do not first
choose lane snapshots or coefficients to obtain observational collisions.

The review establishes the observer's density/mass, flow, speed, counts, ramp
history and timing/support; then asks whether any consequential lane contrast
survives those observations over a feasible common history. Where measurements
already reconstruct it, document aggregate sufficiency. A different future
flow after intervention is not a measurement available before that intervention.

**Evidence to collect:** measurement definitions and independent versus derived
quantities; physical occurrences of the admitted constrained regime; lane-specific
FD/source adaptation limits; admissible initialization and ramp balances;
competing aggregate state-estimation/control results. Current free-flow and
stage-collapse results are immediate rejection tests, not proof of every regime.

**Pros:** Uses the smallest existing task; keeps the comparison fair; can produce
either a genuine information/action candidate or a useful sufficiency result;
requires no new traffic state merely to start the audit.

**Cons:** Density, flow, independent speed and history may resolve the contrast
even under receiving limits. A real positive lane-information result is not
guaranteed. The idealized observer may not have the physical detector meaning
needed for an applied task.

**Dependencies/scientific consequence:** UG4/G1 observer adoption must precede
the full certificate. Selecting a source-supported operating domain is not
approval to change the fixed G2 law. If that law misses required physics,
report the conflict and reopen only the affected clause.

**Disposition sought:** a scoped regime/observer classification, followed only
where warranted by a feasible information/action argument. The source review
may instead identify an aggregate-sufficient task or an unresolved boundary.

### IG-D2 — a physically justified finite acceleration-lane/mandatory-merge task

**Task/model formulation:** Keep two mainline lanes and rate metering, but
review whether the physical case requires an explicit short acceleration lane,
distributed merging positions, finite storage and lane-end urgency. Meter
release reaches that region after propagation; actual entry still depends on
mainline receiving and feasibility. Known position/geometry is not hidden state.

The information candidate would concern traffic allocation and coupled
receiving/merge readiness along that geometry. Full spatial aggregate/ramp
observations must still be audited: an added spatial coordinate or acceleration
lane cannot simply be declared invisible. Resolving existing ramp geometry and
adopting a new mandatory-merge law are distinct steps.

**Evidence to collect:** actual site geometry, merging-position/urgency
observations, finite ramp/short-lane storage and sources that define a conservative
distributed merge law. Test whether the law changes common rate actions and
whether the strong observer already reconstructs its required state.

**Pros:** Provides a concrete traffic reason for richer spatial interaction;
retains the common rate actuator; distinguishes meter release from realized
merging and can improve traffic-domain validity independently of information
positivity.

**Cons:** Geometry alone may add no hidden information; complete spatial/ramp
history may expose the consequential mass distribution. Distributed merging
adds conservation/receiving dependencies and is not validated by an urgency
coefficient alone.

**Dependencies/scientific consequence:** Related to deferred X2, possibly X1;
new laws require explicit G2 and dependent G1/G3 reopening. An actual short
acceleration lane is not an arbitrary third mainline lane. Its observation
contract must remain explicit. Neither X1 nor X2 is opened by this proposal.

**Disposition sought:** source-based admission or rejection of one geometric
task and its minimum necessary state, not a manufactured hidden-position pair.

### IG-D3 — acceleration/relaxation or composition beyond lane totals

**Task/model formulation:** Keep the same common meter-rate action, but review
merge dynamics that first-order lane mass does not fully determine: bounded
acceleration after a maneuver, transient speed/spacing distributions, or a
supported stream composition/merge-readiness state. A compact continuous
statistic is acceptable if it closes the relevant interaction; a microscopic
model is a possible mechanistic reference, not an automatic required mainline.

The hypothesis is that two states could share admitted aggregate histories yet
respond differently to the same rate change because the distribution/readiness
state affects merge disruption or capacity recovery. Both hiddenness and action
relevance must be proved; neither follows from naming an additional variable.

**Evidence to collect:** a causal physical connection between the omitted state,
metering intervention and departure timing; whether aggregate mean speed,
class data, ramp queue and full history identify that state; state evolution and
conservation/receiving semantics; stronger aggregate speed/memory/composition
competitors and the scope of their sufficiency.

**Pros:** Addresses a physical mechanism absent from elementary first-order
occupancy; can test a compact aggregate augmentation against fuller lane or
particle state; keeps rate-control relevance while allowing a new model family.

**Cons:** A known ramp queue may already explain entry speed; a hysteresis mode
with known initialization may be determined by observed density history.
Acceleration or event physics can add state/parameter and derivative difficulties.
The literature does not supply our complete exact-history/gradient certificate.

**Dependencies/scientific consequence:** Related to deferred X3; requires G2
state/law adoption and G1 observation revision, with G4 event/derivative review
if necessary. No blanket weighted-service multiplier, new mode or extra speed
state is approved. The current two-lane kernel remains a comparison baseline,
not an admission limit on the new physical family.

**Disposition sought:** a supported omitted mechanism and minimum candidate
state, or evidence that a stronger aggregate/history closure already suffices.

### IG-D4 — gap-aligned release timing as a separately admitted control task

**Task/model formulation:** Review detailed infrastructure release timing, such
as aligning releases with feasible mainline gaps, rather than optimizing only
a mean rate/fixed-shape schedule. Retain two mainline lanes where appropriate.
Gap timing/order is the potential information difference. A fair comparison
must give all methods the same timing-action family, feasible releases and
complete all-stream objective; additional sensing is an explicit information
comparison, not a hidden advantage in the controller.

**Evidence to collect:** operational release and sensing requirements; benefits
attributable to gap information separately from changed actuators/controllers;
whether the declared aggregate history/forcing already resolves those gaps;
feasible event and expected-outcome derivative contracts. Sensor averaging or
sampling cannot be weakened silently to create a pair.

**Pros:** A nearby published task directly connects fine gap information to
infrastructure metering. It tests information closely tied to the control
decision, with a clearer physical role than arbitrary extra lane coordinates.

**Cons:** Changes the current control question and sensing/timing contract.
Reported controller improvements are not exact matched-history necessity
proofs. Event/stochastic sensitivities may prevent the current simple gradient
contract; detailed gap representation could exceed the desired model scope.

**Dependencies/scientific consequence:** Reopen G0's action contract and G1/G2,
then G4 if needed. This is neither an automatic rate-only extension nor the
deferred coordinated multi-ramp Candidate C. It needs separate user adoption.

**Disposition sought:** admission of a new timing task with a clean comparison,
or rejection where sensing/actuation/event requirements outweigh its relevance.

## Provisional default ordering and evidence gates

**Recommendation:** source-led observer/task admission, then IG-D1. Review
IG-D2 or IG-D3 only for an independently supported missing physical mechanism;
keep IG-D4 as an optional separately formulated task. This is not a ladder
that automatically adds complexity until a positive result appears.

This would prioritize the bounded measurement/source-first route **UG4.B**
over the earlier provisional idealized-first recommendation A. Both remain
unapproved. UG4.A remains a viable faster conditional mathematical benchmark;
its strongest advantage is tractability without extra traffic dynamics, and its
limitation is a result conditional on the declared speed/support approximation.
An idealized observer can still be admitted after source review if its intended
meaning and claim boundary are acceptable; source-first does not guarantee a
field-exact observation map or require simulator execution.

1. **Evidence orientation:** reuse the current packet to map physical mechanisms,
   operating domains, measurement support and strong aggregate competitors.
   Bound any later targeted search to the specific missing item. Record sources
   against physical mechanisms/model assumptions, information, action and derivative
   claims separately. Do not begin a broad new literature sprint automatically.
2. **Task/observer discussion:** choose and document geometry, initial/common
   forcing, complete observation support and measurement meaning before trying
   to find matching states. Stop if a new observation or physical law needs
   adoption; do not infer approval from this proposed ordering.
3. **Current-task information audit:** classify branches and complete-history
   reconstructibility. Report what is identified, what remains ambiguous and
   whether that ambiguity survives to the time the action operates. Use a
   source-supported parameter/domain family, not a favorable tuned instance.
4. **Decision relevance:** only for a surviving feasible ambiguity, compare the
   same feasible rate perturbations with full affected-population accounting.
   Require a useful-action distinction, not only different local flow. Also
   compare aggregate history, its inferred/augmented sufficient statistic and
   fuller lane state.
5. **Gradient readiness:** trace the consequential state through the action to
   final departures; classify branch/event issues and required validation.
   Numerical correctness and independent usefulness stay future work unless
   separately authorized.
6. **Result disposition:** close a supported conditional result, aggregate
   sufficiency or unresolved finding. A source-supported missing mechanism may
   motivate IG-D2/3 discussion. A negative result alone does not open them.

The first output should be an evidence/observer/task matrix and an adopted or
rejected observation contract, not a preselected positive lane-state example.

### Ordering clarification after user discussion — 5 October

The user's proposed ordering is consistent with the default, with the following
explicit refinements. This records a planning preference and interpretation;
it does not select UG4, amend a law or authorize execution.

0. **Admission principle:** avoid additional assumptions wherever possible and
   prefer a genuine traffic setting over a constructed favorable case. An
   absence of literature refutation is not positive evidence of occurrence,
   hiddenness or action relevance. A plausible unverified assumption may be
   retained as a labeled hypothesis, rather than promoted to an established task.
1. **Existing-task pass:** first audit source-grounded operating regimes under
   the unchanged task/law and the complete admitted observer. If necessary,
   assess independently motivated within-family assumptions or restrictions
   separately. They must be justified by the traffic setting rather than selected
   to hide information, and any resulting certificate is conditional on them.
   Record each assumption's role, support, scope and information consequences.
   A compatible restriction is still an added assumption; changed scientific
   meaning needs adoption before use as the review's task contract. Stop a
   subcase when a decisive reconstruction/action-sufficiency result excludes it;
   do not conclude universal failure from the existing free-flow proof alone.
2. **Alternative-task pass:** compare independently credible alternatives by
   the smallest scientifically meaningful change. IG-D2–D4 are candidate
   families, not a fixed D2 → D3 → D4 sequence. Record changes to geometry,
   dynamical state, physical laws, observations/history, actuator, objective and
   derivative contract. A single added variable with a speculative law can be
   a larger methodological change than several cells describing a real geometry.
   Reusing code or preserving progress is not a ranking criterion. Evidence and
   the core information/control question take priority over formal similarity.

The expectation of a negative present-task result is a working conjecture,
not an acceptance criterion. Hiddenness is tested first, but an ambiguity that
cannot affect common feasible actions is not a positive core-question result.
Alternatives may be scoped from sources in parallel with the current-task audit;
their adoption need not await exhaustive attempts to rescue every subcase.
They still require the applicable user decision before execution.

## Decision ownership, dependencies and reopen rules

There are no implementation components. Mixed issues split into user-owned
Type 2 scientific contracts and dependent reviewer-owned Type 1 evidence.

| ID | Classification / owner | Status and dependencies |
|---|---|---|
| IG-G1 | Type 2 / user | User-confirmed guardrails: no extra mainline lanes just to defeat reconstruction; method-first admission; preserve strong information. Proposed ordering clarification: unchanged task before justified added assumptions; compare alternatives by scientific change, not direction number. |
| IG-G2 | Type 2 / user, RM9-G1/UG4 | UG4-R closed; UG4-O.C approved. Concrete site/initial domain remains unbound; bounded continuation at UG5. |
| IG-G3 | Type 2 / user, RM9-G0/G2 | Select current task or a supported geometry/state/action amendment; pending, extensions still deferred. |
| IG-G4 | Type 2 / shared evidence contract, RM9-G3/G4 | Preserve history/action/accounting and evidence levels; any event/sensing/derivative change requires adoption. |
| IG-E1 | Type 1 / reviewer | Source mapping for physical mechanisms and measurements; informs IG-G2/G3 without adopting them. |
| IG-E2 | Type 1 / reviewer | Stage/history identifiability analysis under adopted G1/G2; after IG-G2 closure. |
| IG-E3 | Type 1 / reviewer | Audit stronger aggregate memory/state-estimation comparators and attribution; supports G3/G4 fairness. |

Global task/observer/state contracts close before dependent certificate details.
If a new physical mechanism is necessary, explicitly reopen the smallest G2
clause and its G1/G3/G4 dependencies; if only observer support fails, reopen G1.
A gap-timing actuator change also reopens G0. No local proof may weaken history,
hide known ramp queues or change common forcing to repair a failed test.

## Source anchors and strict evidence boundaries

These are existing orientation sources, not a completed new admission review:

- [Nagalur Subraveti/Knoop/van Arem](https://repository.tudelft.nl/file/File_2c4359e7-5e5a-4651-964f-6f3610ab89ae):
  lane CTM, heterogeneous FDs and route/cooperation incentives motivate IG-D1/2.
  They do not prove that the adopted two-lane observer hides a useful state.
- [Laval/Cassidy/Daganzo](https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/f/3571/files/2023/03/merges.pdf),
  Section 2: bounded-acceleration lane changers create discharge-reducing voids.
  This anchors IG-D3; the modeled ramp omits acceleration-lane length and does
  not validate IG-D2's distributed geometry or a universal merge-work factor.
- [Klomp/Knoop/Taale/Hoogendoorn](https://repository.tudelft.nl/file/File_c446bd9b-9a19-494b-9989-3d11f96fbb1a):
  gap-detected infrastructure release and acceleration-informed simulation anchor
  IG-D4. Different sensing/timing/controllers limit transfer to the rate-only task.
- [Schmitt/Ramesh/Lygeros](https://arxiv.org/abs/1611.06766): conditional
  optimality in monotonic CTM is a serious aggregate-control comparator, not
  universal sufficiency for every proposed merge mechanism.
- [Capacity-drop aggregate comparator](https://arxiv.org/abs/2106.10347) and
  [existing RM8 source study](../../extraction/rm8_source_studies/aggregate_and_gradient_alternatives.md):
  distinguish physical capacity memory from memory already derivable from
  admitted history and known initialization.
- [Existing isolated-merge evidence audit](../../extraction/rm8_source_studies/isolated_merge_and_hybrid.md):
  field metering effects and shoulder congestion do not alone establish missing
  information; aggregate occupancy and known ramp queues can already inform control.

No source currently establishes the combined whole-history/useful-action/gradient
claim for any direction. Recommendations are inferences about review value,
not positive results or adoption of the full published models.

## Planning work report

Read current protocol/handoff/inventory, adopted equations and information
explanation, RM7/RM8 task/control/source records and X1–X3 deferrals. Rechecked
existing primary lane-model, acceleration/void and gap-meter papers and
aggregate-control abstracts through web open; no broad query campaign, new
archive, CSV/source record or traffic experiment. The isolated-merge report's
direct web PDF failed; its prior local review record remains orientation evidence,
not a new full-text inspection. No dependency or production/slide/PDF change.

This Markdown proposal is formula-free; the existing explanation PDF supplies
the mathematical distinctions. Synchronized the provisional recommendation
in UG4 findings, inventory and handoff and archived the user guardrails and
response in the dialogue. Checked new local links and pending/deferral wording.
No scientific tests were required for this planning document.

RM9 remains open at UG4. Next allowed action: discuss this proposed default and
the user's remaining concerns, then record any explicit observer/route choice.
No proposed execution step has started.
