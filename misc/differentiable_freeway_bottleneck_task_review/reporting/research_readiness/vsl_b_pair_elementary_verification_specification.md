# First elementary VSL verification: one controller, two tuning methods

2026-11-02. **The user selects the matched B pair first; aggregate reference
A is deferred.** This consolidates the review-side methodology for the
first development target. It is not a report of executed tests or an
approved implementation/experiment plan.

**The first question is whether the selected simulator gives a correct,
useful speed derivative for tuning the same controller that can also be
tuned from cost values alone.** Start with a few existing reference cases.
A more elaborate controller or aggregate predictor is not needed to ask
this question.

The intended result may be a gradient benefit, no material difference or
a stronger value-only result. A correct derivative can also lead both
methods to maximum advice. None of those outcomes should be designed away.

## The common task and controller

Use the complete selected lane-cell stack: Subraveti's density/incentive
framework, inherited full Han sending/receiving budgets, the reviewed
Carey-led realization, fixed terminal lane permissions and simultaneous
continuous-mass updates. The mathematical specification remains authoritative.

The common B controller has one continuous speed parameter, currently
30–60 km/h. It applies everywhere in the modeled road and remains constant
during the executed episode. Optimize it separately for each initialized
case; every trial resets that case. There are no later arrivals.
Complete cohort time ends at the agreed choke exit and includes the
exact remaining-time value.

The literature basis is Zhang's parameterized speed-setting/evaluation
design. Our common continuous advice, cohort, evaluator and full-time
objective are declared task adaptations. We do not claim reproduction
of its spatial metering strategy, traffic model or empirical benefits.
Gradient tuning is our extension of the shared design.

[Zhang primary manuscript, Section 3.2](https://ira.lib.polyu.edu.hk/bitstream/10397/92568/1/Zhang_Optimization_Speed_Freeway.pdf#page=12)

[Source/adaptation qualification](vsl_zhang_task_fit_findings_and_choice.md)

[Full selected plant and complete accounting](../../synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.pdf)

| Element | B0 | B-gradient |
|---|---|---|
| **Controller and physical action** | The same constant-speed map and admissible interval. | Identical; at a fixed parameter it must issue the same advice and forward trajectory. |
| **Explicit optimizer feedback** | Complete TST values from the selected detailed simulator. | The same values plus its qualified complete speed derivative. |
| **Traffic-state access** | No raw lane arrays, scenario labels or teacher optima as controller features. | The same feature contract; detailed state influences the derivative internally. |
| **Proposed tuning** | Deterministic nested uniform enumeration over the interval, including interior speeds and both bounds. | Bounded first-order proposals, actual full-cost checks and shortening of unsuccessful trial steps. |
| **Return value** | Best candidate actually evaluated within its budget. | The same best-evaluated rule, including shared initial probes. |

Diagnostic state/branch traces may be retained for validation. They must
not become undeclared optimizer features or case-specific warm starts.
B0's costs can also reveal consequences of lane detail. This is derivative
access during case-specific planning, not a claim of uniquely hidden
information or shared-policy generalization.

## A small reference set with distinct purposes

Keep the inherited reference parameters: ten 100 m rows, 6 s updates,
nominal 60 km/h, backward-wave magnitude 20 km/h, jam density
150 vehicle-equivalents/km/lane and maximum capacity drop 10%.
These are analytical reference defaults, not field calibration.

| Case | Initial condition | Known answer and role |
|---|---|---|
| **Free-flow reference** | One vehicle equivalent in final A, all other cells empty. | It is inside the proved unconstrained regime. Complete population-time is 12, 8 and 6 vehicle-equivalent seconds at advice 30, 45 and 60 km/h. The regular interior derivative is negative and maximum advice is optimal. This checks units, residual accounting and basic differentiation. |
| **X** | Penultimate-row densities are 37.5 in all lanes; final E/A/B densities are 120/60/90; all earlier rows empty. | Initial mass is 38.25 vehicle equivalents. At advice 60, the existing exact first-step completion rate is 4005 vehicle-equivalents/hour. This checks selected lane/terminal dynamics before optimization claims. |
| **Z** | Same as X except final A/B densities are 90/60. | Initial mass remains 38.25; the exact first-step completion rate at 60 is 4350 vehicle-equivalents/hour. Its E and A+B profiles match X, but service differs. |

The X/Z densities are per km per lane. Their rate references are converted
to movement amounts using the 6 s update; they are not whole-episode results.
Their optimal advice and full TST differences remain unknown.

At an interior free-flow advice, compute the score both directly from the
exact remaining-time value and after a finite forward prefix followed by
that value. The score and derivative should agree. This specifically checks
the residual-state and direct travel-time contributions rather than
validating only a truncated trajectory.

Canonical accounting uses vehicle-equivalent hours; the seconds above are
for readable reference values. Derivative comparisons must use the same
cost and speed units.

[Canonical X/Z reference, Section 5, and exact residual, Sections 6–7](../../synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.pdf)

[Free-regime result and regularity, Sections 3–4](../../synthesis/research_readiness/vsl_methodology_review_analytical_addendum.pdf)

## What must be established, in logical order

**First, establish that the evaluator is the reviewed traffic model.**
Development needs conservation, sending/receiving, storage, permissions,
zero-state and simultaneous-update checks. Reproduce the free-flow score
and the full canonical X/Z movement-rate table, since matching only total
discharge would not establish correct lane allocation. Verify that enabling
a derivative graph does not change the forward result at a fixed speed.
Until these checks pass,
an apparent optimization difference is not interpretable.

All selected traffic components remain part of the eventual B comparison.
A component demonstration or simplified free-flow subset can be an early
development check, but must not be reported as verification of the complete
lane-drop gradient pathway.

**Then, check the complete derivative on qualified traces.**
Use double precision and independently evaluated complete-objective
differences with decreasing perturbations at interior regular speeds.
Both sides must remain within the admissible interval and the applicable
regular advice region. Inspect the selected branch formulas along advice
variation. Persistent ties with the same local formula need not invalidate
that derivative; do not require a global state Jacobian where none was claimed.

The derivative must include finite-trajectory effects, the changing
remaining stock and direct remaining travel time. Hold a valid finite
prefix fixed for the local derivative; do not differentiate a stopping
threshold or discard residual traffic. Native switches may instead have
one-sided slopes or jumps. Label those queries separately.

A two-sided derivative test outside the bounds, across a genuine jump or
through an altered smoothed evaluator is not this evidence. A numerical
failure must be diagnosed at the affected contract rather than repaired
by changing traffic equations.

**Finally, measure local guidance and tuning outcomes.**
Evaluate actual feasible speed changes suggested by the derivative.
Distinguish sufficiently small regular changes from finite steps crossing
switches. Report failed or shortened trial steps, zero derivatives and
unqualified queries. A correct derivative does not guarantee a useful
finite step or a global optimum.

After derivative checks, compare full tuning traces for B0 and B-gradient
on each case independently. Use the same model and complete objective.
Do not require X and Z to have different best speeds, or require the
gradient routine to win, as a condition for retaining these cases.

## Fairness of the elementary tuning comparison

Use a common case-independent starting speed; 45 km/h is the proposed
midpoint default. Both methods receive the same initial cost probes,
including 30, 45 and 60, charged to their budgets. The gradient path starts
from the prescribed candidate. Neither gets a hidden-state-dependent start
or a precomputed optimum.

B0 continues its declared interval coverage. The finite grid approximates
the shared continuous action space and is not a different physical
constraint. B-gradient uses the complete derivative at qualified candidates,
proposes feasible changes and tests their costs. An unqualified derivative
stops that gradient path with its reason visible; retain the best observed
candidate. Do not silently substitute another objective or gradient source.

Count all cost evaluations, derivative evaluations, rejected trials,
initial probes and final checks. Report best observed complete TST against
work and wall time. Do not equate a backward pass to one forward pass by
assumption, or compare iteration counts as though their costs were equal.
Use the same precision and computing conditions for any claimed efficiency.

Resolution, step scales, numerical tolerances and resource limits must be
proposed and fixed in the development plan before performance comparisons.
The review fixes the comparison semantics, not an arbitrary unrun tolerance.
Any tuning needed to debug an optimizer must remain visible rather than
being selected retrospectively to obtain a preferred winner.

Because both methods retain the maximum-advice probe, a worse returned
cost than that already evaluated incumbent is a correctness issue for the
specified deterministic comparison. Equal results at maximum advice are
a legitimate scientific outcome, not such a failure.

## What the first report should say

| Finding | Supported interpretation |
|---|---|
| Reference/invariant or shared-forward checks fail. | The implemented evaluator/comparison is not yet qualified; do not interpret tuning performance. |
| Complete derivative agrees on regular traces. | Numerical differentiation evidence for this selected model/objective. It does not establish physical fidelity. |
| Local directions work, but both tuning methods perform similarly. | Correct local information with little observed tuning advantage in this small problem. |
| Gradient tuning reaches better advice or comparable advice with less measured work. | A conditional benefit for this shared controller and specified value-only comparator under the declared cases/budgets. |
| B0 performs better, or both favor maximum advice. | Valid negative or neutral evidence; not proof that the derivative was wrong. |

The first report should retain per-case advice, complete TST, correctness/
regularity status, incumbent history and computational accounting.
An interval plot of TST and the tested candidates can help interpretation;
it remains a numerical reference surface, not a global-optimum certificate.

This first comparison establishes neither performance against aggregate
reference A, a positive lane-information value, generalization of a learned
controller, physical/SUMO validity nor runtime-control feasibility.
Those claims remain separate.

## Deferred A review and the development handoff

The user defers A and requests a simpler established method if suitable.
Its later review must preserve the source's core assumptions and algorithm
backbone, and establish that scenario adaptations retain the behavior the
method is intended to produce. A change that fails either test cannot be
traded against convenience. Zhang is not locked in as A; no alternative
A source is selected or surveyed in this pass.

**The review-side first-verification specification is now consolidated.**
No new methodological fork was needed after the B-first decision.
The numerical acceptance settings remain development-plan responsibilities;
the scientific outcomes remain untested.

The next review action is aligning the existing private handoff with:
the selected literature-backed plant, per-case B-first scope, the common
controller and admitted query timing, A's explicit deferral/criteria and
the distinction between inherited proofs and future numerical evidence.
Its current bootstrap still describes provisional selection and an older
observation-only comparison.

That alignment should preserve the mathematical snapshots and qualify
outdated timing/status text with a current addendum. It must retain the
development repository's implementation workflow. Architecture, APIs,
environments, numerical settings, runnable checks and component sequencing
belong to the developer's own approved planning process.

This pass stops at the consolidated-specification checkpoint. It has not
edited the private handoff, implemented a simulator or run any verification.

[Work scope, decisions preserved and document checks](vsl_b_pair_elementary_verification_work_record.md)

