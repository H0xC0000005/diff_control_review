# S13.00 — Targeted M2 analytical contract and certificate review proposal

Date: 2026-09-30. Status: **Closed 2026-10-01 with M2C-A accepted.**
Parent: [S12 closure](reporting/s12/s12_99_advice_merge_service_sprint_closure.md).
Sequence position: inserted after S12 and before ramp-metering task admission by
explicit user decision.

## Decision and scope of this proposal

S12 admitted M2 as a source-bounded conservative model family that can escape
the S05 fixed-service obstruction. It did not freeze M2's equations or establish
the exact information-to-decision result.

S13 would be a **methodology-only analytical contract and certificate review**.
Approval would authorize targeted source-to-equation work, formal model
specification, exact analytical construction or obstruction, and conceptual
gradient-path classification through S13-UG1 / M2C-R1. It would not authorize
implementation, simulation, SUMO, calibration, numerical traffic experiments,
optimization or automatic differentiation.

## Scientific purpose

The main S13 question is:

> Within the admitted M2 family, can two reachable preparations with identical
> declared strong aggregate histories require different useful common lane-
> uniform VSL actions because hidden lane state changes mandatory-transfer and
> finite-receiving service under complete accounting?

If the answer is positive, S13 should also state the general differentiability
path and its active-set boundaries. If the decision distinction fails, S13 must
return the smallest typed reason rather than change the observer, action set,
accounting or parameter class.

## Verified starting point

These are inherited findings, not claims to rediscover:

1. **S05 information possibility:** conservative lane transfers can cancel from
   aggregate totals in a homogeneous free-flow preparation, allowing different
   lane allocations under the same strong aggregate prefix.
2. **S05 obstruction:** if the fastest advice dominates arrivals and service is
   advice-independent and work-conserving, complete accounting gives one common
   best fastest action.
3. **S12 M2 admission:** conservative per-lane mandatory transfer, finite target
   receiving and an extra lane-change gap cost supply a source-bounded way for
   lane state to affect realized service.
4. **Common-VSL qualification:** related lane-drop/merge evidence supports
   lane-preparation response, but no inspected source supplies the entire M2
   VSL-response law.
5. **Strong aggregate competitor:** aggregate VSL/capacity-drop models can make
   service state-dependent without hidden lane state.
6. **Decision before gradients:** no derivative or useful-gradient claim is
   available until an information-dependent action distinction is established.

## Fixed inherited contracts

- Geometry is a permanent three-to-two freeway lane drop.
- The only action is upstream lane-uniform infrastructure speed advice. There is
  no lane-specific speed, commanded lateral flow, ramp metering or direct vehicle
  actuation.
- Traffic quantity is continuous vehicle-equivalent mass. Lateral transfer is
  paired and conservative.
- Lane topology and permissions are structural metadata.
- Compared preparations must have the same total demand, routes, geometry,
  future forcing, feasible action family and declared full predecision strong
  aggregate history.
- The observer contains spatial aggregate density, flow, speed, cumulative
  counts and their complete declared history, but no lane decomposition.
- Complete affected-cohort time/delay through common clearance is the decision
  reference, including source/approach waiting and residual demand.
- The fastest feasible action must remain in the comparison.
- Aggregate-equivalent and null action results are valid outcomes and may not be
  tuned away.

## Explicit non-goals

S13 will not fit field parameters, select geometry numerically, reproduce a
paper, implement a simulator, run traffic, claim empirical validity or establish
worldwide novelty. It will not weaken the observer to contemporaneous totals,
replace the action by lane-specific VSL, use direct lateral control, or infer
gradient usefulness from differentiability alone.

## Question inventory and ownership

G1–G6 are **Type 2 milestone-global** because they define the equations,
actuator path, information comparator, quantifiers, decision claim and aggregate
fairness. G7 is **Mixed**: its global part fixes the conceptual chain and
nonsmooth-boundary policy; component-level derivative expressions remain local
to the eventual model components and are not required for S13 admission.

Local work sets are:

- **M2C-C1:** source-to-equation and units/conservation audit;
- **M2C-C2:** exact history/witness construction;
- **M2C-C3:** receiving/service and monotonicity analysis;
- **M2C-C4:** complete-accounting action comparison and aggregate countermodel;
  and
- **M2C-C5:** conditional conceptual gradient-path audit.

Closure order is G1 → G2 → G4 → G3 → G5 → G6 → G7. If local analysis conflicts
with a closed global choice, reopen the smallest affected G question; do not
repair it through an undocumented priority, parameter or observer change.

## S13-G1 — Which minimum receiving/service closure should define M2?

**Problem statement:** S12 admitted a family, not one equation. Carey et al.
provide several receiving-priority rules, while FB0030 supplies a different
incentive/constraint structure. Selecting a rule can change service and the
action result.

**Assumed model-chain function:** Lane-changing demand and same-lane demand enter
one target lane and share finite receiving capacity. Lateral flow removes mass
from its donor and adds the same mass to its receiver. A lane-change gap factor
may make lateral entrants consume more receiving space.

**Core gap:** The priority rule, zero-demand convention, mandatory-demand profile
and exact receiving allocation are not frozen. S12 cannot justify choosing the
rule that happens to create an action split.

**Candidate A — neutral demand-proportional receiving allocation (provisional
recommendation).** Use a continuous-mass mandatory-demand law with a spatial
lane-end incentive and allocate binding receiving in proportion to effective
same-lane and gap-weighted lateral demand. Define exact zero-demand limits and
donor/receiver budgets.

**Pros:** Closest to Carey's neutral R2 construction; conservative,
work-conserving and symmetric between demand classes after gap weighting. It
avoids hard continuing-lane priority and exposes a compact analytical class.

**Cons:** Proportional priority remains a behavioral assumption and ratio
denominators require explicit empty-state treatment. It may smooth over ordered
gap effects.

**Dependencies/consequences:** S13 must map the spatial mandatory-demand term and
receiving allocation to inspected sources without adopting their entire models.

**Candidate B — continuing-lane-first priority.** Serve traffic already in the
target lane before lateral entrants use residual receiving.

**Pros:** Simple, conservative and directly represented by Carey's R1 rule. It
may reflect reluctance of target-lane traffic to yield.

**Cons:** Privileges one stream structurally, can create hard active-set changes
and may manufacture a stronger ending-lane penalty than neutral allocation.

**Dependencies/consequences:** A positive information result would be conditional
on this priority and need a robustness check before broader interpretation.

**Candidate C — retain an admissible priority family.** Prove a result uniformly
or classify outcomes over all conservative work-conserving priority shares.

**Pros:** Strongest protection against rule-selection bias and yields a more
general result.

**Cons:** May make the exact witness/action proof intractable and can leave S13
with a family classification rather than one task.

**Dependencies/consequences:** Suitable as a robustness extension after a
minimal contract, not as the first derivation unless the family admits a compact
monotonic proof.

## S13-G2 — How may common VSL reach M2's lane-resolved state?

**Problem statement:** M2 must not silently become lane-specific control or gain
an invented direct effect on lateral flow.

**Assumed model-chain function:** One common advice changes longitudinal
free-flow demand/sending in every lane. Different lane occupancies and receiving
conditions can then produce different realized speeds, densities and feasible
mandatory transfers.

**Core gap:** The literature supports neighboring response effects but does not
provide one accepted common-VSL-to-M2 equation. A direct advice multiplier on
lane-change desire or gap cost would add unsupported behavior.

**Candidate A — shared longitudinal speed bound only (provisional
recommendation).** Let common VSL enter the same longitudinal sending/free-flow
speed relation in every lane. Mandatory desire depends on fixed geometry and
state; lateral realization depends on donor mass and target receiving.

**Pros:** Minimal actuator path, preserves lane-uniform control and lets lane
contrast arise endogenously. It is easiest to compare with a matched aggregate
first-order model.

**Cons:** The response may be too symmetric to preserve or materially change lane
contrast. A negative result is possible and must be accepted.

**Dependencies/consequences:** If this path cannot affect the receiving regime,
S13 should close with an obstruction rather than add an explicit lateral-control
term.

**Candidate B — explicit speed-dependent mandatory-transfer demand.** Let advice
directly change a lane-change propensity or desired-transfer rate.

**Pros:** Provides a stronger action-to-lane channel and can represent observed
speed-related preparation behavior.

**Cons:** Requires a separate source-bounded response law and risks choosing its
sign/magnitude for the desired result.

**Dependencies/consequences:** Needs targeted primary evidence and would expand
the parameter/behavioral contract.

**Candidate C — boundary-arrival control only.** Apply VSL only to aggregate
arrival timing before the M2 region.

**Pros:** Analytically simple and close to S05.

**Cons:** Likely retains arrival dominance and fails to create action-dependent
lane service; it does not use the admitted M2 channel fully.

**Dependencies/consequences:** Useful as a limiting obstruction case, not the
recommended main contract.

## S13-G3 — How should the exact strong-history witness be attempted?

**Problem statement:** Lane-wise receiving may depend on hidden variables, but
that does not prove two reachable preparations share the entire declared
aggregate history when they enter the consequential region.

**Assumed model-chain function:** A preparation creates different ending-lane
mass under an aggregate-invariant upstream branch. At decision time the compared
states reach the spatial entrance of the near-drop M2 region; common future
actions then expose different mandatory-transfer/receiving dynamics.

**Core gap:** S05's exact collision is early and conditional. It has not been
joined to a fixed spatial M2 region without leaking lane information into the
aggregate history before the decision.

**Candidate A — constructive exact spatial handoff (provisional
recommendation).** Reuse the S05 homogeneous aggregate-invariant preparation and
place the decision boundary at first entry into the fixed near-drop interaction
zone. Require exact equality of every declared aggregate history channel up to
that boundary, then propagate both states through the same M2 equations/actions.

**Pros:** Preserves the strong observer and uses a fixed spatial mechanism rather
than switching physics by hidden state. It directly targets the missing join.

**Cons:** Exact arrival at the interaction boundary and lane-contrast persistence
may be impossible under the finalized response law. The construction can fail.

**Dependencies/consequences:** Depends on G1/G2/G4. Failure must be typed as
reachability, observability or contrast-erasure rather than repaired by weakening
history equality.

**Candidate B — abstract non-identifiability proof without a reachable pair.**
Show algebraically that aggregate totals do not determine lane-wise receiving.

**Pros:** Compact and may establish a general information-loss statement.

**Cons:** Does not establish that the ambiguous states are reachable under the
same history and task. S12 has already reached this level.

**Dependencies/consequences:** Insufficient alone for the core decision claim.

**Candidate C — approximate matched histories.** Define a tolerance and compare
near-matched aggregate histories.

**Pros:** Easier and closer to future empirical evaluation.

**Cons:** Reopens the accepted exact information claim and introduces metric,
normalization and tolerance choices.

**Dependencies/consequences:** This would be a different review branch and
requires explicit reconsideration of the comparator.

## S13-G4 — What parameter quantifier prevents favorable tuning?

**Problem statement:** One nominal gap factor, demand level or receiving capacity
could be selected because it creates the desired ranking.

**Assumed model-chain function:** Structural inequalities define an ordinary M2
regime; exact values determine effect magnitude but should not define the result
after it is observed.

**Core gap:** S12 identified positive mandatory demand, binding receiving and
positive extra lane-change space as a nonempty regime, but did not define the
quantifier for a certificate.

**Candidate A — prove existence on an open source-bounded regime (provisional
recommendation).** State parameter inequalities before derivation and require the
result to hold on a nonempty open subset, with aggregate/fixed-service limits
shown separately.

**Pros:** Avoids one-point tuning while keeping the proof feasible. It supports a
conditional scientific claim with explicit scope.

**Cons:** Requires defensible source bounds or qualitative inequalities and does
not establish universality.

**Dependencies/consequences:** The derivation must report failure regions and may
not shrink bounds after observing the action result.

**Candidate B — one transparent nominal parameter set.** Prove one worked
example without claiming robustness.

**Pros:** Lowest analytical burden and can demonstrate logical possibility.

**Cons:** Vulnerable to favorable example selection and insufficient for the
intended coefficient-independent continuation.

**Dependencies/consequences:** Would weaken the S12 admission standard.

**Candidate C — require the result for every admissible parameter.**

**Pros:** Strongest robustness claim.

**Cons:** Likely false because aggregate limits and weak-demand regimes are
intentionally included; it can reject a meaningful conditional mechanism.

**Dependencies/consequences:** Better used to identify impossibility subregions
than as the primary success criterion.

## S13-G5 — What action and decision certificate answers control relevance?

**Problem statement:** A finite favorable menu or local derivative sign can hide
a common superior action. S05 specifically exposed this risk.

**Assumed model-chain function:** The same lane-uniform action family is applied
to both hidden states, including its fastest feasible endpoint. Complete delay is
evaluated through common clearance.

**Core gap:** S13 has not fixed whether to prove a result over a continuous
one-parameter advice family or only a finite menu.

**Candidate A — full bounded one-parameter family including the fastest endpoint
(provisional recommendation).** Use the smallest analytically tractable constant
or fixed-shape VSL family indexed by one continuous magnitude. Establish distinct
optimal/acceptable sets or positive minimax regret over the entire family.

**Pros:** Directly answers the S05 action-menu objection and gives a strong
information-to-decision result.

**Cons:** More demanding than a finite comparison; optima may lie at nonsmooth
regime boundaries.

**Dependencies/consequences:** Requires G1–G4 and an explicit common action
interval. If no distinction exists, report the obstruction.

**Candidate B — finite preregistered menu including the fastest action.**

**Pros:** Easier exact comparison and still prevents omission of the dominance
stress action.

**Cons:** Establishes only menu-relative value and may miss a common action
between probes.

**Dependencies/consequences:** Any claim must remain finite-menu bounded.

**Candidate C — local gradient-sign difference only.** Seek opposite derivatives
at one shared action.

**Pros:** Directly relevant to later gradient optimization and analytically local.

**Cons:** Opposite local signs need not imply different globally useful actions
or downstream improvement.

**Dependencies/consequences:** May be a supporting result only after a decision
certificate, not a substitute for it.

## S13-G6 — How should aggregate sufficiency be tested?

**Problem statement:** Advice-dependent service can be modeled by aggregate
capacity drop. M2 matters only if its consequential state is unavailable to the
declared strong aggregate observer.

**Assumed model-chain function:** A deterministic observer-only predictor or
controller receives the exact same aggregate history and future action in the
paired cases. A source-backed aggregate capacity-drop model is also evaluated as
the concrete baseline class.

**Core gap:** Comparing M2 with one weak fitted aggregate model would not
establish information value, while excluding all conceivable history functions
is neither necessary nor testable.

**Candidate A — exact observer identity plus a strong source-backed aggregate
countermodel (provisional recommendation).** Use the exact history equality to
show any deterministic observer-only rule must act/predict identically at the
decision point, and separately test whether a declared aggregate capacity-drop/
hysteresis closure reproduces M2's action ranking.

**Pros:** Combines an information-theoretic argument with an operationally strong
countercandidate. It does not rely on deliberately weakening the macro model.

**Cons:** The impossibility statement is conditional on the exact observer and
deterministic rule; the concrete aggregate closure cannot represent every
possible learned history model.

**Dependencies/consequences:** Requires G3 exact equality and G5 decision result.

**Candidate B — compare with one calibrated aggregate baseline only.**

**Pros:** Operationally concrete and simple.

**Cons:** A positive M2 result may reflect poor aggregate calibration rather than
hidden information.

**Dependencies/consequences:** Would change the claim to performance against one
model and reopen the accepted observer standard.

**Candidate C — omit an aggregate countermodel.** Rely only on lane-sensitive
M2 behavior.

**Pros:** Lowest burden.

**Cons:** Cannot answer whether lane resolution is necessary; inconsistent with
the core review question.

**Dependencies/consequences:** Not sufficient for S13 closure.

## S13-G7 — What gradient result belongs in S13?

**Problem statement:** The core review also asks whether consequential hidden
information can provide relevant gradient information. Exact component
derivatives depend on the equations selected in G1/G2.

**Assumed model-chain function:** If G5 establishes decision relevance, the
conceptual path is advice → lane-wise sending/state → lateral transfer and
receiving allocation → service → complete delay. Structural metadata is outside
the derivative path; active-set changes may be nonsmooth.

**Core gap:** A general path can be stated, but derivative correctness and
downstream usefulness cannot be inferred from the analytical action result.

**Candidate A — conditional conceptual gradient contract (provisional
recommendation).** After a positive G5 result, identify differentiable continuous
states, structural metadata, component Jacobian boundaries and fixed-active-set
versus nonsmooth regimes. Defer exact component propagation and numerical checks
to their owning components/later review.

**Pros:** Answers the requested general gradient-path question without claiming
unsupported correctness or usefulness. Keeps decision evidence first.

**Cons:** Does not deliver a combined derivative certificate.

**Dependencies/consequences:** If G5 fails, record that the mathematical path may
exist but has no established downstream relevance and stop.

**Candidate B — derive and verify the full combined gradient in S13.**

**Pros:** Could answer the complete gradient question in one review.

**Cons:** Requires implementation or substantial numerical/symbolic validation
beyond the current analytical decision task and risks conflating differentiability
with usefulness.

**Dependencies/consequences:** Would require a separately expanded plan.

**Candidate C — defer all gradient discussion.**

**Pros:** Keeps S13 narrowly focused on the decision certificate.

**Cons:** Leaves the third core research product entirely unaddressed even if M2
is positive.

**Dependencies/consequences:** A new gradient-path review would be mandatory
after any positive decision result.

## Planned review method after approval

1. Reuse S05 and S12 evidence before any narrowly targeted source search.
2. Freeze G1/G2/G4 as a source-to-equation contract, including units,
   conservation, zero-state limits, aggregate limits and active-set conventions.
3. Render the formula-heavy contract and later derivation as LaTeX/PDF under
   `synthesis/s13/`, with source retained beside the PDF.
4. Attempt G3's exact spatial handoff. Audit every aggregate history channel and
   reject approximate equality under the current claim.
5. Derive the M2 postdecision service and complete-accounting outcome for the
   common G5 action family. Include the fastest endpoint.
6. Reapply monotonicity/dominance analysis and classify positive, forward-only,
   aggregate-equivalent or obstruction outcomes.
7. Apply G6's observer/countermodel audit before attributing value to lane state.
8. If and only if decision relevance passes, produce G7's conceptual gradient
   path and boundary map.
9. Stop at S13-UG1 / M2C-R1 for user review; do not open implementation or ramp
   metering automatically.

## Planned outputs after approval

- `extraction/s13_m2_source_to_equation_audit.md`;
- `synthesis/s13/s13_m2_model_contract.tex` and `.pdf`;
- `synthesis/s13/s13_m2_certificate_analysis.tex` and `.pdf` if G3 is reachable;
- `reporting/s13/s13_20_m2_certificate_findings_and_gate.md`;
- `reporting/s13/s13_80_m2_contract_dialogue.md`;
- `reporting/s13/s13_90_m2_certificate_work_report.md`; and
- synchronized sequence, registry and successor-plan records.

## Acceptance criteria and verdicts

The strongest positive result requires:

1. a source-bounded, conservative and unit-consistent M2 equation contract;
2. exact equality of the declared aggregate history for two reachable states;
3. different hidden M2 state that changes endogenous service under common
   actions;
4. a different useful-action result over the approved action family under
   complete accounting;
5. failure of the declared aggregate countermodel to reproduce both cases under
   the same observed history; and
6. a bounded conceptual gradient path with honest nonsmooth boundaries.

S13 will assign one primary verdict:

- **M2C-A — decision-relevant certificate:** all six conditions pass;
- **M2C-B — forward-only distinction:** hidden state changes service/outcome but
  not the useful action;
- **M2C-C — aggregate-equivalent:** consequential state or ranking is captured by
  the strong aggregate observer/countermodel;
- **M2C-D — monotonic obstruction:** the finalized class retains a common best
  action despite endogenous service;
- **M2C-E — contract unsupported or inconclusive:** the source-to-equation or
  exact-history join cannot be defended;
- **M2C-F — multiple viable contracts:** more than one closure survives and the
  choice changes scientific meaning, requiring a user decision before
  derivation.

## Stop conditions

Stop before ordinary findings if a decision-critical source is inaccessible, G1
or G2 cannot be frozen without unsupported behavior, or the recommended global
choices conflict with the S12 admission boundary. During an approved review,
stop and report the appropriate typed verdict when exact history equality fails,
lane contrast is erased, arrival dominance is restored, the aggregate
countermodel is sufficient, or contract choice becomes outcome-dependent.

No negative result may be repaired by weakening history, dropping the fastest
action, truncating waiting, selecting a favorable coefficient, changing to lane-
specific VSL or adding direct lateral control.

## S13-PG1 — Plan decision

The provisional recommendation is:

- G1-A: neutral demand-proportional finite-receiving allocation;
- G2-A: shared longitudinal speed bound only;
- G3-A: constructive exact spatial handoff;
- G4-A: existence on an open source-bounded parameter regime;
- G5-A: full bounded one-parameter action family including fastest advice;
- G6-A: exact observer identity plus strong aggregate countermodel; and
- G7-A: conditional conceptual gradient contract.

Approval authorizes only the methodology-only S13 review through S13-UG1 /
M2C-R1.

## Approval and execution record

The user approved the complete recommended Candidate A set. G1–G5 and G7 were
accepted as definition, guardrail and boundary clearance; G6-A was separately
confirmed as the methodologically correct aggregate-model treatment of hidden
information. The user instructed execution through the next user gate.

The source-to-equation contract, exact spatial handoff, open-regime action
certificate, observer-only regret proof, aggregate countermodel audit and
conditional conceptual gradient path are complete. The provisional verdict is
**M2C-A — conditional decision-relevant certificate**.

**Disposition:** the user accepted M2C-R1 Candidate A on 2026-10-01. S13 closes
with **M2C-A — conditional decision-relevant certificate**. See the
[closure and research-readiness boundary](reporting/s13/s13_99_m2_certificate_sprint_closure.md).
No implementation, empirical validation, ramp-metering review or later gradient
work has started.
