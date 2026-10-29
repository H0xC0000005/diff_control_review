# H1 can close early merging without resolving traffic at successive positions

**The homogeneous route remains viable for a restricted analytical task.** A
uniform cohort can carry one changing ending-lane density and one adjacent-lane
density. Each early merge reduces the first and increases the second. The
adjacent lane consequently claims more of its available service for its own
traffic, leaving less for later merges. This gives the approved P1 causal
chain a concrete, autonomous realization without keeping separate traffic
states at successive road positions.

The qualification is conditional. The construction below is an explicit
homogeneous adaptation of a local receiving rule, not a theorem reducing
Carey's complete CTM or LTM to one stock. It also exposes the next consequential
interface: **a finite physical cohort reaches the lane end over time, and any
waiting there must be reconciled with upstream motion.** Homogeneity has not
been disproved. A complete delay-producing H1 task has not yet been admitted.

Date: 2026-10-13. The user selected **H1 for continued qualification**, preferring
to retain intra-zone homogeneity until evidence shows that it is inadequate.
This bounded H1 pass is complete. It returns to the original **VSL-B2-G1
system-interface gate**, now with a specific terminal-compatibility question.
It does not open another broad review stage or adopt the candidate equations.

## What traffic H1 can describe

Consider a finite, uniformly occupied traffic footprint already inside the
fixed preparation area at the decision instant. The ending lane and its
adjacent continuing lane share the same footprint and common realized speed.
The second continuing lane initially has the same density as the adjacent
lane. There are no later arrivals in this diagnostic member.

“Uniform” means that every occupied part of a given lane has the same density
at a given instant. The density can change over time, and the two lanes can
have different densities. We keep the footprint's known front and rear travel
clock; we do not give different positions independent traffic states. A finite
footprint needs edges. Those edges specify which traffic is present, rather
than introducing a succession of independently evolving longitudinal states.

This is a candidate physical initial condition, not an unnoticed reinterpretation
of S13. S13 puts its analytical cohort at the entrance together and later hands
off a simultaneous batch. A positive mass with finite road density instead
occupies a positive length. A finite entrance release is another possible
initial condition, but traffic entering at different times generally has
different preparation ages. It would not automatically preserve this especially
simple homogeneous lane composition. The initial footprint is therefore the
cleaner member to qualify first; adoption still belongs to the shared task
contract.

At each representative occupied part, the ending traffic eagerly seeks a
merge. Own traffic in the adjacent lane takes feasible receiving first. A
merge uses only the remaining receiving work, with a declared gap-work weight.
Donor availability also limits the transfer. Unsuccessful requests remain in
the ending lane and continue toward the lane end on the admitted free-flow
branch.

The candidate uses a fixed physical interaction length to convert a throughput
budget into the rate of changing lane density. This is an additional modeling
assumption: it specifies the scale of repeated early opportunities. It is held
fixed across actions and is not a numerical time step, a changing road-cell
length, or a calibrated quantity supplied by the source. The rate analogue of
donor availability is likewise declared explicitly. The report does not hide
either assumption inside the word “homogeneous.”

## Why it can stay homogeneous while service changes

Suppose all occupied parts have the same lane densities and all apply the same
local transfer rule. They then transfer the same amount per unit length. Every
part of the ending lane loses the same density, and every adjacent part gains
the same density. Common longitudinal motion translates this uniform footprint.
Within the declared model, there is no process that makes one occupied part
denser than another. This is an invariant homogeneous member of the proposed
first-order transport and lateral-balance equations.

For a concrete receiving relation, the qualification uses a triangular
flow–density diagram whose free-flow speed equals the common advice. Its jam
density and backward-wave parameter stay fixed. The admissible initial traffic
and subsequent transfers keep both interacting lanes on the free-flow branch
over the entire advice range. This makes the common-speed assumption internally
consistent in that member; it does not establish driver compliance or a field
speed-response law.

An important distinction is that the **receiving ceiling itself can stay at
capacity while the service left for merging declines**. On this free-flow
branch, adding merging traffic increases the adjacent lane's own forward flow.
That flow consumes more of the same ceiling. The model therefore has real
state-to-service feedback even before congested receiving or upstream waiting
is introduced. It does not yet represent their additional effects.

For example, at one illustrative opportunity, the receiver has eight units
of work per second and each lateral unit uses two work units. When its own
traffic claims two work units, it has six left; when its own traffic claims
six, it has two left. With the same donor offer of two mass units per second,
completed merging is two in the first case and one in the second. Accepted
mass changes later adjacent-lane demand. These are unit-consistent hand
calculations, not traffic experiments or a reachable information-collision
witness.

The allocation principle is supported by Carey's own-lane-priority rule, R1.
The spatially uniform transfer, common-speed restriction, physical interaction
scale and continuous rate analogue are this review's adaptations. They are
not attributed to the source as a joined VSL model.

[Carey, Balijepalli and Watling: local mandatory requests and R1](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf)

## What speed changes, and what information is sufficient

The construction removes S13's assumption that a fixed fraction completes
merging simply because another second has passed. Here, donor progress and
the adjacent lane's spare service jointly determine completion. Slower
motion provides more elapsed time but also brings less traffic through each
physical opportunity per second. If service per unit progress is unchanged,
those effects cancel. In the illustrative triangular diagram, changing speed
also changes the density that the adjacent lane can carry in free flow; that
can change completed preparation. Neither statement proves a net control
benefit after terminal travel and waiting are counted.

The needed information remains small. Preserve S13's **initial** symmetry
between the continuing lanes and a common known footprint. Aggregate mass
and initial ending mass then determine both continuing-lane initial densities.
Afterwards, every early transfer determines the adjacent lane's increase;
the untouched second lane remains known. One ending-mass augmentation can
therefore reconstruct the proposed homogeneous upstream state exactly. This
is a sufficiency result for the candidate, not a new information/action
certificate. If initial continuing-lane asymmetry were admitted, an adjacent
receiver statistic would generally be needed; that expansion is not made here.

A fair aggregate-plus-ending-mass rival must receive the same footprint,
aggregate observations and fixed model parameters. It can use the same
analytical evolution. No full lane profile, discrete order or extra observable
is established as necessary. A one-zone link queue remains a separate compact
model-form rival; this construction uses physical footprint travel for arrival
timing, rather than repeatedly releasing a fraction of the whole cohort stock.

[Jin: the link-queue model and its distinction from kinematic-wave dynamics](https://arxiv.org/pdf/1209.2361)

## The boundary finding that now matters

The front of a finite footprint reaches the lane end before its rear. Its
total arrival rate and lane composition can be obtained from the compact
state and travel clock. There is no geometric discharge tail. There is also
no single instant at which the whole physical cohort becomes S13's exit batch.

If the terminal can accept every arrival, everyone exits when physically
reaching it. H1 then has a complete, internally consistent nonblocking member.
It has an instructive negative conclusion: faster advice reduces everyone's
travel time, while additional early merging saves no terminal waiting. Hidden
merge information cannot change the preferred speed in that member. The
paper could use it as a limiting verification case, but it would not establish
the intended information-dependent useful-guidance contrast.

If terminal service is insufficient, unfinished merging must wait. That
waiting may block ending-lane traffic that is still approaching, or a target
queue may restrict earlier receiving. An abstract point queue that never
feeds back upstream would preserve the proposed travel clock, but its storage
and no-feedback assumption require justification. The existing three-to-two
geometry does not provide an unlimited detached holding buffer by default.
Ignoring this interaction would reproduce the original service-interface gap.

This is the material challenge to the whole task: **the homogeneous upstream
mechanism is possible, but a useful preparation-to-delay tradeoff still needs
a defensible terminal boundary.** It is not evidence that intra-zone
heterogeneity must now be introduced. A compact queue restriction or an
explicitly bounded homogeneous approximation may still suffice. Its meaning
must be reviewed before it is adopted.

## Direct answers to MP1–MP6

| Question | Core answer after H1 qualification |
|---|---|
| **MP1: opportunity and speed** | A progress-based donor offer joined to spare receiving forms a coherent conditional alternative to fixed completion per second. Extra elapsed time alone is not the benefit: speed also changes throughput and, in the diagnostic diagram, available density headroom. The exact opportunity scale is an explicit adaptation, not a sourced universal law. |
| **MP2: feasible early completion** | The proposed local allocation respects donor availability and the adjacent lane's own-lane-first receiving budget. Accepted mass changes later demand and is conserved between lanes. These properties are established inside the homogeneous candidate. |
| **MP3: minimum information** | With the retained initial symmetry and fixed footprint, aggregate mass plus initial ending mass suffices for this upstream candidate. An independently varying adjacent-lane initial state would require more information, but is outside the member reviewed here. |
| **MP4: early and late costs** | Early merging uses finite spare work without slowing traffic in the qualified free-flow member. Late waiting and any feedback from it remain consequential boundary questions. Fewer residual merges alone does not establish a time saving. |
| **MP5: departures and mean time** | Finite-footprint arrivals can be timed compactly, but they are staggered. S13's simultaneous proportional-batch half-clearance calculation cannot be imported. The complete-time objective stays; a waiting terminal needs an arrival-aware departure contract. |
| **MP6: joint regime** | A restricted no-blocking analytical member is internally coherent and gives the same fastest action across hidden merge states. A delay-producing joined member and applied common-VSL regime remain unadmitted. The inspected sources do not supply the new interaction scale, homogeneous lateral reduction and terminal closure together. |

## The smallest old-to-new stack change

These are proposed consequences of the qualified member, not a frozen methods
contract. The original S13 remains unchanged.

| Component | H1 consequence and decision status |
|---|---|
| **1: population and geometry** | Keep the finite cohort, permanent three-to-two drop and initial continuing symmetry. A finite uniform footprint replaces the analytical instantaneous entrance batch in this candidate. Its physical profile must be common across actions and comparators. |
| **2–3: advice and motion** | Keep one bounded common advice. Use deterministic footprint travel on a proved free-flow branch. Retain the compact clock; change the handoff from one batch time to an arrival history. A waiting boundary cannot silently keep the no-wait clock. |
| **4–5: early completion and receiving** | Form the approved P1 replacement with state-dependent spare service and conservative lane exchange. The uniform local extension, rate analogue and fixed physical interaction scale are explicit proposed adaptations. There is no assertion of exact CTM/LTM equivalence. |
| **6: compulsory lane-end service** | Keep mandatory completion, finite receiving and the separate late-work idea. A nonblocking branch is qualified conditionally. A binding terminal's allocation, storage and upstream influence are not selected. |
| **7: complete time** | Keep time for all cohort mass until final exit. Evaluate it from actual arrivals, waiting and departures; retain no unsupported half-clearance shortcut. |
| **8–9: comparison and gradient evidence** | Keep autonomous initial-state prediction, strong scalar rivals and the distinct correctness/usefulness evidence layers. Initial symmetry gives upstream scalar sufficiency; a new reachable witness and independent usefulness evidence remain later work. |

## Original VSL-B2-G1: decide the terminal scope while retaining H1

**Problem statement.** Can the elementary task admit consequential terminal
waiting while preserving a compact homogeneous upstream description, or should
this review close with the qualified nonblocking limiting member?

**Assumed model-chain function.** The homogeneous upstream state supplies
physical lane-end arrival histories. Finite compulsory merging must turn these
into complete departures and, when necessary, explain whether holding changes
upstream motion or receiving. This connects preparation to the retained
whole-population time objective.

**Core gap.** H1's demonstrated homogeneous invariance assumes that the boundary
does not hold approaching traffic. The source R1 allocation does not supply a
lane-drop point queue with justified storage and no upstream influence. A
binding boundary therefore requires a shared service/motion contract. It cannot
be supplied as an inconsequential adapter to the proposed upstream equations.

**Candidate K1 — close on the nonblocking homogeneous member.** Restrict the
entire action and traffic range so that each terminal arrival can receive
service immediately. Use the footprint's actual arrival times; no terminal
priority matters when all demands fit. **Pros:** gives a complete elementary
analytical member, preserves homogeneity and needs no queue approximation;
provides a clean negative/limiting gradient check. **Cons:** early merging
cannot save terminal waiting, so the preferred speed carries no hidden-merge
contrast. This would narrow G1/G4's intended verification role rather than
establish the desired useful-information result. Its applied validity still
requires the speed/parameter evidence absent from this review.

**Candidate K2 — qualify a compact arrival-aware terminal boundary.** Retain
H1 as the upstream candidate and review one conservative terminal account
that receives its arrival histories, stores unserved mass and determines
departures. Its first burden is to establish a physical no-feedback domain
or state explicitly the homogeneous approximation used for holding and its
effect on upstream motion. Do not grant an unlimited buffer or zero feedback
by default. **Pros:** addresses the exact remaining preparation-to-delay
connection without automatically adding longitudinal state; preserves the
original useful-gradient goal and complete-time objective. **Cons:** this is
a consequential component-6/interface amendment, not a mere transcription.
Storage, allocation and feedback may defeat the compact restriction. A failed
qualification returns to the smallest shared contract and does not authorize
H2/B, a new task or experiments automatically.

**Provisional recommendation: K2**, if the information-dependent useful-gradient
role remains the target. Treat the upstream equations and footprint here as a
concrete candidate to be assessed with that boundary, not a fully adopted model.
K1 remains a legitimate closure if the compact terminal cannot be justified or
the user prefers a limiting verification case. This Type 2 decision is owned by
G3/VQ3-P/T/S, with G1 task-role, G2 profile fairness and G4 time/evidence
dependencies. The review stops at this choice as instructed.

## What is finished, and what is still unfinished

**Finished in this pass:** H1 has received a substantive homogeneous-state,
receiving, transfer, motion and information-sufficiency qualification, including
its explicit adaptations and the terminal compatibility limit. The upstream
state → service → completed-merge question has a concrete conditional answer.
The original B2 plan has reached its specified system-interface stopping gate.

**Unfinished:** the successor roadmap's Pass 2 has not closed the full elementary
modeling chain. MP4–MP6's binding-terminal branch prevents that closure. Pass 3
(the verification protocol) and Pass 4 (paper consolidation) have not begun.
The route decisions A, A-H and H1 are refinements inside Pass 2, not additional
completed stages. The next allowed action is disposition of the terminal scope;
this report starts no dependent review automatically.

[Persistent progress against the original roadmap](vsl_review_progress.md)

[Mathematical candidate, invariance and timing checks](../../synthesis/research_readiness/vsl_h1_homogeneous_window_contract.pdf)

[Viewed-paper reference list, adaptation audit and evidence limits](../../extraction/research_readiness/vsl_h1_source_and_adaptation_audit.md)

[Files, commands and verification record](vsl_h1_work_report.md)

## Subsequent K2 approval and execution — 2026-10-14

The user approved K2, emphasizing that a concrete compulsory-merge model is
needed to complete the revised stack and asking that the next gate name that
model explicitly. K1 was not selected. This closes the review-route choice,
not the exact terminal priority or holding interpretation.

K2's executed candidate uses one ending queue and own-lane-first residual
receiving, with conservative completion, full departures and TST. A finite
terminal reach can protect H1 under a stated storage/receiving domain; adopting
its physical handoff versus a virtual no-feedback approximation is the
remaining original-B2 choice. The pass also corrects the premise that S13
had no concrete analytical choke law and establishes that a forced queue alone
does not ensure an interior optimum. The full modeling stage remains open.

[Executed K2 model and concrete terminal-meaning gate](vsl_k2_forced_merge_findings_and_gate.md)

## T1 selected and the original modeling-chain review completed — 2026-10-14

The user subsequently selected T1's finite physical terminal section.
The joined qualification now retains H1's homogeneous occupied body upstream,
with boundary-count travel and possible nonuniform queued motion in the
terminal section. A conservative physical receiving domain prevents terminal
holding at H1's handoff. The same analytical family has genuinely receiving-
limited early transfer and positive forced waiting.

The original Pass 2 evidence review is finished, and one assembled H1/T1
contract is presented for confirmation before freeze. The earlier H1
terminal-scope choice is no longer open. No position-resolved model inside H1,
new observer, gradient protocol or traffic experiment is adopted.

[Consolidated model, direct answers and current gate](vsl_t1_joined_model_and_gate.md)
