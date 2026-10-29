# Can a compact model remember enough about merging disturbances?

Date: 2026-10-07. T1's bounded review reached a partial result. The user now
approves M1 (option A): investigate grouped restriction positions and speeds.
The [dependent qualification is opened](../../../rm12_64_bp_r_stage3_grouped_recovery_continuation.md).
No concrete grouping or service law is adopted; the traffic task is unchanged.

That bounded pass is now performed. Read the
[current grouping findings and decision](grouped_recovery_findings_and_gate.md)
for its result and Q-G. The material below preserves the memory findings that
motivated the approved state expansion.

Subsequently Q-G is closed as G1: exact retention first, with cost/compression
excluded as criteria. The performed pass reaches
[Q-E, the current exact-state insertion/reset proposal](exact_information_findings_and_gate.md).
Q-E is subsequently closed as E1; the
[sampled-insertion findings](sampled_insertion_findings.md) record its bounded
qualification. Full joined feedback remains partial; E2 is unselected and no
approximate reduction is adopted. The earlier requirement to
complete a reduced competitor concurrently is deferred for this exact-first pass.

**Remembering when a disturbance is created has a compact, supported solution.
Remembering when it stops limiting traffic is still the missing part.** We have
not established that individual vehicle identity is needed, or that a useful
compact model is impossible.

## Why we are examining competitor models

The main question is **how much information a model must retain to predict
the effect of ramp-metering changes on total system time**. Qualifying a compact
competitor is a prerequisite to answering it: we must know what the model
remembers and how it predicts from its own state before attributing a difference
to omitted traffic information. This is a bounded comparison of justified model
families, not a requirement to settle every possible competitor.

Here, “hidden” needs care. In the earlier review it meant traffic information
that remained unresolved after all admitted aggregate observations and their
history. Since the approved BP-R backtracking, the active question concerns
information **not retained by a particular model**. The starting condition may
be known to everyone; compressing it can still lose its future consequences.
The [review-tree explanation](../bp_r/semantic_position_in_review_tree.md)
records this approved change of claim.

For example, everyone might know that a slow group has just merged. A compact
model might retain only its contribution to density, or also remember its entry
time, speed and location. We ask which description can preserve the response to
the same metering changes. If a small summary suffices, that is a useful result
favoring the summary. If a qualified reduction still loses a control-relevant
response, that can support retaining more information relative to that model,
provided other law differences are controlled. Neither outcome by itself proves
that information is unknowable or that all aggregate models fail.

The current pass has reached the representation choice before that complete
comparison. Creation bookkeeping and limited motion results are established;
complete system-time responses and useful gradients are not. The next choice
sets what recovery information the compact rival may retain; it does not finish
the research question or adopt every competitor.

## What this step was trying to do

A slow entrant can restrict traffic while it accelerates. The previous mean
model estimated that effect from the current insertion conditions, so it could
apply a penalty too early or recover too early. You selected the route that
first gives the compact model a stronger memory, then asks whether more detail
is still useful. The aim is to understand what information matters for control,
with a fair compact competitor.

Your description of the two routes as framework-oriented versus following one
approximation more deeply captures their emphasis. Both are legitimate; it is
the kind of conclusion they support that differs.

## What a closed recovery model means, and why it is needed

“Recovery” means the evolution of a merging disturbance: how the slow entrant
accelerates and moves, how surrounding traffic affects that motion, and whether
it still imposes an extra restriction on traffic service. It does not mean that
the whole road has become uncongested. A disturbance can stop imposing an extra
restriction even while traffic remains slow.

“Closed” means the model has enough retained state and specified rules to
predict the next state and its traffic effect from its own state and permitted
inputs. It cannot need the detailed reference's future position, speed or
restriction status to complete each prediction. This is not a closed-loop
controller, a requirement for an exact analytical formula, or a statement that
the review has closed. A specified approximation can also be closed; its
accuracy and the current source-matching requirements still need qualification.

Consider pausing ramp admission after a slow group has merged. No further
entries does not imply that the old group's restriction has disappeared. In
another situation the group has already ceased to restrict traffic. The current
entry rate is zero in both, so that signal alone cannot distinguish their future
service. Counting births also does not settle this difference. This illustrates
why recovery matters, not a newly proved matched-aggregate control witness.

The current task compares complete traffic responses to common metering
changes. It therefore needs a competitor that can evolve the effect of earlier
merges throughout the prediction, then connect that effect to exits and total
system time. Otherwise we have only a fragment of a model, or a model receiving
the reference's answers. A discrepancy would then not isolate the consequences
of its retained information.

That requirement does not prescribe a separate recovery variable or individual
vehicles. Suitable traffic fields, grouped state or memory might supply it.
At this review stage the obligation is to identify and justify such a state,
update and service rule, not implement it or invent a universally exact model.
Whether a compact rule can satisfy the current task remains open; finding that
it can is a favorable result.

## What now has support

The reference creates a moving restriction when enough actual traffic has
transferred, using its declared update times. A compact model can keep the
progress towards that event using its own actual transfers. This is like
remembering how far a counter has advanced towards its next marker. It does
not round physical traffic mass or require a future answer from the reference.

That progress must be kept for each kind and location of transfer that can
create a restriction, including mainline lane changes. A single ramp counter
would miss those other sources. The calculation qualifies event counting;
we have not turned it into a complete capacity formula.

There is also a useful restricted recovery result. If traffic ahead stays free
and the birth conditions are known, the source motion rule determines how an
entrant accelerates and where it moves. Records of when groups entered and
their entry speeds can reconstruct those paths without personal identities.
This is a checked special case of the current physics, not a newly adopted
simplification of the whole task.

## Why that does not finish recovery

Imagine two slow entrants that merged at the same time. One has a clear road
ahead and accelerates. The other encounters slow traffic and is held back.
Knowing only their time since entry would give both the same recovery clock,
although their motion is different. The source actually accounts for traffic
ahead; an unsupported timeout would remove that interaction.

Even the number of restrictions and their average speed are not generally
enough to update the speed average. When traffic ahead imposes a speed limit,
only the faster part of a group is slowed by that limit. Two groups with the
same average can contain different faster parts. The analytical check proves
this limited update problem; it does not prove a full traffic or control failure.

There is a second distinction: a restriction can still be present while adding
no slowdown because traffic around it is already slow. Counting restrictions
does not tell us which ones are currently limiting service. Removing a record
at that instant also needs justification if it could matter again later.

The remaining challenge is therefore to connect compact recovery information
to **where and when traffic can actually be served**, using the same physical
mechanism. We have not found a complete supported rule for that connection in
the bounded set of methods inspected. That is an evidence limit, not a finding
that all aggregate models fail. Existing aggregate acceleration models and
mean-capacity successes remain serious comparison candidates.

## A concrete direction survives

We can describe the restrictions by where they are and how fast they are moving,
without giving each one a personal name. At full detail, that preserves their
configuration; it does not yet make the model compact.

The next possibility is to group that information: for example, a record saying
that restrictions in a part of a lane occupy a certain range of speeds. The
research question becomes whether those groups preserve the relevant service
response while retaining less detail. The ordinary traffic mass is still
counted separately and only once. These group records describe restrictions,
not additional traffic population.

This is a proposed family to qualify. Choosing an average representative for a
group or adding separate penalties from each group could change the mechanism.
Neither rule has been approved or justified by this pass. Keeping every original
record and calling it a distribution would also fail to demonstrate compression.

## What the result means for the main review

| Question | Current answer |
|---|---|
| Can disturbance creation be remembered compactly? | Yes, its source counting rule can be preserved from own actual transfers. |
| Can a simple recovery clock finish the full task? | Not under the current evidence; traffic interactions must be handled. |
| Is there a way to proceed without personal identities? | Yes as a source-preserving description; a genuinely reduced grouping rule is still unqualified. |
| Have we shown additional detail changes useful metering decisions? | No. Complete exit timing and total system time still need to be connected to the reduced law. |
| Have we established useful gradients? | No. That remains a separate later review. |

## Approved direction: investigate grouped spatial recovery information

The inventory below records the choice presented to the user. **M1 is now
approved; M2 and M3 are unselected.** This authorizes qualification of the state
family, not its concrete projection, update or service rule.

**Problem statement.** Should the compact competitor be allowed to retain
grouped information about restriction positions and speeds, or should the next
attempt remain limited to a few summary numbers in a narrower supported regime?

**Function in the traffic chain.** The meter controls admission to the ramp
approach. Actual transfers create restrictions; their motion affects service,
exit timing and total time spent by all traffic. The disputed representation
sits between creation and service. It is not a new meter, lane layout or source
of traffic mass.

**Core gap.** We have qualified creation and conditional motion, but no compact
update/service law for general recovery. An unlabelled full configuration supplies
a defensible endpoint. The amount of that configuration we permit the rival to
retain changes what we will be testing. T1 approval authorized the qualification;
it did not adopt a distribution model or its grouping law.

### M1 — investigate grouped spatial recovery information

Keep the current task and source interaction physics. Extend A's candidate
memory from a few totals to a lane-wise description of where restrictions are
and their speeds. Start from the exact unlabelled configuration as an equivalence
check, then qualify a smaller grouping projection, its independent update and
its service rule. Preserve source births, public initialization and the current
requirement to remove any extra penalty when restrictions do not bind.

**Pros:** follows the mechanism actually causing the current gap; avoids removing
traffic interactions just to make a clock work; gives a concrete family of
retained-information comparisons. A sufficiently coarse group description would
be a favorable compact-sufficiency result.

**Cons:** extends the proposed state representation. A distribution with one
record per restriction is still detailed, and coarse groups may introduce new
activation/service errors. No passing grouping law is guaranteed or currently
adopted. State size and update complexity must be stated as part of this change,
without imposing an arbitrary quantitative cost target.

**Dependency/consequence:** approves qualification of this state family, not
bin sizes, an average-trajectory rule, new physics or an experiment. A concrete
compact law still returns for adoption when it is reviewable.

### M2 — qualify a few summaries only within a supported simpler regime

Keep a small set of event/birth/recovery summaries and first determine whether
a source-supported regime makes them sufficient, such as the conditional
free-motion setting. Declare and justify the restrictions on initial conditions,
traffic interactions and rate choices. The current full-task qualification stays
partial; the simpler domain cannot silently replace it.

**Pros:** keeps the compact representation small and allows exact deductions
where the source motion is tractable. It could produce a useful limited result
without a distribution model.

**Cons:** adds task-domain restrictions, and their persistence under metering is
unproved. It risks excluding the recovery interactions motivating the task.
Free-motion reconstruction alone still does not supply a service law, useful
rate tradeoff or full-system-time result.

**Dependency/consequence:** any narrowed main task needs explicit approval and
a renewed control-relevance check. Do not engineer a scenario solely so that
the chosen summary passes.

### M3 — accept this partial result and park compact-law qualification

Record exact event accounting and conditional kinetic support, while leaving
the full compact recovery/service law unresolved. Make no complete task or
gradient claim. A later review may reopen this specific gap.

**Pros:** provides an honest stopping point without adding an unqualified model
or narrowing the traffic setting for a favorable answer.

**Cons:** leaves the current line short of a complete research-ready comparison;
it does not answer how much recovery information is sufficient.

**Dependency/consequence:** closes only this bounded attempt if selected.
Final Stage 3 disposition remains a separate user decision; Stage 4 does not open.

**Provisional recommendation: M1.** The evidence points to the location and
motion of restrictions. Investigating a grouped description keeps that cause
in the current task and asks directly how much of it must be retained. This is
a choice about the next model family, not an already successful compact law.

## Optional evidence and formal status

The [source audit](../../../extraction/rm12/bp_r_stage3/event_memory_source_audit.md)
and [technical assessment](../../../synthesis/rm12/bp_r_stage3/event_memory_qualification.md)
contain the precise boundaries. The [four-page analytical companion](../../../synthesis/rm12/bp_r_stage3/event_memory_math.pdf)
retains the equations; reading it is not required to understand this finding.

S3-G2-Q-T is closed as T1. The bounded S3-I3.Q-P.A-T pass is completed.
**S3-G2-Q-M is closed as M1, Type 2/user.** Grouped-state qualification
S3-I3.Q-P.A-M is performed to Q-G, the concrete grouping/approximation choice.
No G option is adopted. Concrete compact-law adoption and final formulation
closure remain pending. Stage 3 is open; Stage 4 and experiments
remain unopened. B keeps its previously qualified companion role. No reference,
actuator, priority, geometry, objective or predecessor closure changes here.
