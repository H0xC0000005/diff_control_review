# Ramp-metering feasibility review protocol

Date: 2026-09-14
Status: **Closed 2026-09-15.** RM0--RM3 are complete; RM4 rejected promotion of ramp metering as the parallel task; B1-P promotion and detailed RQ3--RQ5 formulation are halted; the colleague brief is approved; and RM5 is closed. Final record: `reporting/closure_record.md`.

Final conclusion and decision chain: `reporting/closure_record.md`, `discussion/feedback21_decision_record.md`, `discussion/feedback22_colleague_report_amendment.md` and `discussion/feedback23_objective_voice_revision.md`, followed by the approved brief at `reporting/colleague_brief/ramp_metering_parallel_task_assessment.pdf`. D1 found an internally coherent transfer test only when merge-input eligibility intervals do not overlap. The broader evidence debate establishes that this is not enough for orthogonal parallel-task status because the decisive order primitive is shared with TSC/M3 and macroscopic freeway gradient methods are already strong. General overlapping/multilane B1 remains outside current contracts. No repair or project change is authorized.

Closure override (2026-09-15): all prospective execution, open-gate and continuation language below is protocol history. No review phase or candidate branch remains active. A project-documentation synchronization pass is separate and was explicitly not started during closure.

Feedback-20 execution amendment (2026-09-15): do not formulate B1-P before debating the current evidence and its intended role. The debate pass may refine searches within the approved evidence strategy, archive sources and compare the candidate with the original parallel-task criterion. It may not open another task family, amend project files or convert B1-P into a required experiment without user approval.

Latest execution amendment (2026-09-14): continue the B1 review until a well-supported conclusion for or against is available, then stop for discussion. To preserve that instruction, RM4 now starts with the remaining conceptual feasibility audit rather than assuming suitability from target approval. Earlier scope/access stop rules remain active. The conclusion checkpoint precedes detailed formulation; no automatic task promotion, multi-ramp expansion or shared-method change follows. Current evidence: `synthesis/b1_initial_audit.md`; access request: `reporting/b1_access_request_batch_1.md`.

B1 approval boundary: examine one upstream optimized ramp meter and a downstream route-sensitive exit restriction, with fixed routes and downstream supply. Resolve the five promotion conditions in `synthesis/rm3b_mechanism_and_added_value.md` before recommending detailed formulation. Stop at the resulting feasibility checkpoint, or earlier for a decision-critical access need or scientific scope conflict. This approval does not establish suitability, freeze a scenario, or authorize implementation. See `discussion/b1_approval_and_context_continuity.md`.

Feedback-19 amendment discussion: distinguish isolated merge, one-meter/one-exit B1, multiple physical ramps with one control, coordinated multiple meters, and compact weaving. The comparison and provisional candidates B1-E/B1-C/B1-W are in `discussion/feedback_19_amendment_single_vs_multi_ramp.md`, §5. The user requested discussion, not adoption of those extensions. B1 remains active. Its audit must separate route identity, local lane/storage information and fine order, and must not infer any of their necessity merely from ramp count. This clarification leaves existing execution gates unchanged.

Feedback-19 refinement: screen distinct validation value beyond the closed TSC formulation during feasibility, before task promotion. A remains a correctness-reference candidate only; deferral/closure was not selected. The current evidence and narrowed alternatives are in `synthesis/rm3b_mechanism_and_added_value.md` and `reporting/rm3b_user_gate.md`.

Execution amendment: the user approved a minimal initial feasibility/necessity pass. Expand evidence only to resolve decision-critical uncertainties; proceed to detailed formulation only if inclusion is justified and the RM3 user gate permits it. A qualified or negative early finding is a valid checkpoint outcome.

## 1. Purpose and decision

Determine whether ramp metering can be a parallel second task that tests the selective-discreteness hypothesis while respecting the established simulator architecture and component closures. Return separate judgments on physical/model compatibility, scientific diagnosticity, and practical evidence feasibility. Formulate a candidate only if the findings warrant it.

The study replaces the broad future-task map. It does not reopen the closed green-allocation review or its V0–V4 suite. V5/I1 is not imported as a ramp-review requirement. “Parallel” describes two scientific applications, not authorization for simultaneous implementation.

## 2. Accepted boundaries

- Strict compatibility with aggregate first-order propagation, continuous traffic mass, fixed structural route/topology semantics, and the closed component contracts is the baseline requirement.
- Task-specific node/merge dynamics may be assessed as adaptations. Their necessity and adequacy are findings, not assumptions or permission to implement changes.
- Preserve the distinction between existing components, unresolved planned M3 behavior, and new capabilities. M3 owns service-order resolution, intra-bin homogeneity and defragmentation decisions.
- Do not modify project context, roadmap, source, tests, configuration, approved plans or milestone archives without a separate explicit instruction. Compatibility findings and amendment proposals stay in this package.
- A task must expose a justified question about the retained information. Generic control performance alone does not establish suitability. Negative or aggregate-sufficiency findings remain legitimate.
- Begin with one controlled on-ramp and a local merge. Justify any extra scenario complexity by a necessary mechanism and show why a simpler construction cannot test it. Strict compatibility continues to apply.
- Essential backbone changes, microscopic lane-changing dynamics or independent speed dynamics trigger a scope/compatibility decision rather than an implicit model extension.
- Real-site availability, particularly documented US examples, is an evidence dimension; field reconstruction is not mandatory. No implementation, calibration campaign or simulation experiment is authorized by this review.

## 3. Review questions

**RQ1 — physical compatibility.** Which ramp/merge mechanisms can the existing architecture represent credibly? Distinguish aggregate merge allocation from explicit lane-change trajectories, and equilibrium/derived speed from an independently evolving speed state. Which missing phenomena would invalidate the intended experiment?

**RQ2 — diagnostic value.** What local order, lane access, finite ramp/merge storage or spillback information could change attainable discharge and useful control sensitivity beyond aggregate alternatives? Is that information part of the project's representation, and can it be isolated fairly?

**RQ3 — controller and derivative contract.** Which continuous action is appropriate: an open-loop metering-rate schedule or parameters of a feedback rule? What state-to-control feedback and temporal paths result? Verify conventional-controller terminology and claimed effectiveness under the source's actual conditions. Do not equate fewer decision variables with a shorter dynamic gradient chain.

**RQ4 — evidence and implementation feasibility.** Which equations, reference cases, software, documented sites and data are usable? What are the data, licensing, calibration and evaluator limitations?

**RQ5 — conditional task.** If supported, what minimum geometry, objective, action, baseline ladder, scenario contrasts, gradient tests and external evaluation would make a defensible second experiment? Which later milestone owns each dependency?

## 4. Evidence strategy

Use a focused, project-bounded literature mapping and equation-level feasibility audit. Do not claim an exhaustive systematic review or require database-scale institutional searching by the user.

First inventory relevant sources in the two existing reviews and their archives. Search accessible scholarly indexes, arXiv, publisher/author repositories and primary transport-agency material. Use primary papers for scientific assertions and official manuals/software documentation for operational and engineering assertions. Follow backward/forward citations from the closest merge-model and ramp-control studies until the decision-critical mechanisms are covered or the evidence gap is documented.

Initial search families (refine vocabulary during the pilot):

| Family | Illustrative terms / purpose |
|---|---|
| Control lineage | ramp metering, local feedback, integral/PID control, optimal metering, constraints and queue override |
| Backbone compatibility | LWR, CTM, LTM, merge node, supply/demand, ramp queues, first-order versus second-order models |
| Local mechanisms | merge priority, lane distribution, lane changing, finite ramp storage, blockage, spillback, capacity drop |
| Differentiation | sensitivity, gradients, adjoint, automatic differentiation, metering-rate optimization, feedback parameter optimization |
| Evaluation/data | documented freeway ramp sites, calibration, detector data, official case studies, reproducible simulator scenarios |

Retrieve no arbitrary quota of papers. Maintain a coverage table over RQ1–RQ5 and contested mechanisms. Before stopping discovery, require direct method evidence for every positive compatibility claim, a strong simpler-model comparator, explicit examination of the lane-change/speed objections, and a documented citation pass around the nearest studies. Mark remaining gaps; absence from the retrieved corpus is not proof of impossibility or novelty.

## 5. Screening, extraction and quality

Include studies that specify relevant ramp-control decisions, merge dynamics, local mechanisms or evaluable control outcomes. Retain contradictory or out-of-scope models as contextual evidence when they clarify missing requirements. Exclude unrelated freeway prediction or broad coordinated-control studies without an extractable local implication. Deduplicate versions, recording substantive differences and publication/preprint status.

Assign stable `RM0001`-style IDs. Extract title, authors/year, persistent identifier, source/version/access status, study role, equations/sections, geometry, traffic state, control, objective and units, constraints, merge/lane/speed assumptions, order/storage treatment, derivative method and events, controller/model baselines, validation, external evidence, code/data/license availability, adoption mode, closed-component implications, and reviewer inference/uncertainty.

Assess evidence by claim: a source may establish an aggregate merge operator without establishing local lane fidelity or useful gradients. Abstracts can screen candidates but cannot substantiate decision-critical equation compatibility. Every substantive verdict must trace to a source location or be explicitly labeled an inference or unresolved gap. Do not treat a successful controller in another model as evidence for the selective representation.

## 6. Compatibility and decision framework

For each candidate classify dependencies as: unchanged existing capability; bounded task-specific operator using current interfaces; unresolved planned functionality requiring its normal gate; or incompatible/new capability requiring separate review. Trace both forward traffic meaning and derivative/state interfaces. The name “node adapter” cannot conceal a change to shared physics or component acceptance contracts.

Use three independent verdict axes:

| Axis | Positive finding requires |
|---|---|
| Physical compatibility | Necessary mechanisms have credible in-scope equations/interfaces; missing behavior and approximation limits are explicit |
| Hypothesis diagnosticity | A justified representation contrast, strong aggregate alternative and interpretable positive/equivalence/negative result |
| Evidence feasibility | A plausible matched objective/intervention, source/reference access and evaluator strategy with bounded unresolved calibration |

Recommend **suitable**, **conditionally suitable**, **unsuitable within scope**, or **insufficient evidence**, with separate axis judgments. Conditional suitability must name the unresolved dependency and who must approve it. Insufficient evidence is not a negative physical proof.

No weighted score decides promotion. A compatible but nondiagnostic benchmark does not qualify as the requested parallel task. An essential out-of-scope dynamic model cannot be assumed merely to obtain a positive answer.

## 7. Conditional formulation requirements

After the feasibility gate, a supported candidate must define the physical action and feasible set; objective/population/time/terminal accounting; fixed scenario and structural variables; continuous state transitions and control-feedback chain; nonsmooth events and derivative-check conditions; minimum mechanism-isolating scenarios; controller and representation comparisons as distinct axes; richer-evaluator mapping; held-out/replication design where appropriate; interpretation of negative results; implementation owners and calibration items.

Do not copy TSC's four-group simplex or its exact baseline realizations automatically. TST may be considered for comparable accounting, but objective suitability must be justified for this task. Formula-heavy explanations will have editable LaTeX and a rendered PDF. Exact numerical settings remain later planning outputs unless essential to deciding feasibility.

## 8. Phases and checkpoints

| Phase | Work and deliverable | Exit / authority |
|---|---|---|
| RM0 — plan | Accepted-scope handoff and this draft protocol | User approval before literature execution |
| RM1 — pilot and discovery | Archive inventory, queries/log, deduplicated records, coverage map | Continue automatically under approved scope |
| RM2 — evidence audit | Screening decisions, extraction matrix, claim/source and component compatibility tables | Continue; stop for batched access need or material scope conflict |
| RM3 — feasibility synthesis and target selection | Primer, initial findings and shortlist; B1 selected | **Closed by user 2026-09-14:** target approval is not a positive feasibility verdict |
| RM4 — B1 feasibility and role decision | Bounded audit, D1 and feedback-20 evidence debate complete | **Closed 2026-09-15:** reject promotion; halt RQ3–RQ5; preserve B1-P only as optional transfer/ablation concept |
| RM5 — colleague brief and closure | Freeze accepted conclusion, draft/render brief after scope approval, then record final closure | **Closed 2026-09-15:** report approved and closure recorded |

An opening of execution after plan approval may cover RM1–RM3 in one pass. It does not authorize crossing RM3's scientific gate. A negative verdict is an acceptable RM3 outcome; the user decides whether RM4 needs only a concise final report.

## 9. Stop rules and access

Stop for a necessary change to the backbone or closed scientific contracts; a different optimized task family such as coordinated multi-ramp control; a missing decision-critical full text; or an incompatibility that cannot be handled by approved method refinement. Document the smallest affected requirement and alternatives. Scope-compliant search refinements and justified local scenario elaboration do not require repeated approval.

Institutional-access requests go in one file with ID, title, authors/year, DOI/URL, why full text is required and requested material. Set the drop location to `archive/user_supplied/`, end the turn, and resume when material is supplied. Do not ask for credentials or institutional database execution. Additional batches are allowed only if newly discovered critical gaps make them necessary.

## 10. Package and reproducibility

Planned layout:

```text
README.md
review_protocol_plan.md
inputs/review_handoff.md
discussion/                    # migrated decisions and new dialogue
search/search_log.csv
search/coverage_map.md
screening/records.csv
screening/decisions.csv
extraction/evidence_matrix.csv
extraction/claim_source_map.md
synthesis/compatibility_matrix.md
synthesis/feasibility_report.md
synthesis/candidate_shortlist.md
synthesis/task_formulation.md  # conditional after RM3
synthesis/project_impact.md
reporting/                     # phase reports, gates and closure
archive/manifest.csv
archive/user_supplied/
```

Create execution files when their phases open. Log queries/date/source, screening rationale, exact source location/version, access limitations and the evidence behind verdicts. Archive new full text, extracted text and metadata here. Existing sources remain in place with cross-package references and identifiers. Do not copy private credentials. No new software dependencies or experiments are part of the default review work.

## 11. Historical approval request and closure outcome

The original request was to approve this protocol for RM1--RM3 and stop at the
feasibility gate. That approval and every later required gate were completed.
RM5 and the overall review closed on 2026-09-15; no critical scope question or
active review action remains.
