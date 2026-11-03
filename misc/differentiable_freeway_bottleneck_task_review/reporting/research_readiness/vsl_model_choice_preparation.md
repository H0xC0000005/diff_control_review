# Preparing VSL planning while the model choice remains open

2026-10-29. **Preparation complete; presented at the requested checkpoint.**
The peer-backed formulation remains the provisional candidate. The completed
task-first formulation remains available for the colleague discussion. This
preparation selects neither version and opens no implementation phase.

Both versions ask whether knowing the division of traffic between adjacent
lane A and far lane B helps choose one common speed advice when ending-lane
E traffic and total continuing traffic are known. They answer that question
through different traffic mechanisms. We can consolidate the research
requirements now, but the selected mechanism must determine the later
software architecture.

## What the pending discussion can change

The recorded colleague concern is difficulty distinguishing the two tasks;
the existing one-page comparison addresses it. The user also requested a
published backbone with few adapted dependencies. The reviewed peer-backed
candidate supplies that construction, with explicit adaptations. Neither
record supplies final colleague agreement on which version to implement.
No additional, unrecorded colleague objection is assumed here.

Two kinds of response have different consequences. Clarifying who supplies
a formula or what the task can claim can leave the model intact. Choosing a
different propagation, merge-service or recovery mechanism changes the
physical evaluator and its later implementation plan. Pending discussion
therefore does not require reopening the entire review, but a request to
combine these mechanisms would require an explicit scientific decision.

For example, imagine E waiting at the choke while A is busy and B has room.
The task-first model keeps B separate and lets recent forced E entries
restrict later A/E service through a recovery account. The peer-backed
model permits continuing-lane redistribution and uses current lane-cell
densities, congestion laws and shared receiving; exited E traffic leaves
no recovery account. These are different causal explanations of service,
not interchangeable implementations of one merge rule.

[Existing one-page functional comparison](../../synthesis/research_readiness/vsl_task_functional_comparison.pdf)

## Requirements that can be carried forward

The following are already shared at the level stated. Consolidating them
adds no traffic law, parameter choice or new claim of colleague consensus.

| Shared requirement | What it establishes for later planning |
|---|---|
| **Decision and information question.** A three-to-two lane drop, continuous mass, a fixed finite initial cohort independent of one positive constant common advice, and no later arrivals. Hidden A/B loading is the central information distinction. | Preserve this elementary decision question. The permitted initial fields, numerical advice bounds and spatial observation shapes remain specific to each version. |
| **Complete time accounting.** Count every initial unit from the decision until it crosses the designated choke exit. | No omitted residual traffic or external holding cost. The objective formula and its completion procedure must follow the chosen dynamics. |
| **Conserved and feasible traffic.** Realized movements respect the selected model's traffic, service and storage constraints. | Conservation and feasibility are required; their mechanisms and admissible operating domains are not identified across versions. |
| **Fair information comparisons.** Within one chosen plant, compare admitted observations under the same objective, action opportunity and eligible history. Allow legitimate inference and a compact informative rival. | A different plant cannot stand in for the reduced observer. Observation sampling and any compact statistic need the chosen model's definition. |
| **Separate evidence claims.** Forward conformance, derivative correctness, information value, optimizer usefulness and physical fidelity are different questions. | Reuse this evidence structure. Include maximum advice and simple equal-information scalar search as reference directions; executable methods, budgets and tolerances remain for planning. |

The shared objective meaning does not supply a shared residual formula.
Likewise, using triangular-diagram ingredients does not supply a shared
advice-to-capacity law. Illustrative numbers and source-specific assumptions
are not promoted to common fixed settings.

## What selecting a version would require us to plan

This table maps scientific differences to planning consequences. It does
not prescribe software components or interfaces.

| Difference | Task-first formulation | Peer-backed formulation | Consequence for Phase A |
|---|---|---|---|
| **State and admissible initialization** | Uniform approach lane densities; initially empty terminal and recovery account; bounds keep preparation free and B unqueued. | Densities by lane and road cell; nonuniform and congested initial cells are admissible. | State ownership, initialization and reference scenarios depend on the choice. The new near-choke diagnostic cannot be transplanted unchanged into the old domain. |
| **Propagation and early movement** | Homogeneous preparation, receiving-limited E-to-A transfer, then terminal travel delay and point service. | Old-state longitudinal/diagonal advances, density/lookahead incentives, adjacent lateral directions and shared budgets across the road. | Update coupling and the sequence of calculations must be derived from the selected representation. |
| **Scarce merge service and history** | Free-A priority, queued A/E work sharing, speed-mismatch work and recent-discharge recovery. | Fixed equal receiver priorities, capped sharing and unused-share redistribution; unit receiving consumption; history retained through current densities. | Retained memory and service calculations differ. Adding old recovery to the new allocator would create another model. |
| **How advice acts** | Changes the effective diagram's critical density/capacity and arrival timing; point ceilings remain separately fixed. | Caps sending with the nominal diagram fixed; congestion and receiving evolve with density. | Advice dependencies and sensitivity paths must be specified separately. |
| **Complete objective and derivative** | Continuous-time travel/waiting accounting and queue/service/history events, with event-time corrections where required. | Fixed-step population-time plus its derived exact residual; regular-branch differentiation includes residual-state and direct-advice effects. | Evaluator, stopping/completion treatment and derivative checks follow the selected mathematics. Neither construction is copied into the other. |
| **Observation and compact information** | Homogeneous initial lane masses; adding A mass to E and A+B reconstructs that initial state. | Matched rowwise E and A+B observations; final-A density identifies the two diagnostic states only. | Neither observation arrays nor a general claim of compact sufficiency transfer unchanged. |

[Completed task-first model and sensitivity](../../synthesis/research_readiness/vsl_compact_methods_report.pdf)

[Complete peer-backed model and analytical qualification](../../synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.pdf)

[Detailed explanation of the functional differences](vsl_feedback16_old_and_peer_backbone_comparison.md)

## Evidence that remains attached to its own model

The peer-backed diagnostic establishes different service and next-state
evolution under identical E and A+B observations. It does not prove
different optimal advice. The extra final-A reading is sufficient for
that pair, not for every lane field. Its unconstrained cases can have zero
information value and favor maximum advice. These are legitimate outcomes,
not reasons to add the old recovery law or choose favorable scenarios.

The old point model's mechanisms, operating bounds and analytical results
likewise remain conditional on that model. Neither version inherits the
other's control conclusions, derivative formulas or physical validation.
The peer-backed construction retains its source/adaptation qualifications:
Subraveti with inherited Han budgets and a Carey-led movement adaptation,
not a verbatim published or author-certified version of the assembled task.

[Peer-backed conclusions and limits](vsl_methodology_review_findings_and_gate.md)

[Sources and global assumptions](../../extraction/research_readiness/vsl_joined_candidate_sources_and_assumptions.md)

[Prospective information and derivative comparisons](../../synthesis/research_readiness/vsl_joined_candidate_verification_contract.md)

## Checkpoint and the subsequent starting point

This preparation is complete. No new conflict requiring a change to either
backbone was found. Different initial domains, service mechanisms and
derivatives are established differences, not gaps to repair by forcing a
common architecture. The shared requirements and the consequences of each
choice are now available for later planning.

What remains open is which version the user will select after colleague
discussion, and whether any specific subsequent feedback requires an
amendment. No answer is required merely to finish this preparation. There
is no new literature sprint, prototype, experiment or mandatory external
validation task attached to this checkpoint.

After selection, align the VSL handoff with the chosen version and record
any amendments. Then open one full Phase A proposal for that version:
state/data ownership, components and interactions, algorithms, checks and
implementation order. The VSL bootstrap's earlier next-action wording
does not override the user's current hold on opening that proposal.
The user is also the developer; a fresh-developer onboarding exercise is
unnecessary. This review pass stops here, without selecting a version,
freezing a shared architecture or beginning Phase A.
