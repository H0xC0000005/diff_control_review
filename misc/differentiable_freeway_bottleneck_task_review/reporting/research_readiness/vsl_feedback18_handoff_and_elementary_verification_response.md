# Feedback 18: development handoff, rivals and the first elementary verification

**B-first review preparation and handoff complete:** the user accepts
the first target and authorizes local private alignment. Selected-model,
same-controller and case-query timing now replace outdated bootstrap
wording; the accepted specification is local to development. A remains
deferred, and no implementation/experiment is opened by this update.

[Alignment outcome and next development action](vsl_b_first_handoff_alignment.md)

**Current user decision and completed consolidation:** the matched B
pair comes first; A is deferred. The elementary specification now keeps
the same controller and fine evaluator, uses existing free-flow/X/Z
references, and separates derivative correctness from tuning performance.
A's later selection must preserve core assumptions/backbone and intended
behavior; simpler established alternatives remain open. No A survey,
traffic verification or private handoff update is performed here.

[Current B-first verification specification](vsl_b_pair_elementary_verification_specification.md)

**Latest execution:** the user authorizes the listed review plan.
The Zhang task-fit pass qualifies the common B design analytically and
isolates A's unresolved terminal state/boundary. Recommend first verifying
B0/B-gradient with A explicitly pending; the alternative is to qualify A
before the first comparison. No choice is assumed and no private handoff
update is performed.

[Current findings and scope choice](vsl_zhang_task_fit_findings_and_choice.md)

**Current user clarification:** B0 and B-gradient must use one
literature-supported base controller; the source need not have used gradient
optimization. The revised common Zhang-derived speed-setting candidate
and shared adaptations are proposed for review. Earlier two-source
optimizer attributions do not establish that controller.

[Current shared-controller proposal and correction](vsl_shared_controller_correction.md)

**Latest continuation, 2026-11-02:** the user selects per-case speed
optimization as the simpler first verification. The matched-B contract
is now delivered: the same constant advice, fine plant and complete TST
with objective-only or additional derivative feedback. Runtime control
and shared-controller training remain later work. Earlier proposals below
retain their historical scope; A's exact task adaptation and handoff
consolidation remain.

[Current per-case matched optimizer and contract gate](vsl_per_case_matched_controller_contract.md)

2026-11-02. **Discussion response saved for reading.** The literature-backed
stack is the user-selected implementation target. The comparison design
and next steps below are recommendations, not an approved experiment or
implementation plan.

**Clarification incorporated:** detail carried by the gradient is available
inside the simulator but deliberately omitted or aggregated by the baseline.
The central target is its contribution to updates without requiring explicit
representation of that detail in the controller.

**Rival requirement incorporated:** the principal rival must be borrowed
from literature or have established use in this task or a similar traffic
scenario. An invented aggregate baseline is not sufficient.

Feedback 18 resolves the outstanding model choice: **the literature-backed
VSL stack is the implementation target, and its own simulator comes first.**
The traffic-model review can close on that basis. What remains is a small
research-design task: define the first comparison clearly enough that an
elementary implementation produces interpretable evidence.

I recommend **one brief review of baselines and the first verification**,
followed by updating the existing handoff and opening development planning.
There is no need to reopen the traffic stack or begin another broad
literature review.

**Later execution, 2026-11-02:** the user approved the brief review-side
plan and its first rival-selection pass is now complete. Recommend the
published Zhang CTM/enumeration route, with explicit task adaptations
pending review. No comparator is adopted or implemented by this result.

[Current findings and source-route gate](vsl_literature_rival_selection_findings.md)

**Further discussion:** the user identifies the need for a common
gradient-receiving controller with a credible version that does not use
simulator derivatives. That controller is not fixed. The aggregate [1]
reference alone cannot identify the gradient contribution.

[Clarification of the matched comparison and remaining choice](vsl_matched_controller_gradient_comparison_clarification.md)

**Matched review opened and stopped at a choice:** after the user's
approval of the target and brief questions, the source/contract check
identifies a scalar-advice candidate pair. Current-case simulator queries
versus shared-controller training remain a methodological decision.

[Current candidate and feedback-timing gate](vsl_matched_controller_review_findings_and_gate.md)

## 1. The development handoff already exists; it needs alignment, not reconstruction

I checked `/home/zpz/repos/diff_freeway_vsl`. It already contains the complete
mathematical specification, source and adaptation records, analytical
reference cases, evidence requirements, and implementation workflow. No
simulator or approved implementation plan exists.

After the comparison design is settled, the handoff should receive two
updates:

- Record the meeting's model selection and remove the obsolete "awaiting
  model choice" status.
- Add a short specification of the first research verification: rivals,
  permitted information, action timing, objective, expected observations,
  and interpretation of negative results.

The developer can then prepare the first Phase A proposal. Software
architecture, numerical methods, component sequencing and executable
checks remain development responsibilities. Since the developer is you,
another extensive onboarding report would add little.

## 2. The rivals should distinguish simulator detail from optimization method

The user clarifies that the information is available in the simulator but
deliberately omitted or aggregated by the baseline model. The gradient
may account for its consequences even when the controller does not
explicitly represent it. This is a sound research target: simulator state,
baseline representation, controller inputs and derivative source are
different parts of the comparison.

For example, the simulator can retain separate A/B loads and their effects
on E merging, receiving and discharge. A model using aggregated A+B may
lose some of those paths. Differentiating through the detailed simulator
can let those effects influence an advice or controller-parameter update,
without adding separate lane loads to the controller's explicit inputs.
A performance benefit remains a hypothesis to test.

| Comparison | What changes | What it answers |
|---|---|---|
| **Detailed versus aggregated model representation** | Which available traffic detail is retained in prediction and sensitivity computation; controller inputs need not change | Does aggregation discard useful traffic effects or sensitivity paths? |
| **Gradient guidance versus objective-only scalar search** | How advice is selected within a declared representation and access setting | Does the derivative help compared with objective evaluations? |

An objective-only method querying the detailed simulator also encounters
lane effects through its returned TST. It is therefore a useful reference
for how effectively derivatives exploit the same simulator. A derivative
computed only through an aggregate surrogate need not retain the detailed
simulator's paths. An advantage involving different representations should
be attributed to that model-and-gradient pathway, rather than automatically
to optimizer superiority under an identical model.

The earlier response put too much emphasis on whether lane detail was
available at all. Its availability in the simulator is now explicit.
The short review should select a literature-supported rival, verify its
native aggregation and any necessary adaptation, and specify which model
supplies each derivative or objective query and when those queries are used. An observation-gap experiment is supplementary, not a required
central comparison for the clarified target.

Gradient-guided and objective-only versions of a rival remain useful
recommendations. They need not introduce repeated feedback control: the
selected task still chooses one constant advice. The clarification does
not decide whether the first study optimizes advice per episode or trains
parameters shared across episodes.

If a shared controller is trained, identical inputs at deployment still
produce the same deterministic action. Detailed simulator gradients can
improve how that shared action is learned without eliminating the input
ambiguity. This separate limitation does not invalidate the user's target
or require extra controller inputs.

### The principal rival must have literature support

The user further clarifies that the baseline/controller should be borrowed
from literature, or at least have established use for this VSL task or a
closely related traffic scenario. This is a requirement for selecting the
principal scientific rival. An aggregate model invented for this comparison
does not meet it merely because it omits information of interest.

Prefer faithful reuse of a published controller and its native predictive
model/representation. Where scenario adaptation is needed, identify what
the source establishes, what is retained and what is changed. At minimum,
the literature must support using that controller in the relevant traffic
setting; a generic citation to an optimization algorithm or model family
is not sufficient evidence of that fit.

The proposed short review must therefore start by selecting a supported
rival and checking its task compatibility. In particular, inspect its
native observations, retained traffic information, objective, action timing
and control variables. Determine whether a limited adaptation can fit the
selected once-chosen-advice task without changing the controller's core
method. Do not silently convert a repeated-feedback controller into a
different one-action method and attribute the result unchanged to its source.

Maximum advice, scalar search, the best shared action and deliberately
coarsened versions of our simulator can remain diagnostic or numerical
references. They do not replace the required literature-supported rival.
Any modified gradient-enabled version must likewise be distinguished from
the original published controller.

## 3. A useful first verification can be much smaller than a policy-training study

My recommendation is to reuse the existing A/B diagnostic pair and one
unconstrained reference case, under the selected traffic equations.

| Elementary observation | Reference or baseline | What it can establish |
|---|---|---|
| Reproduce the known one-step service difference between the A/B cases | Existing analytical hand calculation | The implementation retains the lane-information effect. This does not yet establish different useful advice. |
| Evaluate complete TST over the scalar advice range | Maximum advice and bounded scalar search | Whether advice matters, and whether the two cases appear to favor different actions. Finite search remains an approximate reference. |
| Check the complete derivative and its proposed direction | Independent objective differences and actual small advice perturbations | Numerical derivative correctness and local guidance within this simulator. |
| Compare detailed and aggregated representations | A literature-supported rival whose native model/observations and necessary adaptations are explicit, with advice evaluated in the same detailed simulator | Whether retained detail gives more useful predictions or update directions. Source fit and the query protocol must be established first. |

For a supplementary observation-gap diagnostic, a clean baseline is **the
best shared advice for the known pair**, accounting for its declared
probabilities. It allows the reduced observer to reason intelligently
about the hidden state instead of forcing an arbitrary equal-lane
reconstruction. The full observer can choose separately. Adding final-A
density supplies the existing compact-information rival.

This is an **information-limited decision baseline**, not a separately
constructed aggregate traffic simulator. It remains a useful diagnostic,
but does not replace the intended representation/gradient comparison.
The latter requires a literature-supported rival with a specified native
aggregation/closure and any necessary adaptations, qualified in the proposed
brief review before it can become an implementation target.

These observations can be developed incrementally: the static service
check first, complete forward accounting next, and derivative and decision
comparisons afterward. They use the selected stack while keeping scenarios,
controls and research machinery small.

Two boundaries should remain explicit:

- The diagnostic pair may share the same best advice. Its established
  service difference does not guarantee an advice gap. The unconstrained
  case should legitimately favor maximum advice.
- Correct derivatives and useful perturbations in this simulator establish
  numerical and methodological findings. They do not establish physical
  fidelity or superiority over scalar search.

The **immediate next deliverable I recommend is a short
comparison-and-first-verification brief**. It should first select and
qualify a literature-supported rival, then identify how simulator detail
reaches each method, distinguish per-episode advice from shared-controller
updates, and specify what each outcome would mean. Source/task-fit checking
belongs in that brief from the beginning. A broader novelty claim can be
assessed once the precise comparison is defined; it is not a prerequisite
for elementary numerical verification.

After that brief is agreed, synchronize the existing handoff and let
development planning begin.

## Supporting review documents

[Complete selected model and analytical qualification](../../synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.pdf)

[Existing prospective comparison and sensitivity evidence contract](../../synthesis/research_readiness/vsl_joined_candidate_verification_contract.md)

The original response was a read-only review and planning discussion.
Saving this note executes none of the proposed review, implementation
or experiment work.
