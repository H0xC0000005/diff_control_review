# What feedback B0 and B-gradient receive, and what is borrowed

**Latest correction:** controller identity is now explicit. The
recommendation uses one common source-derived speed-setting design and
treats value-only/gradient routines as parameter tuning, not two controllers.
The historical method-family explanation below does not select a controller.

[Current shared-controller correction](vsl_shared_controller_correction.md)

**Later source-transfer check:** the algorithm units and the separate
task-eligibility arguments are now explicit. The earlier method-family
description below is retained with its sufficiency claim qualified.

[Algorithm borrowing and transfer findings](vsl_algorithm_borrowing_and_transfer_findings.md)

2026-11-02. Clarification of the proposed per-case matched optimizer.
The selected traffic stack and per-case timing stay fixed. Search details
remain proposals at the existing contract gate.

**Your reading captures the intended difference in directional guidance.
The precise name for B0 is performance feedback without a supplied
derivative, rather than no feedback.** There are two separate feedback
loops to distinguish.

| Where feedback could act | B0 | B-gradient |
|---|---|---|
| **While choosing the advice in simulation** | Each reset trial returns complete TST. The proposed grid schedule covers the interval without using a derivative; the returned costs determine the best observed advice. | Each trial returns complete TST and, where qualified, its derivative with respect to advice. That derivative guides the next proposal; actual TST checks the proposal. |
| **While the chosen advice is executed** | The chosen speed stays constant throughout the episode. | The chosen speed also stays constant throughout the episode. |

Thus neither version is a runtime traffic-state feedback controller in
this first verification. Both use simulator responses during planning.
The distinction is what guidance is available to that planning process.

For an illustrative example, suppose the trial at 45 km/h has lower TST
than the trial at 40 km/h. B0 learns that 45 was better for this case,
despite receiving no derivative. It does not thereby know whether 46
would improve on 45. A valid nonzero derivative at 45 supplies a local
increase-or-decrease direction without requiring a neighboring trial
to estimate it. That direction is obtained from a rollout and sensitivity
calculation; it is not a cost-free signal from live traffic.

Even this local direction is conditional on a regular branch and a
feasible change. It does not certify a large step across a traffic-rule
switch. That is why B-gradient still evaluates the proposed advice.

The fixed grid does not steer its next probe from observed directional
clues. This describes the proposed enumeration schedule, not a general
limitation of methods without derivatives. Objective-only adaptive search
can also use earlier costs intelligently. The intended research question
is whether simulator derivatives help relative to a credible value-only
search, not whether optimization is possible without them.

## What comes from the papers

**Zhang et al. provide a traffic-specific basis for value-based search.**
Their Section 4.3 enumerates speed settings with an aggregate CTM, in
a search domain informed by microscopic optimization. Separately,
Section 3.2 evaluates spatial speed candidates in Aimsun and returns
objective values to a genetic algorithm. The latter is not grid
enumeration in the fine simulator.
[Primary manuscript, PDF pp. 12 and 21](https://ira.lib.polyu.edu.hk/bitstream/10397/92568/1/Zhang_Optimization_Speed_Freeway.pdf)

**Delle Monache, Piccoli and Rossi provide a direct VSL gradient-optimization
basis.** Definitions 3.2–3.3 distinguish random exploration from first-order
optimization using numerically evaluated analytical cost variations.
Section 4.2 also distinguishes precomputed optimized controls from an
instantaneous feedback policy. Their task uses time-varying speed in
free-flow LWR to track a target outflow.
[Primary manuscript, PDF pp. 13 and 15–16](https://arxiv.org/pdf/1603.04785)

These are precedents for the method families and the planning interpretation.
Neither paper supplies the proposed pair unchanged.

| We can borrow | We must adapt or define for this task |
|---|---|
| Enumerate candidate speeds and select by performance; optimize speed directly using first-order cost information. | Use one constant common speed, our selected lane-resolved plant, the finite initial cohort and complete TST. |
| The distinction between searching candidate controls and using sensitivity to guide their changes. | Use the derivative of our own complete objective, including remaining traffic; do not import a source PDE derivative into different dynamics. |
| Published VSL use of these optimization approaches. | Specify the nested grid, common probes, budget accounting, bounded trial steps and cost checks. These are our comparison-design choices. |

In particular, substituting a constant speed for a published spatial or
time-varying control, changing the objective and changing the plant are
methodological task adaptations, even when the optimization idea is familiar.
They must remain explicit. We do not claim the source's control constraints,
proofs or performance transfer automatically.

## How to describe the pair accurately

**The proposed B pair consists of literature-backed direct VSL optimization
methods adapted to a matched per-case task.** It is not a literal reproduction
of a published B0/B-gradient pair. Method precedent alone does not settle
whether the adaptations are eligible for our task. That additionally
requires the algorithm/assumption check now linked above. Neither document
claims reproduction of an unchanged source controller.

The external aggregate reference A has a different role: it supplies the
published model/controller performance benchmark after its own explicit
task adaptation. B0 and B-gradient instead hold the predictive plant fixed
to examine the derivative-access intervention.

A scalar grid can be very strong. Gradient superiority, a lower-advice
benefit and a positive hidden-lane action gap remain unproved. This answer
clarifies semantics and attribution; it does not select a new controller,
run an experiment or advance past the current contract gate.

[Updated matched-pair contract](vsl_per_case_matched_controller_contract.md)

[Source reading and transfer limits](../../extraction/research_readiness/vsl_matched_controller_review_sources.md)

[Work and document checks](vsl_per_case_matched_controller_work_record.md)

