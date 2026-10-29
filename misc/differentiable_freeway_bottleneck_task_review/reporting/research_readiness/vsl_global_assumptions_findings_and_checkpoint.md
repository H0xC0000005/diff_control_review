# The global assumptions form a coherent conditional task

Date: 2026-10-19. **Assumption audit completed; GA-G1 user-accepted.**
The user accepts the established assumption set and has no further checks
for the report plan. The compact methods report is the agreed first writing
priority; no additional methodological planning gate is required to draft it.

The review found an explicit, compatible assumption set for the existing
standalone VSL task. No new traffic law or methodological choice is needed
to write that set down. This is the completed preliminary review for the
report; the full report has not been started.

The model's traffic story is now clear from its roots. Start with a finite,
initially unqueued population approaching a lane drop. Traffic remaining in
E tries to move into A before the terminal, using receiving left after A's
own traffic. Whatever remains in E reaches the choke and needs additional
shared service to merge. Forced E entries can also reduce subsequent service
temporarily. Common speed advice changes both ordinary travel time and the
traffic state that determines those interactions. All travel and waiting
through local completion are counted.

That is one consistent conditional modeling world. It is not a claim that
every real lane drop follows these rules, nor that lane information always
changes the best advice.

## What the audit actually establishes

The earlier work contained many of the required assumptions and had checked
important dependencies. The gap was that they had not been assembled and
examined as a complete root set. This pass read the current asymmetric
forward, information and sensitivity definitions, the joined equations and
forward proofs, and the accepted source/physical-limit records together.

| Core question | Direct answer | Consequence for the report |
|---|---|---|
| **Can the whole model's assumptions be stated without adding a missing law?** | Yes. The task definitions, five backbone assumption groups, local closures and causal branch conventions account for the existing dynamics. | The report can introduce the world first and then formulate its four mechanisms. A reference or a component heading no longer has to carry an unstated global premise. |
| **Can those assumptions hold together over the advice interval?** | Yes within the already accepted sufficient domain. AS1's independent-lane family provides a nonempty example with common coefficients and positive admission margins. | Keep the conservative domain explicit; do not claim arbitrary demand, initial queues or spillback. No new numerical bound or physical calibration was selected. |
| **Does literature establish the entire assumption set?** | No. It supports important ingredients, while homogeneous exchange, the chosen marks/sharing/work law and recent-mass renewal include declared adaptations or study-defined closures. | Give assumptions and provenance separate statements. Mathematical coherence does not turn the joined model into an empirically established traffic law. |
| **Do all conclusions follow under one universal condition set?** | No. The common traffic world has additional conditions for each stronger result. | Attach the history-loading, action-existence and ordinary-gradient conditions to those results. Retain common-action outcomes and nonregular cases. |

## The consequential assumptions, in traffic language

**We keep lane differences but simplify traffic within a lane.** The initial
lane loads are independent, including a hidden A/B imbalance, while each
lane's preparation body is homogeneous. This is enough to distinguish an
easy receiver from a crowded adjacent receiver without tracking positions
inside the preparation region. It excludes longitudinal waves there. The
storage/underload bounds keep the terminal from invalidating that closure.

**Advice acts through the chosen traffic response.** Unblocked traffic
follows the common advice in the selected FD family, with physical parameters
fixed across candidate advice. The merge law then responds to traffic state.
Queued boundary speeds are representative equilibrium marks, not measured
individual trajectories. This is an important modeling assumption; a source
reference alone does not make it a validated speed-response relation.

**Early transfer and forced transfer have different modeled consequences.**
An E unit that successfully merges before the cutoff becomes ordinary A
traffic. The model does not retain a separate early-merge disturbance for
it. Residual E alone undergoes forced-merge work and creates new recovery
loss at the choke. The terminal itself has no ordinary lateral exchange,
and far-lane service is separate. These are existing boundaries of the
model, now made explicit rather than inferred from the equations.

**The point model has memory, despite having one budget reading.** Current
service depends on a retained age/mark history of recent forced E entries.
That history ages and is renewed by E mass. Its fixed mass normalization
also applies before the window fills. A can be slowed through the shared
budget but is not a separate recovery source. The resulting budget is
predicted, not prescribed as a future receiving curve.

**The restriction is represented at the point.** The task counts completion
at the choke and represents the effect on following traffic through reduced
shared service. It does not resolve a physical downstream acceleration zone
or the spatial shape of a backward shock. This is consistent with the
accepted compact point choice, and limits any later physical claim.

## What must not become a global assumption

The matched-history example needs a loading regime where the past does not
identify unused adjacent receiving. Other admitted histories can reveal A,
and the aggregate-information rival is allowed to use them. One extra initial
adjacent statistic still matches the per-lane predictor exactly under the
known initialization. The task does not prove that a large lane representation,
discrete identities or integer mass is necessary.

The positive action certificate may require large forced work, weak mismatch
and fast recovery, and keeps A free. The witness with A delay and active
retirement is a different conditional reference. Combining them into one
jointly realistic, positive-control example would exceed existing evidence.
There is also an admitted range where both hidden states prefer fastest
advice. Neither a useful information gap nor an interior optimum is assumed.

The ordinary complete derivative needs its regular local event/history
conditions. Those conditions are not prerequisites for every forward case.
Nonregular cases stay in the task, with honest one-sided or finite-change
reporting. Numerical gradient correctness and usefulness remain future
evidence, not assumptions that complete the model.

## Correction and completion gate

The audit found one stale live-document restriction: the future physical-
admission contract still said that continuing lanes were initially symmetric.
It now follows accepted AS1 independent E/A/B initialization and actual
three-lane mass. This synchronizes the document with an existing decision;
it does not revise an equation or claim a newly admitted physical range.
Historical proofs, PDFs, source audits and their evidence remain unchanged.

| Planned item | Checkpoint finding |
|---|---|
| **GA-Q1: global representation/causal assumptions** | Complete at review scope. The short statement covers the selected world and retains independent initialization, actual history and point-model limitations. |
| **GA-Q2: compatibility/domain/support** | Complete at review scope. The joined domain is nonempty, common across advice at fixed data, and distinct from physical admission. Source guarantees are not transferred wholesale. |
| **GA-Q3: claim dependencies** | Complete at review scope. Forward, information, finite-action and derivative results have separate explicit conditions and limits; desired outcomes are not premises. |
| **GA-L1: transcription** | Complete. Premises are traced to exact existing sections/equation labels, the old symmetry statement is aligned, and active report notices point to this result. |

**Stop at GA-G1.** The bounded audit is complete and no new methodological
choice was identified. The audited assumption statement is ready to use in
the compact methods-writing pass after this checkpoint. No full report,
simulator, dependency installation or traffic/gradient experiment is opened
by this completion. Original Step 3's recorded formal closure status is
unchanged; applied MP6 remains unexecuted and SUMO optional.

[Short assumption statement for the report](../../synthesis/research_readiness/vsl_global_assumptions_statement.md)

[Premise, source and claim-dependency audit](../../extraction/research_readiness/vsl_global_assumptions_dependency_audit.md)

[Approved audit plan and execution status](vsl_global_assumptions_audit_plan.md)

[Exact static domain/witness checks](vsl_global_assumptions_static_results.json)

[Work, commands and preservation checks](vsl_global_assumptions_audit_work_report.md)
