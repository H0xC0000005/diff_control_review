# Which algorithms are borrowed, and why their adaptations are admissible

**Controller-source recommendation superseded by the user's clarification.**
The loop-level attribution below did not establish the requested common
controller. Its source facts and local eligibility arguments are retained
as historical supporting work. The current proposal uses one common
Zhang-derived speed-setting design in both arms, with gradient tuning
added by us. The user now excludes Delle Monache from the active proposal.

[Current shared-controller correction](vsl_shared_controller_correction.md)

2026-11-02. Focused source-to-algorithm clarification for the proposed
per-case B comparison. The user-selected traffic stack and per-case timing
remain fixed. This refines the recommendation; it does not approve the
search methods or authorize development or experiments.

**The borrowing can be specified more tightly: B0 uses Zhang et al.'s
enumeration approach; B-gradient uses the first-order optimization loop
in Delle Monache et al.'s Algorithm 1. Their adaptation requirements are
different. B0 needs a well-defined score for each feasible candidate.
B-gradient additionally needs a valid derivative of our own score.**

The earlier description as literature-backed method families was not enough
to establish that second requirement. Here the necessary bridge comes
from our existing complete-TST and regularity analysis, not from transferring
the other paper's traffic assumptions.

## The exact unit borrowed

| Proposed method | Published algorithm unit | Operations retained | What this does not mean |
|---|---|---|---|
| **B0** | Zhang et al., Section 4.3: enumeration of speed settings with CTM. | Generate admissible candidates, evaluate each traffic outcome, compare scores and keep the best evaluated setting. | We are not importing the paper's complete microscopic-GA-plus-CTM study, its calibrated traffic laws or its optimized spatial profile. |
| **B-gradient** | Delle Monache, Piccoli and Rossi, Section 4.2.3, Algorithm 1: the first-order speed-optimization loop. | Start from a control, obtain cost sensitivity, update opposite the gradient, rerun the traffic model, recompute cost and repeat subject to stopping rules. | We are not importing its PDE cost-variation formula or treating its native controller as already qualified for congested lane-drop TST minimization. |

The primary locations are
[Zhang, PDF p. 21](https://ira.lib.polyu.edu.hk/bitstream/10397/92568/1/Zhang_Optimization_Speed_Freeway.pdf#page=21)
and
[Delle Monache et al., PDF pp. 15–16](https://arxiv.org/pdf/1603.04785#page=15).
This is algorithm-level attribution, rather than a claim of verbatim
pseudocode or author-code reproduction. In particular, the source specifies
enumeration but does not supply our nested-grid schedule.

There is no single inspected paper supplying the entire matched B0/B-gradient
pair for this task. The borrowed search loops are placed around the same
reviewed evaluator. The matching rules belong to our comparison.

## B0: the adaptations are admissible without a traffic-specific search proof

The source objective is finite-period throughput; our objective is complete
total system time. The source also constrains a spatial speed profile.
We replace that with one common constant advice in 30–60 km/h.
[Zhang, Section 2, PDF pp. 7–9](https://ira.lib.polyu.edu.hk/bitstream/10397/92568/1/Zhang_Optimization_Speed_Freeway.pdf#page=7)

Consequently, **Zhang also involves a task adaptation**, not just moving
an unchanged controller to a new geometry. The reason it is a straightforward
algorithmic adaptation is that enumeration does not assume a particular
relationship between speed, congestion and the scalar score.

The exact changes and their justification are:

| Change | Why the search rule remains applicable |
|---|---|
| Replace the source's predictor with our selected lane-resolved simulator. | Enumeration needs comparable scores for feasible candidates; it does not derive its search direction from a specific traffic law. The existing task analysis establishes finite, complete TST for the admitted cohort. |
| Replace throughput with complete TST. | Rank candidates by lower complete time. This changes what is optimized, but does not invalidate comparing their scores. It is not a claim that throughput and TST are equivalent. |
| Replace the spatial profile and source constraints with one constant bounded advice. | Enumerate candidates in the task's own feasible set. This is a new action set, not necessarily a feasible subset of the source's profile constraints. |
| Use the initialized cohort, no subsequent arrivals, a nested grid and explicit budgets. | These define the evaluator and sampling schedule. They do not require a new traffic-dependent enumeration rule. |

The mathematical guarantee is deliberately small and exact: among the
feasible candidates actually evaluated correctly, retaining the lowest
TST returns the best observed candidate. No smoothness, unimodality or
convexity is needed for that statement.

Thus **B0 is analytically eligible for the elementary comparison once
the evaluator is implemented correctly**. A separate empirical study is
not needed merely to justify applying enumeration to a different scalar
objective. Numerical competence and the necessary grid resolution are
still future evidence. A finite grid is not a global-optimum certificate;
native jumps can even make an unusually good isolated speed easy to miss.

## B-gradient: task migration needs a separate bridge, which is available locally

The source task is free-flow LWR with time-varying speed and an outflow-tracking
objective. Its cost variations are derived for that task.
[Delle Monache et al., Sections 2–3](https://arxiv.org/pdf/1603.04785#page=2)

Our problem changes the dynamics, objective, cohort/completion accounting
and control parameterization. Therefore **using its native sensitivity
formula or inheriting its conclusions by default would be unjustified**.

What can be retained is the first-order outer loop. Its target-task
requirements are checked independently:

1. **Our scalar objective must be well-defined.** The existing analysis
   proves complete cohort accounting with an exact remaining-time value.
   It is not a truncated sum whose uncounted traffic changes with advice.
2. **The derivative must belong to that objective.** The reviewed sensitivity
   includes the trajectory, the remaining stock's sensitivity and direct
   remaining travel time. The source PDE derivative is entirely replaced.
   With one tied speed, this is a derivative with respect to that one
   parameter, not a selected component of an unrelated time-varying gradient.
3. **There must be places where first-order guidance is meaningful.**
   For each admitted fixed initialization, the analytical addendum establishes
   smooth advice intervals separated by finitely many exceptional values.
   At a regular interior speed, a nonzero derivative gives a sufficiently
   small improving move in the opposite direction. At a bound, that direction
   must also be feasible.
4. **The actual search must respect those limits.** The proposed version
   keeps advice within bounds, evaluates full TST at trials and shortens
   unsuccessful steps. These feasibility, trial-check and branch-qualification
   rules are explicit adaptations, not a claim to copy the printed
   Algorithm 1 unchanged. At an unqualified derivative, stop that gradient
   path and report the best evaluated candidate and the qualification failure.

The local argument in item 3 follows directly from differentiability:
if a small speed increase raises cost to first order, a sufficiently small
decrease lowers it, provided it stays feasible and within the regular region.
Step shortening can reach such a region in exact arithmetic. It does not
make a derivative at a genuine switch valid.

[Existing complete objective and derivative, Section 7](../../synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.pdf)

[Existing regularity result, Section 3](../../synthesis/research_readiness/vsl_methodology_review_analytical_addendum.pdf)

These are our analytical establishments, not source claims. They justify
**a bounded, value-checked local first-order variant for elementary
within-model verification**. They do not justify an unchanged source method
over all speeds, global convergence across switches, successful numerical
AD, superiority to B0 or physical traffic validity. Those claims still
require their respective numerical or empirical evidence.

## Extra simulator information is compatible with the borrowed algorithms

B is a direct speed optimizer, not a second traffic predictor with its own
required state vector. The simulator may retain richer lane information
than the optimizer explicitly consumes. B0 uses candidate speeds and TST;
B-gradient additionally uses the qualified speed sensitivity. Raw lane
arrays or additional simulator outputs need not be passed to either.

That is compatible with the algorithms' cost/sensitivity interfaces.
It is not evidence that lane detail is absent from B0's performance feedback.
Both versions can encounter its consequences through their admitted
current-case queries.

## The recommendation and its boundary

**Retain the proposed pair, with this explicit provenance: adapt Zhang's
enumeration algorithm for B0; adapt Delle Monache et al.'s first-order
outer loop for B-gradient, replacing its entire traffic/objective
sensitivity calculation with our analytically qualified one.**

The applicability claims rest on separate arguments. B0's
eligibility follows from finite candidate comparison; B-gradient's
eligibility requires, and here has, a target-specific regular-derivative
argument. No new empirical traffic experiment is needed in this review
to establish those limited statements.

No new source survey or traffic-law change is needed for that bounded
recommendation. The exact search details remain proposed at the matched-B
contract gate. The external aggregate reference A still needs its own
predictor/task compatibility check; B0's eligibility does not close that
different question.

[Current matched-pair contract](vsl_per_case_matched_controller_contract.md)

[Primary reading record](../../extraction/research_readiness/vsl_matched_controller_review_sources.md)

[Work and document checks](vsl_per_case_matched_controller_work_record.md)

