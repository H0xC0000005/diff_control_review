# Feedback 16: how the peer-backed task differs from the earlier task

2026-10-23. **Clarification of the established models; no model change.**
The comparison uses the final task-first formulation, including its
asymmetric initialization, forced-merge service and recent-discharge
recovery account. It does not compare the new task with an earlier,
incomplete S13 draft.

[Earlier task-first formulation](../../synthesis/research_readiness/vsl_compact_methods_report.pdf)

[Current colleague-facing report](../../synthesis/research_readiness/vsl_literature_backbone_review_report.pdf)

[Complete current model definition](../../synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.pdf)

Your comparison is broadly sound. The largest correction concerns point 5:
**lane-change desire determines requests, not receiving priority, and the
objective counts delay rather than imposing an extra merge penalty.**
Point 4 also conceals a substantive change in how advice affects capacity.

The overall change is from a homogeneous approach plus a specially
constructed point-merge and recovery mechanism to a lane-cell traffic
model whose incentives, shared receiving and congestion dynamics generate
the merge interaction. The research question is retained; several physical
mechanisms are deliberately different.

## Direct answers to the six points

**1. State-dependent lane-change desire replaces the distance-based
preparation law — broadly correct, with two qualifications.**

In the old model, a fixed interaction length governs the E-to-A offer;
when that offer limits flow, E density decays exponentially with distance
traveled. Adjacent receiving headroom can still restrict realized merging,
so the old model did not guarantee an unconditional fixed realized fraction
per distance in every state.

The new model compares the origin and destination lanes' perceived
densities, including downstream lookahead, and modifies that comparison
with a movement-specific incentive multiplier. The result is a desired
proportion of the origin's sending amount. Normalization and receiving
allocation then determine the actual transfer. It is more precise to call
this a normalized, incentive-weighted density contrast than a difference
between independently normalized lane preferences. Distance still matters:
the E-to-A route incentive increases as the lane end approaches. What
disappears is the old fixed-distance preparation law.

**2. A lane-resolved CTM replaces the LTM-style boundary formulation —
correct at the broad level; the important change is spatial state.**

The old approach body was homogeneous along the road. Its terminal used
cumulative arrivals, a travel-time shift and point discharge/waiting,
following LTM-style boundary logic. It was not a full field of lane densities
at successive road positions.

The new task stores a density in every lane of every 100 m road section,
and updates the whole road in six-second steps. Congestion and receiving
restrictions can therefore develop at successive positions. Both models
use continuous traffic mass and remain macroscopic; “CTM” does not mean
microscopic vehicle tracking. “Coarse” describes the chosen grid, rather
than the essential difference between the two approaches.

**3. Additional lateral directions are now permitted — correct, subject
to geometry and traffic state.**

The old task allowed only E-to-A exchange in preparation, followed by
forced E-to-A service at the choke; B had independent service. The new
interior geometry allows adjacent E-to-A, A-to-E, A-to-B and B-to-A
movements. There is no direct E-to-B connection. A permitted movement can
still have zero desire or zero realized service.

At the final boundary, there is no downstream E lane: E can only request
the A outlet, while A/B may use their own or the other continuing outlet.
Thus A-to-E is permitted before the end, not into a nonexistent lane beyond
it. Route urgency encourages leaving E but is not a blanket prohibition
on entering E upstream.

**4. Both have a triangular-FD foundation — correct, but their advice and
congestion laws are different.**

In the old task, advice sets the effective free speed and thereby changes
the selected critical density and capacity. Its undisturbed point-service
ceiling is separately fixed; special merge-work and recovery rules then
determine the point-service restriction.

In the new task, the nominal free speed, critical density and reference
capacity are fixed. Advice directly caps sending. The Han-based
density-dependent discharge ceiling and receiving constraints add
congestion/capacity-drop behavior to that nominal triangular foundation.
Receiving changes as traffic densities evolve; it is not directly
reparameterized by advice. The two stacks therefore do not share an
identical capacity law merely because both use triangular-FD ingredients.

**5. Forced-merge service changes — correct; preference-controlled
priority and a TST merge penalty are the critical misunderstandings.**

The old point model gave a fitting free A flow priority and shared work
when both streams queued. E could consume more work per unit mass,
depending on the speed difference, and earlier E discharge could reduce
the remaining shared budget through recovery.

The new allocator instead uses fixed equal reference priorities. A strong
lane-change incentive can increase a request upstream, but it cannot
increase that request's priority at a scarce receiver. At the lane end,
E's entire sending offer is assigned to A regardless of its preference
value: E must merge or wait. If E and A are the only competitors and both
request enough, they share the available A receiving budget equally.
Smaller requests, other competing requests and state-dependent receiving
change the realized fractions; equal priority is not a constant realized
merge fraction.

There is no separate E maneuver-work multiplier in this allocator. E can
still cause delay by consuming A service, making A or E wait and causing
density accumulation that restricts later traffic. **Those are effects of
the traffic equations. TST records the resulting unfinished traffic's
time; it does not manufacture an extra E-merging time loss.** The same
accounting distinction applies to the old model: its delays came from its
work/recovery dynamics before they were counted by TST.

**6. The explicit discharged-E recovery effect is removed — correct;
all influence of traffic history is not removed.**

The old model retained the age and insertion speed of recent forced E
discharge. Traffic could complete its own trip yet continue restricting
following service as its downstream acceleration effect faded.

The new task has no such post-exit recovery account or downstream recovery
zone. Once mass leaves the modeled road, it generates no additional
post-exit restriction. Within the road, however, previous movements have
changed the current lane-cell densities, and those densities determine
later service, capacity drop and congestion propagation. Two identical
full lane-cell states under the same advice produce the same next update
without consulting earlier discharge ages. Recovery as density decreases
is distinct from the removed insertion-speed history mechanism.

## Three additions complete the big picture

**The operating domain is less restricted spatially.** The old sufficient
domain kept preparation free, terminal storage available and B unqueued.
The current member admits nonuniform initial lane-cell densities, including
congested cells; receiving/storage feedback can accumulate traffic in any
lane and extend congestion upstream. Neither model tracks individual
microscopic maneuvers. The new geometry, initialization and traffic dynamics
are not a functionally identical transcription of the earlier task.

**The objective and sensitivity remain complete, but their construction
changes.** Both tasks initialize a fixed cohort independently of one common
constant advice, allow no later inflow, complete trips at the lane-drop
exit, and count every unit's time until completion. The old model uses
continuous-time arrival/service events, with event-time sensitivity where
needed. The new model differentiates a fixed-step stock update and adds
an exact remaining-time value after a suitable cutoff. Its derivative is
a discrete branch-trace chain rule, not the old continuous-time saltation
formula. The residual value counts future time; it is not a new physical
delay mechanism.

**The information/control question survives; its evidence must be
qualified for the new model.** Both compare E plus combined A/B information
against separate lanes and include simpler information/optimizer rivals.
The new central reduced observer retains E and A+B at each road section,
so its disadvantage is the hidden lane split, not fewer observed road
positions. One initial A mass reconstructed the old homogeneous state;
one final-A density identifies only the current two-state diagnostic pair,
not arbitrary lane-density fields. Different service has been established
analytically for that pair, but a positive optimal-advice gap, an interior
optimum, useful numerical gradients and physical fidelity do not follow
automatically or inherit the old model's certificates.

## Record, checks and scope

Read feedback 16, both complete formulations, the current report, its
source/assumption record and the analytical findings. The six numbered
answers above preserve the user's questions together with their responses.
No follow-up choice is required to describe the already selected models.

Save this response, append a summary to the successor dialogue and link it
from the package introduction. Keep both PDF/LaTeX reports, all equations,
source contracts, feedback and prior results unchanged. Inspect with `rg`
and `sed`, edit with `apply_patch`, and use Python only for file hashes and
local-link checks against `/tmp/vsl_feedback16_comparison/before.json`.
The reproducible document-only verification command is:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_feedback16_comparison/document_checks.py
git status --short
```

No numerical trajectory, finite difference, optimization, simulator code,
dependency installation or new literature/model review is performed. The
public report remains finalized; the existing analytical and numerical
evidence limits remain unchanged. The next allowed action is further
conceptual discussion, without opening another methodological stage.

Document checks pass: all six points are answered, 169 checked local links
resolve, and 606 other snapshotted files are unchanged. Both reports and
the complete current model specification are byte-preserved in PDF and
LaTeX. Only the package introduction and successor dialogue change, with
this response added. Detailed check output is retained at
`/tmp/vsl_feedback16_comparison/validation.json`.

**Module-ownership follow-up, 2026-10-23.** The user additionally asks
which modules Subraveti plus Han and Carey define separately. The answer
distinguishes lane state/incentives and sending/receiving limits from
movement realization, while making clear that the source papers overlap.
The Carey-led adaptation applies throughout the road, not only at the
forced-merge boundary. The exact three-lane allocation, donor normalization
and permanent E-end closure remain our adaptations. No report or model
is changed.

[Explicit module roles and traffic example](vsl_literature_backbone_peer_work_overview.md#the-module-boundary-desire-and-available-service-versus-realized-movement)

**Native-rule follow-up, 2026-10-23.** The user asks what allocation
Subraveti itself used and why replace it. Add the lateral-first,
adjusted-forward calculation and exact article locations to the source-first
overview. Explain the previously established negative-receiving and
joint-donor counterexamples, the motivation for the selected conservative
Carey-led completion, and the limits of this judgment. No claim about an
uninspected author implementation or empirical superiority is made; Carey
is not asserted to be the only possible remedy. The public report stays
unchanged.

[Native allocation and the replacement rationale](vsl_literature_backbone_peer_work_overview.md#what-subraveti-originally-does-and-why-replace-that-component)

**Carey intention/realization follow-up, 2026-10-23.** The user asks how
Carey's rules determine lateral directions and proportions. Distinguish
the original study's predefined exit-lane target, alternative
location-dependent intentions and receiving-priority rules. In the current
task, geometry and Subraveti still supply directions/desires; the
Carey-led adaptation realizes requests with fixed equal receiving
priorities, shared limits and forward continuation. No original Carey
intention/cohort or extra headway model is newly adopted.

[Carey's direction, intended fraction and realized share](vsl_literature_backbone_peer_work_overview.md#how-carey-determines-lateral-direction-and-proportions)
