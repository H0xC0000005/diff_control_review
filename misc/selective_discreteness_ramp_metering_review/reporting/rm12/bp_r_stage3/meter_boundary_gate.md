# BP-R Stage 3 — S3-G2-M: where does the rate permission act?

Date: 2026-10-06. **Closed: S3-G2-M.A approved; continuation authorized.**
S3-G2.A, the continuum–particle reference qualification route, is approved.
Stage 3 remains incomplete; Stage 4 is unopened.

## User decision

The user selects A because upstream admission followed by ramp travel is the
natural first formulation. Record approval of **S3-G2-M.A**, separately from the
already approved S3-G2.A reference route. B remains unselected; its validity as
an aggregate ramp-metering abstraction is not refuted. Continue the bounded
source/static review through the dependent boundary/entry and comparison work,
stopping at the next methodological choice or Stage 3 completion. This approval
does not select a launch law, allocation amendment or numerical experiment.
The candidates and provisional reasoning below preserve the discussion basis.

## The semantic decision

**Does the meter hold traffic before it enters the ramp approach, or hold it at
the approach's exit into the freeway in the reference model?** These are
actuator-boundary abstractions, not two verified physical signal layouts. B can
represent an effective ramp-entry permission without placing a real stop line
at the exact merge. Both use the already approved open-loop
rate schedule. They can produce different ramp congestion and entering speeds,
which matter to the selected disturbance family. This is not another vote on
hybrid terminology, a demand for a continuous closure or a release-timing actuator.

**Classification/owner:** Type 2/user, a child actuator-abstraction decision within
S3-G2. Depends on the approved reference route and inherited G1. Dependent local
work S3-E2.M transcribes the selected boundary/sending/receiving/queue interface;
S3-E1.C qualifies the source's coupled motion/allocation. Final E3/E4 follow
those bindings. No baseline may change this placement independently.

## Problem statement

Choose where the common rate cap acts in the model before binding rate-to-entry
and entry-speed behavior. A permission is an upper bound; actual transfer also
needs available traffic and downstream receiving. The choice does not grant
additional control variables, private sensing or optimized event phase.

## Assumed model-chain function

Common offered ramp traffic encounters the selected cap and any storage limit.
Admitted traffic travels through the ramp approach; its terminal state determines
available merging demand and, under qualified source motion, entrant speed.
Actual entry competes for finite freeway receiving and generates disturbances.
Their trajectories affect subsequent flow and exits. TST includes traffic held
outside the entrance, on the ramp and on the mainline, through clearance.

## Core gap and evidence

The source models the ramp as a KW stream with point transfer, changes supplied
ramp demand and shows distinct queued/unqueued regimes. It does not provide a
complete rule locating our rate permission relative to that stream. The prior
open-loop decision selects rate control, not its boundary abstraction. Classic ACTM
explicitly caps actual ramp entry, but has a different traffic/node law; importing
it would not automatically preserve the source reference.

For example, suppose traffic has already passed the ramp entrance when the rate
is reduced. An entrance cap does not directly restrict that traffic's later
merge entry; a merge cap can restrict it when it arrives. Congestion can further
affect both, but their causal paths differ. Neither the reference choice nor equal rate values make
these two control maps interchangeable. This does not by itself establish two
different real-world signal locations.

See [post-approval evidence and access limits](../../../extraction/rm12/bp_r_stage3/reference_qualification_after_A.md),
particularly RM8-P01 Sections 2–4 and RM0001 Section 2. This is a source-backed
transfer gap plus an explicit reviewer inference from finite propagation.

## Clarification: is B still ramp metering?

**Yes, as an effective ramp-entry rate constraint.** RM0001 Section 2, equations
8–13, explicitly bounds actual onramp-to-mainline flow by ramp demand, available
mainline space and a metering rate, and conserves unserved traffic in an onramp
inventory. This is established macro ramp-metering accounting. It supports the
category of B, not the exact spatial KW/continuum–particle adapter or its speed law.

Physical design guidance distinguishes a meter stop line from the later merge:
[FHWA Handbook Section 10.4.1](https://ops.fhwa.dot.gov/publications/ramp_mgmt_handbook/manual/manual/10_1.htm)
balances upstream queue storage with downstream acceleration distance;
[Caltrans Sections 1.6–1.7](https://dot.ca.gov/-/media/dot-media/programs/traffic-operations/documents/ramp-metering/rmdm-a11y.pdf)
explicitly separate upstream waiting from downstream acceleration and merging.
Thus describing this gate simply as choosing the meter's physical placement was
too literal. It is corrected here; no selection is inferred from the correction.

In B, treating the boundary permission as a physical meter command without a
post-meter travel process collapses that part of the actuator path. A rate change
need not immediately affect vehicles already released by a real upstream signal.
A stopped queue at that signal also does not imply zero entrant speed: released
traffic can accelerate before reaching the freeway. Whether such collapsing is
adequate depends on the question and time scale; physical proximity alone is not
a qualification. It especially needs evidence when entrant speed and acceleration
generate the very disturbance under review. A KW approach in A likewise does not
automatically supply a qualified stopped-vehicle launch/acceleration law.

B stays within ramp metering if the control grants a rate permission to the ramp
stream, actual entry still respects demand/receiving, and unserved mass remains
counted. Directly controlling total merge capacity, mainline/ramp priority or
individual gap-targeted merge decisions would change the actuator/task. Those
actions are not authorized by B. Its command-to-entry timing and donor-speed
mapping remain qualification obligations, not new assumed physical laws.

## S3-G2-M.A — regulate admission to the ramp approach

Place the rate cap at the upstream boundary of a finite-storage KW ramp approach.
External offered demand is fixed across controls; any traffic not admitted
remains in a counted pre-meter waiting inventory. Admission requires available
traffic, permission and approach receiving. The approach then evolves with the
qualified KW/constraint law and sends traffic to the point merge. Freeway
receiving and the source allocation determine actual entry; it is not set equal
to the upstream permission.

Use ramp terminal traffic conditions to initialize merge disturbances under the
qualified source rule. The permission itself supplies no independent speed,
stopping penalty, signal pulse or release phase. In a lightly loaded approach,
releasing less traffic need not make every entrant slow. If the merge causes a
queue that reaches the entrance, approach receiving can further limit admission.

**Pros:** closest to interpreting the source's varied ramp inputs as the output
of an upstream rate regulator while preserving its internal queued/unqueued ramp
mechanism. Keeps permission, travel and entry separate. Avoids introducing a
new launch-speed law or making metering automatically synonymous with slow entry.
Continuous-mass waiting and finite storage are straightforward to account for.

**Cons:** requires a declared finite approach and its travel/storage interface;
the exact source geometry has not been visually verified. An upstream cap is an
explicit control adaptation, not a uniquely identified source meter location.
It delays the direct influence of a rate change, and may leave important actual
stop-line/startup effects outside this initial task. It gives no guaranteed
control benefit or need for particle detail.

**Dependencies/consequence:** qualify approach geometry/boundaries, source node/
CM coupling and the terminal speed definition. Use this same admission/entry
mapping in all reductions. Exact lengths, grid and rates remain later task
settings; assigning them cannot silently change this physical placement. No
real-site reconstruction or extra acceleration lane is selected.

## S3-G2-M.B — effective ramp-entry cap at the point-merge boundary

Let offered ramp traffic enter the same finite-storage KW approach subject to
its receiving; overflow waits upstream and remains counted. Apply the common
effective rate permission at the approach's exit into the freeway. This locates
the model's constraint, not a verified real signal stop line. Available terminal
traffic, the cap and joint freeway receiving/allocation constrain actual entry
in one coherent node calculation. The cap cannot reserve unused freeway capacity
without a justified allocation rule or create extra receiving.

Holding traffic occurs within the approach until spillback requires upstream
waiting. Initialize each admitted disturbance from the qualified terminal donor
state. Retaining this spatial donor state is part of the proposed adapter; the
ACTM's lumped waiting inventory does not qualify its entrant-speed interpretation.
This is an averaged service-cap model; it does not automatically model a
red/green pulse, an individually stopped vehicle's launch or gap-conditioned
release. If those effects are necessary, they require a separately supported
extension before being asserted.

**Pros:** directly regulates the entry flow that generates disturbances; aligns
with the familiar aggregate ramp-entry permission interpretation in RM0001.
Retains a physical ramp queue/terminal state rather than replacing all held
traffic by a featureless external queue. Avoids adding a separate post-meter
travel process to the actuator interface and can be a reasonable approximation
when the omitted meter-to-merge timing and acceleration do not affect the studied
response. That adequacy remains to be evidenced in this disturbance-sensitive task.

**Cons:** couples meter-induced queuing directly to the sending state used for
merge disturbances. That can change the physics of the source's ramp-input
experiment and needs explicit interpretation. The averaged cap does not justify
actual stop/start acceleration; its speed mapping must not be guessed. ACTM
precedent supports rate accounting, not transplantation of ACTM dynamics or
proof of an actual stop line at the merge. A terminal model queue must not be
identified with stopped vehicles' physical merge speed without evidence. It gives no guaranteed
control benefit or need for particle detail.

**Dependencies/consequence:** qualify the joint capped-node allocation and its
donor speed/state convention, and declare whether the schedule denotes effective
entry permission or a physical signal command. A needed command-to-entry delay
must be qualified rather than silently ignored. Share the same boundary with every reduction.
An explicit signal or launch trajectory would reopen the smallest additional
physical/actuator contract; selecting B alone does not authorize it.

## Fair comparison and provisional recommendation

| Aspect | A: approach admission | B: merge-boundary service |
|---|---|---|
| Where the meter initially holds traffic | Before the modeled approach | At its downstream end, spilling upstream if needed |
| Traffic already downstream of the upstream entrance | Evolves toward the merge under existing traffic constraints | Can be directly held at the controlled merge boundary |
| Rate-to-entry response | Through approach propagation and receiving | Direct entry cap, conditional on available traffic and receiving |
| Entry-speed obligation | Terminal approach state, no imposed launch penalty | Terminal queued state, no automatic stopped-vehicle launch rule |
| Main adaptation from the examined merge experiment | An upstream permission/holding adapter for its ramp input | A controlled service cap inside its merge-entry interface |
| Physical stop-line claim | Upstream interpretation still needs a qualified travel/startup mapping | Effective boundary constraint; no literal signal at the merge is established |
| Common invariants | Continuous mass, counted overflow/waiting, point merge, finite receiving, rate-only action, complete TST | Same |

**Provisional recommendation: S3-G2-M.A.** Start with an upstream admission cap
and let the qualified ramp/merge dynamics determine how admitted traffic enters.
This follows the source's input-demand pathway with the smallest new speed/
startup commitment. The recommendation is conditional on a defensible approach
interface; it does not imply that upstream placement is universally more realistic
or better for control. B is an established type of ramp-metering abstraction,
and is preferable if an effective entry permission suffices and its speed/timing
interface can be defended. A's source-input continuity is a provisional reason,
not proof that B is invalid ramp metering. The decision is about causal traffic/control
meaning, not computational cost.

Selection closes placement only. Source CM/IT and mandatory merge coupling,
geometry, clearing and strong comparator closures remain named qualification
work. Nothing here certifies a useful gradient or silently closes Stage 3.


## Supplied-original continuation update

The first two originals are now read. Source CM/local IT is explicit; the missing
third construction is not a blanket adaptation blocker and the user directs
no further retrieval. The dependent [S3-G2-N gate](merge_allocation_gate.md)
is now closed with fixed priority/reallocation A approved. The bounded
continuation reaches [S3-G3 with a partial result](post_priority_findings_and_disposition.md).
The M.A placement approval and M.B's unselected status remain unchanged.
