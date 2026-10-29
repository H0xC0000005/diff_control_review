# S12.00 — Analytical advice–merge–service admission review proposal

Date: 2026-09-30. Status: **Closed; G4-A approved and AMR-A accepted.**
Parent: [S11 closure](reporting/s11/s11_99_temporary_closure_recovery_sprint_closure.md)
and [approved post-closure ordering](synthesis/s10/s10_post_closure_next_step_plan.md).
Branch lineage: S05/DG-R2 Candidate B → S10/DG-R7 Candidate B → approved Step 2.

## Decision and scope of this proposal

S11 closed temporary-closure recovery at task admission because the inspected
sources did not jointly support the reopening-specific state-to-service and
strong-observer links. That stopping reason does not invalidate the analytical
branch: S12 would ask openly whether a conservative source-bounded model class
can contain the missing advice-dependent merge/service coupling.

S12 is a **lightweight methodology/model-admission review**. Approval would
authorize source reuse, bounded missing-link search and logical/structural
screening through S12-UG1 / AMR-R1. It would not authorize a full equation set,
parameter selection, analytical certificate derivation, implementation,
simulation, SUMO, calibration, optimization or gradient computation.

## Scientific purpose

The S05 obstruction showed that a hidden lane contrast plus advice-independent
work-conserving service does not make slower advice useful when a fastest action
dominates arrivals. The missing path is:

`common lane-uniform advice → lane/gap/merge evolution → endogenous receiving or
service → complete-accounting action distinction`.

S12 will decide whether at least one source-supported conservative mechanism
family can make that path structurally possible without choosing coefficients or
branches because they produce the desired result.

The admission question is:

> Is there a source-supported conservative merge/receiving/service mechanism
> class, compatible with common lane-uniform VSL at a permanent lane drop and the
> exact strong-history information target, that can escape the S05 fixed-service
> arrival-dominance obstruction without a favorable parameter choice?

## Verified starting point

These findings are inputs, not claims to rediscover:

1. **Information-side possibility is conditional.** S05 constructs equal strong
   aggregate histories with different lane allocations in a homogeneous
   conservative free-flow subcase. It does not establish a consequential
   near-drop collision in native traffic.
2. **Fixed service is insufficient.** If service is action-independent and one
   feasible advice makes cumulative arrivals no later for every hidden state,
   that action is a common best action under complete all-cohort accounting.
3. **Mechanism evidence exists but is fragmented.** S06 and S11 support
   lane-distribution response to speed control, gap/relaxation effects,
   lane-changing disturbances, spatial merging and transient discharge. They do
   not supply the full common-advice analytical closure.
4. **Strong aggregate models remain competitors.** Aggregate capacity-drop,
   hysteresis, queue/storage and recovery models can already make service
   state-dependent. A mechanism does not justify hidden lane state if its relevant
   state is recoverable from aggregate density, flow, speed and history.
5. **Actuator transfer is restricted.** Benefits from direct lateral-flow,
   lane-specific speed, ramp-metering or vehicle-trajectory control cannot be
   attributed to the common infrastructure VSL.
6. **Decision evidence precedes gradients.** A differentiable closure or finite
   derivative cannot substitute for a supported action distinction.

## Fixed contracts inherited by S12

- The domain returns to the closed permanent three-to-two freeway lane drop; S12
  does not continue the temporary-reopening geometry.
- The actuator is upstream lane-uniform infrastructure speed advice. Lane-
  specific limits, commanded lane changes, direct vehicle actuation and ramp
  metering are excluded.
- The information claim remains intrinsic: compared preparations provide the
  same declared strong spatial aggregate state and full predecision history.
- Total demand, route population, geometry, future forcing and feasible action
  set are common. Unknown lane allocation may not hide changes in total input.
- Traffic mass, lateral transfers and node flows must be conservative. No mass
  may be dropped to create a service benefit.
- Full affected-cohort time/delay supplies the decision-level accounting
  reference. Clearance, discharge, queue and lane-change measures are supporting
  diagnostics/guardrails rather than substitutes for complete accounting.
- A mechanism is not admitted by fitting a coefficient, selecting a branch or
  excluding the fastest feasible action after observing the desired ranking.
- Forward relevance, decision relevance, derivative correctness and downstream
  gradient usefulness remain separate claims.

## Explicit non-goals

S12 will not adopt numerical geometry, an action menu, parameter bounds,
smoothing, capacity values, lateral-transfer rates, tolerances or terminal time.
It will not prove a matched-history pair, choose a minimum state, derive a full
certificate, reproduce a paper, calculate a gradient or claim field validity. It
will not reopen the approximate-observer claim or the closed S11 recovery result.

## Question inventory and ownership

The four questions below are Type 2 milestone-global contracts because they
control the task domain, eligible mechanism class, information meaning and pass
standard. Local source extraction and logical checks cannot alter them. The
closure order is AMR-G1 → G2 → G3 → G4.

Local review work is divided into:

- **AMR-C1:** source/method extraction for mechanism families;
- **AMR-C2:** conservation, monotonicity, units and state-dependence audit;
- **AMR-C3:** S05 obstruction and aggregate-equivalence audit; and
- **AMR-C4:** derivative-boundary classification.

If local work conflicts with a global contract, S12 must reopen the smallest
AMR-G question rather than repair the mechanism locally.

### AMR-G1 — Which domain does the analytical screen describe?

**Problem statement:** The branch could return to the permanent lane drop that
created the S05 obstruction, carry the temporary closure into the analytical
model, or use an abstract merge with no fixed geometry. These choices answer
different questions.

**Assumed model-chain function:** A lane-ending region creates mandatory merging.
Common upstream advice can change arrivals and preparation; a candidate mechanism
may make realized receiving/service depend on the evolving lane-resolved state.

**Core gap:** Candidate B was created as the analytical sibling of the permanent-
drop review. Carrying S11's reopening into it would mix two branches and make the
analytical result depend on a recently closed evidence gap.

**Candidate A — permanent three-to-two lane drop (provisional recommendation).**
Return to the original fixed lane-drop topology and analyze only the smallest
near-drop merge/service mechanism.

**Pros:** Directly tests the S05 obstruction, preserves branch lineage and avoids
a time-varying topology. Existing lane-drop, lateral-flow and VSL sources are
most relevant here.

**Cons:** The permanent-drop literature reviewed through S10 did not already
establish necessity of lane contrast. A new analytical result remains
conditional on its model class.

**Dependencies/consequences:** S11 recovery findings remain reusable mechanism
context but do not define the domain. A passing S12 screen would plan a new
analytical contract, not reopen S05's old derivation silently.

**Candidate B — temporary obstruction and reopening.** Build the analytical
mechanism around S11's three-to-two-to-three event.

**Pros:** Could target transient service where lane/gap/order effects may be most
visible.

**Cons:** S11 closed because the reopening-specific join lacked support. Using it
here would confound the analytical branch with that unresolved transfer and add a
hybrid event unnecessarily.

**Dependencies/consequences:** Would reopen S11 scope and require a different
successor plan.

**Candidate C — geometry-free abstract merge.** Screen a generic two-stream
receiving/service operator without a specific lane drop.

**Pros:** Analytically compact and may expose general monotonicity conditions.

**Cons:** Weakens operational meaning and can hide whether common VSL can reach
the modeled inputs. A positive abstract result may not transfer to a lane drop.

**Dependencies/consequences:** Any later traffic interpretation would require a
separate geometry/actuator mapping review.

### AMR-G2 — How should mechanism families be screened?

**Problem statement:** Selecting one favored equation now risks engineering the
desired action split; screening every conceivable interaction would be unbounded.

**Assumed model-chain function:** An eligible mechanism accepts conservative
lane-resolved traffic state and common-advice-induced evolution, then limits or
redistributes receiving/service according to source-supported traffic behavior.
It cannot take the desired action label or outcome ranking as an input.

**Core gap:** Existing sources support neighboring mechanisms under different
actuators and contexts. The review needs a bounded family inventory and common
eligibility tests before choosing any model contract.

**Candidate A — screen a bounded mechanism portfolio under common structural
tests (provisional recommendation).** Evaluate:

1. lane-change anticipation/relaxation or gap-created voids affecting discharge;
2. spatially distributed mandatory merging and continuing-lane imbalance;
3. finite receiving/storage or spillback that couples preparation to service;
4. aggregate capacity-drop/hysteresis as a countercandidate that may erase the
   need for hidden lane state.

For every family require conservation, work-conserving limits, compatible units,
common-advice reachability, hidden-state dependence beyond the strong observer,
and no outcome-selected sign.

**Pros:** Tests the plausible mechanisms already exposed by S05–S11 without
preselecting a winner. The aggregate countercandidate prevents lane detail from
being admitted merely because a state-dependent capacity law helps.

**Cons:** The screen may end with multiple partially viable families rather than
one clear contract. Source transfer across studies must remain qualified.

**Dependencies/consequences:** A materially distinct source-supported family may
be added with the same tests and recorded rationale. A passing family returns to
a user gate before equations.

**Candidate B — preselect lane-change gap/relaxation service.** Focus only on
relational gaps, anticipation and relaxation as the missing service mechanism.

**Pros:** Closest to S11's microscopic state-to-discharge evidence and to the
project's selective semantic-order hypothesis.

**Cons:** Direct evidence is strongest at active merges/bottlenecks, not the exact
common-VSL matched-history case. Preselection risks treating plausible micro
behavior as necessary lane state.

**Dependencies/consequences:** Requires a later state representation capable of
retaining the approved relational variables without microscopic vehicle dynamics.

**Candidate C — preselect an aggregate capacity-drop/hysteresis law.** Let advice
change whether or how the aggregate bottleneck enters a lower-service regime.

**Pros:** Strong literature precedent, compact state and a direct route around
advice-independent fixed service.

**Cons:** It may answer a standard aggregate VSL question and provide no hidden-
information contribution. Hard switches can create nonsmooth derivatives.

**Dependencies/consequences:** If strong aggregate history supplies all required
state, S12 should close the resolution branch rather than relabel the law as
mesoscopic.

### AMR-G3 — What information claim must a mechanism preserve?

**Problem statement:** A state-dependent service law can create different actions
while still being fully reconstructible by the strong aggregate observer. That
would escape fixed service but not answer the core hidden-information question.

**Assumed model-chain function:** The candidate mechanism may use lane/gap/order
state only if that state can differ under the same declared aggregate history and
has an independent effect on advice-dependent service.

**Core gap:** S05 proved an information collision only in a homogeneous early
free-flow subcase; S06–S11 did not prove a consequential near-drop collision.
S12 cannot assume that a mechanism's state is hidden merely because it is
lane-indexed.

**Candidate A — retain the exact strong-history target and require an observer-
separation argument (provisional recommendation).** At admission, require a
coherent reason the mechanism depends on variables not reducible to aggregate
queue, density, flow, speed, cumulative counts and their full history. Do not
claim an exact pair yet.

**Pros:** Preserves the intrinsic research question and the accepted comparator.
It distinguishes a useful aggregate capacity model from a resolution-dependent
mechanism.

**Cons:** Many viable service models may fail this screen. A coherent separation
argument remains weaker than a later exact construction.

**Dependencies/consequences:** A passing full analytical plan would still need a
reachable matched-history witness. Failure may establish only aggregate-
equivalence for the screened family.

**Candidate B — change to performance against one approximate aggregate model.**
Admit a mechanism if it improves over a specified fitted aggregate closure.

**Pros:** Easier to evaluate and potentially useful in practice.

**Cons:** Reopens the research claim, introduces fitting/fairness choices and can
manufacture value through a weak comparator.

**Dependencies/consequences:** This is DG-R1 Candidate B, not the currently
opened DG-R2 analytical branch, and would require separate approval.

### AMR-G4 — What is enough to pass the lightweight screen?

**Problem statement:** Mere physical plausibility is too weak, while requiring the
full analytical certificate now would skip the intended model-admission gate.

**Assumed model-chain function:** A passing family must provide a conservative,
source-bounded route by which common advice changes endogenous service and must
not collapse to the S05 fixed-service or strong-aggregate cases.

**Core gap:** No numerical parameters or full equations are approved. The screen
needs to decide structural viability without proving the later result or choosing
a favorable coefficient range.

**Candidate A — require a source-bounded function class plus a coefficient-
independent structural escape (provisional recommendation).** The review must
identify admissible inputs/outputs and invariants, explain which S05 premise is
broken, and show that the mechanism can in principle produce state-dependent
action response over a nonempty ordinary regime. The argument may use
monotonicity, limiting cases or sign-indefinite alternatives, but may not depend
on one fitted favorable coefficient. It must also state an aggregate-equivalent
limit and falsification conditions.

**Pros:** Stronger than a mechanism list and weaker than a full certificate. It
makes later equations reviewable and lets an obstruction close the branch early.

**Cons:** Some traffic mechanisms may be too empirical or high-dimensional for a
coefficient-independent screen. Passing remains conditional and does not prove a
useful action split.

**Dependencies/consequences:** A pass returns for approval of a full analytical
model contract and derivation plan. A fail closes Candidate B with a typed reason.

**Candidate B — require the full conditional certificate in S12.** Freeze
specific equations and prove a matched-history useful-action split now.

**Pros:** Would give a decisive analytical result and avoid another planning
stage.

**Cons:** Exceeds the approved lightweight first stage and invites premature
parameter/equation choices before mechanism admission.

**Dependencies/consequences:** Requires explicit authorization for a larger,
formula-heavy analytical sprint.

**Candidate C — admit any plausible source-supported mechanism.** Pass if sources
show that lane changes, gaps or spillback can affect service somewhere.

**Pros:** Low-cost and inclusive of uncertain mechanisms.

**Cons:** S05–S11 already establish that level of plausibility. It would not test
whether the mechanism is reachable by common advice, hidden from the strong
observer or capable of escaping arrival dominance.

**Dependencies/consequences:** Would repeat prior findings and provide no safe
basis for a full analytical contract.

## Bounded review method

1. Reconstruct the S05 information lemma and fixed-service obstruction, the S06
   mechanism inventory, S10 Candidate B boundary and S11 source/observer result.
2. Reuse FB0001, FB0030, FB0038, FB0039, FB0040, S06-S1/S2/S3 and S11-S1–S4
   before new discovery. Search only for a missing conservative common-VSL
   merge/receiving/service class or a decisive aggregate-equivalence result.
3. Build a mechanism-family table recording traffic meaning, state, control path,
   inputs/outputs, units, conservation, receiving/storage limits, monotonicity,
   aggregate limit, evidence level and actuator transfer.
4. For each family, trace
   `advice → realized approach/lane evolution → receiving/service → complete
   outcome`; mark every link as direct evidence, conditional deduction or absent.
5. Reapply the S05 obstruction. State whether the family breaks arrival dominance,
   makes service endogenously action-dependent, or merely renames a fixed
   capacity. Include the fastest feasible action in the logical dominance check.
6. Audit observer separation. Reject a resolution claim if aggregate state and
   full history contain all variables required by the mechanism.
7. Classify the prospective derivative regime—smooth, fixed-active-set,
   nonsmooth/hybrid or structurally discrete—without deriving a gradient.
8. Assign an S12 verdict and stop at S12-UG1 / AMR-R1.

## Admission criteria and verdicts

The branch is admitted for a later full analytical model contract only if one
mechanism family satisfies all of these conditions:

1. direct or carefully bounded primary-source support for the traffic mechanism;
2. compatibility with a permanent lane drop and common lane-uniform VSL;
3. conservative mass transfer and physically bounded receiving/service;
4. a non-circular advice-to-service path that breaks a stated S05 premise;
5. a coherent hidden-state dependence not already exhausted by the strong
   aggregate history;
6. a nonempty structural regime not defined by choosing favorable coefficients;
7. complete decision accounting and a strongest-action dominance check; and
8. a classifiable derivative boundary without claiming gradient usefulness.

The findings must assign one verdict:

- **AMR-A — admit:** one mechanism family passes; return for approval of a full
  analytical model/derivation plan.
- **AMR-B — aggregate-equivalent:** a viable advice-dependent service mechanism
  exists, but its consequential state is recoverable by the strong aggregate
  observer; close the hidden-resolution branch for that family.
- **AMR-C — actuator mismatch:** the mechanism requires lane-specific, lateral,
  ramp or direct-vehicle control; close it for common VSL.
- **AMR-D — monotonic obstruction:** every admissible screened family retains
  arrival dominance or an equivalent common-best-action result.
- **AMR-E — evidence inconclusive:** no family can be admitted or ruled out from
  the bounded sources; record the smallest missing evidence.
- **AMR-F — multiple viable families:** more than one family passes but selecting
  among them changes model meaning; return the smallest candidate comparison for
  user choice before equations.

## Planned outputs

If approved, S12 will produce:

- `extraction/s12_advice_merge_service_source_audit.md`;
- `synthesis/s12/s12_mechanism_admission_matrix.md`;
- search/access logs only if new discovery is needed;
- `reporting/s12/s12_20_advice_merge_service_findings_and_gate.md`;
- `reporting/s12/s12_90_advice_merge_service_work_report.md`; and
- synchronized sequence, registry and decision records.

If the structural screen needs multiple formulas or a substantial derivation, the
mathematical explanation will be rendered as LaTeX/PDF under `synthesis/s12/`.
That artifact would remain an admission analysis, not the unapproved full
certificate.

## Stop conditions

Stop before ordinary findings only for a decision-critical inaccessible source,
a contradiction in the inherited S05 obstruction, or evidence that every viable
mechanism requires an excluded actuator. At the ordinary endpoint, stop at
S12-UG1 / AMR-R1 for all verdicts. Do not draft the full analytical contract,
start Candidate B derivation, reopen ramp metering or start S13 automatically.

## S12-PG1 — Plan approval

The provisional recommendation is the complete Candidate A set:

- G1-A: permanent three-to-two lane drop;
- G2-A: bounded mechanism portfolio under common structural tests;
- G3-A: exact strong-history target with observer-separation audit; and
- G4-A: source-bounded class plus coefficient-independent structural escape.

Approval authorizes only the lightweight review through S12-UG1 / AMR-R1.
Changes to the domain, mechanism eligibility, information claim or pass threshold
require explicit reopening of the smallest affected global decision.

## Approval and execution record

The user approved **G1-A**, **G2-A** and **G3-A** on 2026-09-30 and instructed
execution of the bounded S12 plan. The final G4 choice remains deliberately
deferred until the completed evidence screen. G4-A was therefore used only as
the working assessment standard; it is not yet a closed global decision.

The source audit and structural screen are complete. The provisional result
under working G4-A is **AMR-A — admit one bounded family for a later analytical
model-contract/derivation plan**. The admitted family is conservative per-lane
flow with endogenous mandatory lateral demand, finite target-lane receiving and
a gap-acceptance cost. This result admits a function class; it does not prove an
exact matched-history useful-action split.

## User decision and closure

The user approved **G4-A**, accepted AMR-A as the bounded S12 result and directed
proper closure. The user also inserted a targeted M2 continuation, S13, before
the planned ramp-metering review.

S12 therefore closes with one admitted analytical family and no claim that the
exact strong-history action distinction is proved. See the
[S12 closure](reporting/s12/s12_99_advice_merge_service_sprint_closure.md).
S13 is opened only at its planning gate; no equation contract, derivation,
implementation or experiment has started.
