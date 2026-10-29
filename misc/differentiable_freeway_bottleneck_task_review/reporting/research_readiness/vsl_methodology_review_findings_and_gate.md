# A coherent lane-information task, with explicit adaptation and claim limits

2026-10-21. **Approved analytical review completed; delivered at JM1.**
No new methodological choice is required by this review. User acceptance
of these findings remains the checkpoint; no later work starts automatically.

The joined stack is a defensible elementary task at the methodological
level. It describes traffic by lane densities, lets drivers seek neighboring
lanes, restricts all competing movements by common traffic and space budgets,
and counts every unfinished unit through the lane-drop exit. Its assumptions
and derivative fit the same physical update. The review therefore supports
recommending it as a candidate for the intended lane-information question.

The honest description is **a published lane-density framework with a
qualified congestion/VSL budget and one explicit replacement of movement
realization**. It is a completed adaptation, not a verbatim published
benchmark. That replacement contains several related assumptions; calling
it one component does not make those assumptions disappear. The review
does not establish empirical fidelity, a need for full lane detail, or a
performance advantage for gradients. None is required to finish this review.

**What model is actually formed.** E is the ending lane, A its adjacent
continuing lane, and B the farther continuing lane. These are current lane
stocks, not permanent vehicle classes: traffic leaving E becomes traffic
in its receiving lane. Ordinary redistribution and preparation occur along
the approach; at E's last cell, traffic must enter A's outlet or wait.

The lane-density framework of Nagalur Subraveti and colleagues [1] supplies the
reasons for changing lanes: relative density, approaching the lane end,
keep-right behavior and cooperation. The same-author thesis clarifies the
lookahead weights [2]. The already selected Han lineage [3], [4] supplies traffic and
receiving budgets and the advice-dependent sending restriction. The
Carey/Wright-based composition [5], [6] decides which requests can happen together.
The model adds no microscopic identities, ordered driver records or
separate slow-entry/recovery meter.
Reference numbers correspond to the linked source audit and its IEEE list.
Realized merging follows current desires and shared service; only the
nominal priority weights are fixed.

| Part | What is retained or changed | Why the interface fits; important limit |
|---|---|---|
| **Traffic state and lane preferences** | Retain lane densities and density/incentive-based desires. Declare the common FD, mode choices, finite lookahead and empty-donor conventions. | Preferences say where traffic wants to move; they do not grant extra traffic or receiving space. These conventions are explicit member assumptions, not recovered author code. |
| **Traffic/receiving service and VSL** | Use the selected full Han budget from the principal paper's congestion lineage; advice caps sending. | Each receiver has one common allowance for all arrivals. Advice affects later receiving through traffic-state evolution, not a separately prescribed advice-to-merge formula. Source calibration and wave fidelity do not transfer. |
| **Realized movements** | Replace the native same-cell lateral/adjusted-forward sequence with joint donor normalization, capped sharing, diagonal advancement and one forward fallback. | Every departure spends one donor budget and one target budget. All flows use old stock. At E's end no forward escape exists. This is the substantive adaptation; it need not maximize unrestricted throughput. |
| **Task and completion** | Initialize a closed cohort, choose one constant common advice, and complete traffic across the common free outlet line. | All unfinished mass is counted until this exit, with no external holding queue. Travel after the line is outside the declared task. These boundaries limit the claim and introduce no downstream traffic mechanism. |

**Root assumptions.** This qualification uses continuous mass, fixed finite
geometry and a common lane FD; initial traffic independent of advice; one
positive constant advice; no later arrivals; free A/B outlets; old-state
one-row advancement with a valid time step; fixed positive priorities and
unit merging-headway consumption. They define the elementary member. Their
empirical validity and robustness to changes are not established here.

**The direct answers to VC1–VC3.**

| Question | Finding and conclusion |
|---|---|
| **VC1: does the joined model form a coherent, supported whole?** | **Yes, conditionally on the declared common-FD, geometry and boundary assumptions.** The selected budgets supply nonnegative available traffic and receiving space; normalization and allocation prevent reuse; the simultaneous update conserves mass and respects storage. The source joins are explicit and require no additional state or traffic law. The adaptation remains ours, with fixed nominal priorities and no extra merging-headway penalty. |
| **VC2: are full accounting and sensitivity justified?** | **Yes for this closed-cohort discrete model, with qualified switching behavior.** The complete residual value follows from eventual unconstrained advancement. Its assumptions hold for the selected allocator. A bounded additional argument establishes a finite partition of advice into intervals with rational full-objective formulas; ordinary derivatives exist inside those intervals. At switching values, jumps or unequal slopes can remain. This is an analytical result, not a software-gradient check. |
| **VC3: does the task support the intended question and colleague response?** | **Yes as a focused lane-information task; a positive control benefit remains an open research outcome.** The actual A/B diagnostic proves that the reduced observation loses service/transition information. One adjacent-lane scalar recovers the diagnostic modes exactly. Thus the task can ask how much information is enough, but cannot use this pair to claim that all lane fields or discrete order are necessary. A fair scalar-search rival remains essential to any future optimizer claim. |

**Why the accounting and derivative checks are substantive.** Continuous
traffic can approach zero without becoming exactly empty at a finite update.
The model avoids discarding the residual. Once the remaining cohort is small
enough, every requested movement receives service. Every unit then advances
at the same advice-dependent rate, regardless of its lane. Its remaining
distance determines its exact remaining population-time.

The prior progress proof is valid for the joined model: the furthest
occupied row always has a positive-service destination; no arrivals can
replenish the road. The argument can allow every admissible desire split,
so it does not incorrectly assume that the native incentives are continuous.
Its compactness argument also supplies one finite prefix length that works
throughout the allowed advice interval. No numerical stopping tolerance or
traffic run is needed for this conclusion.

That common finite prefix is useful for sensitivity. Each update has only
finitely many branch choices and uses arithmetic and ratios on a chosen
branch. The resulting rational functions are ratios of polynomial expressions
in advice, with continuous-valued traffic stocks. For fixed initial traffic,
only finitely many advice values can
separate the resulting rational formulas. Persistent exact ties can belong
to an interval; they do not require a global state derivative. Thus the
complete objective really has ordinary speed sensitivities on intervals,
including its future-time term. This does not mean that the derivative is
nonzero, that every chosen advice is regular, or that finding the intervals
is computationally easy.

The full sensitivity includes three effects: changes in the simulated
prefix, changes in the residual stock, and the direct effect of advice on
the residual's travel time. Native switches can invalidate a two-sided
derivative at their advice values. The evaluator uses fixed time steps;
the old continuous-time point model's saltation formula is not applicable.
No smoothing or replacement traffic rule was needed.

**An important boundary on the information claim.** In the unconstrained
small-cohort regime, changing the lane split while retaining the same
traffic at each road position leaves the complete objective unchanged.
Faster advice simply reduces all remaining travel time. The maximum
allowed advice is optimal for every nonempty state in that regime, and
lane information has no action value. This is a useful analytical negative
case, not a defect to remove.

The existing X/Z diagnostic is outside that regime. Its same E and A+B
profiles give different E service and exit flow because receiving and
continuing-lane redistribution differ. That is a genuine state-information
effect under the selected rule. It is not a complete-objective action
certificate. Whether the two cases favor different advice, or share the
same best advice, remains unproved. The equations contain a state-dependent
congestion channel rather than a universal rescaling of time, but that
alone does not prove that slower advice ever wins. This review establishes
no general maximum-advice dominance theorem and no positive-gap theorem.

**Which simpler rivals remain credible.** The central reduced observer
knows E and rowwise A+B and may reason over the known hidden-state
distribution; it must not be weakened to an arbitrary equal-lane guess.
The extra final-A density is exactly sufficient on the two-state diagnostic.
Maximum advice is the natural common-fastest reference. With one constant
scalar control, bounded scalar search is a strong optimizer rival. These
comparisons isolate information and optimizer value within the same plant.

The [earlier Jin–Jin aggregate/spatial task comparison](vsl_published_backbone_findings.md)
identifies a simpler published
alternative if the question becomes traffic location along the road. It
does not retain the selected hidden A/B distinction. History-aware aggregate
or source feedback controls remain relevant comparison directions, but
different observations, action timing or dynamics cannot silently be credited
as the same information comparison. Future aggregate flow can reveal the
mode; the current decision is made before that flow is observed.

**What this answers about complexity.** We can now give a narrower and more
credible response than defending the original collection of mechanisms:
the candidate uses an established lane-density/incentive architecture, its
cited congestion lineage and a single explicitly qualified movement component.
The thesis and two Han papers explain existing modeling families; Carey and
Wright support allocation principles. Six references do not mean six added
physical mechanisms. Equally, their number does not prove simplicity.
The reduction concerns the amount of traffic modeling we author; the model
still retains physical cells, lane redistribution and congestion dynamics.
The task layer remains ours: the papers do not supply this exact closed-cohort,
one-advice, hidden-A/B comparison as an unchanged published scenario.

The real remaining modeling burden is visible: the native transport stencil
is changed, the receiving allocator is a new composition, and free outlets,
common FD, mode conventions and unit merging-headway consumption are
assumptions. In particular, the thesis explicitly omits bounded acceleration
of a lane-changing vehicle. The present stack therefore cannot inherit the
old point model's slow-entry/recovery explanation or its positive-action
certificates. It addresses the same information/control question through
lane densities and congestion, without requiring functional identity to
the old model. This follows the user's accepted review direction.

**JM1 disposition.** The planned analytical/methodological sprint is complete.
Recommend the joined stack as a conditionally qualified elementary candidate,
with the adaptation and limitations above. No new component or methodological
fork is needed to make the model/accounting/sensitivity contracts coherent.
Numerical correctness, useful gradients and physical validity remain future
evidence, not missing review tasks. User acceptance of JM1 is pending.
The accepted report and original Step 4, separate historical gates, closed
ramp line and urban work are unchanged. Stop here; no implementation or
experiment is opened.

[Analytical addendum: regularity and the free-flow information limit](../../synthesis/research_readiness/vsl_methodology_review_analytical_addendum.pdf)

[Source/adaptation and interface audit, including reference list](../../extraction/research_readiness/vsl_methodology_review_source_and_interface_audit.md)

[Work record and preservation checks](vsl_methodology_review_work_report.md)
