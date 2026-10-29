# S03.20 — Route B findings and next-evidence user gate

Sprint: [S03](../../00_review_sequence.md#s03) · Role: 20 findings / decision evidence · Predecessor: S02 / approved Route B · Gate: RB-UG1.

Date: 2026-09-17. **Sprint closed; RB-UG1 Option A approved: draft a separate
diagnostic experiment plan.** Paper request1 is resolved. No experiment or
simulator implementation is authorized. [Closure and handoff](s03_99_rb_sprint_closure.md).
Recommendations/alternatives below preserve the finding-stage discussion;
the user's decision closes next-scope choice only, not open scientific claims.

## Main conclusion

**Keep lane information as a testable control hypothesis, but do not build a
new differentiable lane model yet. The cheapest defensible next step is to
plan a bounded reference diagnostic of reachable matching and advice decisions.**
Its cost/feasibility must be checked in that plan; success is not guaranteed.

The proposed distinction is not “lane-aware traffic models can be differentiated.”
Those models, speed optimization, aggregate adjoints and aggregate autodiff
already have substantial predecessors. The potential contribution is conditional:
identify when a strong aggregate response/history model loses information that
changes useful common-speed-advice decisions, then test the smallest conservative
refinement and its independently useful gradients. This review does not prove
that such a case exists or clear worldwide novelty.

## What the supplied paper resolves

[Chen et al.2025](https://doi.org/10.1016/j.physa.2025.130876) is the verified
final17-page paper, not the19-page public preprint. Its lane CTM/MPC is optimized
with NSGA-II, discrete5km/h limit choices and efficiency/conflict objectives.
Sections5.2–6 compare VSL with no VSL, not aggregate versus lane-resolved models
under matched actions, fitting and search. Python/SUMO evaluation is relevant
prior work, but no candidate-gradient transfer or retained-state ablation is
reported in the inspected paper.

An important correction: four vehicle types feed an expected headway/flow law;
the displayed rollout does not transport four separate class masses or preserve
individual order. Analytic probabilities are not automatically a sampled
mass-shift process. The paper therefore does not justify adding response classes
or intra-lane order to our candidate.

Its lane-indexed feasible-control formulation is not certified identical to our
shared continuous advice. Illustrated cell schedules do not settle lane equality
or the microscopic response interface. Its scenario is an on-ramp merge, not
the approved exogenous mainline lane reduction/reopening.
[Verification, exact locations and equation audit](../../extraction/rb_source_studies/FB0040.md).

## Findings, gaps and reusable modeling

| Finding | Evidence and consequence |
|---|---|
| Strong aggregate response/history is a real alternative | [Frejo2019](https://doi.org/10.1016/j.trc.2019.01.001) dynamic mean speed; [Wei2025](https://doi.org/10.1111/mice.13492) entry-speed history. Compare credible aggregate families/observers, not an artificially memoryless baseline. |
| Lane distribution has a plausible causal role | [Subraveti2020](https://doi.org/10.1177/0361198120948055) supports constrained merging. Continuing-lane balance and spatial location can matter; one ending-lane share is not a proved sufficient statistic. Its tested2–1 no-gain case concerns lateral control, not proof our task requires3–2. |
| Slower advice is not guaranteed to help | [Soriguera2017](https://doi.org/10.1016/j.trc.2017.01.024) warns against automatic metering/homogenization. Conditional no-gain evidence limits general VSL-benefit claims. |
| Whole published lane schemes are not AD-ready by inspection | Source donor/receiver budgets, empty-state denominators, wave-sign conventions and hard capacity branches need exact audit. Continuous mass alone proves neither continuity nor gradient fidelity. |
| The intended information-to-useful-gradient claim remains unresolved | No inspected full-method source supplies the reachable strong-baseline-matched pair plus common-action independent decision test. That is an evidence gap in this bounded corpus, not proof the literature never answered it. |

New incident work supplies additional conditional no-benefit evidence, not the
missing state-ablation result. See the
[primary-source frontier and coverage limits](../../extraction/rb_source_studies/final_frontier.md).

Reuse priorities:

1. Strong spatial mass/mean-response/history and source-queue accounting first.
2. If justified, source-informed deterministic paired transfer, finite receiving
   and lane-end incentives; receiving room can be derived rather than treated
   as an independent new state.
3. Test conservative compressed lane/group statistics against fuller lane state.
   Do not remove storage/conservation constraints to make an ablation.
4. Keep response classes and order conditional; no source equation repair,
   smoothing, sampling or saltation exception is approved.

Shared action exposure, desired versus realized response, all-population time
spent including pending/unfinished traffic, and closure recovery must match.
SUMO documents relevant capabilities but no working dynamic-advice adapter or
empirically validated response bundle has been verified.
[Common-contract recommendations](../../synthesis/s03/rb_common_contract.md).

## What must be learned next

The one proposed contrast has different ending/continuing-lane occupancy while
matching the actual aggregate model's spatial mass, mean response, queues,
counts and declared memory. Physically valid lane-biased preparation is a
candidate route, not a demonstrated matched pair.

The first missing evidence is feasibility of that match and a robust difference
in preferred common advice action or action ranking in an independent reference.
Forward differences alone are insufficient. A lane-state observer inferred
from aggregate history might erase the distinction; that is legitimate
counterevidence. If matching needs another uncontrolled mechanism or weaker
baseline, stop rather than manufacture success.
[Contrast, falsification and information audit](../../synthesis/s03/rb_contrast_and_information_audit.md).

A positive reference decision result would motivate—but not prove—a native
continuous candidate's derivatives/usefulness. Internal derivative checks and
external gradient-guided improvement remain later separate obligations.

## RB-UG1 — decision requested

**Problem:** Is the remaining conditional information-to-decision question worth
a bounded feasibility/decision diagnostic before simulator construction?

**Model-chain function:** shared advice changes desired traffic response;
omitted lane occupancy may change constrained merging and independent system
time spent. Only later would checked candidate gradients guide those actions.

**Core gap:** reachable strong-baseline matching, advice-ranking differences and
a fair reproducible evaluator remain unproved. There is no evidence-backed
minimum lane/class/order architecture to approve now.

### A. Draft a separate diagnostic experiment plan — recommended

Plan the reference setup and reachable preparation/memory match first; then
shared advice perturbations, unchanged-advice control, full accounting,
response/capacity robustness, calibration/held-out separation and explicit
success/failure/stop criteria. Inspect installed software and lawful support
during planning; no experiment follows without its own approval. Do not
construct a new AD lane simulator merely to screen this hypothesis.

**Pros:** tests the actual missing decision evidence; can reject unnecessary
detail or justify a compressed refinement before substantial construction.
**Cons:** setup/calibration or matching may dominate cost; synthetic evidence
will not establish field usefulness; the hypothesis can fail.
**Dependencies/consequences:** new plan and approval, a credible strong aggregate
comparator/information set and independent reference. Positive results open
later model/gradient planning, not automatic lane/class/order approval.

### C. Halt or defer the freeway branch

Archive the conditional opportunity and unresolved evidence without further
diagnostic construction. This is defensible if expected setup/evidence cost
outweighs the qualified contribution.

**Pros:** avoids building an unneeded differentiated model and novelty rescue.
**Cons:** leaves a plausible task-specific information question untested.
**Dependencies/consequences:** user closure/defer decision; no urban project
change and no claim of refutation or aggregate sufficiency.

The approved plan's aggregate-sufficiency alternative B is not independently
recommended now: the review has not established sufficiency or a distinct new
domain boundary for that study. It can become a substantive later option if
diagnostic counterevidence supports it; it is not a relabeling of present
uncertainty.

**Provisional recommendation:** A, restricted to drafting the diagnostic plan.
Stop here for the user's next-scope decision; do not run or implement anything.

## Review closure and question ownership

RB-G0 remains fixed. G1 overlap is qualified, G2 common-contract recommendations
are documented, G3 reachability is explicitly unresolved, G4 information/hazards
are screened: closed as review findings, not accepted scientific equations.
C1–C4 source extractions inform those conclusions; G5 is closed by the user's
Option A planning approval. No diagnostic execution or equations approved.

Six query families plus nearest backward/update frontiers were covered.
The final targeted pass added no new decision category. Uninspected abstracts,
inaccessible methods and uncertain publication dates remain labeled; no global
first/absence claim is made. Documentary checks and protected-file integrity
are recorded in the [work report](s03_90_rb_work_report.md).
