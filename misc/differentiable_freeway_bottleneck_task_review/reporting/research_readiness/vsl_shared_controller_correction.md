# One shared VSL controller, with and without gradient-based tuning

**Current continuation:** the user selects this matched B direction
for the first verification and defers A. Its common-controller/reference-
case/evidence specification is now consolidated; numerical outcomes remain
untested. Private handoff alignment is the next review action.

[Current elementary-verification specification](vsl_b_pair_elementary_verification_specification.md)

**Executed task-fit continuation:** the shared B specification and
gradient pathway are analytically qualified under the common task
adaptations. The separate A predictor is not yet qualified at the choke.
The current choice concerns A's timing in the first verification, not
different controllers for B0 and B-gradient. The original correction
below retains its historical discussion status.

[Current findings and scope choice](vsl_zhang_task_fit_findings_and_choice.md)

2026-11-02. The user clarifies the required ablation: one literature-supported
base controller in both versions, with simulator-gradient access as the
main intervention. The source need not have used gradient optimization.
Per-case optimization, one constant advice and the selected traffic stack
remain fixed. The shared-base recommendation below is provisional.

**The controller must be identical, not merely supported by separate
papers saying that two controllers work reasonably well.** I conflated
the controller with its optimizer when assigning Zhang to B0 and Delle
Monache to B-gradient as their overall algorithm sources. That was the
wrong level of attribution for the requested ablation.

There is a useful distinction in correcting this. The written B contract
already prescribed the same constant-speed action, fine plant and complete
TST in both versions. It did not actually import Delle Monache's free-flow
dynamics or outflow objective into B-gradient. Nevertheless, separate
search-loop citations did not qualify the requested common controller.

## The corrected comparison

B should be one direct speed-setting controller. For this elementary task,
its single parameter is the common advised speed. Once chosen for the case,
that speed is held throughout the episode.

| Part | B0 | B-gradient |
|---|---|---|
| **Base control design** | The same parameterized speed-setting controller. | Identical controller, not a different source's policy. |
| **Parameter and execution** | One continuous advice in 30–60 km/h, applied commonly and held constant. | The same parameter, bounds, spatial application and timing. |
| **Explicit traffic-state features** | No raw lane arrays are supplied to this direct speed parameter. | Identical; detailed state stays inside the simulator. |
| **Plant and objective** | The selected lane-cell stack and complete cohort TST. | Exactly the same stack, accounting and initial case. |
| **Optimization setup** | Common prescribed initialization/probes and declared resource accounting. | The same setup, charging sensitivity work and rejected trials. |
| **Update information** | Simulator costs, without simulator-provided derivatives. | Costs plus the qualified derivative of that same objective with respect to the same parameter. |
| **Proposed tuning routine** | Value-only enumeration. | First-order tuning with actual value checks. |

For example, set the parameter to 45 km/h. Both versions issue precisely
the same advice at every controlled location and every execution step.
They therefore generate the same forward trajectory and cost from the
same initialization. The difference arises when the tuning routines select
different parameter values.

That is an identity of the control design, not a claim that two independently
optimized controllers will ultimately produce equal speeds or performance.
It needs no empirical argument that distinct controller families behave
approximately alike.

## One literature source for the common base

**Recommend Zhang et al.'s parameterized speed-setting design as the common
base candidate for both versions.** Its Section 3.2 represents a solution
as an array of segment speed settings; simulation evaluates each proposed
setting. The optimization method is separate from the resulting advice
that traffic receives.
[Primary manuscript, Section 3.2, PDF p. 12](https://ira.lib.polyu.edu.hk/bitstream/10397/92568/1/Zhang_Optimization_Speed_Freeway.pdf#page=12)

The source's native spatial profile and discrete speed constraints differ
from our task. Both versions must receive the same declared adaptations:

- Use one common continuous speed instead of the source's discrete spatial
  settings and source boundary constraints.
- Evaluate it in our selected initialized-cohort lane-cell task, with its
  fixed complete-TST objective and completion accounting.
- Retain the same adapted controller in both versions. Add gradient-based
  parameter tuning only to B-gradient.

These are task adaptations, not an assertion that our common advice is a
feasible subcase of every original source constraint.
[Source action constraints, Section 2](https://ira.lib.polyu.edu.hk/bitstream/10397/92568/1/Zhang_Optimization_Speed_Freeway.pdf#page=8)

The common direct-setpoint base remains an adapted candidate, not a literal
reproduction of an unchanged published controller. The source supports
the speed-setting design in a closely related lane-drop task. The previously
recorded candidate-ranking and complete-objective arguments support the
specific task adaptation. It has not been user-selected or empirically
validated by this clarification.

The user subsequently excludes Delle Monache from the active proposal,
including as an added optimization dependency. Its earlier reading remains
historical only. Adding simulator-gradient tuning to the common Zhang-derived
controller is our extension, supported by our own complete sensitivity.

## Why this common controller can receive gradients

The shared task already uses a continuous speed parameter. The derivative
required by B-gradient is the complete TST sensitivity with respect to
that parameter through the selected simulator and its advice interface.
There is no need to differentiate through the enumeration or genetic
algorithm used to find parameters in a source paper.

The source's integer-valued speed restriction cannot simply be differentiated
unchanged. Continuous advice is an explicit common adaptation for B0 and
B-gradient; it is not available to just the gradient version. A finite grid
is B0's numerical search over that shared interval, not a different physical
action constraint.

The existing complete-objective and regularity analysis supplies the
model-specific derivative on regular advice intervals. Its numerical
correctness must still be checked. At native switches it may not exist;
the earlier qualification and trial-value rules remain. This establishes
a gradient pathway, not guaranteed optimization success.

[Complete objective and regular sensitivity, Section 7](../../synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.pdf)

[Regular advice intervals, Section 3](../../synthesis/research_readiness/vsl_methodology_review_analytical_addendum.pdf)

## What the ablation can claim

The intended comparison is now explicit: **the same adapted speed-setting
controller, tuned without versus with simulator-provided derivatives.**
There is no controller-family or traffic-task change between the two arms.

The tuning algorithms necessarily use their different admitted information.
A result therefore concerns gradient-enabled tuning against the specified
value-only tuning method under reported computational budgets. It does not
make the effect independent of every optimizer choice or prove superiority
over every objective-only method. An additional finite-difference version,
if later useful, would test estimated versus simulator-provided derivatives;
it would not be a no-gradient version.

This first task remains per-case direct advice optimization. It is not a
trained state-feedback controller deployed across unseen cases, consistent
with the user's earlier selection. An explicit aggregate-state feedback
law would be a different controller design and would need its own source
qualification rather than being silently added here.

## Status of the correction

Withdraw the earlier two-source presentation as the proposed controller
construction. Preserve its source facts and local optimization-eligibility
reasoning as historical supporting work. The user requirement is fixed:
one common base, or an explicit reopening if a genuine controller change
is needed. The recommended common Zhang-derived base and its adaptations
remain proposed for review.

This correction does not change the traffic equations, per-case timing or
physical action contract, and introduces no second controller. No numerical
experiment or development work is performed. The current discussion remains
at the revised common-controller proposal; A's separate predictor/task
qualification and final handoff remain later work.

[Revised active contract](vsl_per_case_matched_controller_contract.md)

[Sources and reading limits](../../extraction/research_readiness/vsl_matched_controller_review_sources.md)

[Work and document checks](vsl_per_case_matched_controller_work_record.md)

