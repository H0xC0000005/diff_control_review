# S10.99 — Freeway VSL methodology review closure

Date: 2026-09-30. Status: **Closed by explicit user approval of DG-R7
Candidate A in Feedback 25.**

## Closure decision

The methodology-only freeway review is complete and closes with conditional
findings. Closure means that the task, comparison standard, evidence ladder,
known obstruction and unresolved claims are now documented well enough to guide
or reject later work. It does not mean that lane-resolved information has been
proved necessary, that a decision-distinct traffic case has been observed, or
that a useful freeway gradient has been established.

DG-R7 Candidate A is accepted. The analytical model study formerly listed as
DG-R7 Candidate B and the targeted static SUMO-source audit are not required to
complete this review. The analytical route remains available only as the
separately gated fallback recorded in the
[post-closure next-step plan](../../synthesis/s10/s10_post_closure_next_step_plan.md).
The S08 exact-prefix design remains a future empirical protocol; it is neither an
executed experiment nor an outstanding prerequisite for this closure.

## Final task formulation

The reviewed task is common infrastructure speed advice upstream of a freeway
lane reduction. The same advice applies to every lane; drivers and traffic
interactions determine realized speeds, lane changes and merging. The initial
controlled domain is homogeneous traffic at a permanent synthetic three-to-two
lane drop. A strong aggregate comparator receives spatial traffic amount, mean
speed or response, queues, cumulative counts and the declared predecision
history. It is not made artificially memoryless.

The candidate omitted information is a near-drop bundle containing lane
allocation, gaps, order, leaders and lane-change memory. Lane occupancy is a
selection marker, not an accepted sufficient state. The useful-decision test
requires the same common-advice action set and complete accounting of source
waiting, approach travel and residual queues. Forward difference, derivative
correctness and downstream gradient usefulness are separate claims.

This task formulation is literature-grounded: aggregate VSL and its gradients,
imperfect response, lane-changing and lane-use effects, richer microscopic
evaluation and closure/recovery accounting all have precedents. No reviewed work
combines them under the exact information and action contract needed to establish
the proposed selective-resolution result.

## Answers to the core review questions

### 1. What hidden information could change a macro controller result?

Lane allocation, continuing-lane balance, local gaps, vehicle or packet order,
leaders and lane-change memory are physically relevant candidates. The review
proved conditionally that conservative lane transfers can be invisible in total
mass during a homogeneous free-flow preparation. It did not establish a native,
reachable near-drop pair with exactly equal strong aggregate histories and a
consequential hidden contrast. Full aggregate history may recover some apparently
hidden information.

### 2. Can the hidden information change useful common speed advice?

The literature supplies plausible response, gap and merge mechanisms, but no
reviewed source isolates the required information-to-decision chain under the
same lane-uniform advice and complete accounting. The S05 fixed-service result is
a substantive negative boundary: if advice only changes arrival time and service
is fixed and work-conserving, faster feasible advice remains a common best action.
Different fixed capacities or lane queues alone therefore do not establish useful
slowing. A positive case requires endogenous advice-dependent merge, receiving or
service behavior tied to information absent from the declared history.

### 3. What task and gradient path can be formulated?

A defensible staged task is available: establish a declared-channel information
collision, establish different useful common advice, identify the smallest
adequate retained state, verify its internal derivative, and then test small
gradient-guided perturbations in an independent richer evaluator. The general
path is methodologically clear. The traffic instance, minimum state and combined
forward-to-useful-gradient evidence are not established.

## Evidence that is established

- First-order aggregate VSL and response/history-aware models are credible
  baselines, not straw men.
- Lane use, mandatory merging, finite gaps and native lane-change response are
  physically relevant around lane reductions.
- A homogeneous free-flow construction can hide conservative lane transfers from
  total aggregate history under stated assumptions.
- Fixed advice-independent service plus arrival dominance obstructs the simplest
  attempt to turn hidden lane state into different useful advice.
- The S07 preparation repair and S08 dual-step protocol form a bounded, defensible
  future test of exact sampled-history collision for one synthetic preparation
  bank.
- The S10 matrix states exactly which later evidence would be required for
  decision, minimum-state and gradient claims.

## Claims that remain open

- Existence of a reachable native pair with equal declared strong history and a
  consequential hidden near-drop state.
- Different acceptable common-advice sets, or material common-action regret, for
  that pair after all-demand accounting.
- Necessity or sufficiency of lane occupancy, gap/order state, response class or
  any compact combination.
- A conservative differentiable freeway closure that reproduces the relevant
  mechanism.
- Correct task-specific gradients and their usefulness in an independent richer
  evaluator.
- Transfer from the synthetic permanent lane drop to temporary closures, field
  operations or feedback policies.

These gaps cannot be closed by further static synthesis alone. The reviewed
papers change actuator, objective, observer, dynamics or fidelity together; none
supplies the joint controlled comparison. An analytical answer would require new
traffic equations, while a native answer would require an empirical reference
study. Both are successor studies rather than unfinished documentation.

## Recovery map for later reviewers

Read the following in order:

1. [Review recap through closure](../../01_review_recap_through_s06.md) for the
   scientific narrative and definitions.
2. [S10 claim–evidence matrix](../../synthesis/s10/s10_claim_evidence_sufficiency_matrix.md)
   for the exact boundary of each claim.
3. [S05 analytical findings](../s05/s05_20_rb_certificate_findings_and_gate.md) and its
   [analysis PDF](../../synthesis/s05/rb_certificate_analysis.pdf) for the conditional
   hiding result and fixed-service obstruction.
4. [S06 reference bridge](../s06/s06_20_reference_bridge_findings_and_gate.md) for the
   response/merge mechanism evidence and qualifications.
5. [S07 preparation findings](../s07/s07_20_reachable_preparation_findings_and_gate.md)
   and [S08 contract](../../synthesis/s08/s08_exact_prefix_feasibility_contract.md) for
   the prospective exact-prefix construction.
6. [S09 scope correction](../s09/s09_35_scope_correction_and_methodology_alternatives.md)
   and [S10 findings](s10_20_protocol_sufficiency_findings_and_gate.md) for why
   SUMO execution is outside this review and why closure is valid.
7. [Colleague report](s10_19_vsl_methodology_colleague_report.pdf) for the concise,
   context-independent account.

Source-level evidence, access limits and prior-art boundaries remain in the
`extraction/`, `search/` and `archive/metadata/` records linked from the owning
sprints. This closure does not replace those records.

## Approved successor ordering

The next-step sequence is documented, but no successor review is opened:

1. temporary lane-closure recovery with the same VSL actuator;
2. if that branch does not establish the information-to-decision link and its
   stopping reason leaves an analytical route meaningful, the lightweight
   conservative advice–merge–service admission screen;
3. if the VSL line then has a documented stopping reason, reopen ramp metering
   from the S01/F2 task-admission breakpoint around one specific omitted-
   information hypothesis.

If temporary recovery establishes decision relevance but gradients fail, the
next question is gradient meaning around hybrid reopening events; that is not a
negative result triggering the analytical fallback. Each successor requires an
explicit opening instruction and its own user gate.

## Final scope and status

No freeway simulator, controller, differentiable component, SUMO environment,
traffic experiment or gradient test was created or run. There is no remaining
decision gate inside the closed review. The next allowed action is to open the
temporary-closure recovery task-admission review when explicitly requested.
