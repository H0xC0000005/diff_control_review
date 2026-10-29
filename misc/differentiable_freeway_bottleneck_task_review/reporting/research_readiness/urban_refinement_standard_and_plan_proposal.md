# Proposed urban refinement: a complete methodology before the final report

**Review order selected by the user, 2026-10-20.** Settle the urban model's
global assumptions and interfaces first, then review its coupled components.
"Global" refers to contracts within the urban task, across its components,
V0–V4 conventions and comparison rules; it does not require a unified
urban–VSL model. The representative-V3-first order is unselected. The
completion rubric and detailed sprint inventory remain opening-review
outputs; no particular traffic law is selected by this order decision.

[Order selection and handoff readiness](urban_review_order_selection_and_handoff_ready.md)

Date: 2026-10-20. **Planning discussion only.** The user clarifies the target
as a research-ready urban methodology framework and task formulation at
the specification standard reached by VSL. This proposal refines the user's
steps 0–3. The user's later clarification explicitly permits overriding
P8's delegation and considering other methods for that modeling aspect
when necessary. No specific alternative or operator is selected, and no
urban model-review sprint or closed VSL stage is opened here.

[Accepted P8 reconsideration scope](urban_p8_override_scope_clarification.md)

## The proposal is sound; make its completion test explicit

Your sequence addresses the right problem. The existing urban review gives
a strong task and comparison contract, but some of the traffic rules that
must realize it remain schematic or assigned to future milestones. The
next effort should identify and resolve the methodological dependencies
needed for a complete model, then present that model clearly.

The practical completion test is: **a knowledgeable reader can reconstruct
the represented traffic dynamics, the task and the intended sensitivity
comparison without inventing a missing traffic rule.** Implementation may
still choose data structures, numerical solvers and calibrated parameter
values within the declared model and later approved execution plan.

This is a stronger target than the original urban task-selection review.
Its earlier closure remains valid for that earlier scope. The new review
would extend its specification rather than restart task selection.

## 0. Proposed meaning of the VSL-like standard

These are urban completion criteria for discussion, not a requirement to
copy VSL's particular model, proof or document length.

| Standard | What an acceptable urban formulation must make explicit |
|---|---|
| **Concrete task and scientific purpose** | Road/lane/bay setting and V0–V4 roles; traffic population, initialization and arrivals; physical action and feasible set; complete objective and completion/clearance semantics; the precise information/control question. |
| **Assumptions and admitted domain** | A coherent root assumption set, further component closures, parameter meanings/units and conditions under which the claims and derivative are made. Distinguish assumptions, sufficient bounds, defaults and deductions. |
| **Complete forward mechanisms** | The selected propagation, lane intent/realized occupancy, bay admission/access, storage, service, queue/blockage and spillback rules determine traffic evolution. An essential access or receiving operator is defined, not merely named. |
| **Consistent interfaces and accounting** | Conserved traffic, a single physical meaning for each stock/flow, compatible timing and update order, feasible receiving/service, initialization and terminal treatment. Coupled components agree on what information passes between them. |
| **Traceable literature use** | Each defining component/equation identifies what is reused, adapted, defined here or derived. Source applicability is distinguished from the study's own assumptions. A source list alone is insufficient attribution. |
| **Fair information and comparison contract** | Selected strong simpler rivals receive their declared observations and lawful inference. Matched states are meaningful at that information level. Representation and optimizer comparisons remain distinct; aggregate sufficiency and negative outcomes remain admissible. |
| **Complete conditional sensitivity** | The physical allocation reaches complete TST through the actual selected traffic operators. Local derivatives, fixed structural metadata and event/active-branch limits are specified. A generic chain-rule recursion does not complete an undefined traffic operator. |
| **Inspectable reasoning and clear presentation** | Hand-auditable reference/limit cases check the causal mechanism and its neutral cases; a final consistency audit joins the model. A compact LaTeX PDF explains it, supported by derivations, source maps and decision records. |

Methodological readiness does not imply numerical AD correctness, measured
gradient usefulness, a calibrated urban model or successful external transfer.
Those require their separate execution/evidence. Neither an interior optimum
nor a positive order-information advantage is a completion requirement.
Urban's own accepted external-evaluation contract remains in force; VSL's
optional-SUMO scope is not transferred.

## Refined sequence and concrete outputs

| Step | Core question and work | Inspectable output and gate |
|---|---|---|
| **0. State the target; recover the current authorities** | Adopt a clear completion rubric, then reconstruct the latest accepted urban task and ownership decisions. Resolve obsolete proposal/status wording through the closure records. | A short standard and authoritative starting-state map. Do not judge an old draft as a current gap before checking later records. |
| **1. Audit components and interactions against that standard** | For each necessary mechanism, ask what is fully defined, what is recoverable, what is missing, why that matters, and which other components depend on it. Check literature and claim support as well as equation completeness. | A gap-to-review matrix: current rule/status, unmet criterion, traffic consequence, proposed bounded review, owner, dependencies, closure evidence and smallest reopen condition. The first gate confirms this inventory and the bounded review plan. |
| **2. Agree the smallest amendments and global urban contracts** | Retain adequate accepted decisions. Distinguish previously unselected choices, documentary clarifications and actual changes to accepted meaning. For a change, explain old/new behavior, source basis, consequences and affected dependencies. | An amendment/decision register and a consistent urban methodological backbone. Close global contracts before dependent local work; do not overwrite historical closure or treat every earlier decision as automatically reopened. |
| **3. Review and resolve the necessary mechanism blocks** | Reuse reviewed sources first; inspect further sources for decision-critical gaps. Formulate the selected laws, test their interfaces with analytical/hand cases, derive the relevant sensitivities and compare the strongest simpler explanations. Review tightly coupled access/storage/service behavior together where necessary. | A concrete reviewed result per planned sprint, with direct traffic findings and its gate. Stop at a completed sprint or a new consequential choice. Do not expand into simulator construction. |
| **4. Check the complete chain and write the report** | Verify that assumptions, model, variants, rival information, objective and derivative describe one consistent task. Check whether simplifications preserve the intended order/access-to-control mechanism. Synchronize the formulation and provenance, then present it compactly. | A complete methodology contract, supporting consistency/reference evidence, and the urban PDF/source. Final review gate closes the stated scope; numerical/physical evidence retains its honest status. |

The important changes to your ordering are the early recovery of records
and the explicit final integration/report stage. Reviewing components alone
can miss a problem in their combination. For example, a bay may have spare
storage while its left-turn demand is trapped behind through traffic. A
complete formulation must determine whether that traffic can reach the bay,
how admission and discharge change the obstruction, and how a feasible
service reallocation changes total time. A sensible storage rule and a
sensible service rule do not settle that coupled question by themselves.

Prefer the smallest coherent component change that closes an evidenced gap.
A single source-backed replacement is preferable to several compensating
patches when both can serve the same scientific contract. Preserve adequate
components; do not retain a rule solely because the earlier, narrower
review accepted it if the new audit exposes a consequential limitation.

## P8 reconsideration is within the authorized review scope

The historical P8 decision assigns service-order resolution to M3; it does
not select exact FIFO. The user now explicitly authorizes overriding that
delegation if needed, including using other methods to handle the affected
modeling aspect. The review may examine a replacement approach as well as
a change in decision ownership. It need not retain the old FIFO/bin-policy
framing merely because that was the earlier delegated question.

No further permission is needed simply to reconsider this aspect. The
review should document its traffic purpose, the reason for any override,
the proposed old/new behavior and its consequences. A concrete replacement
still needs its scientific review and decision at the relevant gate; none
is selected by this scope clarification. Implementation remains separate.
The other task boundaries and scientific invariants retain their status.

Respecting the records means preserving their history and making the new
amendment traceable. Software progress does not determine the task's
scientific design.

[Accepted urban impact/ownership record](../../../selective_discreteness_downstream_task_review/synthesis/project_impact_matrix.md)

### Initial decision-ownership map for the opening audit

The following is an initial scaffold, not a completed inventory or a claim
that every accepted global decision needs reopening. The new agent should
give concrete audit findings stable question IDs before a review sprint
begins.

| Set | Classification and owner | Dependencies and amendment boundary |
|---|---|---|
| **UG0: scope and completion standard** | Type 2; user decides the new review target and scope, reviewer proposes it | First. Retain V0–V4 and exclusions unless an explicit scope amendment is proposed. |
| **UG1: represented lane/order state and ownership** | Type 2; user has authorized P8 override/reconsideration; reviewer evaluates alternatives, with consequential model selection at its gate | UG0; recover the starting records and apply the user's superseding scope clarification. Ownership and the method for the affected aspect may change if justified; no replacement is preselected. Defines the information the model can retain/relax. |
| **UG2: common traffic interfaces and accounting** | Type 2; reviewer audits accepted action/objective/initialization, coupling and conservation; user decides changes | UG0–UG1. Existing effective-service/TST semantics are inputs, not automatic new choices. A new access/service law that changes another component returns here. |
| **UG3: rival information and evidence meaning** | Type 2; reviewer audits, user decides changes | UG0–UG2. Governs meaningful matching, baseline fairness, optimizer separation and the urban external-evaluation contract. |
| **UG4: whole-model derivative domain** | Type 2; reviewer specifies the conditional contract, user decides consequential changes | UG1–UG3. Fixed metadata, regular branches and complete-objective sensitivity constrain dependent component derivations. |
| **UC1: propagation and population accounting** | Mixed: global meaning in UG2; Type 1 local transcription/reference work assigned to the propagation component | UG2. Preserve the approved longitudinal backbone and single-count physical mass. |
| **UC2: access, bay storage and point/node service** | Mixed: retained state/traffic coupling in UG1–UG2; Type 1 equations, units and branch deductions after those globals close | UG1–UG2, with coupled subquestions grouped as needed. A local equation cannot choose order semantics or alter another component silently. |
| **UC3: concrete B1/B2 realizations** | Mixed: capability/information contract in UG3; Type 1 faithful source transcription under that contract | UG2–UG3. Any change to what a rival knows or represents reopens UG3. |
| **UC4: component sensitivities and explanatory artifacts** | Type 1 derivation, provenance and report work under the selected laws and UG4 | Accepted component laws and UG4. A missing derivative caused by a changed state/law returns to its global contract. |

The final audit checks the globals and local components together. A local
result that conflicts with a closed global contract reopens the smallest
affected contract and dependent questions, rather than being patched in
an adapter or hidden as a report-writing convention.

## Selected review order and considered alternative

The user has selected global urban assumptions/interfaces first, then
coupled components. The table retains the comparison and its rationale;
the second order is unselected. Both were considered against the same full
urban target and initial bounded authority/standards/gap audit.

| Option | Core idea | Pros | Cons and dependencies |
|---|---|---|---|
| **Global assumptions/interfaces first, then coupled components — selected** | Establish the urban state/order, interface, information and derivative contracts, then solve the necessary component blocks in dependency order before the final report. | Best protection against incompatible local choices; makes the deliberate deferrals and ownership amendments visible; supports the complete V0–V4 framework. | The first complete worked model appears later. Keep the audit bounded so it does not become a survey of every possible simulator. Global gates precede dependent local ones. |
| **Representative mechanism first, then full-suite completion — unselected** | After the common outer audit, use one V3 finite-bay obstruction case to develop the selected coupled mechanism concretely, then check its V0/V1/V2 limits and V4 applicability. | Produces an intuitive worked model early and may expose the few decisions driving most of the problem. | Can overfit assumptions to one example and require rework in other variants. Concrete method/global-contract decisions still need their gates; P8 reconsideration itself is already authorized. One successful V3 case cannot close the full review, and scope is not silently reduced. |

Use the selected first order. Evidence that it must change would require
an explicit reconsideration of that ordering decision; the alternative is
not an active continuation. A worked V3 example can still explain a coupled
component after its governing global contracts are settled.

The global contracts are shared within urban: components agree on state,
order, timing and conservation; variants retain common action/objective/
accounting conventions; comparison models share the physical task and
fairness rules while retaining their own representations/laws. The decision
does not demand one model common to VSL and urban.

The immediate next assignment for a fresh urban agent is **steps 0–1 only**:
propose the precise standard, recover the accepted state and present the
gap-to-review/ownership matrix and bounded sprint sequence. Stop at that
opening gate. A full new literature review, law selection or report-only
rewrite is not inferred from this planning discussion.

[Updated fresh-agent handoff](urban_report_refinement_fresh_agent_handoff.md)

[Updated copyable opening prompt](urban_report_refinement_start_prompt.txt)

[Work and verification record](vsl_urban_planning_followup_work_report.md)
