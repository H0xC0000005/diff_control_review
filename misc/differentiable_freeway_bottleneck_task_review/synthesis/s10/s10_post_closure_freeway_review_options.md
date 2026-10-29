# S10 annex — Post-closure freeway review options

Date: 2026-09-30. Status: **successor portfolio; Option 3 selected as the first
planned successor, but no successor review is open.** Parent:
[S10 closure](../../reporting/s10/s10_99_vsl_methodology_review_closure.md).

## Purpose and boundary

This annex lists four review directions beyond the already proposed lightweight
DG-R7 Candidate B and the new ramp-metering task review. It uses the current
findings instead of restarting the search: strong aggregate history is the fair
baseline; hidden lane occupancy is only a marker for a bundle of lane, gap,
order and lane-change-memory differences; fixed service plus arrival dominance
blocks the simplest VSL certificate; and gradient correctness, decision value
and minimum retained state require separate evidence.

“Evade negative results” is interpreted as avoiding routes already shown to be
weak, redundant or structurally blocked. Every option below still admits a
negative finding. Its first gate is designed to make that negative result early,
bounded and informative rather than burying it in model construction.

## Option 1 — Minimal-observation value review under the existing VSL action

**Problem statement:** Instead of trying first to prove that lane contrast is
intrinsically necessary, ask whether one small, operationally observable addition
to a strong lane-blind history changes VSL action ranking or reduces worst-case
decision regret.

**Assumed model-chain function:** A strong aggregate response/history observer is
the baseline. It receives, one at a time, a compact candidate observation such as
ending-lane share, continuing-lane imbalance, a lane-resolved occupancy moment or
a local merge-opportunity index. The review traces how that observation could
affect prediction, common-advice choice and later gradient evaluation.

**Core gap:** The current work identifies candidate hidden contrasts but does not
show which statistic is measurable, adds information beyond full aggregate
history, or changes a control decision. Adding a statistic also cannot by itself
establish that lane-resolved state is universally necessary.

**Pros:** This is the smallest post-closure change; it reuses the VSL task,
observer boundary, all-demand accounting and candidate-state work. It can deliver
a useful sufficiency/value claim even if an exact information-collision proof is
too brittle. It gives a direct admission test for any later candidate model.

**Cons:** The conclusion is sensor- and observer-specific. A positive result can
show incremental value, not irreducible necessity or minimality; a poorly chosen
statistic can encode the desired answer or duplicate information already present
in history.

**Dependencies and first gate:** Freeze one measurable statistic, a strong
baseline observer and an outcome-independent selection rule. Stop if the statistic
cannot be obtained without changing the actuator, using future information or
embedding the evaluation outcome. If admitted, the next review compares
information value before discussing a differentiable representation.

## Option 2 — Robust VSL review under a set of hidden states

**Problem statement:** Ask whether a common VSL decision based on the declared
aggregate history remains acceptable for every plausible lane/gap/order state
consistent with that history, rather than requiring one exact matched pair to
carry the full necessity claim.

**Assumed model-chain function:** The aggregate history defines an uncertainty
set of admissible hidden states. A controller chooses one common action; the
review evaluates worst-case or regret-bounded performance and asks whether a
compact refinement shrinks the decision-relevant uncertainty. Gradients would be
assessed later as robust feasible directions, separate from ordinary derivatives
inside one selected state.

**Core gap:** No defensible uncertainty set, probability law or non-vacuous regret
threshold has been established. If the set is chosen freely, almost any desired
need for extra state can be manufactured.

**Pros:** It turns the present observability ambiguity into the subject of the
review and remains useful when exact native history collisions are rare. Both a
robust common action and a failure of robustness are informative outcomes. It
also tests the strongest aggregate alternative directly.

**Cons:** Results depend on the state-set construction and may be conservative.
This route establishes robustness for a declared envelope, not universal lane-
state necessity. Nonsmooth worst-case selection complicates any later gradient
claim.

**Dependencies and first gate:** Derive the hidden-state envelope from physical
constraints, source evidence and the fixed observer boundary before evaluating
actions. Stop if the envelope is arbitrary, contains physically unreachable
states, or makes every action fail trivially. Keep robust decision value distinct
from the exact-information claim.

## Option 3 — Temporary lane-closure recovery review with VSL

**Problem statement:** Reopen the retained F4 scenario dimension and ask whether
the lane/gap/order configuration present when a temporary lane reopens changes
queue dissipation and the useful upstream VSL response under the same aggregate
history.

**Assumed model-chain function:** Closure and reopening times are fixed exogenous
events. VSL affects arrivals and lane preparation before reopening; the hidden
near-zone configuration affects discharge and recovery afterward. Outcomes cover
all cohorts and terminal queues. The [FHWA incident-recovery guidance](https://ops.fhwa.dot.gov/publications/fhwahop08059/30.htm)
supports treating queue dissipation after reopening as an operationally distinct
phase, while [FHWA work-zone guidance](https://ops.fhwa.dot.gov/wz/traffic_mgmt/wzsm.htm)
supports VSL around lane closures; neither source proves the proposed hidden-state
or gradient claim.

**Core gap:** The current permanent 3-to-2 case removes the time-varying recovery
mechanism. No reviewed evidence yet shows that two admissible configurations with
the same strong aggregate history clear differently enough to alter useful VSL.

**Pros:** This preserves the VSL actuator while adding a mechanism that escapes
the permanent fixed-service obstruction. It uses the already retained recovery
scenario rather than inventing a new task and gives physical meaning to terminal
queue accounting.

**Cons:** Reopening creates a hybrid event and can confound representation effects
with timing, capacity jumps and demand transients. Gradients near event boundaries
may be discontinuous or unstable, and field calibration would be a later task.

**Dependencies and first gate:** Fix the closure schedule independently of VSL,
define the recovery objective and identify a source-supported state-to-discharge
mechanism. Stop if the only behavioral difference comes from unequal aggregate
queues, different reopening times or an assumed favorable capacity term. A passed
gate should return for approval before a full protocol is drafted.

## Option 4 — Safety/feasibility-sensitive VSL review near a merge or lane drop

**Problem statement:** Ask whether hidden gap/order/lane state changes the
feasibility margin of a VSL action even when aggregate travel-time ranking is not
shown to reverse. The target becomes a control-relevant safety or merge-feasibility
constraint and its sensitivity.

**Assumed model-chain function:** A shared upstream VSL changes arrival speed and
gap formation; a richer reference supplies lane/gap/order-resolved feasibility;
the controller minimizes delay subject to a fixed safety or merge-service
constraint. The later gradient question is whether the aggregate gradient gives
a correct feasible direction, not merely whether an unconstrained objective has
a finite derivative. Safety-constrained freeway analyses show why merge release
and usable gaps can restrict throughput ([Pooladsanj, Savla and Ioannou, 2022](https://arxiv.org/abs/2207.02360);
[2023 network extension](https://arxiv.org/abs/2303.06569)), but those ramp-metering
models do not establish a VSL-specific result.

**Core gap:** No continuous, forward-faithful safety/feasibility quantity has been
accepted for the current VSL task, and a microscopic surrogate may introduce more
state than the proposed mesoscopic refinement can support.

**Pros:** Constraint activity can reveal decision-relevant hidden information
without demanding a travel-time ranking reversal. It creates a precise place for
lane/gap/order state and separates feasible-direction quality from raw objective
gradient correctness. It can also inform, without duplicating, a later ramp-
metering admission review.

**Cons:** This is the largest semantic shift of the four. Hybrid gap acceptance,
collision indicators or minimum-headway constraints may be nondifferentiable;
over-smoothed safety metrics can lose physical meaning. Direct vehicle trajectory
or lane-change control would change the actuator and require a separate task.

**Dependencies and first gate:** Fix a source-supported safety/feasibility
contract, its observation boundary and an independent richer-reference check.
Stop if no meaningful continuous margin or feasible-direction test can be defined
without microscopic control, favorable smoothing or future information.

## Rough portfolio recommendation

Choose **Option 1** when the priority is maximum reuse and the smallest claim
change. It directly tests whether a compact observation earns its place before
any new model is formulated. Choose **Option 2** when the practical concern is
safe decision-making under incomplete state rather than a universal necessity
proof. Choose **Option 3** when keeping VSL is essential but a stronger endogenous
service mechanism is needed. Choose **Option 4** only when constraint-sensitive
control is scientifically central enough to justify a broader task contract.

Do not schedule all four as a serial program. After current closure, select one
admission review. The provisional order by scope and reuse is **1 → 2 → 3 → 4**;
the order by likelihood of exposing a stronger physical lane/gap mechanism is
**3 → 4 → 1 → 2**. A failed admission gate closes that branch without being
interpreted as aggregate sufficiency or as failure of the overall research
question.

**Feedback 25 decision:** Option 3 is the first planned successor because it
preserves the VSL actuator while adding a stronger physical recovery mechanism.
If it does not establish the information-to-decision link, the lightweight
analytical advice–merge–service screen follows only when the recorded failure
mode leaves that mechanism meaningful. Ramp metering is the third task-admission
branch. The detailed [next-step plan](s10_post_closure_next_step_plan.md) governs
these transitions. This decision selects an ordering, not execution.
