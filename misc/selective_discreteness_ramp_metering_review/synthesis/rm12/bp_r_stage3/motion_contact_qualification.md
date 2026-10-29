# Own traffic can close local motion; an interval speed cannot also be ending speed

**Current status update, 2026-10-08:** Q.J.K is closed as K.A by user approval;
its synchronization retains the component stack. Conditional joined bookkeeping
and a local exact-anchor reconstruction are now established. The current shared
decision is Q.J.F, field/count compatibility (A recommended; neither candidate
adopted). Full endogenous joining, clearance and complete-TST response remain
partial. Stage 3 open; Stage 4 unopened. The following earlier findings and
candidate discussion are preserved as historical evidence, not reopened gates.

[Current findings and field/count decision](../../../reporting/rm12/bp_r_stage3/joined_step_findings_and_gate.md)


Date: 2026-10-08. Q.J-A approved; conditional analytical completion performed.
No new joined reference law adopted. Stage 3 open; Stage 4 unopened.

[Readable finding and genuine timing choice](../../../reporting/rm12/bp_r_stage3/motion_contact_findings_and_gate.md)

[Derivations and worked example](motion_contact_math.pdf)

[Source boundaries](../../../extraction/rm12/bp_r_stage3/motion_contact_source_audit.md)

## What is established

For a source-free local triangular-KW problem with piecewise-constant initial
traffic and a held desired restriction speed, a determinate moving-wave
construction gives the restriction's motion and the traffic it induces. It
handles an already slower queue, empty space ahead, the free-speed inactive
limit, and a finite group born at exactly the same point with the same count.
The records have zero added population. The construction uses immediate
one-sided traffic traces rather than an arbitrary density-averaging distance.
This is an analytical conditional reference for a field discretization, not
an adopted replacement of the whole CTM/source/node update.

The results remove two local reasons for the previous incomplete status:
one need not apply a stationary zero-capacity mask to a nonbinding free-speed
record, and coincidence alone does not require invented ranks or compression.
They do not qualify arbitrary wave interactions with lateral sources or prove
the full metering task and gradient claims.

## Local kernel and its conditions

Use the inherited per-lane triangular FD. At the initial restriction point,
let left/right densities be rho_L/rho_R, and let s in [0,u] be its desired
speed held over the local segment. Vacuum speed is defined as u. Set the
actual speed to the minimum of s and the right traffic's equilibrium speed.

If that traffic is slower, the restriction rides it. The ordinary entropy
solution already has zero relative passing at that path: adding a further
capacity deduction would be wrong. If the restriction is slower, its active
following trace is the intersection of the congested FD and the line with
slope s, and its adjacent downstream trace is vacuum. The downstream vacuum
front joins the original right traffic and moves faster than the restriction.
An entropy connection to the original left traffic lies behind the path.
At zero left density, the saturated upstream trace has zero width until
traffic reaches it; the formula does not conjure a queue without traffic.

The PDF proves this through relative flux and shock speeds, including branch
and degenerate cases. It is restricted to constant local desired speeds,
one-sided states, and no internal lateral sources. Continuation through the
explicit queue encounter below has a finite number of wave segments. There
is no general theorem here about infinitely many contacts or all endogenous
multilane interactions. Nor is this a proof against the source's single-speed
numerical approximation. Numerical motion/field error is allowed if explicitly
qualified; exact retention does not require exact continuum event resolution.

## Coincidence is compatible with exact metadata

A finite group at one lane position, time and count can retain distinct kinetic
parameters. For held desired speeds, cap each by the same initial right-stream
speed. The slowest record controls the upstream wave if it is binding. Faster
ones separate through the vacuum it leaves; a front record can ride the right
stream boundary. There is no traffic mass between those paths, so all can
continue to have the same count label. Same-speed records remain present.

This proves neither that the slowest record alone remains sufficient after
later acceleration/source events nor that other records may be deleted. No
identity order is manufactured. It is a source-free compatibility result for
the E1 coincidence, not an approval of a different birth rule.

## A queue encounter separates distance, ending speed and receiving

Use u=30 m/s, w=5 m/s, jam density 0.15 equivalents/m, a queue of density
0.075 equivalents/m beginning 20 m ahead, and one existing restriction whose
desired speed is held at 15 m/s. The queue moves at 5 m/s. Its far end and
outlet are outside the four-second diagnostic's causal domain.

The restriction travels at 15 m/s for two seconds, reaches the queue at 30 m,
then travels at 5 m/s for two more seconds. At the fourth second it is at
40 m: its average speed was 10 m/s, but its ending speed is 5 m/s. Holding
15 m/s for the whole interval crosses the queue; holding 5 m/s brakes before
the queue is reached. A 10 m/s straight path reaches the same endpoint but
has a different traffic-wave history.

With plentiful ordinary entrance demand behind this existing record, the
slowdown's backward wave reaches the entrance only at second eight. At
second four, cumulative entrance flow is 2.25 equivalents for the contact-
resolved path, versus 2 for the straight 10 m/s path. The PDF verifies this
by both a retarded wave/count construction and a density integral. This is
an isolated diagnostic with no accepted lateral sources or new births during
the interval, not a reached pair of ramp-meter controls, a full TST comparison,
or an amendment eliminating future E1 births from the admitted task.
The four seconds are a readable analytical window, not a prescribed CTM
timestep. For any regular timestep, an old record sufficiently close to a
queued cell face can encounter it inside that step; the same distinction
between distance and ending speed then applies under an ordinary CFL bound.

## Candidate fixed-clock completion: prepared, not adopted

This preserves regular meter/state/reset times while resolving old records'
traffic contacts inside an interval. It is a proposed source-to-task adaptation:

1. Start from each old exact record's desired sampled speed and the own
   reconstructed KW field. The initial instantaneous speed is capped by the
   immediate ahead trace; records add no mass.
2. Between wave contacts, use the local moving-relative kernel. At a newly
   encountered slower own stream, brake instantly, as allowed by the source
   CM idealization. There is **no positive reacceleration inside this interval**:
   after braking, the speed ceiling stays lowered until the next regular update.
3. Integrate the actual piecewise motion for position. Keep the true final
   kinetic speed separately from displacement divided by timestep.
4. At the next regular update, refresh desired speed from that ending speed
   using the source sampled acceleration function. For source-faithful comparison,
   retain the original start-of-interval position as the acceleration's grade
   argument; the level-road example removes that argument. This specific phase
   must be part of adoption, not concealed in an implementation convention.
5. Keep completed-source/E1 creation at regular times and its existing donor
   speed and count anchor. Newborn records receive no retroactive motion or
   acceleration credit. All distinct signatures remain retained.

The running minimum of the own traffic-speed caps expresses item 2 in the PDF.
Using only the original desired ceiling would allow an instantaneous return to
high speed after a queue disappears; that would evade the bounded recovery
mechanism. Distinguishing ending speed from average speed fixes the kinetic
memory, not just the position update.

On a no-contact interval this reduces to the source's position/desired-speed
recurrence. With an interior contact it intentionally changes the source's
single-speed interval transcription. The existing spatial KW/CTM backbone,
M.A meter, N.A priority and E1 reset are preserved; freezing this timing
adaptation requires the smallest affected CM/Q reference contract to be
explicitly revised. It is not already approved by Q.J-A's work authorization.
An internal contact calculation does not require asynchronous external meter
or descriptor-birth decisions. No implementation API or field-error theorem
is claimed from this local construction.

## Alternative continuous kinetic completion: also not adopted

Instead of holding the sampled acceleration schedule, integrate the source
acceleration function continuously between traffic contacts; instantaneous
deceleration still prevents crossing a slower own stream. After that stream
releases, positive acceleration resumes immediately subject to the traffic cap.
External meter and E1 times can remain regular.

This changes the free-motion recurrence as well as interior-contact recovery.
For a level-road linear acceleration law, the PDF contrasts its exponential
free-motion solution with the source's discrete recurrence. The acceleration
family is source-backed; adopting this particular joined timing is an original
completion, not a published theorem for our reset/node task. It explicitly
reopens the source sampled-kinetic transcription within M1/Q and its dependent
comparisons, while leaving information retention, actuator and births intact.

Both options retain exact records and own traffic histories. Their comparison
turns on reference traffic behavior and timing, not storage or runtime cost.

## Source-style numerical continuation: viable but still unqualified

K.C preserves the one-speed sampled recurrence and the already explicit
normalized own density-window predictor. Replace the direct stationary
zero-capacity mask by a prescribed-segment moving-relative field construction,
and qualify prediction/path/wave errors against the new contact reference.
The mesh-dependent window remains a numerical estimate, not a physical
lookahead interaction. Full retained state and E1 remain unchanged.

The local proof does not establish that C fails or that an exact event solver
is necessary. Its advantage is continuity with source numerics and the current
sampled transcription; its gap is a joined endogenous feedback/error contract,
not simply a count theorem. It requires explicit numerical accuracy/convergence
qualification at Q, not a silently tolerated physical mismatch. No particular
tolerance or new acceptable-error claim is frozen. A remains recommended for
the constructive contact-based completion; C remains a fair alternative.

## Shared update and research questions: still conditional

The field remains necessary: a current restriction-speed cap cannot replace
delayed receiving waves or available storage. The existing single-resource
N.A budget and paired population debits/credits remain required. A point source
exactly on an old path still needs an explicit one-sided attachment; the
source-free constant count cannot be carried into a sourced lane unchanged.
Those contracts must be joined after the motion timing is selected.

No theorem for all record/wave/source encounters, clearing guarantee, reached
rate-to-complete-exit/TST response, differentiable event interface, gradient
correctness/usefulness, or necessity against a strong macro/memory competitor
is established. The earlier finite-birth bound remains valid at the declared
forward-directed grid, independently of these stronger missing claims.

## Living question inventory and review order

| ID | Type / owner | Status / dependency |
|---|---|---|
| S3-G2-Q.J | Type 2 / user | Closed as A: explicit same-family completion authorized; B unselected |
| S3-I2.J.V | Type 1 / reviewer | Conditional motion/activation and finite coincidence result established; whole-source update not qualified |
| S3-G2-Q.J.K | Type 2 / user | Genuine reference timing/accuracy decision: A fixed-clock contact completion recommended; B continuous kinetics and C source-style numerical qualification alternatives; none adopted |
| S3-I2.J.V.K | Type 1 / reviewer | Transcribe selected interval speed, displacement and ending-speed phases after K; does not choose their meaning |
| S3-I2.J.S | Type 1 / reviewer | Join receiving, source attachment, simultaneous retained records and E1 after K; do not change N/E/G locally |
| S3-I2.J.C | Type 1 / reviewer | Clearance/integrable tail and meaningful full-TST control response after S |
| S3-G2-Q | Type 2 / user | Whole joined-law adoption pending; local kernel alone insufficient |
| S3-G3 | Type 2 / user | Final Stage 3 disposition pending; Stage 4 unopened |

K is the shared scientific timing contract; V.K is its dependent transcription.
This explicitly splits the mixed issue. Close the global timing first, then
finish source/receiving and clearance serially. Reopen Q for a changed physical
interaction; N for priority/resource changes; E for births; G for lost exact
records; ACT/M for changed actuation. This is not another source-access or
generic continue/defer decision.
