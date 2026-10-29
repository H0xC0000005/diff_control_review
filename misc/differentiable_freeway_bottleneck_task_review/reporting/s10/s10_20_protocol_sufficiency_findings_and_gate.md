# S10.20 — Future-protocol sufficiency findings and methodology gate

Date: 2026-09-29. Status: **Closed on 2026-09-30 by explicit user approval of
DG-R7 Candidate A.** Parent: [S09 scope correction](../s09/s09_35_scope_correction_and_methodology_alternatives.md).

## Main finding

The S08 contract is methodologically sufficient for a future **bounded
exact-prefix feasibility test**, but it is not an end-to-end test of the core
information-to-useful-gradient question. This is a valid staged design rather
than a defect requiring current execution.

The prefix stage can test whether the frozen preparation bank contains a pair
with exactly equal declared lane-blind histories and different hidden lane state,
with outcome-blind selection at two numerical resolutions. Its positive and
negative interpretations are appropriately bounded. It cannot establish that
lane occupancy is the causal/minimum hidden variable, that useful common advice
differs, or that any differentiable model supplies correct or useful gradients.

The [claim–evidence matrix](../../synthesis/s10/s10_claim_evidence_sufficiency_matrix.md)
records each supported conclusion and missing bridge.

## Key methodological judgments

1. **Observer boundary:** past lane-entry assignments are hidden preparation
   inputs. A positive result is valid for the declared controller boundary, but
   it is not a claim about a controller that knows those assignments or every
   possible aggregate sensor/history.
2. **Hidden variable:** final-400 m lane occupancy is a selection marker. The pair
   also differs in gaps, order, leaders and lane-change memory, so occupancy alone
   is not shown necessary or sufficient.
3. **Resolution:** exact equality at 0.5 s and 0.25 s is a strong reproducibility
   check, not continuous-time indistinguishability.
4. **Decision stage:** complete all-cohort accounting and common-action regret are
   sound requirements, but the action contract is not frozen. The omitted
   held-100 trajectory and finite open-loop menu limit any future claim.
5. **Gradient stage:** neither prefix equality nor sampled action ranking provides
   derivative evidence. A separately approved candidate refinement, internal
   AD/finite-difference checks, matched macro comparison and independent
   perturbation evaluation remain necessary.

## S10-UG1 / DG-R7 — Should the methodology review close or open another conditional study?

### Problem statement

The current methodology products now define the research question, a bounded
future prefix protocol, its interpretation limits and the later decision/
representation/gradient obligations. Should the review close with those
conditional findings, or spend another sprint on an analytical model or static
provider-source question?

### Assumed model-chain function

Methodology review should determine whether the research chain is coherent and
what evidence each step requires. It need not supply the empirical result. Any
additional study must either reduce a decision-critical uncertainty or be marked
as a new conditional model/source analysis rather than disguised execution.

### Core gap

No source or current proof establishes the joint near-drop chain from exact
hidden information through advice-dependent native merging to different useful
common advice. Static audit can expose that gap but cannot make the traffic case
exist. A new analytical closure could explore it only under additional equations;
a source audit could sharpen native feasibility but not produce numerical
collision or controller outcomes.

### Candidate A — close the methodology review with conditional findings (provisional recommendation)

Archive S08 as a future empirical protocol and close with the S10 matrix as the
claim boundary. Record that information collision, useful-decision distinction,
minimum refinement and gradient usefulness remain sequential future evidence
obligations.

**Pros:** Completes the assigned review without pretending missing empirical
evidence is a methodological defect; preserves the strongest aggregate
alternative and avoids inventing favorable merge dynamics; leaves a precise,
reviewable future protocol.

**Cons:** The root information-to-decision hypothesis remains unresolved; no
positive or negative traffic certificate results.

**Dependencies and consequences:** Explicit closure. No SUMO, model construction,
component plan or gradient work follows automatically. Future empirical work can
reopen from S08 under separate scope.

### Candidate B — open a bounded analytical certificate/obstruction study

Specify the smallest conservative shared-advice/merge/service model capable of
violating the fixed-service arrival-dominance premise, then seek a conditional
proof or obstruction without implementation.

**Pros:** May clarify the minimum causal mechanism and whether the conceptual
information-to-decision link is internally achievable; keeps work inspectable and
methodological.

**Cons:** Introduces substantive equations and assumptions not established by the
current sources. Choosing a response or merge term to force a favorable decision
would be circular. Any result remains conditional and does not certify native or
field traffic.

**Dependencies and consequences:** Reopen the earlier analytical route and freeze
a new Type 2 model contract before derivation. Preserve conservation, full history,
complete action comparison and the fixed-service obstruction as a check.

**Lightweight first stage:** Selecting B should initially authorize only a model-
admission screen. It must identify a source-supported conservative mechanism by
which common advice changes merge/receiving service, state the necessary monotonic
and conservation properties, and test whether the desired decision split is
possible without choosing favorable coefficients. If no admissible mechanism is
found, stop without drafting a full equation set. A passing admission screen
returns for approval before any analytical certificate derivation.

**Branch lineage:** This reopens **DG-R2 Candidate B**, created after S05 showed
that a free-flow information collision plus fixed service does not change the
best advice. DG-R2 B keeps the intrinsic exact-information claim and proposes an
explicit conservative advice/merge/service model. It does **not** reopen **DG-R1
Candidate B**, the earlier and different option to change the research claim to
performance of a particular aggregate model/observer. S06–S08 developed DG-R2
Candidate A's reference-first branch; the current Candidate B would return to its
analytical sibling because empirical execution is outside the present scope.

### Candidate C — conduct a targeted static SUMO source audit

Choose a source version and inspect, without installing or executing it, only the
anticipation, desired-speed response, lane-change state and output semantics that
could invalidate the proposed future protocol.

**Pros:** Could identify a structural incompatibility or necessary preparation
amendment before any future empirical setup; remains non-executing.

**Cons:** Version-specific source paths are complex; static inspection is unlikely
to prove exact numerical history equality or useful action separation. Earlier
documentation review already established capability and major limitations.

**Dependencies and consequences:** A precise source question and version must be
approved first. Findings qualify future feasibility only; they do not become
empirical evidence.

## Post-closure successor option — a new ramp-metering task review

A ramp-metering review is feasible only as a new task-selection branch after the
current VSL review closes. The earlier F2 review already found mature aggregate,
multiclass, adjoint, feedback, storage and fairness baselines, but no supported
selective lane/order-state necessity. Reopening generic differentiable ramp
optimization would repeat that stopped question.

A new admission review must instead nominate and test one specific missing-
information mechanism, provisionally the lane/gap-resolved opportunity for a
ramp vehicle to merge safely under the same aggregate mainline state, ramp queue
and continuous metering action. It must keep conventional infrastructure ramp
metering separate from CAV trajectory or lane-change control, compare against a
strong aggregate/multiclass observer, include ramp storage/queue spillback and
all-stream delay, and stop early if aggregate closure or feedback recovers the
decision-relevant information.

This successor is compatible with Candidate A closure or with completing the
lightweight Candidate B admission screen first. It is not an alternative that
silently changes the actuator inside the current VSL review.

Four additional post-closure routes are compared in the
[freeway successor portfolio](../../synthesis/s10/s10_post_closure_freeway_review_options.md):
minimal-observation value, robust hidden-state control, temporary-closure
recovery, and safety/feasibility-sensitive VSL. They are rough planning choices,
not added DG-R7 candidates or opened reviews. Each has an early admission stop so
that the next review does not repeat a known obstruction or depend on a favorable
outcome.

### Provisional recommendation

**Candidate A.** The methodology has reached a defensible stopping point. The
remaining gaps are scientific evidence obligations, not missing review structure.
Candidate B is justified only if a conditional analytical result is itself a
desired product; Candidate C only if a specific source-level uncertainty would
change the future protocol.

**Original planned stop reached.** The subsequent Feedback 25 decision below
closes DG-R7; no further review, experiment or model formulation begins
automatically.

## User closure decision — Feedback 25

The user approved Candidate A and closed the current methodology review with its
conditional findings. The permanent-lane-drop VSL task is literature-grounded and
the staged evidence path is methodologically defined, while the reachable
information-to-decision case, minimum retained state and useful gradient remain
unproved. See the [complete closure](s10_99_vsl_methodology_review_closure.md)
and [colleague report](s10_19_vsl_methodology_colleague_report.pdf).

The approved successor ordering is recorded in the
[post-closure plan](../../synthesis/s10/s10_post_closure_next_step_plan.md): temporary
lane-closure recovery first; the lightweight analytical admission screen only if
the recovery result and its stopping reason leave that route meaningful; then a
new ramp-metering task-admission review if the VSL line closes. This ordering does
not open any successor sprint.
