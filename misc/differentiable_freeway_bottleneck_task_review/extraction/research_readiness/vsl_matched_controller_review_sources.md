# Matched-controller review: primary readings and transfer limits

**Current scope:** the user selects the matched B pair first and defers
A. The elementary specification reuses the source/controller qualification
and existing analytical references; no new paper or A alternative is
surveyed in this consolidation. Delle Monache remains excluded.
A's future source/adaptation selection is open under the user's stricter
assumption/backbone and intended-behavior requirements.

[Current consolidated specification](../../reporting/research_readiness/vsl_b_pair_elementary_verification_specification.md)

**Task-fit continuation executed:** the common B adaptation is
analytically qualified; the separate A terminal model remains unresolved.
Zhang's cited FD source was traced only for that boundary question.
Delle Monache remains historical and excluded from the active proposal.

[Primary readings and exact limits of this pass](vsl_zhang_task_fit_sources.md)

**Current source status:** the user excludes Delle Monache from the
active controller/optimization proposal. Its entry below records historical
reading, not an adopted dependency. The working common-controller source
is Zhang; its exact task fit remains to be completed.

**Continuation, 2026-11-02:** the user has selected per-case planning
queries for the first verification. The conditional scalar pair supported
by this reading is developed in the current contract. Zhang supports
enumeration/objective feedback; Delle Monache et al. support direct
first-order VSL optimization. Nested uniform coverage, common probes,
constant advice and complete TST are our declared comparison adaptations,
not a published matched experiment. No new source results are claimed.

[Current per-case contract](../../reporting/research_readiness/vsl_per_case_matched_controller_contract.md)

2026-11-02. This reference list supports the
[matched-controller findings](../../reporting/research_readiness/vsl_matched_controller_review_findings_and_gate.md).
It records actual primary-source reading rather than a new comprehensive
controller survey. No source code, traffic simulation, optimization or
numerical gradient test is executed.

## [1] Zhang et al.: objective-feedback speed parameters

C. Zhang, E. Chung, N. R. Sabar, A. Bhaskar, and Y. Ma, “Optimisation of
variable speed limits at the freeway lane drop bottleneck,”
*Transportmetrica A: Transport Science*, vol. 19, no. 2, Art. no. 2033878,
2023, doi: [10.1080/23249935.2022.2033878](https://doi.org/10.1080/23249935.2022.2033878).

[Institutional manuscript](https://ira.lib.polyu.edu.hk/bitstream/10397/92568/1/Zhang_Optimization_Speed_Freeway.pdf)

**Reading in this pass.** Reopen the primary 44-page manuscript and reuse
the immediately preceding source checks of Section 3.2, PDF p. 12, and
Section 4.3, PDF pp. 19–21. The former specifies the control-parameter array
and the simulator fitness loop; the latter supplies the distinct enumeration
branch. This is a focused reading, not a new complete-paper/code audit.

**What is retained.** Evidence that direct speed-parameter optimization
from simulator objective evaluations is applied in this traffic setting.
No new shared policy architecture is attributed to the source.

**Our proposed adaptation.** One common continuous scalar advice, the
selected lane-resolved plant, finite cohort and complete-TST objective.
The source's spatial profile, discrete settings, actuator constraints and
reported best values are not copied as though already compatible.

[Fuller earlier source/version record](vsl_literature_rival_selection_sources.md)

## [2] Delle Monache, Piccoli and Rossi: a direct gradient-control precedent

M. L. Delle Monache, B. Piccoli, and F. Rossi, “Traffic regulation via
controlled speed limit,” arXiv:1603.04785, v1, March 15, 2016.

[Primary PDF](https://arxiv.org/pdf/1603.04785)

[Previously archived PDF](../../archive/full_text/FB0002.pdf)

**Actual reading.** Abstract and introduction, and Definitions 3.2–3.3 in
Sections 3.2–3.3 on PDF p. 13. Selected Section 4 numerical-method context
was checked. The earlier accepted
[derivative frontier](../n2_source_studies/response_lane_derivative_frontier.md)
is reused, not represented as a new derivation here.

**Decision-relevant source facts.** The control is a time-varying speed
limit for free-flow LWR with a target-outflow cost. The random exploration
uses endpoint-valued speed sequences, while the gradient procedure uses
numerically evaluated one-sided cost variations and first-order descent.
This is not an AD implementation certificate or a native lane-drop/full-TST
experiment.

**Consequences for the candidate.** It supports the direct gradient-speed
optimization family. It does not justify an endpoint-only B0 for our
continuous scalar action, transfer the PDE gradient to the selected congested
lane-cell model, or prove ordinary derivatives at our native switches.
Those are our methodological deductions, not source claims.

No reported numerical percentage or computational result from this paper
is used to predict our performance. No journal-version equivalence is
assumed; the cited preprint version is explicit.

## Local mathematical and information inputs

- [Complete selected member](../../synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.tex),
  Sections 1, 5, 7–8: fixed finite cohort, initial observation pair,
  complete residual, regular derivative and admitted decision timing.
- [Analytical regularity addendum](../../synthesis/research_readiness/vsl_methodology_review_analytical_addendum.tex),
  finite branch intervals and the free-regime maximum-advice result.
- [Prospective evidence contract](../../synthesis/research_readiness/vsl_joined_candidate_verification_contract.md),
  controller observation, equal-information reasoning, strong scalar
  optimizer references and the qualification needed for changed histories.
- [User clarification and matched comparison](../../reporting/research_readiness/vsl_matched_controller_gradient_comparison_clarification.md):
  simulator detail may influence updates without explicit controller
  features; B0 versus B-gradient must preserve the forward plant.

## What this pass does not establish

The candidate direct scalar pair is conditional on a per-case planning-query
protocol. It is not a literature-qualified learned aggregate-observation
controller. It gives no numerical competence claim against A, no novel-
gradient-control claim, and no result about generalization or the value
of the hidden A/B split. The two optimization timings in the findings
are alternatives for the next user decision, not silently selected
experimental settings.


## 2026-11-02 — feedback meaning and exact borrowing boundary

Reopen the institutional Zhang manuscript, Section 3.2 PDF p. 12 and
Section 4.3 PDF p. 21; distinguish CTM enumeration from Aimsun/GA queries.
Reopen Delle Monache et al. v1 Definitions 3.2–3.3 on PDF p. 13 and
Section 4.2/Algorithm 1 on PDF pp. 15–16. The latter distinguishes
precomputed optimized controls from instantaneous feedback.

Interpretation: B0 has objective feedback without supplied derivatives;
both proposed B versions execute constant advice. The fine-plant
enumeration/gradient pair and its numerical comparison rules are explicit
adaptations. No paper is credited with this exact pair, our lane-cell
sensitivity or its numerical performance. No new paper, source code or
experiment is inspected. The existing contract gate remains unchanged.

[Question and detailed answer](../../reporting/research_readiness/vsl_matched_feedback_and_borrowing_clarification.md)

## 2026-11-02 — exact algorithm units and target-task eligibility

Recheck Zhang Section 2/equation (1), PDF pp. 7–9, Section 3.2 p. 12
and Section 4.3 p. 21. Recheck Delle Monache et al. Section 2,
Definition 3.3 and Section 4.2.3/Algorithm 1, PDF pp. 15–16.
No new source or author code is introduced.

Compare the borrowing assumptions with the existing complete-member
Section 7 and analytical addendum Section 3. Finite-candidate ranking is
independent of the objective's traffic form. Local first-order eligibility
instead needs the target's regular derivative, which the earlier analysis
establishes. The native sensitivity is not transferred.
The grid schedule, target cost/action and safeguarded search rules remain
explicit adaptations; numerical and physical success remain unproved.

This tightens the earlier similar-task-support statement: precedent is
necessary context, not automatic permission to transfer task-specific
assumptions or conclusions. No algorithm is user-selected in this exchange.

[Exact mapping and eligibility findings](../../reporting/research_readiness/vsl_algorithm_borrowing_and_transfer_findings.md)

## 2026-11-02 — qualify the common controller rather than two optimizers

The user fixes the same-base-controller requirement; prior gradient use
by the source is unnecessary if the common controller admits gradient
optimization. Recheck Zhang Section 3.2, PDF p. 12, for speed-parameter
representation and simulator evaluation; Section 2, pp. 8–9, for the
native action constraints; Section 4.3 p. 21 for separate enumeration.

The common candidate is one adaptation of that speed-setting design in
both arms. The continuous common advice/action constraints, plant and
complete objective are shared adaptations. Controller outputs at a fixed
parameter are identical, not empirically similar source policies.
The gradient pathway uses our own complete derivative; no source
optimizer is differentiated. The source's discrete constraints are not
silently kept in B0 while removed from B-gradient.

Delle Monache's factual reading and first-order precedent are retained,
but its loop is no longer proposed as a second base controller.
No source certifies numerical competence of our common adaptation.
The candidate remains provisional; no new paper, controller code,
traffic experiment or gradient experiment is inspected.

[Current correction and common-base proposal](../../reporting/research_readiness/vsl_shared_controller_correction.md)
