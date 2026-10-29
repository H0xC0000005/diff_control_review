# S02.35 — Feedback 23 — task candidates, retained information and the gate

Sprint: [S02](../../00_review_sequence.md#s02) · Role: 35 feedback clarification · Predecessor: S01 · Gate: N2-UG1.

Amendment follow-up: [novelty and component necessity review](s02_36_feedback23_amendment_novelty_and_component_necessity.md).
The candidate below remains provisional; known lane/control/AD ingredients
are not standalone novelty. Its current rationale is a go/no-go study of
task-specific information sufficiency for useful advice gradients, not
approval to construct all candidate components.

Date: 2026-09-17. Status: discussion at N2-UG1; no route/model approved.
Feedback source: `temp_content/feedback/baseline_novelty_audit_feedback.md`, item23.
The feedback is preserved, not marked/rewritten. No supplementary file is linked
from item23. This response refines the living candidate inventory; it does not
execute Route B or amend the approved N2 protocol.

## 1. What the previous report should have made explicit

Both questions belong here at **candidate/feasibility level**. A useful gate must
describe a traffic task, the hypothesized lost information and a credible route
to deterministic differentiated dynamics. Saying only 'the gap is unresolved'
does not give enough substance to judge whether further work is worthwhile.

What this phase cannot establish is a proven minimum representation, a frozen
complete equation set, or verified useful gradients. Those require later
approved design and evidence, potentially numerical diagnostics. The user
should choose a motivated investigation, not supply the missing empirical truth.

Terminology: B2 currently labels **lane-and-response-group traffic**, not a
separate control task. Here 'B2 task candidate' means a variant of the accepted
speed-advisory task where lane-resolved information might matter. B0/B1/B2
are working model hypotheses, not a mandatory construction sequence. 'Route B'
is the evidence-refinement route and is unrelated to model label B2.

## 2. Candidate 1 — merge-pressure-sensitive speed advice

**Task.** Choose a common upstream, link-level speed-advice schedule for a fixed
lane reduction. Closing and continuing lanes receive the same advice in each
zone. Geometry and closure/reopening times are fixed scenario inputs; drivers'
realized movement and lane transfers remain traffic dynamics, not commands.
Evaluate the same population's complete delay/time-spent accounting, including
upstream waiting and, for temporary events, recovery until clearance or an
explicitly approved complete tail-accounting rule.

**Assumed model-chain function.** Advice → realized mean speed/propagation →
arrival into the merge region → constrained transfer from ending lanes into
continuing lanes → bottleneck service/queues → objective. The lane refinement
must transmit receiving-lane congestion/storage back to feasible merging;
it cannot instantly allocate traffic to its desired lane.

**Diagnostic hypothesis.** Two admissible scenarios can match the lower-
resolution model's retained segment states, demand, geometry, response
population and advice, while placing more traffic in an ending lane in one
scenario. The candidate lane model can distinguish the different merge demand
and receiving opportunity. Whether this changes the ranking of a feasible
advice perturbation in a richer evaluator is **unknown**. Different service
trajectories alone do not establish different useful advice gradients.

Reachable initializations/history must be specified later: an arbitrary lane
redistribution cannot be assumed physically realizable. Matching totals does
not automatically match all mean speeds, flows, histories or boundary conditions.
Nor is reduced speed assumed always to improve merging; its net effect depends
on response, receiving conditions and the upstream delay it introduces.

**Literature basis.** FB0030 provides per-lane conservation, mandatory lane-end
incentives, downstream lookahead and receiving-limited transfer (printed
1760–1766, equations1–22), with field lane-drop prediction. FB0024 supplies
endogenous lane-group density-imbalance transfer for on-ramp conditions, not a
complete lane-drop law. These support components, not this proposed decision
contrast or external gradient result.
[FB0030](https://doi.org/10.1080/21680566.2019.1700846),
[FB0024](https://doi.org/10.1061/JTEPBS.0000481).
Strong aggregate response/propagation comes from the FB0026 family; recovery
reference logic from FB0021. Do not combine components without auditing their
units, budgets, boundaries and response assumptions.

**Smallest plausible refinement.** Spatial continuous mass/density separated
between ending and continuing lanes, fixed adjacency/lane-end metadata, and
deterministic lateral flux constrained by donor traffic and receiving room.
Retain baseline mean-response/speed dynamics or history wherever needed.
'Ending versus continuing' is an initial information partition, not proof that
two groups capture every geometry: non-equivalent lanes, multiple merge paths
or transfer-distance differences can require more detail. Lane groups are not
necessarily physically homogeneous merely because they share a continuation.

**Pros:** directly tied to the lane-reduction task; does not first require
identifying persistent response classes; uses inspectable endogenous structures
without per-vehicle dynamics or commanded lane changes.

**Cons:** a calibrated homogeneous bottleneck may already reproduce useful
decisions; transfer/response calibration and continuous branch fidelity remain
real burdens; better lane prediction may not alter the preferred advice.

**Dependencies/scientific consequence:** shared strong baseline/evaluator
contract, reachable matched contrasts and gradient checks. Testing lane
information without fixed response classes is a proposed refinement of the
working G2/G5 inventory, not an approved replacement for the frozen B2 wording.
No urban ledger/FIFO design is assumed. A continuous multi-lane model is often
called macroscopic in this literature; the contribution must be about retained
information and useful sensitivity, not the 'mesoscopic' label.

## 3. Candidate 2 — response composition positioned across merging lanes

**Task.** The same advice control task, but investigate whether knowing which
fixed response groups occupy ending versus continuing lanes changes decisions.

**Assumed model-chain function.** Shared advice → group-specific realized
response → lane-dependent arrival and transfer pressure → feasible discharge
and delay. A lane-by-response-group mass table retains the association between
response and lane location; group weights are not sampled or reselected by advice.

**Diagnostic hypothesis/core gap.** Where feasible, contrast scenarios with
the same lane totals and same overall response-group totals but different
lane–response associations. This isolates information discarded by retaining
only either set of marginal totals. Response parameters and aggregate observed
speeds/histories must also be controlled or explicitly accounted for. The
literature reviewed motivates response and lane effects separately; it does
not establish that this joint association is necessary for advisory ranking.
No such contrast has been constructed or run.

**Literature/adaptation boundary.** FB0026 supports calibrated mean response;
FB0005/33 provide advisory/work-zone response evidence; FB0004 has lane/class
state but an all-CAV car/truck population and commanded transfers. None is a
ready-made validated fixed human-response-group/lane model for our task.
The class-response and class-preserving transfer closure remains to be justified.

**Pros:** explains why the original lane-and-response-group candidate retains
joint information; can isolate a genuine information-loss mechanism if the
association matters beyond calibrated mean response and lane totals.

**Cons:** substantially greater identification/coupling burden; persistent
membership and deterministic group closure may be inadequate; separate response
or lane models may suffice. Full B2-first construction is not justified now.

**Dependencies/scientific consequence:** viable fixed response laws/population
support and a fair one-axis-versus-joint-information attribution. A homogeneous
lane-resolved intermediate may be needed to avoid confusing lane benefit with
response-class benefit. That intermediate is a candidate comparison, not a
new implementation authorization or approved four-model ladder.

**Provisional priority:** Candidate1 is the simpler initial diagnostic
motivation; Candidate2 is conditional on evidence that mean-response plus lane
information cannot explain the decision effect. This is a recommendation for
refinement priority, not selection of exact equations or a result that classes
are unnecessary. A strong response-only contrast could change the priority.

## 4. What 'minimum information' can mean now

There are three different questions:

1. **Minimum to distinguish a chosen behavior:** a link-total-only state cannot
   distinguish two scenarios that differ only in a discarded lane allocation.
   Lane occupancy is therefore required to represent that distinction in the
   candidate state (or a justified equivalent sufficient statistic). This is
   an information argument, not proof the distinction changes control.
2. **Smallest plausible dynamical closure:** lane partition, local spatial
   occupancy/storage, donor/receiver-constrained transfer, continuation metadata,
   and sufficient speed-response/history. This is a supported candidate family,
   not a proved exact number of states or lanes/classes.
3. **Minimum for useful independent sensitivity:** establish whether removing
   those states changes feasible rankings or downstream improvement after
   controlling baseline response/calibration. This is the research outcome.

For Candidate2, marginal lane totals and marginal class totals generally do
not reconstruct their association; a joint table or demonstrably adequate
compressed statistic is the candidate extra information. Its necessity for
control still must be tested.

An alternative effective merge-pressure state may compress lane densities,
but only if its closed dynamics can be justified across the chosen scenarios;
calling it a smaller state does not guarantee it is sufficient. Conversely,
traffic-resolution detail already represented by a strong baseline should
not be counted again as a novel refinement.

## 5. Native differentiation without probability shifts

The plausible route uses continuous veh-equivalent mass and deterministic
conservative fluxes, with fixed structural metadata. Advice changes speeds
and flux magnitudes, not class membership, categorical draws, lane topology,
vehicle integer counts or optimized closure-event times. Continuous traffic
moving between lanes is physical transport, not a random categorical process
with control-dependent probability mass.

With a valid deterministic update, differentiation follows advice → response →
longitudinal/lateral flux → subsequent state → objective. No smooth surrogate,
random-choice gradient estimator or hybrid reset correction is assumed.
Continuous min/max operations can be differentiated piecewise away from their
boundaries; boundary and one-sided fidelity still require checks. A published
model being differentiable almost everywhere is not enough to establish this
whole chain or external usefulness.

Crucially, the complete FB0030 scheme has empty-density denominators, a special
lateral branch and capacity/mode switches flagged in the source study.
It is not certified native-AD-ready. Any adaptation/repair needs explicit later
approval; arbitrary smoothing or bypassing a necessary sensitivity is not
allowed. Fixed exogenous closure times do not have advice-dependent event-time
derivatives, but control-dependent traffic thresholds still require scrutiny.
No Gap7 exception has been justified.

## 6. What to decide at N2-UG1

**Problem statement:** is the identified mechanism/gap worth a bounded next
investigation, and which scope/burden should it have?

**Assumed model-chain function:** choose an evidence target and limits for
the next review/design pass, before selecting the final differentiated traffic
system. Shared advice and independently useful sensitivity remain the target.

**Core gap:** minimum state, decision relevance and common calibrated evaluator
are not established. The user cannot close these by declaration; the next pass
must supply candidate contracts or return with the finite missing evidence.

The gate's existing alternatives remain:

- **Route B, recommended:** refine Candidate1's omitted-lane-information contrast
  and strong baseline/common evaluator contract, with Candidate2 conditional.
  **Pros:** finite, mechanism-specific and lower initial complexity.
  **Cons:** may end without a viable task or require a separately planned
  diagnostic. **Dependency:** a new short plan; no experiments implicitly approved.
- **Route A1:** knowingly pursue the fixed-response-group-first hypothesis,
  lane refinement conditional. **Pros:** coherent nested response investigation.
  **Cons:** identification/necessity less well established than generic response
  relevance. **Dependency:** detailed evidence/design plan; classes remain a
  hypothesis, not a gate-approved minimum.
- **Route A2:** choose a narrower aggregate-sufficiency study and one meaningful
  challenge. **Pros:** lower scope and informative negative outcomes.
  **Cons:** a domain/contrast is still needed to distinguish it from already
  established aggregate success. **Dependency:** approve that scientific question
  and later sufficiency/failure acceptance logic.
- **Route C:** defer. **Pros:** avoids speculative construction/calibration cost.
  **Cons:** leaves the qualified opportunity untested. **Dependency:** record
  an evidence/cost decision, not proof of impossibility or prior coverage.

The substantive choice has three parts: (a) which phenomenon/omitted information
deserves investigation, (b) whether a candidate diagnostic is enough to justify
further work despite unproved necessity, and (c) the acceptable next-step scope
and stop conditions. Selecting a route need not decide class counts, transfer
equations, exact partitions, calibration tolerances or estimator methods now.

**Recommendation:** keep Route B, but make its deliverable concrete: a task–
mechanism–retained-information candidate and strong common-contract screen,
not another generic literature-gap summary. Prefer lane merge-pressure as
the starting hypothesis without requiring response classes first. If review
cannot establish a fair credible contrast, return for deferral or a separately
approved diagnostic; do not indefinitely continue reviewing or construct B2
by assumption. All priorities remain unapproved.

## 7. Work record

Changed this response, the living N2 gate and gap inventory, plus phase dialogue.
Reused inspected source studies; primary university PDFs re-opened for method
support, with no new technical result or search campaign. Tools: rg/sed/tail,
git status, primary web opens, apply_patch, read-only document checks. No source,
tests, configs, environment, feedback or closed packages edited. No numerical
experiment or code test applies. Scope assumption: 'B2 task' refers to variants
of accepted F1, not a new actuator/task. Main uncertainty remains matched
decision relevance and native differentiated closure/evaluator fidelity.
Current status N2-UG1 discussion; next allowed action is user route/scope decision
or further clarification, then a separately approved plan—not execution now.
