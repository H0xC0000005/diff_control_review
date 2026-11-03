# Review discussion log

## 2026-10-29 — independent review repository and VSL handoff

Feedback 17 approves the prior bridge proposal and requests two standalone
online repositories. All original misc collections are imported with
source/export hashes. Referenced local context is archived separately;
exported Markdown navigation is made portable, without changing traffic
equations or the original source tree. Broken historical relative paths
are repaired only when ancestor context identifies one existing target;
the complete issue/repair inventory remains in migration.

The review-to-development boundary remains explicit: this repository
establishes the current model, analytical findings and evidence obligations;
the VSL development agent proposes software/validation planning in its own
repository. Bootstrap is documentation/repository work only. See
migration/README.md and the VSL START_HERE.md for the handoff.

## 2026-10-29 — review public, VSL private

The original bootstrap completed before the interrupted turn returned.
The user's new instruction explicitly makes the review repository public
while keeping VSL private. Update repository settings, current root guidance
and publication receipts accordingly; preserve the imported scientific archive
and the history of the initial private bootstrap. Development still begins
with Phase A planning, and no simulator or experiment is opened.

## 2026-10-29 — prepare shared requirements without a common architecture

**Question and approved response.** The user points out that both versions
can require different components and interactions, so a detailed Phase A
compatible with both may be premature. The user is also the developer;
separate onboarding is unnecessary. Revise the proposal to a bounded
preparation note, then execute it and stop at the checkpoint or an ambiguity
that would alter backbone behavior. This supersedes the earlier suggestion
to open a provisional implementation proposal before the model choice.

**Finding.** The research question, elementary decision setting, complete
time-accounting meaning and evidence/fairness principles can be reused.
Their mathematical realization cannot be conflated. In particular, the
old uniform approach and empty terminal do not admit the new congested
near-choke initialization unchanged. Advice/capacity coupling, service
sharing, retained recovery history and derivative construction also differ.
Record these as known selection consequences; do not repair them with a
common interface or combine the mechanisms. No new backbone ambiguity
requiring an amendment is found. Colleague concerns are limited to those
actually recorded; no final consensus or additional objection is invented.

**Deliverable and stop.** [Preparation note](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_model_choice_preparation.md). It supplies common
requirements, a qualitative selection-impact table and the subsequent
entry into one full Phase A after model choice. The peer-backed baseline
remains provisional, and no model selection or implementation phase opens.
Only current root navigation/context/decision records and the new note
plus its document-check record are written. Migrated scientific records,
source feedback, both implementation repositories and all model/PDF/TeX
contracts remain untouched.

**Checks.** Source reading uses rg and sed. Document checks use installed
Python and standard-library hashing/link inspection; no traffic arithmetic
or experiment is executed. Staged helpers are
`/tmp/vsl_model_choice_preparation_20261029/prepare_changes.py`,
`apply_changes.py` and `validate_changes.py`. Preparation is run with
`/home/zpz/miniconda3/envs/differential_sim/bin/python` followed by each
helper path; the apply helper alone requires filesystem escalation to
write the standalone review repository.
[Document-check result](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_model_choice_preparation_validation.json) records the permitted file changes,
source preservation and working links. Full Phase A remains deferred
until the user selects a version and authorizes its opening.

## 2026-10-29 — SUMO server and remote GUI preparation

The user adds a preparation topic independent of the unsettled VSL model
choice: check whether Ubuntu can support programmable SUMO, preferably
libsumo, and a GUI visible on a Windows 11 SSH client. This task requests
feasibility and setup guidance, not installation or traffic experiments.

Read-only inspection confirms Ubuntu 24.04.4/x86-64, Python 3.12, no SUMO
in the inspected paths/environment, installed xauth and configured X11
forwarding. Compatible SUMO 1.28.0 application/libsumo wheels exist. The
recommendation is an isolated installation with matching versions: libsumo
for runs without a GUI and TraCI with sumo-gui for visible sessions.
libsumo GUI is explicitly experimental on Linux. Windows X11/OpenGL
rendering and possible missing GUI runtime libraries remain unverified;
server inspection alone cannot close that visual checkpoint. An initial
sandbox GPU failure is resolved by a successful read-only escalated check.

[Assessment, official references and setup sequence](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/sumo_server_preparation_assessment.md).
An authorized setup pass can finish at import/executable checks, a stock
example, a TraCI GUI session and a saved image, with user confirmation of
the Windows display. No VSL model is selected, SUMO validation requirement
reintroduced, implementation phase opened, package installed or traffic
experiment performed by this assessment. The prior model-choice
preparation checkpoint and pending selection retain their status.

## 2026-10-29 — tailored SUMO installation guide and dummy checks

The user asks for documentation review and an installation procedure
meeting the Python/libsumo and Windows-visible GUI requirements, including
local dummy tests. This authorizes writing the guide and its small
installation-check helpers, not executing installation or simulations.

[Guide](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/sumo_installation_guide.md) supplies one pinned isolated installation route, two
small cases, libsumo/TraCI control checks, MobaXterm X11/OpenGL diagnostics,
PNG export, acceptance criteria and version records. The helpers query
traffic, change one car's maximum speed and require every car to finish
without teleporting. They do not implement either research traffic model.
A GUI file/command pass is kept distinct from Windows visual confirmation.

[Source reading, checks and scope](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/sumo_installation_guide_work_record.md). Static Python/XML,
shell-syntax, link and preservation checks are performed; network
conversion, SUMO execution and end-to-end rendering remain untested.
Existing model decisions, the preparation checkpoint and both implementation
repositories are preserved. The next possible action is an authorized
installation/check pass following this guide; no continuation is started.

## 2026-10-29 — exported video replaces required live GUI

The user clarifies that the purpose is to visually understand/check a
scenario, and accepts exported video downloaded to Windows. They request
a guide revision if that makes the procedure easier. It does simplify
the PC/network requirement: ordinary file transfer replaces X11 forwarding.
The server still needs virtual-display/OpenGL rendering and an encoder.

The [revised guide](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/sumo_installation_guide.md) makes Xvfb/Mesa plus native PNG capture and
external FFmpeg MP4 encoding the default. This avoids a requirement for
built-in SUMO FFmpeg support or experimental libsumo GUI. Bulk numerical
work can still use libsumo. Live TraCI GUI remains optional. The checker
adds complete frame accounting, encoding/probing/decode checks and
explicit playback rate; its traffic inputs/control/completion stay intact.

[Reading scope and verification](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/sumo_installation_guide_work_record.md). The earlier guide/helper
package and check record are preserved together. Static checks do not
claim a produced video; no installation or SUMO/encoder run occurs.
User inspection of the downloaded movie completes visual acceptance.
No scientific backbone choice or new VSL implementation activity opens.

## 2026-10-29 — locate and correct the SUMO GUI shutdown wait

The user reports a silent idle video-check run and asks what is happening
and how to locate/fix it. Read-only host inspection and partial outputs
locate the wait after traffic completion: 93 images and all 12 trip
elements exist, Python waits for a child, and sumo-gui remains in its event
loop. The helper omitted --quit-on-end. Fontconfig warning is not the
blocking condition; it recurred in a successful corrected run.

Add GUI auto-exit, progress messages/progress.json and a delayed Python
stack dump; retain complete-output checks. Correct guide shell setup and
replace the unnecessary rg filter with grep. An independent bounded copy
of the installation example passes, with 93 native frames and an 18.6 s
MP4 that fully decodes. The original run is not terminated or modified.

[Diagnosis and evidence](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/sumo_gui_shutdown_troubleshooting.md). Windows playback remains the user
check. This is installation troubleshooting, not VSL scientific evidence;
model selection, review contracts and both implementation repositories
retain their status. No packages or system settings are modified.

## 2026-10-30 — explain speed advice, congestion and total system time

**Question and request.** After confirming successful SUMO installation,
the user asks how the literature-backed VSL model generates delay without
an extra E-forced-merge penalty, then requests an explicit account of what
changes when advice increases and how diminishing returns could arise.
The user asks to preserve that explanation as PDF or Markdown for paper
or presentation use. This is explanatory documentation, not a new model
selection, implementation task or traffic experiment.

**Answer.** At a fixed traffic state, higher advice increases or leaves
unchanged sending offers; receiving, density-dependent ceilings, lane-change
desires and priorities are not directly changed. Actual service remains
constrained and can be redistributed. Later density changes depend on
arrivals versus departures: faster clearing can help, whereas concentrated
arrivals, shared A service, capacity drop and spillback can hurt. Travel-time
savings shrink with further equal speed increments; bottleneck saturation
can limit additional completion. Lower advice has a conditional congestion
benefit and an opposing travel-time cost. It does not automatically create
extra merge preparation, and relocating a queue without changing cumulative
exits does not reduce complete TST.

**Evidence boundary.** The note interprets the existing equations and adds
no law, calibration, numerical result or optimum certificate. Maximum advice
is optimal in the established unconstrained small-cohort regime. A benefit
from lower advice, different optimal advice for the hidden A/B pair, an
interior optimum and useful numerical gradients remain open. The current
topic is communication of the traffic mechanism; the prior model-choice
hold remains. Further colleague discussion is the next allowed activity.

[Explanatory note](misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_speed_advice_and_total_system_time.md)

**Files and checks.** Add that Markdown note and its REVIEW_INDEX entry;
append this discussion record. Source reading uses rg and sed against the
finalized report, complete model and analytical review. Stage and validate
with `python3 /tmp/vsl_speed_tst_note_20261030/prepare_delivery.py`, apply
only these three files using the staged `apply_delivery.py` with filesystem
approval for the standalone review repository, then run the staged
`validate_delivery.py` and `git diff --check`. Checks cover local source
links, exact staged bytes, preservation of existing index/log text and
preservation of all other review files. No code, packages or traffic runs
are involved. The standalone note has no substantial mathematics requiring
a LaTeX companion; the user explicitly accepts Markdown.

## 2026-11-02 — archive the feedback-18 response

**User decision and question.** Feedback 18 selects the literature-backed
VSL stack for implementation, starting with the written simulator rather
than SUMO. The user asks how to complete the handoff, define credible
aggregate-information rivals and start with elementary verifications.
They authorize reviewing/planning only, then explicitly request saving
the long response to a file for easier reading.

**Response and recommendation.** Reuse the existing VSL bootstrap and
complete specification. Recommend a short comparison-design review to
define observation/gradient access and minimal baselines, then align the
handoff and open development Phase A. Separate information access from
optimization method and repeated feedback control. Reuse the analytical
A/B diagnostic and an unconstrained reference; the best shared advice
is an information-limited decision reference, not a new aggregate
simulator. Positive advice gaps and gradient superiority remain unproved.

[Saved response](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_feedback18_handoff_and_elementary_verification_response.md)

**Scope and checks.** Add the Markdown response and index link and append
this log entry. These document the user's model decision and recommendations;
they do not approve or execute the proposed follow-on review, synchronize
the private development repository, or start implementation/experiments.
The existing handoff files retain their prior bytes pending an authorized
alignment task. The user's feedback inbox is preserved. Stage using
`python3 /tmp/vsl_feedback18_response_20261102/deliver.py prepare`, apply
with its `apply` mode under the required filesystem approval, then run
`validate` and `git diff --check`. Check local links, delivered bytes,
existing index/log prefixes and preservation of all other review files.
The next proposed action remains the short comparison-design brief;
its scope and recommendations await discussion.

## 2026-11-02 — clarify information carried by the gradient

The user clarifies that the information is available in the simulator but
deliberately omitted or aggregated by the baseline. The gradient may account
for it without the controller explicitly representing it. Accept that
meaning and distinguish simulator state, baseline representation, controller
inputs and derivative source. A detailed gradient can retain sensitivity
paths lost by the aggregate model. A benefit remains unproved.

Correct the active feedback-18 response: make representation/gradient effects
central, with the observer information-gap comparison supplementary.
Objective-only detailed-simulator queries also reflect lane effects via TST;
they remain useful strong references. Per-episode optimization versus shared
training, aggregate closure and derivative/query protocol remain open for
the proposed short review. No new experiment or traffic-model change is
approved by this clarification. Preserve earlier discussion as chronology.

[Updated response](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_feedback18_handoff_and_elementary_verification_response.md)

Update only that response and append this log. Use the staged helper at
/tmp/vsl_gradient_detail_clarification_20261102/update.py with prepare,
apply and validate modes, obtaining the required outside-workspace write
approval for apply. Verify payload hashes, original log prefix and local
source links, and run git diff --check. The full model, private VSL handoff,
user feedback, code and experiment scope remain unchanged.

## 2026-11-02 — require a literature-supported principal rival

**User clarification.** The baseline/rival should be borrowed from the
literature, or its use should at least be established for this task or a
similar scenario. Accept this as an explicit requirement. A deliberately
invented aggregate closure is not an adequate principal scientific rival.

**Proposal correction.** Update the active feedback-18 response to make
source-backed rival selection and task-fit verification the first work of
the proposed short review. Prefer faithful reuse; identify the source's
observations, aggregation, predictive dynamics, objective and action
timing, and disclose necessary adaptations. Generic algorithm citations
alone do not establish traffic-task suitability. In particular, check the
once-chosen-advice contract before adapting feedback controllers.
Keep maximum advice, scalar search, best shared advice and controlled
coarsening as supplementary diagnostics/numerical references, without
presenting them as the required literature-supported controller.

No particular paper or controller is selected by this terminology
discussion. The traffic stack remains fixed; the proposed review is not
executed or approved as an implementation/experiment plan. The open
comparison questions about derivative sources and per-episode versus
shared-controller updates retain their status.

[Updated response](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_feedback18_handoff_and_elementary_verification_response.md)

Update only that response and append this log. Use the staged helper at
/tmp/vsl_literature_rival_clarification_20261102/update.py with prepare,
apply and validate modes, using filesystem approval for the outside-root
write. Check exact payloads, source links, prior log preservation and
git diff --check. No full model, implementation repository, user feedback,
packages or traffic experiments change.

## 2026-11-02 — execute the bounded literature-rival selection review

**Authorization.** The user accepts the brief review-side plan and requests
execution, stopping at the next gate or a methodological choice. Execute
only the first item, selecting and qualifying a published rival route.
The selected lane-resolved stack stays fixed. A review does not authorize
simulator development, dependency installation or traffic experiments.

**Finding.** Recommend Zhang et al.'s aggregate CTM plus enumeration.
Section 4.3 supplies a real aggregate speed-selection precedent at a lane
drop, distinct from its microscopic GA branch. This is a better elementary
source route than importing an entire rolling-horizon controller merely
because its traffic-model ancestry is shared. Han's flow decisions/cost,
Hegyi's feedback/speed state, Jin–Jin's boundary actuation and Wei's
future-controller discussion are qualified separately.

**Gate and limits.** The proposed common-advice, finite-cohort, complete-TST,
state-projection and choke-boundary changes are task adaptations, not
published results. No final adapted baseline contract is claimed.
Source-route adoption is the next user decision. If accepted, comparison
design must close those scientific interfaces before elementary verification
and final handoff. Different traffic laws mean this is initially a
model-and-gradient contrast, not attribution to lane aggregation alone.
The same-plant objective-only reference remains important. Numerical benefit,
an interior optimum, a positive A/B action gap and physical fidelity stay open.

[Main report and recommendation gate](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_literature_rival_selection_findings.md)

[Primary references and reading limits](misc/differentiable_freeway_bottleneck_task_review/extraction/research_readiness/vsl_literature_rival_selection_sources.md)

**Records and checks.** Add the main report, source list, work record and
document validation JSON. Synchronize the active proposal and review
navigation/context/decision records with feedback 18 and this pending
recommendation. Preserve the original feedback, scientific PDFs/LaTeX,
archives and both implementation repositories. Use the staged delivery
helper and git diff --check as recorded in the linked work report.
No numerical traffic/AD experiment, package install, code change,
commit or push occurs. Stop at the source-route gate.

[Work scope and document checks](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_literature_rival_selection_work_record.md)

## 2026-11-02 — clarify the rival's rules, optimization and gradient compatibility

The user asks whether reference [1] is rule-based, whether its optimization
uses gradients or state, and whether it can support gradient optimization.
Recheck the primary manuscript's Sections 3 and 4.3 and practical discussion
on PDF p. 22/Figure 19. Distinguish objective-driven GA/enumeration from
demand-conditioned practical application and proposed half-interval feedback
search. State conditioning and derivative use are different dimensions.

The recommended CTM branch is a published non-gradient speed-search
reference. A continuous speed-parameter gradient variant is a possible
adaptation, not yet qualified: discrete choices, a hard capacity-drop
switch and regular-branch derivatives require explicit treatment.
Differentiate the rollout's objective with respect to controls, not the
GA/enumeration algorithm. No relaxation, smoothing, controller variant,
simulator change or experiment is approved.

Append the clarification to the findings and source record; preserve the
recommendation's pending status. Record this exchange here. The earlier
source-gate validation JSON remains its original delivery record; this
later editorial change has its own guarded checks via
/tmp/vsl_rival_controller_clarification_20261102/save.py prepare/apply/validate
and git diff --check. Only these three documents change. The selected plant,
private implementation repository and original user feedback stay untouched.

## 2026-11-02 — the matched controller without simulator derivatives is missing

**User questions.** The user accepts the proposed source-task adaptations
in principle, asks whether the gradient-receiving controller is still
unfixed, and argues that an intermediate version of the same controller
using aggregate information without simulator gradients is required.
They ask what the review actually establishes on these points.

**Answer and source check.** Confirm that no common gradient-receiving
controller has been selected. The earlier equal-information/objective-only
comparison principle did not identify and qualify a concrete matched
controller. A direct aggregate-reference versus unrelated gradient method
comparison could test overall performance, but would not identify the
simulator-gradient contribution.

Recheck [1] Section 3.2, particularly the speed-parameter representation
and fine-simulator fitness evaluation on PDF p. 12. It supplies a possible
source-backed objective-feedback workflow; no gradient counterpart,
learned policy or performance equivalence is established. A simple common
speed parameter may suffice for the first task, but that versus a shared
controller remains unselected. The absence of a native gradient optimizer
does not prove the speed parameters cannot receive gradients.

**Proposal amendment.** Retain the aggregate CTM/enumeration as a candidate
performance reference. Make the missing matched-controller pair explicit:
same controller/parameterization and explicit aggregate input contract,
same detailed forward plant and objective, credible objective-only versus
simulator-derivative updates. Account for data/query/computation costs.
Do not remove lane detail from the no-derivative plant. No-simulator-gradient
methods may use other derivatives, so label the distinction accurately.
Baseline competence is a future empirical check, not a review result.

The user's description of adaptations as non-methodological is corrected:
action, objective and completion changes affect scientific comparison
meaning even with a fixed plant. Acceptance in principle does not make
those interfaces merely mechanical or close their specification.

[Discussion response](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_matched_controller_gradient_comparison_clarification.md)

Update the findings, active feedback-18 response, primary-source record and
current context; preserve prior chronology and source-screen findings.
No controller architecture is adopted, no experiment is run and no private
handoff is changed. The gate remains open with the common controller as
the next bounded scientific question. Staged helper:
python3 /tmp/vsl_matched_controller_20261102/deliver.py prepare/apply/validate.
Apply requires outside-root filesystem approval. Verify exact payloads,
source links and the original log prefix, then git diff --check.
Earlier delivery validation records retain their historical scope.

## 2026-11-02 — open matched-controller review; stop at simulator-feedback timing

**Authorization.** The user accepts the brief target/questions and requests
opening the review. Execute primary-source reconciliation and analytical
task reasoning, stopping at a recommendation gate or methodological choice.
No implementation or traffic experiment is authorized.

**Source finding.** A simple direct speed parameter is a possible common B.
Zhang supplies parameterized speed search and objective feedback from a
fine simulator. Delle Monache/Piccoli/Rossi supply a direct VSL gradient
optimization precedent. Recheck the latter's introduction and Definitions
3.2–3.3: its random exploration uses endpoint-valued time sequences, while
the gradient method uses cost variations. Do not transplant that endpoint-only
comparator as B0 for a continuous scalar interval. The selected lane-cell
contract, not the source PDE, supplies our complete regular derivative.

**Candidate and limits.** B0 uses objective-only bounded speed search and
B-gradient uses complete simulator sensitivities, holding the scalar action,
forward plant and objective fixed. This is a source-supported adaptation,
not a new neural-controller architecture or a published matched experiment.
Scalar objective feedback is not an E/A+B state-observation vector.
Numerical correctness, competence against A and gradient advantage remain
unproved; maximum advice and strong scalar search remain serious references.

**Choice and stop.** Per-case queries may reveal hidden lane effects through
costs or derivatives before final advice. A shared controller evaluated only
on identical aggregate observations must instead output the same action.
Both can issue one constant speed in an executed episode, but they define
different information and training/planning protocols. The user's simulator-
detail clarification does not choose between them. Recommend the per-case
scalar pair for the first elementary optimizer/gradient verification, with
that narrow claim; it does not establish a shared-policy training result.
Stop at this methodological choice without selecting an option.

[Findings and candidate comparison](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_matched_controller_review_findings_and_gate.md)

[Actual primary readings and transfer limits](misc/differentiable_freeway_bottleneck_task_review/extraction/research_readiness/vsl_matched_controller_review_sources.md)

Add the findings/source/work/check records and synchronize active proposal,
clarification and navigation/context/decision records. Preserve original
chronology, complete model equations, private VSL tree, user feedback and
urban implementation roots. The staged delivery helper and document checks
are recorded in the work note. No code, package, simulation, optimizer run,
training, commit or push occurs. After the user's protocol decision, the
next work is to complete only that common-B comparison contract; it is not
opened automatically by this report.

[Work scope and checks](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_matched_controller_review_work_record.md)

## 2026-11-02 — per-case optimization selected; matched-B contract delivered

**User decision and question.** The user chooses optimizing each case as
the simpler first verification. They emphasize episode-specific gradient
information and the possible later value of a current optimization
direction for runtime use; they ask to continue with per-case optimization.

**Review answer.** Define B as the bounded scalar advice. Propose B0 as
objective-only nested uniform enumeration with global interval coverage,
and B-gradient as bounded first-order search with full-cost checks and
step shortening. Match the reset cohort, fine lane-resolved plant, exact
complete TST, case-independent start/common probes, feasible action and
best-evaluated incumbent. Include interior speeds; do not transplant the
endpoint-only random comparator from Delle Monache et al.

**Source and interpretation.** Zhang supplies traffic-task precedents for
enumeration and objective-feedback speed optimization. Delle Monache,
Piccoli and Rossi supply a first-order VSL precedent. The scalar/common
action, exact complete objective and matched query rules are our task
adaptations; the latter source's PDE derivative is not transferred.
Use the selected plant's full regular derivative, including residual effects.

Per-case query histories may expose the consequences of hidden A/B detail
through both costs and derivatives. The derivative is a richer response
channel by design, without raw lane features at the optimizer input.
The historical observation-only shared-action bound does not govern this
pair. Preserve it conditionally and add an explicit timing amendment.
Do not claim a shared-policy or runtime-control result.

**Gate and remaining questions.** The matched-B definition is delivered
at its planned contract gate. Per-case timing is selected; concrete search
families and comparison details remain recommendations for acceptance.
No new methodological fork is needed in this continuation. Numerical
derivative correctness, local usefulness, search benefit, physical
validity and a positive action-information gap remain unproved.
A's exact common-advice/cohort/boundary/complete-TST mapping is the next
remaining review topic, followed by elementary-target/handoff consolidation.

[Current contract](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_per_case_matched_controller_contract.md)

**Records and checks.** Add the contract, work record and validation JSON;
synchronize active topic/proposal/navigation/source status and append
this decision/discussion. Preserve prior log/decision prefixes, all
unrelated review files, full model equations/PDFs, private VSL tree and
original urban roots/user feedback. Use the guarded prepare/apply/validate
helper in /tmp/vsl_per_case_contract_20261102 and git diff --check;
outside-root delivery needs filesystem escalation. No simulator/optimizer
code, package install, traffic/AD experiment, training, commit or push
occurs. Stop at this contract gate.

[Work scope and document checks](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_per_case_matched_controller_work_record.md)

## 2026-11-02 — B0 feedback and literature borrowing clarified

**User question.** Can B0 be understood as grid probing with no feedback
in the sense of no optimization-direction hint, while B-gradient supplies
that direction? Can the methods be borrowed or must they be adapted?

**Answer.** The directional distinction is useful but no-feedback is
ambiguous. B0 receives TST values and can compare tried speeds; the fixed
grid does not steer probes by a supplied derivative. B-gradient adds a
local sensitivity to guide trials, still checked against complete TST.
Both execute constant advice; neither is an online state-feedback
controller. Objective-only adaptive search can also use earlier costs;
the proposed grid is not a claim that value-only methods lack direction.

Primary passages distinguish Zhang's CTM enumeration and Aimsun/GA loop,
and Delle Monache et al.'s first-order method and precomputed-control
timing. Borrow the published method principles, explicitly adapt the
plant, scalar action, cohort/objective and matched-query/search rules.
Do not call the proposed pair an unchanged published controller or
transfer source gradient formulas, proofs or performance.
This meets the agreed similar-task method-support criterion, rather
than a literal-reproduction criterion.

The contract and source record now make these distinctions explicit.
No optimizer choice is approved by asking this question; the existing
matched-B contract gate remains. A compatibility and later consolidation
are not executed. Guarded delivery and checks are recorded in the work note.
All unrelated review/model files, private VSL files and original
feedback/urban roots are preserved. No code, experiment, install or Git
publication occurs.

[Detailed answer](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_matched_feedback_and_borrowing_clarification.md)

## 2026-11-02 — name the borrowed algorithms and check migration eligibility

**User requirement.** Identify the overall algorithm from each work and
its exact adaptations. Extra simulator information may be left unused.
A scenario change needs a task-fit explanation; changing the task itself
needs additional justification or evidence. Do not assume applicability
from a literature precedent alone.

**Answer and refinement.** The previous family-level description was too
broad to establish task eligibility. Identify the enumeration unit for B0
and Algorithm 1's first-order outer loop for B-gradient. Source physics,
action constraints, sensitivity formula and empirical conclusions are
not transferred. The matched pair remains an explicit adaptation, not
an unchanged source controller.

Even B0 changes the task objective/action. Its finite-candidate rule only
needs feasible candidates and well-defined comparable scores; best-observed
selection then follows without continuity or a specific traffic law.
For B-gradient, recheck the complete-member Section 7 and analytical
addendum Section 3: exact full-cohort TST, complete sensitivity and smooth
advice intervals provide the needed target-specific local justification.
This does not qualify native switches or prove numerical performance,
global convergence or physical validity. Future numerical evidence is
still necessary for those empirical claims, not a new review experiment.

The simulator's extra state can remain internal to the declared
cost/sensitivity interface. No shared learned-controller claim or
information-exclusive-to-gradients claim follows.

**Scope and status.** Retain the proposed pair with tighter attribution
and a conditional local eligibility conclusion. No new methodological
fork or traffic-law change is required, and no proposed algorithm is
approved by this question. Stop at the existing matched-B contract gate;
A's distinct predictor/task compatibility remains later work.

Add the findings and document-validation JSON, synchronize the active
contract/source/current-context records, qualify earlier sufficiency
wording, and append this exchange. Preserve unrelated reviews and model
PDFs/LaTeX, the private VSL tree and original feedback/urban roots.
The helper/commands and preservation checks are recorded in the work
note. No code, traffic or AD experiment, install, commit or push occurs.

[Findings and exact adaptation arguments](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_algorithm_borrowing_and_transfer_findings.md)

## 2026-11-02 — distinguish one controller from its gradient/no-gradient tuning

**User objection.** The two-source presentation appears to compare different
models and task assumptions, weakening the no-gradient/gradient ablation.
The user wants one base controller in both versions; separate similarity
evidence would be needed for distinct control designs. Previous gradient
optimization in the source is unnecessary if the shared controller can
support it.

**Correction.** I conflated the controller with its optimizer. The written
B pair already shared a constant advice map, plant and complete TST;
Delle Monache's native dynamics/objective were never actually imported.
Nevertheless, citations to two outer loops did not qualify a common
literature-supported controller. Withdraw that two-source controller
presentation explicitly, retaining source facts and the analytical
eligibility work as supporting history.

**Revised proposal.** Recommend one common Zhang-derived speed-setting
design in both arms. The same continuous advice, spatial application,
execution timing, state-feature contract, fine evaluator, complete
objective and task adaptations apply. At an equal parameter they execute
exactly the same advice and trajectory; no empirical approximate
equivalence between separate controller families is needed.
Value-only versus gradient-enabled parameter tuning is the intervention.
Delle Monache is optional numerical background, not a second base model.

The source's native spatial/discrete constraints must be adapted
identically; B0's grid is only its search approximation. The existing
complete sensitivity supplies a path through the continuous advice;
do not differentiate a source enumeration/GA or import a source PDE
gradient. Numerical correctness and optimizer performance remain untested.
The comparison remains conditional on the specified tuning routines and
budgets rather than independent of all algorithm choices.

**Status.** The same-base requirement is user-fixed. The common adapted
Zhang candidate is provisional and not user-selected. Per-case timing
and the accepted traffic stack are preserved. No new traffic law, state-
feedback policy, experiment or implementation is introduced. Stop at
the revised common-controller proposal; A's distinct compatibility check
and handoff remain later work.

Add the clarification and document checks, revise the active contract
and current context/proposal, add historical supersession notices and
append source/decision/work records. Preserve all unrelated review and
scientific model content, private VSL files and original feedback/urban
roots. Guarded commands and verification scope are in the work record;
no code, package, numerical run, commit, push or private handoff update.

[Current shared-controller correction](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_shared_controller_correction.md)

## 2026-11-02 — remove the extra source and identify the next review work

The user rejects adding Delle Monache to the active proposal and asks
what comes next and whether anything remains unclear. Remove its optional
dependency role and active contract reference. Preserve its historical
reading and earlier discussion; do not change the traffic-model stack.

The conceptual target is clear: one common source-derived controller,
identical task/plant/action/objective, with costs alone versus additional
simulator derivatives for tuning. No known additional user decision is
needed before the next bounded review. This does not mean all source/task
compatibility details have already been qualified.

The next topic is Zhang task fit: specify the common continuous advice
adaptation once for both B versions; close reference A's aggregate
initialization, bottleneck/completion placement and complete-TST accounting.
Do not invent an uncredited constitutive law or copy a fine-model residual
formula. A discovered conflict with accepted task semantics triggers a stop.
After that topic, consolidate the elementary comparison and align the
development handoff. No new broad survey or implementation plan is needed
merely to begin this review topic. The topic is identified, not executed
by this planning/status response.

Update the active contract, common-base response, source-status notice,
current context and decision/work logs. Preserve unrelated review files,
private VSL files and original urban roots/feedback. The guarded commands
and document checks are recorded in the work note. No traffic experiment,
optimizer run, dependency, simulator code, commit, push or private handoff
update is performed.

[Active contract and remaining work](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_per_case_matched_controller_contract.md)

## 2026-11-02 — execute Zhang task fit; stop at the aggregate terminal model

**Authorization.** The user accepts the clarified direction and requests
execution of the listed review plan. Read the current review instructions,
context, source/task contract and feedback 18. Do not implement simulators,
install dependencies or run scientific experiments.

**Common-controller result.** One continuous advice parameter is applied
to all task road rows and held for the case. Both versions use identical
action/bounds, plant, initialization and complete TST. At fixed parameters,
outputs/forward dynamics are identical. The source profile/discrete/boundary
constraints are replaced identically; the existing full regular derivative
supports our gradient-tuning extension. This is analytical task eligibility,
not empirical competence or source-performance transfer.

**A result and missing decision.** Aggregate initialization by rowwise
lane-stock summation preserves mass; the cohort and choke-time objective
can be stated. However, A's source capacity-drop law uses a finite
bottleneck cell's own density. Tracing the paper's existing FD reference
confirms a finite bottleneck region distinct from upstream discharge.
Moving the trigger to the last upstream row or retaining post-choke
predictor state changes predicted service. Moving completion changes
the task; replacing the stateful law by fixed capacity weakens the rival.
No unique compatible terminal adapter or complete A residual is qualified.

This is not proof that a compatible A is impossible. It is the point
where an explicit terminal-model interpretation is needed. Source
screenshots were not inspectable; the finding relies on primary
method prose and the inherited equations, not a claimed visual/code audit.

**Choice and recommendation.** Recommend the first elementary study use
the qualified shared B controller with cost-only versus derivative-enabled
tuning, keeping A pending. That can test numerical sensitivities and
tuning usefulness, not competence against A or aggregate-predictor
advantage. Alternatively, require A first and continue terminal-model/
complete-time qualification before consolidation. Neither choice is
selected; do not treat A as completed, silently remove the former
competence-check goal or advance the handoff.

**Scope and checks.** Add the findings, inspected-source list, work record
and document-validation JSON. Synchronize current context/navigation,
active proposals and decision/source records. Accepted model PDFs/LaTeX,
all unrelated reviews, the private VSL tree and original urban roots/
feedback remain unchanged. The source PDF download required approved
network escalation after sandbox DNS failure; it stays in /tmp, while
the durable record lists references only. Document commands and exact
preservation/link checks are in the work note.

No traffic/AD/FD experiment, optimization, training, dependency install,
simulator code, Git commit/push or private handoff update is performed.
The authorized continuation stops at this methodological/scope choice;
later consolidation is not executed under an assumed answer.

[Findings and direct choice comparison](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_zhang_task_fit_findings_and_choice.md)

[References actually inspected](misc/differentiable_freeway_bottleneck_task_review/extraction/research_readiness/vsl_zhang_task_fit_sources.md)

[Work scope and document checks](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_zhang_task_fit_work_record.md)

## 2026-11-02 — consolidate the selected B-first elementary verification

**User decision and deferred concern.** The user selects the matched B pair
first because it is the core verification. They question the credibility
cost of adapting a complicated A, require preservation of core assumptions/
algorithm backbone and intended behavior, prefer a simpler established A
if suitable, and explicitly defer that discussion. Do not search A now.

**Executed review work.** Consolidate one common continuous constant-advice
controller and the same selected detailed plant, complete objective and
per-case query contract. B0 uses cost-only interval enumeration; B-gradient
adds qualified complete sensitivity and actual-cost trial checks.
No extra controller or physical model is added.

Reuse one one-mass unconstrained reference and canonical X/Z, distinguishing
known free-time/service answers from unknown whole-trajectory outcomes.
The free reference checks exact accounting and prefix/residual derivative
consistency; X/Z retain their full movement table and lane-service contrast.
Their optimum advice need not differ. Separate evaluator conformance,
numerical derivative correctness, local finite-step guidance and measured
tuning results. A gradient win, interior optimum or new empirical scenario
is not required for this first review target.

The review fixes feedback/action/objective matching and work accounting.
Development must propose executable settings, tolerances, numerical steps
and budgets before comparisons, using its existing workflow.
The first study cannot claim performance against A, a positive information
gap, shared-policy generalization, runtime feasibility or physical validity.

**Handoff boundary and checkpoint.** Read-only inspection of the private
bootstrap confirms outdated provisional-selection and observation-only
comparison text. The next review action is to align that handoff with
the selected plant and consolidated B-first specification while preserving
mathematical snapshots and implementation customs. Stop here at the
consolidated-specification checkpoint. No new methodological fork appeared;
private files remain unchanged and no scientific test is run.

Add the specification/work/document-validation records and synchronize
scope/proposal/navigation/context, deferred A candidate status, sources
and decision logs. Preserve original feedback, accepted equations/PDFs,
all unrelated review files, private VSL tree and urban roots.
Guarded delivery/link/hash checks are recorded in the work note.
No traffic/AD/FD experiment, simulator/optimizer code, package install,
training, commit, push or private handoff update occurs.

[First-verification specification](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_b_pair_elementary_verification_specification.md)

[Work scope and document checks](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_b_pair_elementary_verification_work_record.md)

## 2026-11-02 — align the accepted B-first handoff and close this preparation

**Authorization.** The user accepts the B-first direction and specification,
confirms A is not required early and authorizes the stated local handoff
alignment. This is an independent review/document transition, not Phase A
or simulator development.

**Work.** Inspect the private bootstrap and its initial twenty-file manifest,
all of which match their original export hashes. Replace provisional model
selection and qualify old observation-only timing in current wrappers.
The first target is the same direct advice controller and fine plant, with
costs alone versus additional complete derivative information during
case-specific planning. Preserve complete accounting, reference cases,
regularity limits, work accounting and neutral/negative outcomes.

Export the accepted review specification locally with declared navigation
rewrites/status notice. Required mathematics stays local. Add current-scope
interpretation and versioned alignment provenance rather than overwriting
the original source snapshots. Preserve the entire AGENTS implementation
workflow suffix, initial snapshot manifest and workflow derivation.

**Boundary.** The review-side B-first preparation/handoff is complete.
The next development task is its first Phase A implementation/system
proposal, owning APIs, numerical settings, executable checks and sequence.
No such proposal or code is created here. The handoff reflects selected
query timing; old observation-only information bounds remain conditional.
A is deferred under the user's non-negotiable source-core/backbone/
intended-behavior requirements, and simpler alternatives remain open.
No A survey, shared-policy, runtime or physical-validation work is opened.

**Checks.** Guarded delivery covers only the two authorized repositories'
inspected document paths. Exact payloads, local/portable links, source/export
hashes, original snapshots, workflow bytes, append-only logs, unrelated files,
original urban roots/feedback and unchanged Git HEAD values are checked.
Private implementation material is not copied into the public review.
Detailed export/wrapper provenance stays private; the public note records
the transition and evidence limits. Commands are in the work note.

No simulator/optimizer implementation, scientific traffic/AD/FD run, package
install, new milestone approval, commit, push or visibility change occurs.
Stop after handoff alignment as authorized.

[Concise completion note](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_b_first_handoff_alignment.md)

[Work and preservation checks](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_b_first_handoff_alignment_work_record.md)

## 2026-11-03 — publish the completed review and handoff material

The user asks whether review changes have reached the remote. A live
check confirms remote main and local HEAD at 44eb3e2; the later review
files are still modified/untracked. The user then explicitly requests
committing and pushing those changes.

The publication covers 66 files already present in this review working
tree, including the current B-first specification/handoff, supporting
source and comparison records, and SUMO installation material with its
archived dummy-case verification. The private VSL repository is outside
this publication scope.

Pre-publication checks confirm scope, file sizes, relative local links,
JSON parsing, Python syntax without executing the helpers, tracked diff
formatting, and absence of credential-like content. Preserve reviewed
source bytes and archived raw logs/CSV, including their existing cosmetic
whitespace and line endings. Commit the checked
files and push main normally, then compare the live remote commit with
local HEAD and confirm the working tree is clean. No new traffic or
gradient experiment is executed by this repository publication task.
