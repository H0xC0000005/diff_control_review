# A published backbone can reduce the modeling burden, with a choice about the task

**Later decision and evidence, 2026-10-20.** The user selects the lane-information
recommendation for qualification and allows backtracking if needed. The first
native-flow check now finds a substantive receiving/allocation obstruction
in the displayed source rules. The task-information choice below is closed
in favor of lanes; the new question concerns the flow-realization component
or backbone. No exact source repair or complete replacement is admitted.

[Current lane-backbone qualification and LF1 choice](vsl_lane_backbone_qualification.md)

The bounded-comparison findings below retain their delivery-time scope.

Date: 2026-10-20. **Approved short assessment executed; recommendation
delivered. No replacement model selected or constructed.**

The comparison supports a simpler starting point. We do not need our own
preparation, point-service and recovery mechanisms merely to create a
meaningful VSL problem: published models already contain traffic congestion,
capacity drop and a reason to regulate approaching flow. What is not yet
established is a source-faithful replacement that preserves every detail of
our present task and its analytical results.

**For the current lane-information question, the strongest starting point
among the two lane models checked in detail is Nagalur Subraveti et al.'s
multilane model.** A concrete small addition to examine is Han et al.'s VSL
sending-flow restriction. **For the smallest elementary VSL task regardless
of which information is hidden, Jin–Jin is simpler:** one paper already
provides both a spatial traffic model and its link-average approximation.
Choosing between these changes the research setting, so neither is adopted
here. [1]–[3]

## What the sources let us keep

“Backbone” means the traffic state and most evolution laws come from the
chosen work. The information comparison and gradient study are built around
those laws. It does not mean citing one source while retaining our present
collection of new service rules.

| Candidate | Retained published backbone | Necessary changes or additions | Research questions supported; remaining burden |
|---|---|---|---|
| **Jin–Jin [1]** | Aggregate spatial LWR traffic; link-queue approximation; VSL-regulated entry; threshold capacity drop; upstream point queue; I/PI control references. | Observation/scenario and optimizer comparisons. Use the source's queue in complete population-time accounting. No extra merging law is needed. | Compact control/gradient task. A spatial-information question is possible, but the source has no A/B lane distinction. Its discontinuous discharge requires an explicit sensitivity contract. |
| **Nagalur Subraveti et al. [2], with a VSL component from Han et al. [3]** | Lane densities in successive road cells; native lateral incentives, receiving interaction, longitudinal propagation and capacity drop. | Proposed addition: advice caps sending demand. Keep physical cells fixed. Specify its interaction with lateral demand and the existing capacity-drop branch. The native lane-drop case is four-to-three; three-to-two is an explicit geometry adaptation. | Preserves the substantive lane-loading question. Source branch/zero-state conventions, transfer budgets, lane-end clearance and the VSL interface still need qualification. This is a concrete candidate direction, not a complete admitted two-paper model. |
| **Wei–Han–Wang [4]** | Aggregate link propagation retaining entry/speed history, coexistence of speed cohorts and bottleneck capacity drop. | Comparison design around the native sign-at-entry action; clarify source transcription and the derivative of its time-step eligibility tests. | A credible history-aware aggregate reference or cohort-information task. It has no explicit A/B lane state; it is not a ready differentiable version of our current task. |
| **Carey et al. [5]** | Multilane cell transmission, desired exit lanes, mandatory transfer and receiving-allocation alternatives. | VSL action map and a qualified permanent lane-end/finite-population boundary. | Useful simpler receiving/mandatory-transfer lineage. Compared with [2], more of the complete lane-drop task must be supplied here. Detailed methods evidence is inherited from the earlier audit, not newly reread in full. |

Sources and exact reading scope are listed in the
[source record](../../extraction/research_readiness/vsl_published_backbone_sources.md).
This is a bounded comparison, not a claim that these are the best models
in the entire literature.

## Why the lane model is a plausible simplification

Consider two cases with the same ending-lane traffic E and the same total
continuing traffic. In one case, much of the continuing traffic is in the
adjacent lane A; in the other, more is in a farther lane B. The scientific
question is whether this concealed difference changes merging opportunities,
then the useful speed decision and its sensitivity.

A published lane model gives us a way to ask that question without inventing
a new point-service mechanism. The smallest proposed addition has a clear
interface: use Han et al.'s advice-dependent sending restriction where the
lane model calculates how much traffic can move. Retain the native lane
interaction and capacity-drop laws; do not import a second capacity-drop
model or our recovery meter. How the changed sending demand feeds the native
lateral-demand calculation must be explicit, rather than an implementation
convention. This compatibility claim is our proposed adaptation, not a
published validation of the combination. [2], [3]

**This simplifies the traffic assumptions we author while retaining the
published model's spatial state.** Its price is accepting spatial cells and the
source's lane redistribution, including continuing traffic changing lanes.
Consequently, an initial A/B imbalance can evolve differently from our
present model. None of the existing information/action certificates transfers
automatically. Removing those native behaviors just to recover our earlier
proof would undermine the point of whole-model reuse.

This route is therefore feasible as a focused qualification target. It is
not yet defensible to tell colleagues that “[2] plus [3] is our completed,
validated benchmark.” The unresolved source and coupling checks in the table
are substantive. If resolving them requires new traffic laws rather than
faithful clarification, the assumed simplicity advantage must be reassessed.

## Why Jin–Jin is simpler, and what it changes

Its control idea is to hold approaching flow back enough to avoid activating
the bottleneck's lower-discharge mode. The paper already models upstream
holding as a point queue and compares cumulative arrivals and departures;
we need not add a new merge-interaction law to obtain congestion costs.
VSL regulates entry to the modeled road, rather than instantly changing
every vehicle's speed throughout our present preparation zone. [1]

Our proposed information question would also change. Two road states can
contain the same total traffic while placing it differently: one has traffic
concentrated near the downstream choke, another farther upstream. The native
spatial model can distinguish them; a single link-average state cannot.
Whether admissible histories reveal that distinction, and whether it changes
a useful action, remain questions to establish rather than assumed benefits.

For a fair information test, use **the same spatial forward model** with
different admitted observations. Comparing the native link-queue simulator
against LWR changes dynamics as well as information; that is a separate
model/gradient-fidelity comparison. The source's own successful I/PI control
also makes it a demanding baseline, rather than evidence that a new optimizer
is needed. This is the clearest single-source route if a spatial-information
question is acceptable. It does not answer the concealed A/B question.

## What the CS comparison still has to earn

For either route, first ask whether omitted information changes service or
future traffic under the **same** physical model, then whether it matters to
control. Give the aggregate peer the histories it is allowed to observe;
do not assume concealment is absolute. In a lane comparison, match spatial
sampling so that giving per-lane observations does not also give extra road
locations. Test a compact additional statistic before attributing an advantage
to all lane details.

Separate this from optimizer value: compare gradient-based decisions with
equal-information search or other appropriate derivative-free control. For
one constant speed, bounded scalar search is a particularly strong check;
for richer action schedules it is not a complete optimizer reference. Keep
no-control and source feedback controls where applicable. Count all released
traffic, including upstream holding, through a declared common objective and
clearance convention. A reported advantage is an outcome, not a selection
requirement.

None of the inspected papers supplies our complete gradient claim. Jin's
discharge switch can change event timing; Wei's binary travel-distance tests
can hide timing sensitivity from ordinary differentiation of a fixed rollout.
These are different issues. Neither is resolved by observing a finite AD
gradient. The lane route likewise needs regular-branch and event-boundary
qualification. No smoothing, source repair, numerical gradient agreement,
useful-gradient result or physical validation is established by this review.

## Recommendation and the choice exposed

**Provisional recommendation: preserve the lane-information question first,
and use [2] with the single sending-control component from [3] as the next
qualification target.** This addresses the colleague's concern without
abandoning the reason the A/B distinction was introduced. **Pros:** it
retains that question with fewer study-defined traffic mechanisms.
**Cons:** it brings native spatial/lane-changing machinery and an unclosed
source/interface audit. It is a direction with a specified component to
check, not a finished replacement formula set.

**If minimizing the elementary benchmark takes precedence over keeping
the lane-information mechanism, prefer [1].** **Pros:** a compact
single-source VSL setting with existing controls and population accounting.
**Cons:** it changes both the information contrast and the actuation
meaning; its switched sensitivity still needs work.

The immediate choice between these leading routes is whether to retain
**which lane holds traffic** as the information question, accepting a
published spatial lane model, or use
**where along the road traffic is located** to obtain the simpler task.
This is a consequential task/model choice. The approved bounded comparison
ends here without selecting it. The current accepted model/report remains
intact; VSL Step 4 remains closed and the separate historical Step 3 acceptance
entry is unchanged. No urban revision, code or experiment is opened.

[References, source locations and access limits](../../extraction/research_readiness/vsl_published_backbone_sources.md)

[Work record and preservation checks](vsl_published_backbone_work_report.md)
