# Review recap through the S10 methodology closure

As of 2026-09-30. Scope: this freeway review; not urban simulator development.
**Current position: S07 closed with localized Candidate A; S08 closed with the
full dual-step Candidate A. S09 opened the exact-prefix continuation and stopped
before execution because no SUMO provider was found; the user then reaffirmed
that concrete experiments are outside this methodology-only review. DG-R6
provisioning is withdrawn. S10 completed the static sufficiency audit, and the
user approved DG-R7 Candidate A to close the review with conditional findings.
No freeway traffic experiment or gradient validation has been performed.** The S01–S06 chain below
remains the scientific recap; current S07–S08 results are summarized at the end.

## 1. The central question and desired outcome

The question is **not** “Can we build a differentiable lane-aware simulator?”
or “Can speed control improve traffic?” Both have substantial predecessors.

The current research direction is:

> Identify when a strong aggregate response/history model loses information
> that changes useful common-speed-advice decisions, then test the smallest
> conservative refinement and its independently useful gradients.

The task anchor is a freeway narrowing. Infrastructure recommends the **same
speed to every lane in a road zone**; drivers and traffic interactions determine
actual movement. We are not commanding individual vehicles or lane changes.
The first proposed diagnostic is a homogeneous, permanent three-to-two lane
reduction. Temporary-closure claims would additionally require reopening and
recovery accounting. Historical “VSL” literature includes regulatory speed
limits; that is related evidence, not automatically the same advisory task.

### Core questions, in dependency order

1. **Is there a worthwhile task-specific information gap?** A strong aggregate
   model already knows spatial traffic amount, mean speed/response, queues,
   cumulative counts and relevant history. What useful distinction, if any,
   does it genuinely miss? Existing aggregate success is a serious alternative.
2. **Can the missing information change a useful decision?** Seek physically
   reachable situations that look identical through the declared aggregate
   history but differ in omitted information, initially lane allocation. Do
   they need different common advice after counting all traffic's waiting and
   travel? Different queues or a reversal between two poor actions is not enough
   if another common action works well in both situations.
3. **If so, what is the smallest adequate refinement?** Try conservative
   continuous lane/group statistics before classes, detailed order or full
   microscopic dynamics. Ending-lane mass, spatial placement and continuing-lane
   imbalance are candidates, not established minimum states.
4. **Can that refinement produce correct and useful gradients?** Eventually
   establish forward correctness, internal derivative correctness and improvement
   from gradient-guided advice in an independent richer evaluator. These are
   separate evidence obligations; none follows merely from differentiability.

Two meanings of “aggregate failure” must remain separate: **information loss**
means even the declared complete input/history cannot distinguish useful choices;
**model inadequacy** means one model uses available information poorly. We chose
to pursue the first claim, not silently substitute the second.

**Desired positive outcome:** a bounded information-to-decision result, a
justified compact representation, and independently useful sensitivities.
**Admissible alternatives:** strong aggregate control suffices in a specified
domain; extra detail brings insufficient value; or the required diagnostic is
infeasible/unjustified at acceptable cost. A failed bounded construction would
not prove universal aggregate sufficiency or task impossibility.

Fixed safeguards: same actions and accounting across models; no artificially
forgetful baseline; no invented merge penalty to force a result; prefer
deterministic conservative mass transfers. Control-dependent random discrete
mass shifts and reset/saltation machinery require exceptional justification and
separate approval. Server configuration is outside the current review.

## 2. The review chain

The progression is **choose a task → audit predecessors → sharpen the lost-
information hypothesis → audit its evidence logic → attempt a construction →
check reference mechanisms and preparation feasibility**. It is not six
successive model-development phases.

### S01 — Choose a freeway task worth investigating

Key findings:

- Aggregate speed control and its gradients already exist; those alone are
  not a new contribution.
- Driver response and lane-dependent merging plausibly affect advice outcomes,
  but evidence does not establish that extra state is necessary.
- Coordinated ramp metering did not reveal a comparably supported missing-
  information mechanism for this research question.

**Consequence:** narrow to common infrastructure speed advice upstream of a
lane reduction, rather than generic freeway simulation. Initially consider
aggregate response classes and lane refinement as hypotheses.

**Decision taken:** select the narrowed speed-advisory task for fuller review;
do not pursue ramp metering as the primary alternative. Recovery belongs in
temporary-event evaluation, not a separate control task.

[S01 findings and accepted gate](reporting/s01/s01_30_n1_user_gate.md).

### S02 — Check close predecessors and avoid a premature model ladder

Key findings:

- Strong aggregate models already represent imperfect mean response and speed
  history; response classes need not be the first refinement.
- A close lane-group control paper changes actions, objectives and optimization
  effort. Its improvements do not isolate the value of retained information.
- Lane models, speed sensitivities and recovery accounting have predecessors;
  the unresolved opportunity is information needed for useful decisions/gradients.

**Consequence:** abandon a mandatory “aggregate → response classes → full lane/
class model” construction sequence. First motivate one omitted-information
contrast under a fair common contract; lane allocation is the simpler initial
candidate, with response–lane association conditional.

**Decision taken:** choose “Route B,” the bounded evidence/contrast-refinement
route, before detailed model design. “Route B” is a review route, not a model.

[S02 findings](reporting/s02/s02_20_n2_findings_and_gate.md).

### S03 — Ask whether the lane contrast actually earns further work

Key findings:

- Continuing-lane balance and where merging occurs can matter; a single
  ending-lane share is not shown sufficient.
- The supplied lane-aware control paper does not establish an information-only
  advantage under our common advice action, nor useful gradient transfer.
- Existing transfer/storage concepts offer modeling ingredients, not an
  already validated continuous, differentiable closure.

**Consequence:** keep lane information as a conditional hypothesis, but do not
build a differentiable lane model. The immediate missing evidence is a reachable
matched-information case with consequential common-advice outcomes.

**Decision taken:** close this review and draft a separately gated diagnostic
plan. You explicitly endorsed the conditional contribution quoted above.

[S03 findings](reporting/s03/s03_20_rb_findings_and_gate.md).

### S04 — Audit what the diagnostic would actually prove

Key findings:

- Exact information loss differs from a particular model/observer's inadequacy;
  full history may reveal apparently hidden lane information.
- Preparation must be physically reachable. Different hidden past lane-entry
  assignments are different past forcing, not identical complete scenarios.
- Useful decision loss requires comparing the complete action menu and checking
  whether one common acceptable action remains; forward differences are weaker.

**Consequence:** retain exact matching of the declared strong history channel
and separate decision evidence from later minimum-state/gradient claims. The
numerical design remains prospective; its methodology was reviewed, not run.

**Decision taken:** pursue a source-grounded analytical/constructive example of
exact information loss, rather than switch to approximate observer comparison.
Close S04 and open S05 under methodology-only scope.

[S04 findings](reporting/s04/s04_20_rb_diagnostic_methodology_findings_and_gate.md).

### S05 — Attempt to connect hidden lane information to useful advice

Key findings:

- In a homogeneous free-flow subcase, conservative lane transfers can be
  invisible in aggregate histories. This is conditional early-preparation
  evidence, not a native near-narrowing certificate.
- With advice-independent fixed service and fastest-arrival dominance, slowing
  only adds/moves waiting. Highest advice is a common best action, even when
  hidden configurations have different fixed capacities.
- The proposed pulse menu omits continuously holding the highest advice;
  different preferred pulses would not rule out an untested common better action.

**Consequence:** the missing link is endogenous advice–merging/service coupling
that outweighs slowing's delay **and depends on history-unrecoverable information**.
A fixed lane-dependent penalty does not solve it. Adding the highest-advice
stress action was proposed, not approved.

**Decision taken:** choose the reference-first direction rather than invent a
merge law. After scope clarification, authorize documentary reference/methodology
review only—not SUMO execution. S05 is explicitly closed with partial conclusions.

[S05 plain-language findings](reporting/s05/s05_19_certificate_semantic_summary.md),
[closure and approved handoff](reporting/s05/s05_99_rb_certificate_sprint_closure.md).

### S06 — Check the reference mechanism and prospective preparation

Key findings:

- Native speed/gap/cooperation interactions and speed-dependent lane redistribution
  have precedents. They do not imply universally beneficial slowing or prove
  that extra lane information is required.
- Aggregate-observation advisory success and occupancy-conditioned lane-flow
  results strengthen the simpler alternative. Strong regulatory low-speed
  lane-drop results do not automatically transfer to our moderate advice response.
- The prospective40/60s decisions precede arrival in the required final400m under
  intended road-start/speed bounds. The80s snapshot is sparse under screened
  entry defaults. This is a conditional design deduction, not a SUMO result.

**Consequence:** there is a defensible mechanism basis, but neither a complete
joint information/decision certificate nor a justified minimum refinement.
The preparation contract needs reconsideration before further diagnostic design.
No server check or simulation was used.

**Decision:** retain the near-drop contrast and review reachable revised
preparations. The user approved this route on 2026-09-29. Entry conditions,
timing, anticipation scope, observability and the small preparation bank are
outputs of that next review, not settings approved by the route selection.

[Current S06 findings and decision gate](reporting/s06/s06_20_reference_bridge_findings_and_gate.md).

## 3. Where we stand now

**Established progress:** a focused task, credible strong baselines, sharper
information/decision standards, a conditional hidden-information construction,
a restricted fixed-service obstruction, and supported interaction mechanisms.

**Still unresolved:** a reachable case combining hidden strong-history information
with genuinely different useful common advice; then the smallest adequate
refinement and its independently useful gradients. No source or review result
has closed that chain, positively or negatively.

S07 has now determined that later decision times can populate the final 400 m,
but later timing alone does not preserve hiddenness. The old quota bank can create
lane-specific insertion queues visible in the strong history. A localized balanced
six-vehicle block is the smallest repair; native anticipation can still expose it.

The user selected S07's localized one-block preparation. S08 froze its 18 prefix
IDs, rational departure/block indices, exact observation/equality contract, pair
selection, budgets and failure labels. At [S08-UG1 / DG-R5](reporting/s08/s08_20_exact_prefix_planning_findings_and_gate.md),
the user selected full dual-step screening: all 18 preparations at both 0.5 s and
0.25 s before pair selection. The [S08 closure](reporting/s08/s08_99_exact_prefix_planning_sprint_closure.md)
defined a bounded future execution handoff. S09 performed a read-only provider
audit and found no local executable or matching Python API, but the subsequent
[scope correction](reporting/s09/s09_35_scope_correction_and_methodology_alternatives.md)
withdraws provisioning as a review gate. S08 is retained as a future empirical
protocol; current work is restricted to static or analytical methodology.
Earlier “Candidate A” labels are gate-specific and do not mean one unchanged
option throughout this review.

S10 establishes that S08 is sufficient for a bounded future exact-prefix
feasibility claim, but not for useful-decision, minimum-state or gradient claims.
The [S10 findings](reporting/s10/s10_20_protocol_sufficiency_findings_and_gate.md)
closed with that conditional result. The [closure and recovery map](reporting/s10/s10_99_vsl_methodology_review_closure.md)
records the final claims, and the [next-step plan](synthesis/s10/s10_post_closure_next_step_plan.md)
orders separately gated future branches without opening them.

For navigation to every protocol, source audit and closure, use the
[ordered reading guide](00_review_sequence.md). This recap is a snapshot; the
closure and decision inventory retain authority for the completed review.
