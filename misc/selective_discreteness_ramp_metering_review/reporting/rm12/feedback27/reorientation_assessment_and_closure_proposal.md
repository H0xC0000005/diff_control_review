# Return to an elementary companion task

Date: 2026-10-12. Response to feedback 27. Status: **assessment accepted;
method-first ramp line subsequently closed by explicit user approval.**
The accepted VSL transition roadmap is ready for a fresh agent's opening plan.
The assessment below records the reasoning before approval; its prospective
closure/discussion language is superseded by the final disposition.

[Final closure, retired gate and evidence handoff](method_first_review_closure.md)

## The main conclusion

I support stopping the current ramp-metering construction and returning to the
VSL lane-drop task. The strongest reason is its **role in the intended study**:
the ramp branch has not produced a qualified elementary companion to the urban
task. Its recent work has needed increasingly detailed coupling between
continuously moving restrictions, the ordinary traffic field and timestep
updates. Those questions are legitimate, but completing that model has become
a substantial scientific project before the proposed first verification can
even begin.

This is a sound task-selection reason to close the branch. It is not evidence
that ramp metering is universally simple, that PID is optimal, or that useful
fine-information gradients are impossible in freeway merging. The existing
partial results should survive the closure with their original claim limits.

The VSL task is a better starting point because it already has an accepted,
bounded causal example: information about traffic still needing to merge can
change both the preferred common speed advice and the analytical improving
direction. However, that result is not yet a complete research methodology or
a novelty finding. The next review should turn this small result into a clear,
source-supported task before enlarging its traffic model.

## 1. Comments on the process and the new purpose

The colleague discussion adds two task-selection requirements: the freeway
case should be an elementary first verification, and it should contribute to
one understandable research story with the urban case. These requirements were
not the binding criteria of the previous method-first freeway opening. That
opening explicitly allowed different models, software and papers after the
task evidence was assessed. The change should therefore be recorded as an
intentional change of purpose, rather than retroactively treating every ramp
decision as a mistake.

[Earlier method-first opening and its paper-unity boundary](../../../../differentiable_freeway_bottleneck_task_pre_review/pre_review_closure_and_handoff.md)

A shared research story does not require identical traffic equations. The urban
case asks whether local movement order and finite lane access change useful
service-allocation gradients. The present VSL example asks whether merge
preparation changes useful common-speed gradients. Both can examine the minimum
traffic information needed to predict a worthwhile control perturbation, with
continuous conserved mass, strong simpler models and complete traffic-time
accounting.

There is also an important limit to that connection. The accepted VSL example
can compress its consequential lane state to **one continuous remaining-merge
statistic**. It does not establish that discrete vehicle identity, FIFO order
or full per-lane state is necessary. It can be an elementary companion showing
how to test information value and gradient value separately. It cannot be
presented as a second proof of the urban discrete-order hypothesis without
additional evidence. The paper framing must make this distinction explicit.

That leaves one important framing question for the next discussion: is VSL
intended only as an elementary information/gradient verification, or must it
also directly validate selectively retained discrete metadata? The accepted
member supports the former; it has not qualified the latter. Connecting the
two cases in a paper must not silently broaden the project's primary
discreteness hypothesis. No project-level claim amendment is made here.

[Accepted VSL result and nonclaims](../../../../differentiable_freeway_bottleneck_task_review/reporting/s13/s13_99_m2_certificate_sprint_closure.md)

[Why one scalar can suffice in the current VSL member](../../../../differentiable_freeway_bottleneck_task_review/reporting/s13/s13_35_study_sufficiency_and_extension_audit.md)

The lesson for the next review is to check task role and the shared claim early.
Do not continue constructing a model merely because its next local interface
has a legitimate unresolved question. When resolving that question would turn
the elementary companion into a different research program, return to task
selection before proceeding.

## 2. What needs correcting in the proposed reasons and next steps

### Ramp metering gives strong influence, not complete control of traffic

The meter controls upstream admission permission. It does not directly control
mainline demand, downstream receiving, traffic already stored on the ramp or
the motion of earlier entrants. Our last selected task deliberately separates
permission, approach admission and actual merging. Holding traffic also costs
time, which the all-stream objective must count.

Established feedback methods are serious competitors. ALINEA, for example,
regulates downstream occupancy using integral feedback; a full PID controller
is a different controller specification. Their existence does not show that
any one of them optimizes the complete objective under all constraints.
Official guidance explicitly treats the tradeoff between mainline conditions
and ramp waiting/queues. [FHWA ramp-management handbook, §5.3.1](https://ops.fhwa.dot.gov/publications/ramp_mgmt_handbook/manual/manual/5_1.htm),
[FHWA detector handbook, local traffic-responsive metering](https://www.fhwa.dot.gov/publications/research/operations/its/06108/03.cfm).

PID is also a feedback rule, not a traffic representation. A comparison against
PID can test controller performance, but by itself cannot isolate what traffic
information a prediction model loses. A fair gradient study keeps representation
and optimization/controller comparisons distinct.

Thus, the defensible ramp conclusion is that **this reviewed construction is
not admitted as the intended elementary companion**, not that the control
problem is solved or inherently trivial. Strong conventional alternatives and
the unresolved diagnostic value support that role decision, while the missing
whole-model construction prevents stronger scientific claims.

### A well-studied control problem can still support a representation study

The maturity of ramp metering is a reason to demand a precise contribution,
not a proof that all meaningful information questions are covered. The same
warning applies to VSL: macroscopic VSL optimization is established, including
METANET-based predictive control. First-order VSL/capacity-drop models and
multilane macroscopic lane-changing models also exist.
[Hegyi, De Schutter and Hellendoorn, 2005, abstract and §3](https://www.dcsc.tudelft.nl/~bdeschutter/pub/rep/03_016.pdf),
[Wei, Han and Wang, 2025](https://onlinelibrary.wiley.com/doi/full/10.1111/mice.13492),
[Carey, Balijepalli and Watling, author manuscript](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf).

These precedents do not jointly settle the proposed VSL information/gradient
question. They do rule out assuming that a VSL label, lane resolution or a
differentiable control objective is itself new. The next review must ask what
the closest existing models retain, which causal effect they already reproduce,
and whether the proposed comparison adds an unresolved result.

Your third requirement should therefore be tested as a specific claim:

> Is there a source-supported VSL regime in which a declared simpler model
> omits information that changes a useful common-action direction, and what is
> the smallest augmentation that repairs that omission?

Do not assume the answer is yes. If aggregate-plus-scalar state reproduces the
relevant behavior, that is a meaningful minimum-information result, but it
cannot support a claim that fuller mesoscopic information is required. If the
same comparison and conclusion are already established, the case may remain
useful for elementary verification while failing the proposed novel-study role.
Those are different dispositions; the latter must not be concealed by calling
the former a new research contribution.

Gradients do not supply missing traffic information by themselves. The model
must first represent the causal dependence that changes action value; the
gradient then exposes a direction within that model. A correct derivative of
an incomplete model can still give the wrong traffic-control advice. This is
why the new framework must separate model information, derivative correctness
and independent decision usefulness.

### VSL needs refinement, not promotion of the S13 proof into a field model

Within the accepted analytical member, slower common advice gives traffic more
time to transfer out of the ending lane before the choke. That can reduce merge
work, but adds travel time. When little merge work remains, fastest advice wins;
with more remaining merge work, a slower interior action can win. This is why
the example avoids a universally best endpoint under its stated assumptions.

The exponential transfer specialization and proportional batch clearance are
explicit analytical adaptations. They have not been calibrated as universal
freeway laws. Preparing paper-like prose cannot remove that limitation. The
next review must either justify their bounded use and robustness, or replace
only the smallest unsupported element with a source-supported alternative.

[Source adoption versus analytical adaptation](../../../../differentiable_freeway_bottleneck_task_review/extraction/s13_m2_source_to_equation_audit.md)

The urban task needs an audit before any rewriting. Its closed review already
contains a formal action/objective/derivative contract, a V0–V4 mechanism suite,
baseline realizations and an external-evaluation protocol. It is more developed
than a purely conceptual sketch, although numerical settings and implementation
choices remain downstream. Reuse that approved content and fill only the gaps
needed to align the two tasks at methodology-section level.

[Closed urban task and formal formulation](../../../../selective_discreteness_downstream_task_review/reporting/closure_record.md)

[Urban task contract and evidence sequence](../../../../selective_discreteness_downstream_task_review/synthesis/experiment_formulation.md)

## 3. Proposed closure and next-step preparation

The proposed closure statement is:

> Close the method-first ramp-metering branch with a negative task-selection
> verdict for the elementary companion role now requested. Preserve its scoped
> negative information audits and positive local modeling results. The branch
> has not qualified a complete forward/control/gradient task, and no universal
> impossibility or PID-optimality conclusion is claimed.

Final closure need not resolve the last field-carryover choice. That choice
belongs to further construction of a task no longer selected. On closure it
should become an **unselected, archived question**, not an implicitly approved
choice or an alleged refuted method.

The handoff should preserve the following facts:

| Item | Last scientific state to retain |
|---|---|
| Earlier implementation-anchored RM0–RM5 | Historical scoped closure; distinct from the method-first reopening. |
| RM9, RM10 and RM11 | Accepted bounded negative findings; no universal no-hidden-information theorem. |
| RM12 BP-I | Operational-input audit did not bind all initial/history knowledge; insufficient admission evidence. |
| RM12 BP-R / Stage 3 | Revised to declared projections of a shared known physical state; supported reference family and partial constructive qualification. |
| Last selected rules | M.A/N.A/G1/E1/K.A/T.A/P.A/D2 remain recorded with their approved scope. |
| Last completed evidence | D2 finite allocator/static consistency; local own-field/motion/transfer/count/birth certificates. |
| Last open decision | Q.J.F.R ordinary-field carryover; neither candidate selected. |
| Unfinished products | Autonomous repeated forward evolution, clearance, complete-TST control response, a qualified independent reduced competitor and useful-gradient evidence. |
| Execution boundary | No traffic simulator, SUMO, optimizer, implementation or traffic-gradient experiment was opened. Stage 4 remains unopened. |

[Last scientific finding and pending field decision](../bp_r_stage3/d2_forward/findings_and_field_gate.md)

The proposed next review has four bounded stages: first check the elementary
role and closest literature; then specify the smallest complete VSL model;
then define fair baseline and gradient tests; finally reconcile the urban
methodology, discuss with the experts and freeze the task/execution plan. The
first product should be a short paper-like methodology outline with its claim
and evidence gaps, not another open-ended solver-construction program.

[Draft VSL transition plan](../../../../differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/feedback27_paper_ready_transition_proposal.md)

The prior S13 robustness/domain/comparison/freeze roadmap remains an accepted
historical proposal. The new draft puts task role, paper connection and nearest
literature coverage before detailed refinement. Its changes are explicit and
are not silently treated as approval to execute that roadmap.

## 4. A fresh agent is appropriate for the next task

I recommend a fresh primary-agent conversation for the VSL formulation after
the disposition is agreed. The next job is task specification and paper-method
design; this conversation mainly carries a long review and its local gates.
A fresh context can reduce the tendency to continue the most recent ramp
interface instead of assessing the new task's purpose.

That is a context-management benefit, not an assurance of scientific independence.
The next agent must read the accepted VSL result and its limitations, the closed
urban task and the transition scope. It should not start from a blank literature
search or treat the S13 theorem as a calibrated model. It also should not import
the ramp moving-particle construction into the elementary VSL task by default.

Keep the accepted sources and findings in their current branches. Give the
fresh agent a small authoritative reading packet with separate labels for
approved results, new proposed requirements and unresolved decisions. Ask it
to draft the bounded review/task plan first. Later implementation should be a
separate approved task under the repository workflow.

[Prepared fresh-agent handoff](../../../../differentiable_freeway_bottleneck_task_review/reporting/research_readiness/feedback27_fresh_agent_handoff.md)

No agent has been spawned, and no message has been sent to colleagues.

## Work and evidence limits

Read feedback 27 and the current ramp checkpoint, VSL S13 closure, source audit,
study-sufficiency audit, deferred roadmap and closed urban task formulation.
Rechecked the listed primary publications and official ramp guidance on
2026-10-12 only for the bounded claims above. This is not a new comprehensive
novelty search, evidence that PID attains the optimum, or a fresh VSL robustness
review. The proposed VSL contribution remains unverified.

Created this response/closure proposal, a VSL transition draft and a fresh-agent
handoff. Updated branch entry points to mark the reorientation discussion hold
and appended its dialogue record. The feedback inbox receives only the allowed
`(answered)` marker. Commands: read-only `rg`, `sed`, `cat`, repository status and
SHA-256 snapshots; browser primary-source checks; `apply_patch` document edits;
local-link/status/preservation checks. No scientific test or traffic run is
appropriate to this documentary assessment. No project context, roadmap,
production code, source evidence, closed conclusion or equation is changed.

Subsequent boundary, 2026-10-12: the user accepted the assessment and transition,
then explicitly instructed proper ramp closure. The line is now closed, its
unselected field gate archived, and further ramp qualification discontinued.
The accepted VSL roadmap awaits a fresh agent's bounded opening plan; the
detailed successor review and implementation have not been executed here.

Document checks passed: 23 local links in the three new artifacts resolve;
the feedback edit is only its allowed answered marker; the dialogue is
append-only. SHA-256 comparison of the 674-file pre-edit snapshot confirms
that closed records, source evidence, urban task files and project context/
roadmap were preserved. Only the listed branch navigation/status records,
dialogue and feedback marker changed among existing files. Existing user-owned
AGENTS.md/PLANS.md modifications were preserved.
