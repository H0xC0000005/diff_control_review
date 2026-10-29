# Urban methods report: work and evidence

**Current topic, 28 October: clean colleague-facing edition completed for review.** Both PDFs are black, with 9/11 pages. Only reader-irrelevant implementation/review scaffolding is removed; scientific explanations, provenance and all 58 equation bodies/numbers are retained. The [current guide](../../temp_content/research_readiness/unified_methodology_draft.md) links the separate clean copies and sources. Earlier versions remain intact; detailed verification is appended below.

26 October 2026. The user accepts the proposed syllabus and explicitly opens the next step. This authorizes technical methodology writing, not simulator implementation or experiments. All planned broad question batches remain closed.

The first draft connects the physical accounts, inherited cumulative propagation, ordered route mass, progressive ideal allocation, restricted access/service cases and complete-time objective. It derives the known allocation and head-service responses, then states the full-system sensitivity composition conditionally. It does not pretend that the full next-state operator is finished.

[First draft and reading guide](../../temp_content/research_readiness/unified_methodology_draft.md)

[Mathematical draft — PDF](urban_unified_methodology_draft.pdf)

[Retained LaTeX source](urban_unified_methodology_draft.tex)

[Equation/source and completeness map](../../extraction/research_readiness/urban_unified_methodology_sources.md)

## Concrete finding and bounded return

A new two-lane hand case exposes a consequential receiving definition: fair final interval totals and fair current ready-head sharing both respect elapsed service and use all downstream receiving, yet leave different lane residuals. Their analytic local response to a green transfer differs. The isolated case does not establish different total TST. The separate reading note explains the traffic, alternatives and provisional current-head recommendation; neither completion is approved.

[Separate focused receiving-timing note](../../temp_content/research_readiness/receiving_priority_timing.md)

The smallest affected definition is explicitly reopened under UR-G2/UR-C3-Q1. Selected green weights, equal-within-leg sharing, caps/reuse, order, allocation, commitments and information boundary stand. This pass does not create another generic question batch. Candidate and current status records are synchronized; the earlier mathematical companion and historical responses remain preserved.

Full ingress/history composition, exact qualified B1/B2 instances, the actual full-map derivative/completion domain and a selected R2 mapping remain writing obligations. An illustrative external mapping is clearly unapproved. The final compact report is not presented as complete.

## Work selection and sources

The useful new work is the joined transcription and the counterexample, rather than another model-family survey. Sources are reused at their recorded reading depth. Local checks read the approved M0/M1 equations and actual LTM/objective code; the M2 neutral domain is distinguished from the new internal-bay composition. No publication is credited with the whole proposed model. Only the relevant official SUMO documentation is checked externally in this drafting pass, for static-program and trip-accounting definitions; its details are cited in the PDF and source map. No external reference run is performed.

## Build and checks

The available toolchain is pdfTeX 1.40.25, TeX Live 2023/Debian. Run the following command twice, then copy the built PDF beside the retained source:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_unified_methodology_latex_20261026 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_unified_methodology_draft.tex
```

The final build has eight pages and no LaTeX warnings, unresolved references or box issues. Python 3 in the existing `differential_sim` environment and pypdf 6.15.0 verify nonempty extracted text on each page and equality of the delivered PDF to the built file. Build logs, extracted page text and PDF check data are in `/tmp/urban_unified_methodology_latex_20261026/`. No raster visual-inspection claim is made.

Exact rational arithmetic checks the two receiving completions, feasible green-transfer domain, conservation, local derivative coefficients, previous ready-head service example and ideal allocation examples. These are hand-definition checks, not traffic, autograd, finite-difference or usefulness experiments. Local artifact links/cited lines, stable question/candidate counts and protected files are checked against `/tmp/urban_unified_draft_before_20261026.json`. The scoped result is `/tmp/urban_unified_draft_check_20261026.json`; the final counts are recorded in the discussion log after verification.

Verification passes: 189 local links/cited lines, fifteen stable question IDs, thirty-four high-level candidate entries and eleven named directions. The 109-file snapshot accounts for nine intended current-record edits and 100 unchanged files, plus six new draft/issue/source/work artifacts. The delivered eight-page PDF exactly matches the clean build. Read-only Git status still lists only the pre-existing tracked changes to `AGENTS.md`, `PLANS.md` and `memo.txt`.

Feedback, earlier answers, prior PDFs/LaTeX, approved implementation plans, root files and source/tests/configs are preserved. No package installation, production edit or scientific run is undertaken. The scope of the new draft is explicit; the receiving timing decision is the one current written question.

## 27 October: selection recorded and priority law transcribed

The user selects option 2 and gives two connected reasons: both alternatives already require a discharge-order-aware solver, and current-head sharing lets discharge follow that order directly, while whole-interval fairness compensates for some of its effect. The decision is recorded with that rationale. This is not treated as empirical runtime or fidelity evidence. The current note and live candidate/status/source records now mark the time basis closed and final-total balancing unselected.

The draft continues with the algebraic capped sharing sublaw implied by the agreed policy. At a given causal time, weight each currently competing leg once by its relevant movement green, cap and reuse across legs, then cap and share equally among that leg's ready lanes. Derive the fixed-active-set response and include the effect of head-event times on interval discharge. Zero-green/zero-supply and fully capped branches are explicit. This is conditional on valid physical supply, readiness and individual caps; it does not silently replace cumulative receiving by interval allowance divided by timestep. Full physical history and conservative ingress composition remain unfinished. No new question is posed.

A missing backslash in the previous ready-prefix equation's spacing command is also corrected. The previously stated amounts and derivative examples are unchanged. All other existing displayed equations are retained; new priority and event-response equations are attributed to transcription/calculus of the selected policy.

The verified pdfTeX toolchain is unchanged. The revised build command, run twice, is:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_receiving_selection_latex_20261027 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_unified_methodology_draft.tex
```

The final PDF and scoped-check results are recorded below after the build. Checks cover exact rational receiving/redistribution cases, conditional derivative identities and head-event accounting; local links and retained candidates; PDF text/references; and protected files against `/tmp/urban_receiving_selection_before_20261027.json`. These remain hand-definition/document checks, not a simulator implementation, finite-difference/autograd experiment or SUMO run. No new literature search is undertaken in this selection/transcription update.

Verification passes. The revised PDF has ten pages, text on every page, no LaTeX warnings, box issues or unresolved references, and exactly matches the built file. Seven exact capped-sharing cases, the selected two-lane perturbation, branch-derivative identities and the head-event term pass. All nineteen previous equation labels/bodies are preserved apart from the spacing correction; six new labels cover the priority and derivative equations. No raster visual-inspection claim is made.

There are 192 valid local links/cited lines. Fifteen stable question IDs, all thirty-four candidate paragraphs and eleven named directions are retained; `R.reuse` records the approved timing update. The 115-file snapshot accounts for fifteen intended current-artifact edits and 100 unchanged files, with no new repository files. Feedback, prior responses, other PDFs/LaTeX, root files, approved implementation plans and source/tests/configs are unchanged. Git still lists only the pre-existing tracked edits to `AGENTS.md`, `PLANS.md` and `memo.txt`. Results are `/tmp/urban_receiving_selection_check_20261027.json` and `/tmp/urban_receiving_selection_math_check_20261027.json`; build logs and extracted text are in the dated build directory above. The receiving-timing choice is closed; no new question is returned.

## 27 October continuation: reconcile the service and propagation histories

The user asks where the work stands, then explicitly asks to continue and adds a reporting preference: after work, briefly state the current step, whether it is complete and whether anything needs their decision. They will read the full PDF when finished. This is recorded in the decision record and syllabus; intermediate drafts are no longer presented as review handoffs without a concrete question. The already authorized drafting continues, without another permission request.

The first physical coupling check follows how selected elapsed service writes the history later queried by propagation. The current M0 plan and actual LTM code were read directly. They interpolate cumulative boundary counts uniformly. The selected server can instead produce two different rates before/after its head clears. A prepared ready-lane hand case shows end discharge 0.3 in both descriptions but past-query counts 0.08 and 0.12, giving different next-interval storage-limited receiving. The example uses compatible triangular-FD storage/delays, available past data, no direct nonempty initializer and no current-departure immediate vacancy credit.

Analytic receiving slopes under a feasible green transfer are 0.4 versus 0.2, away from event ties. Thus the question changes traffic and sensitivity, rather than only representation notation. The next TST response is not inferred from those numbers: source-to-road transfer leaves immediate total population unchanged, and complete TST needs the full evolution. A proposed moving-knot interpolation derivative records the event-time sensitivity if actual service-time histories are chosen. No new history law is approved here.

The short note presents the two viable completions, their concrete consequence and the provisional recommendation to preserve service-time history. Keeping M0's reconstruction remains a declared coarse numerical alternative. Both retain continuous mass, first-order propagation and average service. Native/ref numerical differences must be visible in comparisons. The narrow C1/G2 question is the only current user action. Other broad decisions and current-ready-head sharing stay closed. The full model, complete sensitivity, final comparison/reference qualification and compact report remain unfinished.

[Short decision note](../../temp_content/research_readiness/service_history_consistency.md)

This continuation is bounded to the physical seam that must be resolved before further joined derivation. It opens no new literature survey, implementation, package installation, traffic/AD/finite-difference/optimization/SUMO run or numerical calibration. New mathematical cases are exact hand-definition calculations. Existing displayed equations and prior feedback/results are preserved; the working draft receives a supporting history section and all current status/candidate/source records are synchronized.

Build command, run twice with the available pdfTeX toolchain:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_history_coupling_latex_20261027 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_unified_methodology_draft.tex
```

The hand result is `/tmp/urban_history_coupling_hand_check_20261027.json`; the pre-edit snapshot is `/tmp/urban_history_coupling_before_20261027.json`. PDF/link/candidate/protected-file check results are recorded below after verification. The full PDF remains support for the unfinished drafting task; the user-facing handoff is the short decision note and a brief status.

Verification passes. The working PDF has eleven pages, nonempty text throughout, and no LaTeX warnings, box issues or unresolved references; the delivered file matches the build. All twenty-five prior equation labels/bodies remain unchanged, with five history-case/derivative labels added and every mathematical label mapped to source/status. Exact rational checks confirm the compatible triangular-FD identity, past-query values, active receiving bounds, stable-branch slopes and the moving-knot derivative. These are hand calculations, not an executed simulator or gradient experiment. No raster-inspection claim is made.

There are 207 valid local links/cited lines. All fifteen question IDs, thirty-four candidate paragraphs and eleven named directions are retained. The 115-file snapshot accounts for fourteen intended current-artifact edits and 101 unchanged files, plus one new short question note. Feedback, earlier responses, other PDFs/LaTeX, root/source/test/config files and approved implementation plans are unchanged. The scoped result is `/tmp/urban_history_coupling_check_20261027.json`; build logs/text are in the dated build directory. Current step after this pass: **unified methodology drafting, incomplete; one C1/G2 history choice needs a decision**. The PDF will be presented for full review when drafting is finished.

## 27 October scope correction: retain timestep interpolation and complete the admission map

The user says the event-history question is sound by itself but is not justified by the present scope: the initial gradient target is the state/output at timesteps, without an additional between-step research question. The response accepts this boundary and withdraws the refinement as a blocking gate. Showing that a refinement can alter a prediction did not establish that the current method lacked a rule; M0 already defines interpolation. The original comparison is retained in a deferred appendix and historical note, rather than selected or invalidated.

One factual qualification is recorded from the actual LTM code: even at a timestep endpoint, a fixed delayed-history query can fall between stored past boundaries. Thus interpolation can influence timestep outputs and derivatives, without making an intermediate-time observable the research target. This requires using the established interpolation consistently, not replacing it. Internal elapsed/head service remains the selected computation of a step's discharge; it does not introduce an event-resolved propagation history. This distinction is now explicit in the main draft and live records.

The already authorized work then continues on the actual one-step conservative admission map. The earlier agreed targets 0.4/0.6 and lane allowances 0.3/0.5 had nonbinding common sending. A ready, already committed parent with capacity-limited common sending 0.6 produces a new concrete ambiguity: capped target-proportional admission gives 0.24/0.36, while actual-queue balancing within the same target caps gives 0.20/0.40. End lane counts differ as 0.44/0.36 versus 0.40/0.40. Both preserve commitments, parent order, storage and continuous mass. The common bound can be active with the whole parent ready; this is not an off-grid timing example.

The draft now states both candidate laws, the shared max-admitted-volume constraint, end-state Jacobian responses to sending and preexisting queues, and the conservative source/feeder-to-lane transaction. Candidate A uses existing remaining commitments as admission weights; B adds a criterion that rebalances realized queues. A is provisionally recommended, not approved. This is a local realization criterion under C2/C3, not a global heterogeneous allocator, artificial target sequence, reassignment or new green-aware preference. It is the one current question. The old generic partial-admission/bookkeeping vote remains withdrawn: this binding-bound case supplies the distinct next-state outcomes the earlier example lacked.

[Current short admission note](../../temp_content/research_readiness/shared_sending_admission.md)

The broad decisions, current-ready-head priority and macro information boundary stand. No traffic equation in production code, approved implementation plan, dependency, experiment or user feedback is changed. There is no new literature survey or simulation/AD/finite-difference/optimization/SUMO run. The mathematical examples are exact hand-definition checks. Event-history equations remain unchanged as deferred support, and all current source/candidate/status documents are synchronized.

Build command, run twice:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_step_scope_latex_20261027 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_unified_methodology_draft.tex
```

Pre-edit snapshot: `/tmp/urban_step_scope_before_20261027.json`. Exact hand check: `/tmp/urban_step_admission_hand_check_20261027.json`. Final PDF/document/protected-file results follow below. Current step is still unified methodology drafting; the final compact PDF is unfinished.

Verification passes. Both proposed admission laws reproduce the accepted nonbinding-sending result 0.3/0.5; the finite-sending case and its queue/sending Jacobian identities pass exact rational checks with inactive-cap neighborhoods. The working PDF has thirteen pages and no LaTeX warnings, box issues or unresolved references, and exactly matches its build. All thirty previous equation labels/bodies are retained, including the deferred history appendix; four admission/state-response labels are added, with every label mapped to source/status. No raster-inspection claim is made.

There are 219 valid local links/cited lines. Fifteen question IDs, all thirty-four high-level candidate paragraphs and eleven named directions remain unchanged. The 116-file snapshot accounts for fifteen intended current-artifact edits and 101 unchanged files, plus one new short admission note. Feedback, earlier answers, other PDFs/LaTeX, root/source/test/config files and approved implementation plans are unchanged. The result is `/tmp/urban_step_scope_check_20261027.json`. After this work: **unified methodology drafting remains incomplete; event-history refinement is deferred, and the one current decision is the shared-sending admission criterion under C2/C3**. The full PDF remains support until drafting is finished.

## Feedback 9: answer the dependency question only

The user clarifies that allocation should be computed from known actual transfer capability, rather than first fixed independently and then rationed. They acknowledge that blockage/capability may change during allocation without reversing the logical dependency. The instruction explicitly limits this turn to answering this question and forbids continuing to the next step.

The answer accepts the capability-aware direction: known sending/receiving, storage and accessibility constrain new queue-balanced allocation. It withdraws the old A/B gate and target-proportional recommendation for the normal new-allocation process. The existing numerical case illustrates fresh feasible admission 0.6 balanced as 0.2/0.4, leaving queues 0.4/0.4 and upstream mass 0.4. This is not a vote selecting the old B law with an independently fixed whole-packet target vector. No exact new solver, waiting-commitment construction or derivative is derived in this reply.

Two qualifications prevent a false agreement. Known feasible capability is not already-known final realized discharge; when allocation changes blockage, enforce/update the relevant dependent constraints consistently instead of assuming an oracle outcome. Also, the previous counterexample explicitly postulated valid commitments already made; current capacity knowledge does not automatically cancel or retarget them. Its mathematics remains conditional reference evidence, not a general requirement to ignore known constraints when creating targets. The user's proposal corrects normal new assignment; exact reconciliation with previously valid waiting commitments is later transcription, not a new question here.

The source check is bounded and read-only: actual `simulation_step` computes link limits before node-flow calculation (lines 279 onward), supporting this dependency pattern. It does not claim the refined lane allocator already exists. Queue-based preference, source-order processing, route/mass conservation, prior valid commitments, current-ready-head priority and timestep interpolation remain. No service-aware driver cost, production change or empirical result is selected.

[Separate feedback 9 response](urban_feedback9_response.md)

The active question, proposal/source/candidate/status records and current mathematical draft receive premise/status corrections only. All existing displayed equations are retained, explicitly conditional where needed. The user feedback receives only the permitted answered-heading marker. No additional model-development pass, next-step task, literature search, installation, simulation, AD/finite-difference/optimization or SUMO run is performed. This respects the explicit answer-only boundary.

Build command, run twice for the status/premise update:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_feedback9_latex_20261027 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_unified_methodology_draft.tex
```

Pre-edit records are `/tmp/urban_feedback9_before_20261027.json` and `/tmp/urban_feedback9_content_before_20261027.json`. PDF/document/equation/feedback-preservation checks follow below. Current step after this response: feedback 9 answered; overall methodology drafting incomplete; no next step started, as requested.

Verification passes. The user feedback body is byte-for-byte preserved except for appending the permitted `(answered)` marker to heading 9. All thirty-four displayed equation labels/bodies are unchanged and source-mapped. The status/premise-updated working PDF has fourteen pages, text throughout and no LaTeX warnings, box issues or unresolved references; the delivered file exactly matches the build. No new mathematical derivation, solver, numerical gradient check or empirical result is introduced. No raster-inspection claim is made.

There are 224 valid local links/cited lines. All fifteen question IDs, thirty-four high-level candidate paragraphs and eleven named directions are retained; `L.queue` and `A.joint` status text now incorporates known feasibility. The 117-file snapshot accounts for seventeen intended existing edits (sixteen review artifacts plus only the feedback heading marker) and 100 unchanged files, plus the separate feedback-9 response. Earlier responses, other PDFs/LaTeX, root/source/test/config files and approved implementation plans are unchanged. Results are `/tmp/urban_feedback9_check_20261027.json`; build logs/text are in the dated build directory. The reply stops here under the user's answer-only instruction. Drafting is not complete, and no further decision or next step is opened by answering feedback 9.


## 27 October continuation — complete proposed transcription and compact report

The deliverables are a new compact methods report, a mathematical specification and source/coverage map, plus a separate readable assessment note. The older fourteen-page working PDF/LaTeX and its displayed equations are preserved, with current navigation moved to the new documents.

[Compact report](urban_compact_methods_report.pdf)

[Detailed specification](urban_methodology_specification.pdf)

[Review points](../../temp_content/research_readiness/joined_methodology_review.md)

[Sources and coverage](../../extraction/research_readiness/urban_methodology_specification_sources.md)

The actual definition work now joins pre-state cumulative propagation, eligible source-order allocation, feasible entry and waiting intention, valid old targets, common-feeder prefix admission, current-head receiving reuse, boundary-history reconstruction and complete-population sensitivity. New exact transcription choices are explicitly proposed. The report does not claim native B1/B2 adoption is qualified or that a mixture ablation replaces strong macro explanations. Model-owned conversion of original fine observations remains allowed.

The user criticizes time spent in web search. The response acknowledges excessive sequential exploration and confirms that independent searches can be concurrent. No additional web request follows that message. New source checking stops; the rest of this continuation produces the written account and checks its definitions. Independent document builds and pure hand checks are batched concurrently. Source retrieval limits remain visible rather than being concealed by a new literature survey.

Nine exact-fraction hand calculations are recorded in /tmp/urban_methodology_completion_hand_checks_20261027.json. They are arithmetic/definition checks only: no simulator, AD, finite difference, optimization or reference experiment. The storage/population bounds are stated as mathematical consequences within the admitted discrete domain.

The available pdfTeX/TeX Live and existing pypdf environment are used without installing dependencies. Each source is built twice, using separate output directories:

~~~bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_methodology_completion_latex_20261027/specification misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_methodology_specification.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_methodology_completion_latex_20261027/compact misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_compact_methods_report.tex
~~~

Build logs and extracted page text are retained in those directories. The scoped pre-edit snapshot is /tmp/urban_methodology_completion_before_20261027.json. Final page/link/equation/candidate/protected-file results are recorded after verification.

Status after this work: a complete proposed account and compact report are written for review. Assessing the explicitly new definitions is still required before calling them selected; implementation and evidence remain separate. No new broad question batch is started.


Verification complete. The compact report has four pages and the specification seven, with substantive extracted text on every page and no orphan final-page fragment. Both two-pass builds have no LaTeX warnings, box issues or unresolved references, and delivered PDFs equal their built files. All twenty-five specification labels and four compact-report labels are source-mapped. No raster visual-inspection claim is made.

Nine exact hand-definition checks pass. All 672 local Markdown links/cited lines checked across the three review-readiness folders resolve. The fifteen stable question IDs, thirty-four high-level candidate entries and eleven named directions are preserved; relevant status text distinguishes agreed directions from new proposed laws. The pre-edit 215-file scope accounts for eleven intended existing Markdown edits and 204 unchanged files, plus six new report/specification/review/source files. User feedback, earlier response bodies, the historical working PDF/TeX, root files, approved plans and source/tests/configs are unchanged.

Results are /tmp/urban_methodology_completion_hand_checks_20261027.json, /tmp/urban_methodology_completion_pdf_checks_20261027.json and /tmp/urban_methodology_completion_document_checks_20261027.json. The final scope record is /tmp/urban_methodology_completion_check_20261027.json. Git still shows only the pre-existing tracked AGENTS.md, PLANS.md and memo.txt changes.

Current topic: joined-proposal review. The proposed transcription and compact report are written; scientific approval and native/evidence qualification remain outstanding. No next questionnaire, implementation or experiment is started.


## 27 October — expand the questions and make them explicit in the PDF

The requested change is presentation and candidate clarification, not selection of a new traffic law. The note separates legal lane alternatives, location of first commitment, target creation for the unadmitted remainder, conditional old-target realization and downstream receiving-allowance semantics. Each question explains the traffic issue, compares explicit candidates on a shared example, and gives a provisional recommendation. Optional comparison adoption and later numerical/implementation work are separated from the current decisions.

[Expanded note](../../temp_content/research_readiness/joined_methodology_review.md)

[Methods report with the same decision appendix](urban_compact_methods_report.pdf)

Shared left/through permission is now provisionally favored if the primary bay study is intended to exercise responsive allocation. This changes a recommendation because the previous exclusive-target illustration made that allocator inactive; it does not approve a new permission matrix. Exact existing equations stay intact and conditional on their stated realization. The old-target question is inapplicable where the selected empty-loaded model creates no binding multi-lane waiting records.

The compact report now has seven pages: four pages of methods followed by a three-page decision appendix. The detailed specification remains seven pages with status/permission clarification. The entire five-question text is checked against the PDF extraction so the PDF no longer omits the decisions present in the short note. No LaTeX warnings, box issues or unresolved references remain; each delivered PDF matches its two-pass build. No raster visual-inspection claim is made.

The available pdfTeX 1.40.25 / TeX Live 2023 and existing pypdf are reused. Build commands, each run twice:

~~~bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_joined_questions_expansion_latex_20261027/compact misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_compact_methods_report.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_joined_questions_expansion_latex_20261027/specification misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_methodology_specification.tex
~~~

Six exact-fraction hand comparisons and preservation of the four compact and twenty-two detailed display blocks are recorded in /tmp/urban_joined_questions_expansion_hand_checks_20261027.json. These checks introduce no simulator, AD/finite-difference, optimization or SUMO run. The new receiving case gives 0.45/0.15 versus 0.55/0.05 at identical total receiving 0.6, under the stated head and physical-capacity assumptions.

Build logs and extracted text are in /tmp/urban_joined_questions_expansion_latex_20261027/. The prior delivered PDFs are preserved in its before/ subfolder. The scoped snapshot and original TeX bodies are /tmp/urban_joined_questions_expansion_before_20261027.json and /tmp/urban_joined_questions_expansion_tex_before_20261027.json. Final link/candidate/scope checks are recorded after verification.

Current topic: joined-model clarification. The user can clarify the intended traffic behavior and decide from the expanded material; the choices remain open. No next broad batch is started.


Verification complete. The methods PDF has seven pages, with the four-page narrative followed by the three-page expanded decision appendix. Every paragraph of all five questions matches the extracted PDF text. The specification remains seven pages; both builds are clean and equal their delivered PDFs. All 29 equation labels remain mapped and all existing display bodies are unchanged. Six illustrative exact-arithmetic checks pass.

The scoped check validates 678 local links/cited lines, retains all fifteen IDs, thirty-four original high-level candidate paragraphs and eleven original named directions, and records the five focused comparisons under those existing questions. Eleven intended files changed and 210 snapshot files are unchanged, with no new repository file. Feedback, root files, production source/tests/configs and approved plans are preserved. Git still lists only the pre-existing AGENTS.md, PLANS.md and memo.txt edits. Results are /tmp/urban_joined_questions_expansion_check_20261027.json and /tmp/urban_joined_questions_expansion_pdf_checks_20261027.json.

The expansion is finished. Current topic remains clarification of the joined traffic model; no new scientific choice is closed.


## Feedback 10 — answer the five points and stop

A separate response explains each answer and marks resolved/open status. Shared left/through permission is selected for the starting bay case, while permissions remain scenario-dependent. Progressive in-step updates are distinguished from the first binding location. Reading answers 2/3 together, new commitment attaches only to actual lane admission; unadmitted mass has no frozen lane target.

The user also corrects the prior alternative that paused all allocation behind an unassigned residual. The selected processing policy retains priority within movement and may inspect later different movements. Its physical placement is not declared solved: server inspection order and ability to pass a physically occupied common-lane head are distinct. The earlier common-prefix allocation operator cannot silently be retained as the general policy or silently removed from actual physical access.

Q4 is withdrawn because it arose only under the unselected frozen-waiting-target assumption. Receiving A is retained with a factual correction: it removes a separate receiving-pool exhaustion rule, not sequential dependencies from head clearance/current-head competition. No new vote about the already selected service law is opened.

[Separate feedback 10 response](urban_feedback10_response.md)

Active decisions, inventory, question-status, source and navigation records are synchronized. The PDFs receive status/premise changes only; all 26 previous display blocks and 29 equation labels are retained. Waiting-target and old-target equations are explicitly unselected conditional material. The current full traffic map/gradient is not claimed completed. The feedback inbox is changed only by appending the permitted answered marker to heading 10.

Both updated PDF sources are built twice using the existing pdfTeX 1.40.25 / TeX Live 2023 toolchain. No dependency installation or environment modification is performed:

~~~bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_feedback10_latex_20261027/compact misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_compact_methods_report.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_feedback10_latex_20261027/specification misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_methodology_specification.tex
~~~

The methods PDF has eight pages and the specification seven; both carry feedback-10 status on the first page, contain text throughout, build without warnings/box issues or unresolved references, and equal their delivered files. Logs/text are retained in the dated build folders; prior delivered PDFs are preserved under before/. No raster inspection is claimed.

This answer-only pass performs no new literature search, full node-model derivation, hand-model experiment, simulation, AD/finite difference, optimization, SUMO/reference run or production edit. The checks concern document builds, unchanged equations, feedback preservation, candidate status and protected scope.

Pre-edit records are /tmp/urban_feedback10_before_20261027.json and /tmp/urban_feedback10_content_before_20261027.json. PDF and equation/feedback results are /tmp/urban_feedback10_pdf_checks_20261027.json and /tmp/urban_feedback10_equation_feedback_checks_20261027.json. Final link/candidate/scope results are recorded after verification.

Current topic: feedback 10 answered. One model detail remains open: physical access/interface under movement-specific skipping. The response stops without opening the next task.


Verification complete. All 688 local links/cited lines pass. The fifteen IDs, thirty-four original high-level candidate entries and eleven named directions remain; current child-question statuses reflect feedback 10. All 26 display blocks and 29 labels are preserved and source-mapped. The feedback body is byte-for-byte unchanged except for the permitted answered marker on heading 10.

The 221-file snapshot accounts for seventeen intended existing edits (sixteen review artifacts and the single feedback-heading marker), 204 unchanged files, plus the new separate response. Protected root/source/test/config/approved-plan files and earlier response bodies remain unchanged. Git still lists only the pre-existing AGENTS.md, PLANS.md and memo.txt edits. The scope result is /tmp/urban_feedback10_check_20261027.json. The answer stops here; physical application of movement-specific skipping remains open.


## 27 October — consolidated model, sensitivity and clean report

The authorized work applies the closed agreements to the actual report. The four-page compact narrative and seven-page specification now replace historical question/answer material, frozen waiting state, old-target rationing and unmatched optional mixture equations. The previous delivered PDF/TeX pairs, feedback answer and prior source map are preserved under archive/research_readiness/urban_methodology_before_feedback10_application_20261027/. The policy set is closed; mathematical realization is submitted for the user's review.

[Compact report](urban_compact_methods_report.pdf)

[Detailed specification](urban_methodology_specification.pdf)

[Current equation/source map](../../extraction/research_readiness/urban_methodology_specification_sources.md)

[Archived candidate](../../archive/research_readiness/urban_methodology_before_feedback10_application_20261027/README.md)

The key joined-model correction distinguishes input order from physical lane access. The scan can inspect later movements, while an occupied F retains exact physical prefix blocking. There is no bypass around the selected common feeder. Earlier actual admissions update h; unadmitted mass has no future-lane vector and no duplicated stock.

A second necessary correction separates ready candidate mass A from the total sending budget S. Non-prefix pool selection cannot pre-truncate its candidates to the first S mass. Original eligibility provenance is retained, and the scalar delayed-entrance-minus-exit ready count remains consistent because all past departures were eligible. This adapts M1's extraction at unassigned pools without claiming a production implementation change. Physical lanes still serve prefixes.

The sensitivity now differentiates the actual water fill, sequential residual resources, eligibility and entrance-time reconstruction, capped current-head sharing and head-duration changes. It composes into complete TST with state response carried through fixed clearance. Old waiting-vector derivatives are absent. Empty free sets, zero flow and signature changes have explicit limits rather than epsilon repairs.

Sixteen exact-fraction definition checks cover independent scanning and the wrong-prefix counterexample, ready-residual counts, physically compatible common-feeder storage/order cases, paired mass, feasible queue balancing, residual accounting, compatible splitting, analytic local allocation/service responses, receiving reuse, entry/eligibility response, complete population accounting and the neutral scalar limit. These are hand/reference arithmetic, not simulator rollouts, autograd, finite differences or empirical usefulness evidence. Written feasibility and unique-selection reasoning is separate from implementation conformance.

The existing pdfTeX 1.40.25 / TeX Live 2023 toolchain and pypdf environment are reused. Build commands, each run twice:

~~~bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_agreement_consolidation_latex_20261027/compact misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_compact_methods_report.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_agreement_consolidation_latex_20261027/specification misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_methodology_specification.tex
~~~

The current source map covers 33 equation labels, including five compact statements. Retired waiting-target and unmatched ablation labels are absent from the active sources. Archive hashes match the pre-edit originals. Native B1/B2 sources, observation fairness and the external-reference contract remain qualified as stated; no new benchmark family or scientific assumption is silently selected to finish the report.

No web search, dependency change, simulator/AD/finite-difference/optimization/SUMO run, production source/test/config edit or implementation plan change is performed. Review effort is bounded to the actual allocation/access/history/objective/sensitivity coupling and report checks.

Pre-edit snapshot: /tmp/urban_agreement_consolidation_before_20261027.json. Hand checks: /tmp/urban_agreement_consolidation_hand_checks_20261027.json. Equation/archive checks: /tmp/urban_agreement_consolidation_equation_archive_check_20261027.json. PDF text/build data: /tmp/urban_agreement_consolidation_pdf_checks_20261027.json and /tmp/urban_agreement_consolidation_latex_20261027/. Final scope/link results follow after verification.

Current topic: consolidated methodology ready for user review. No further policy question is pending from this set. Native instance qualification, numerical calibration and all empirical validation remain later.


Final verification passes. The compact report is four pages and the specification seven, with substantive extracted text throughout, clean two-pass LaTeX logs and exact built/delivered PDF equality. The final compact layout suppresses single-line widows. All 33 current labels are mapped; frozen-target and unmatched-ablation labels are absent from active sources. Sixteen exact hand-definition checks pass. No raster visual-inspection claim is made.

All 678 local links/cited lines across the current and archive folders resolve. The fifteen stable question IDs, thirty-four original high-level candidate entries and eleven named directions remain; current records close this policy set and link its consolidated realization. Archive originals match pre-edit hashes.

The 222-file snapshot accounts for 17 intended review edits, 204 unchanged files and one unrelated observed memo.txt change, plus seven new archive files. No task command wrote memo.txt; the scope audit found that it now matches current Git HEAD, and it was left untouched. Production source/tests/configs, approved plans, AGENTS.md, PROJECT_CONTEXT.md, PLANS.md, feedback and earlier response bodies remain unchanged against the snapshot. Git now lists the preserved pre-existing AGENTS.md and PLANS.md edits. No restoration or overwrite of the unrelated memo change is attempted.

Final results are /tmp/urban_agreement_consolidation_check_20261027.json and /tmp/urban_agreement_consolidation_document_check_20261027.json. The written consolidation is complete for user review. Native qualification, numerical calibration, implementation and all empirical validation remain separate future work.


## 27 October — presentation and reader flow adapted from the supplied VSL report

The requested change is editorial structure and presentation. The user's exact local VSL PDF has SHA-256 5c7e81bb15d2b64b3094926c0c153775eae8ba08b62213a776428d85a5dde960 and exactly matches the canonical VSL PDF. Its retained TeX is read as the verified presentation reference; neither the supplied file nor the VSL branch is changed.

[Reworked urban report](urban_compact_methods_report.pdf)

[Unchanged detailed specification](urban_methodology_specification.pdf)

[Presentation/equation source map](../../extraction/research_readiness/urban_methodology_specification_sources.md)

[Preserved pre-presentation version](../../archive/research_readiness/urban_compact_before_vsl_presentation_20261027/README.md)

The report now opens with Information/Decision/Gradient research questions, then the concrete urban task and six global assumptions. Numerical operating conditions are separated from those traffic assumptions. The model is narrated in four causal components: propagation/readiness, lane admission/access, elapsed service/receiving sharing, and conservative state/record reconstruction. Complete TST and the V0–V4 information/decision design follow the model. The last section shows actual local sensitivities and their complete cost composition.

The reference's compact title/headings, 10-point text, 18-mm margins, short display spacing, adjacent attribution and numbered references are adopted. The previous abstract/scope front matter and deliverable-style ending are replaced by direct scientific exposition. Urban retains its own arrivals, lane semantics, fixed FD, service control and timestep sensitivity; no VSL recovery, advice-response dynamics, scalar information simplification or scalar optimizer is imported.

All five original compact equation blocks are preserved exactly. Twelve additional compact labels copy existing specification equations verbatim apart from labels; one domain display restates the existing physical/timestep conditions. There are now eighteen compact labels and twenty-eight detailed labels, all mapped. The companion source/PDF and closed question register are byte-for-byte unchanged. Existing sixteen hand checks are not rerun, and no new method or scientific experiment is introduced.

The revised main PDF has five pages: questions and global assumptions on page 1, causal traffic model on pages 2–3, information/decision tests on page 3, complete sensitivity on page 4 and the evidence note/references on page 5. The main text is expanded by promoting relevant laws from the companion, without adding a traffic assumption. The companion remains seven pages.

The installed pdfTeX 1.40.25 / TeX Live 2023, cite/glyph mapping and existing pypdf are reused. The command is run twice:

~~~bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_vsl_presentation_latex_20261027 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_compact_methods_report.tex
~~~

The build has no warnings, box issues or unresolved references/citations. Page text and heading order, source equation preservation and built/delivered equality are checked. Local raster converters are unavailable in the inspected toolchain; no raster visual-inspection claim is made. No dependency is installed to expand this editorial task.

Pre-edit snapshot/source records are /tmp/urban_vsl_presentation_before_20261027.json and /tmp/urban_vsl_presentation_source_before_20261027.json. Reference extraction is under /tmp/urban_vsl_presentation_reference_20261027/. Content and PDF checks are /tmp/urban_vsl_presentation_content_checks_20261027.json and /tmp/urban_vsl_presentation_pdf_checks_20261027.json. Build logs/text are under /tmp/urban_vsl_presentation_latex_20261027/. Final scope/link results are recorded after verification.

Current topic: revised presentation ready for user review. Scientific decisions remain closed; no implementation, new literature review, numerical calibration, simulator, AD/finite-difference, optimization or SUMO run is opened.


Final checks pass. The revised PDF is five pages, with research questions and all six assumptions on the first page; causal traffic components follow on pages 2–3, information/decision tests on page 3, and complete sensitivity on page 4 before the evidence note/references on page 5. The delivered PDF equals the clean two-pass build. Numbered citations and references resolve.

All five original main equation blocks are unchanged. Twelve promoted labels copy existing companion blocks exactly apart from labels; the domain display restates its existing conditions. All eighteen main and twenty-eight companion labels are mapped. The supplied VSL PDF, canonical VSL source/PDF, companion source/PDF, closed question register and protected implementation/root/feedback records are unchanged. No prior scientific check or experiment is rerun for this editorial task.

The 232-file scope accounts for eight intended existing edits, 224 unchanged files and five verbatim/archive-guide files. All 690 checked local links/cited lines resolve; 15/34/11 inventory counts remain. Pre-edit report/companion copies match their recorded original hashes. Git still lists only the preserved pre-existing AGENTS.md and PLANS.md edits. Final scope results are /tmp/urban_vsl_presentation_check_20261027.json.

The requested presentation revision is complete. Current topic remains user review of the report; no scientific decision or implementation stage is opened.

## 28 October: feedback-11 geometry and explanation revision

The user opens the first accumulated PDF revision batch. The report keeps the five VSL-derived main sections while adding causal explanations before every main display, defining V and lambda beside the allocation rule, and replacing compact inspection/eligibility phrases with examples and plain language. The main narrative no longer uses private agreement/approval history as an explanation for a traffic law. Attribution and evidence limits remain.

The representative geometry becomes U→{F1,F2}, F1→{B,T1}, F2→T2. The two feeders cover the upstream part of the local zone; the bay-opening cross-section divides each from its terminal section. Left uses F1/B, right F2/T2, and through chooses F1 or F2 on actual admission from U using current receiving-feeder load and feasible receiving. There is no cross-feeder movement after entry. The companion's geometry, permissions, access text and examples are updated with the main report. The shared left/through head-service example is explicitly V1, not a permission for left turns in T1. V2/V3 and baselines share the new declared geometry; the smaller diagnostic remains available.

All 18 main labeled equation blocks are byte-for-byte preserved. Only eq:geometry changes among the companion's 28 labeled blocks; the other 27 are unchanged. The old main/companion PDFs and TeX plus source map are archived verbatim in `misc/selective_discreteness_downstream_task_review/archive/research_readiness/urban_before_feedback11_20261028/`. No old source, feedback or prior answer is overwritten merely to mark it handled.

Exact local arithmetic verifies the updated admission contrast: F1 admits 0.2 versus 0.8 under reversed order; independently ready F2 admits 0.3 in either case, giving 0.5 versus 1.1. Compatible triangular-FD receiving values, retained-plus-transferred mass and the through-feeder balancing example are checked. These are definition checks, not simulator or numerical-gradient evidence. The earlier sixteen hand checks are not rerun or claimed as validation of the new topology. Results are `/tmp/urban_feedback11_content_checks_20261028.json`.

The structural note proposes three alternatives without implementing them: mechanism-first; complete model separated from study design; and a narrative organized around the information, decision and gradient claims. Mechanism-first is recommended provisionally because it establishes why each ingredient is needed before introducing its symbols. Alternative structure selection remains separate from this completed batch.

The existing pdfTeX/TeX Live toolchain is retained. Run each command twice, then copy the resulting PDF beside its source:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_feedback11_latex_20261028 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_compact_methods_report.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_feedback11_latex_20261028 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_methodology_specification.tex
```

Both final builds are clean: no LaTeX warnings, box issues or unresolved references/citations. The main report has six pages and the companion eight. Delivered files equal the builds. Existing pypdf 6.15.0 in the `differential_sim` environment checks page counts and nonempty extracted text throughout; no package is installed. `/home/zpz/miniconda3/bin/pdftoppm` renders the PDFs. All-page contact sheets are visually inspected, with final main pages 3–4 inspected at full rendered size after paragraph grouping prevents split explanatory examples. The companion front matter is aligned with the colleague audience.

An optional Poppler `pdftotext -bbox` probe aborts with `std::out_of_range` on both files. Layout is instead assessed from rendered pages and clean TeX output, with text verified independently by pypdf and successful layout-text extraction. No bounding-box verification is claimed. This tool failure changes no traffic law or acceptance criterion. Final PDF checks/hashes are `/tmp/urban_feedback11_pdf_checks_20261028.json`; build logs and page text are in the build directory above.

Current topic after this work: user review of the revised methods report. The requested first batch is complete. Alternative structures are proposals only; implementation, numerical calibration, qualified baseline adapters and empirical usefulness remain later work. Protected-scope/archive/link checks are recorded below after final verification.


Final verification passes: six-page main report and eight-page companion; clean two-pass builds; delivered files match builds; 18 main and 28 companion labels retained, with only the companion geometry equation changed. All 724 checked local links/cited lines resolve. Fifteen stable question IDs, 34 high-level candidate entries and 11 named directions remain. The 244-file snapshot accounts for 13 intended review edits and 231 unchanged files, plus eight new files (two discussion/response documents and six archive files). Archived originals match pre-edit hashes; protected root, source/test/config, approved implementation and feedback files are unchanged. Final scope results are `/tmp/urban_feedback11_scope_checks_20261028.json`. Current topic: report review; the first improvement batch is complete and alternative structures remain proposals.


## 28 October: feedback-12 second accumulated revision batch

The work is bounded to the user's requested component source/representation/explanation changes. The component provenance check was necessary to distinguish a literature idea from this model's particular law and to resolve the supposed spatial-CTM omission. The existing project context and M2 record explicitly choose cumulative-mass/rank bins and a ledger-authoritative reconstructed grid. Their overlap representation is restored to the report, with its continuous sensitivity. Physical LTM equations, the two-feeder geometry and the accepted traffic policy are not replaced. The comparison information boundary and exact-baseline selection policy remain.

Gong's equilibrium idea, Han's average service, the first-order node framework, Daganzo's cell-based lineage and de Souza's individual-tracking contrast now appear adjacent to the components they inform. The current queue-cost, exact access, continuous ledger/grid and priority choices are distinguished from copied source equations. An existing T0017 author error is corrected in the adoption matrix only; its original raw snapshot is archived. Primary indexed text/abstracts and existing verified project/source records support this bounded credit check. Direct publisher/CTM retrieval failures do not become claims of full-paper reproduction. Reading depth is in the provenance note.

The main PDF adds two grid labels and retains all eighteen earlier labels; the companion adds two derivative labels and retains its twenty-eight earlier labels. The entry interval is rewritten with named endpoints, admitted mass and rank offset z. All over-dot derivative notation is replaced by d/d-alpha along a defined feasible service transfer. The causal gradient diagram and overall state-chain equation precede the module derivatives. Internal comparator codes are expanded to their scientific roles; scenario families are presented as mechanism ablations and a reserved robustness test. The explicit V4 variables are not newly calibrated values or an executed scenario bank.

Red highlighting uses xcolor, already available in TeX Live, with HTML color D13F43. Changed or added passages are grouped in the revision environment; unchanged forwarding equations remain black. The report's five main sections remain in the VSL-derived order. No alternative structure is implemented. All pre-edit PDF/TeX files, the source map and the bibliographically corrected matrix are preserved in `misc/selective_discreteness_downstream_task_review/archive/research_readiness/urban_before_feedback12_20261028/`.

Exact active-branch checks in `/tmp/urban_feedback12_math_checks_20261028.json` verify grid/ledger movement-mass and derivative identities, the partial-bin capacity mask, a later ready fraction of an admitted segment, and the head-service example/local slope. The arithmetic uses rational first-order quantities, without running a traffic model, numerical differentiation, AD, optimization or a richer reference. Existing evidence is not relabeled as newly executed.

Build each command twice, then deliver the checked PDFs beside the retained sources:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_feedback12_latex_20261028 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_compact_methods_report.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_feedback12_latex_20261028 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_methodology_specification.tex
```

The existing pdfTeX/TeX Live toolchain, Poppler raster/layout-text utilities and installed pypdf 6.15.0 are used without installing anything. The earlier known failing Poppler bbox probe is not repeated. Build logs, extracted text, page renders and contact sheets are kept under `/tmp/urban_feedback12_latex_20261028/`. Verification records are written separately after inspection.

Current topic: red-marked report review. This second batch is complete once the artifact/scope checks below pass. There is no new scientific vote, simulator authorization or experiment. The structural alternatives remain proposals; numerical calibration, qualified comparator instances and external usefulness remain future evidence.


Final feedback-12 verification passes: eight-page main report and nine-page companion, with clean two-pass builds and delivered PDFs matching the build hashes. All pages have nonempty extracted text. Raster checks confirm the requested red color; all-page contact sheets are inspected, with the service example, full gradient-path page and final companion page viewed at readable size. All 50 equation labels are mapped; every earlier label is retained, eleven main forward equation blocks remain byte-for-byte unchanged, and the rewritten timing/derivative notation is identified. All 725 checked local links/cited lines resolve. The 15/34/11 question/candidate/direction counts remain. The 262-file snapshot accounts for 14 intended review/bibliographic edits and 248 unchanged files, plus nine new response/provenance/archive files. Original archive hashes match, including the attribution-matrix snapshot; root files, implementation plans, source/tests/configs and user feedback are unchanged. Results are `/tmp/urban_feedback12_pdf_checks_20261028.json`, `/tmp/urban_feedback12_equation_checks_20261028.json`, `/tmp/urban_feedback12_math_checks_20261028.json` and `/tmp/urban_feedback12_scope_checks_20261028.json`. The second revision batch is complete; current topic remains report review, with no new scientific vote, implementation or experiment.


## 28 October: feedback-13 model-to-gradient presentation revision

The user explicitly approves the balance-first presentation and opens this accumulated revision batch. Work is bounded to those report explanations and their supporting records. No literature survey is needed: the forward model is already defined, and the issue is making its derivatives and causal role readable. Source interpretations and reading-depth limits remain those recorded for feedback 12.

Files changed are the main and companion PDF/TeX pairs, current equation/source map, feedback-13 response, current reading guide, readiness overview, review plan/status, decision record, question-register status and discussion log. The original four report files and source-map snapshot are preserved under `archive/research_readiness/urban_before_feedback13_20261028/` with a README. User feedback is preserved verbatim. Root policy/context/roadmap, implementation plans, source/tests/configurations, older archives and the standalone clarification notes are not edited.

The main remains eight pages; the companion has ten. The main now defines the forward service-amount sum before its derivative. Its sensitivity blocks follow the same order as the causal diagram and explicitly reference the forward allocation, sharing, head-time, grid, entry and TST laws. Allocation and leg sharing start from total derivative balances and individual cases; common-level solutions are distinct equations. The head-clearance formula is a separate branch contribution to the service-duration channel. The companion makes the other stopping branches explicit. These are algebraic transcriptions of existing rules, not a new event-history model or traffic policy.

The full numeric shared-lane example is optional companion material. Its direct rate-loss term -0.5 and time-gain term 0.75 give the existing local derivative 0.25. The main instead explains how serving a blocker can help followers despite reducing their own green, why that is relevant to retained order, and why it does not establish complete-TST benefit. The grid definition now names the already-used overlap omega and explicitly defines movement/bin mass M and lane population n. Every old revision-color command and notice is removed.

Build each source twice with the installed TeX Live 2023 toolchain:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_feedback13_latex_20261028 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_compact_methods_report.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_feedback13_latex_20261028 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_methodology_specification.tex
```

The final built PDFs are copied beside their retained sources. Both two-pass builds have no warnings, overfull/underfull boxes or undefined references. Each page has nonempty extracted text. All pages are rendered with Poppler; grayscale and visual-layout checks cover the final output. The equation map covers 23 main and 35 companion labels. The main retains 19 old labels and adds four; its old numeric-example label is relocated to the existing companion example. The companion retains all 30 earlier labels and adds five. Fifteen original main equation blocks and 27 companion blocks are unchanged after whitespace/label normalization; the other changes are the explicit omega definition and the three reorganized derivative blocks, with their separated expressions preserved.

Seven exact rational first-order checks cover the admission balance, weighted sharing balance, head-clearing duration, sending-exhaustion duration, final timestep remainder, fixed-head-mass cancellation, and the optional example. These validate identities in the new displays; they are not simulator, numerical finite-difference, AD, optimization or richer-reference experiments. The only assumptions are the existing fixed active categories, selected stopping condition, structural metadata and fixed external demand/time domain. No new smoothing, threshold, tie-breaking policy or dependency is introduced.

Evidence is `/tmp/urban_feedback13_latex_20261028/report_checks.json`, the final build logs and rendered page/contact images in the same directory. Scope/link/archive results are `/tmp/urban_feedback13_latex_20261028/scope_checks.json`. The pre-edit hash snapshot is `/tmp/urban_feedback13_before_20261028.json`.

Current topic: the feedback-13 revision is complete for user review. It opens no scientific decision or implementation task. Numerical calibration, actual baseline qualification and empirical forward/gradient/control-usefulness evidence remain later work, as before.


Final feedback-13 verification passes: eight-page main report and ten-page companion, delivered PDFs matching final build hashes, clean two-pass builds, nonempty text on every page and zero color-channel difference across all 18 final rendered pages. Final all-page contact sheets were inspected, with the causal-framework/service page and full duration-branch page also viewed at readable size. All 58 current equation labels are mapped; all 39 internal equation references resolve. Seven exact first-order identity checks pass. Scope checks account for 12 intended existing edits, 184 unchanged snapshot files and seven new response/archive files. All 212 checked local links resolve; archived originals match their hashes and the original question inventory content is preserved beneath its new status paragraph. Protected project files, user feedback, older archives and standalone clarification artifacts are unchanged. The batch is complete for report review, with no new scientific question, model change, implementation or experiment.


## 28 October 2026 — selective red highlighting of feedback 13

The user supplements feedback 13 with an explicit request to mark this revision's changes in red, approximately, while avoiding whole red blocks. This supersedes the temporary all-black delivery. Only short new/revised phrases, source references, balance terms and a few small added equations are highlighted, using the existing D13F43 color. Earlier blanket feedback-12 highlighting is not restored. The main has 51 short highlight spans and the companion 39; unchanged surrounding prose and most formulas remain black.

This is formatting only: stripping the highlight wrappers exactly reproduces each prior LaTeX source. Both PDFs have clean two-pass builds, and extracted page text, all equation numbers and page counts remain unchanged (eight and ten pages). Representative main/companion pages are rendered for visual inspection. Current status/response wording is synchronized; historical black-output checks above retain their original scope. No mathematical or simulation checks are rerun, since the content is unchanged.

Build each retained source twice with the same command options, using `/tmp/urban_feedback13_highlight_20261028` as the output directory:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_feedback13_highlight_20261028 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_compact_methods_report.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_feedback13_highlight_20261028 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_methodology_specification.tex
```

The built PDFs are delivered beside the sources. Before-formatting PDF/TeX copies, hash records, build logs and comparison checks are retained in that temporary directory. The feedback-13 batch remains complete for report review; this adds no scientific choice or subsequent task.


## 28 October: formula-provenance reporting pass

The task is bounded to explicit attribution beside formulas. The prior extraction/source record already distinguishes the relevant literature ideas from project definitions, so the required work is local source verification and writing, not another model survey. The M0 discrete domain/histories/LTM/objective, M1 continuous ledger and affine timing, and M2 rank-grid representation are inspected at the relevant definitions. The prior primary-source reading-depth limits remain unchanged. “Defined here” identifies a model choice; it does not claim universal novelty.

Previous highlight wrappers are cleared, then 27 main and 36 companion short source-relation spans are tinted D13F43. No old formula or heading is recolored wholesale. The main has 9 pages and the companion 11. Equation bodies and numbers are unchanged: 23 main and 35 companion. Statements distinguish reused LTM/transcription/bookkeeping, adapted literature ideas, project-defined geometry/access/priorities/receiving conventions, derived mass/rate-time/entry identities and calculus of the stated model. The existing research questions, representative geometry and comparison policy remain.

Existing edits are the current source map, guide, overview, review-plan status, decision record, question-register status and discussion/work logs. New files are separate provenance PDF/TeX pairs, the provenance response, all-formula inventory and six-file archive. The existing canonical main/companion PDF/TeX pairs are restored from the saved originals and preserved byte-for-byte, following the user's instruction to save this revision separately. Historical extraction, literature-adoption records, old archives, user feedback, implementation files and standalone clarification notes are not edited.

Build both retained sources twice with the installed TeX Live 2023 toolchain, then copy the built PDFs beside their sources:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_formula_provenance_20261028 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_compact_methods_report_formula_provenance.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_formula_provenance_20261028 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_methodology_specification_formula_provenance.tex
```

Final two-pass builds are clean. The verification compares all 58 mathematical bodies and equation numbers against the archived originals after removing color wrappers and whitespace. It checks internal equation references, local source links, extracted page text, provenance coverage, new red output and layout. No mathematical simulation checks are rerun: only attribution prose and grouping change. Source/baseline implementation qualification and empirical gradient usefulness remain later work.

Build logs, `report_checks.json`, `formula_origins.json`, page renders/contact sheets, color checks and final scope/link/archive checks are retained under `/tmp/urban_formula_provenance_20261028/`. The pre-edit hash manifest is `before_hashes.json` there. The old PDFs, LaTeX sources and source-map snapshot are preserved under `archive/research_readiness/urban_before_formula_provenance_20261028/`.

Current topic: the provenance revision is complete for user review. It opens no scientific choice or implementation task.


The user additionally requests saving the provenance revision as another PDF without overwriting the current version. The new deliverables are `urban_compact_methods_report_formula_provenance.pdf/.tex` and `urban_methodology_specification_formula_provenance.pdf/.tex`, with the main linking to the new companion. The existing canonical report/companion PDF/TeX pairs are restored from the saved pre-revision originals and verified against the initial hashes. Current provenance links point to the separate versions. This changes delivery/versioning, not report content or scientific scope.


Final verification of the separately saved provenance versions passes: nine-page main and eleven-page companion, clean two-pass builds, all 58 equation bodies and numbers unchanged, all 54 internal equation references resolved, complete 58-formula provenance coverage, and all 234 checked local links valid. The new main links to the new companion. Prior highlight spans are cleared; only the new 27/36 short attribution spans are red. Layout is reviewed through all-page contact sheets and targeted source/formula pages, with the final paragraph-boundary adjustment checked separately. Final PDFs match their build hashes. The original canonical main/companion PDF and LaTeX files match the pre-revision hashes exactly. Scope accounts for eight intended metadata edits, 195 unchanged snapshot files and twelve new variant/response/inventory/archive files. User feedback, protected implementation/project files and the original question inventory content remain unchanged. The reporting revision is complete for review; it introduces no scientific choice, implementation or experiment.


## 28 October 2026 — numbered citation for the Gong attribution

The user notices that the new sentence naming Gong et al. has no IEEE-style numbered marker. The preceding paragraph already cites the paper, but the new attribution should identify it directly as “Gong et al. [3]”. The IEEE Reference Guide, Section I.A, permits author names followed by square-bracketed numbers and uses et al. for three or more in-text authors. The guide is verified at https://ieee-pes.org/wp-content/uploads/2023/04/IEEE_Reference_Guide-12Aug2022.pdf (page 3). The primary Author Center guide URL redirected to a JavaScript-only Google document, so the accessible official IEEE guide is used for this stable rule.

A separate corrected main-report copy adds the Gong marker to the attribution and uses “Gong et al. [3]” in the first narrative mention. It does not assert that the complete bibliography or the differently formatted companion has undergone a full IEEE-style audit. The existing canonical and provenance PDF/TeX pairs are all preserved unchanged.

[Corrected main report](urban_compact_methods_report_formula_provenance_citation_fix.pdf)

[Retained source](urban_compact_methods_report_formula_provenance_citation_fix.tex)

Build the retained source twice with `pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_citation_fix_20261028`; then copy the PDF beside the source. The final build is clean, has nine pages, retains every equation body and verifies the printed attribution as “Gong et al. [3]”. Results and build logs are under `/tmp/urban_citation_fix_20261028/`. Current topic remains report review; this is a local citation correction with no scientific change.


## 28 October 2026 — clean colleague-facing edition

The user accepts the tone and asks to remove all red tints and only those scaffolds that address the ongoing dialogue instead of helping colleagues understand the method. This authorizes a narrow editorial pass. Separate `_clean` PDF/TeX pairs preserve all earlier versions, in line with the prior versioning instruction.

The main report retains its traffic story, examples, source relations, derivative-to-forward references and periodic gradient-framework explanations. One stray `ev{...}` markup artifact is removed, and an instruction-like entry-history introduction is made declarative. The LTM bibliography link receives a reader-facing technical title. The Gong numbered citation is retained.

The companion removes implementation-status claims about milestone code, replaces the unexplained internal merge-condition identifier with its exact affine timing meaning, removes references to discarded waiting-target alternatives, and recasts a few implementation guardrails as scientific conditions. Local hand examples remain reference checks distinct from empty-loaded task scenarios. Complete clearance, exact realized-lane FIFO, current-load allocation, fixed receiving, reference fairness and population accounting remain unchanged. The shortened comparison heading is descriptive. Scientific evidence limits are retained; the pass does not imply executed validation.

What is deliberately kept: conceptual signposts, the whole gradient path and each module's role, formula provenance, notation reminders, illustrative traffic mechanisms, source/representation distinctions and branch/evidence limitations. These serve the colleague-facing purpose and are not treated as disposable scaffolding.

[Clean main report](urban_compact_methods_report_clean.pdf)

[Clean companion](urban_methodology_specification_clean.pdf)

Build both sources twice with the installed LaTeX toolchain:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_clean_report_20261028 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_compact_methods_report_clean.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_clean_report_20261028 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_methodology_specification_clean.tex
```

The clean sources are retained beside their PDFs. Builds have 9/11 pages and no warnings, overfull/underfull boxes or unresolved references. Verification compares every equation body and number to its source version, checks links, old-version hashes, visible process-language remnants, grayscale output and page layout. No simulator, derivative experiment, literature search or new scientific decision is introduced. Evidence is under `/tmp/urban_clean_report_20261028/`.

Current topic: the clean editorial edition is complete for report review. The next action is the user's reading/review; no new question batch or implementation is opened.


Final clean-edition verification passes: nine-page main and eleven-page companion, clean two-pass builds, nonempty text on all pages, unchanged bodies/numbering for all 58 equations, and all 54 internal equation references resolved. All 20 rendered pages have zero color-channel difference and their contact sheets are visually inspected. The corrected Gong [3] citation and the clean main-to-companion link are retained. All 174 checked local links resolve. Scope records seven intended metadata edits, 172 unchanged existing files and four new clean PDF/TeX files. Every prior PDF/TeX version and user feedback file is preserved. No simulator or gradient experiment was rerun for this editorial task. The clean colleague-facing edition is complete for review.
