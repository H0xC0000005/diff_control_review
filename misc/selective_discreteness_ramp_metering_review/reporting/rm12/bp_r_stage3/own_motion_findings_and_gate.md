# The traffic-to-motion link is supported, but the joined reference is still unfinished

**Current status update, 2026-10-08:** Q.J.K is closed as K.A by user approval;
its synchronization retains the component stack. Conditional joined bookkeeping
and a local exact-anchor reconstruction are now established. The current shared
decision is Q.J.F, field/count compatibility (A recommended; neither candidate
adopted). Full endogenous joining, clearance and complete-TST response remain
partial. Stage 3 open; Stage 4 unopened. The following earlier findings and
candidate discussion are preserved as historical evidence, not reopened gates.

[Current findings and field/count decision](joined_step_findings_and_gate.md)


Date: 2026-10-08. Supplied-paper checkpoint resolved; targeted source and
analytical continuation complete. Step 67 and Stage 3 remain open.

**Subsequent decision:** Q.J-A is approved, explicit same-family completion;
B is unselected. The local completion result and genuine kinetic timing
choice supersede the procedural continue/defer gate below:

[Current motion/contact findings](motion_contact_findings_and_gate.md)

**The paper supports the physical idea we are pursuing: a slow merger changes
the traffic behind it, while traffic ahead limits how quickly it can recover.
It does not supply a complete update for our metered, lane-changing task.**
The remaining work is now a declared source-to-task completion, rather than
waiting for the requested paper. This is a partial positive result for the
model family, not a negative result about exact retained information.

The [supplied journal](../../../archive/user_supplied/rm12_bp_r_stage3/On%20the%20numerical%20treatment%20of%20moving%20bottlenecks.pdf)
was read, including its discussion and references. I also found and read the
relevant sections of the cited [Laval thesis](https://www.researchgate.net/profile/Jorge-Laval/publication/35936658_Hybrid_models_of_traffic_flow_impacts_of_bounded_vehicle_accelerations/links/54e764500cf2cd2e0293f478/Hybrid-models-of-traffic-flow-impacts-of-bounded-vehicle-accelerations.pdf).
No further paper upload is required at this checkpoint.

## What the sources actually add

Imagine a slow entrant that has just merged. On an empty road ahead, its
acceleration limit determines its motion. If it catches a queue, the queue's
speed limits its motion instead. Its resulting path creates traffic waves;
those waves, together with unused road space, determine what the next entrants
can receive. The meter remains at the upstream entrance of the ramp approach.

The 2005 paper rigorously studies the restriction-to-traffic direction with
prescribed paths. Section 5 explicitly separates the reverse direction and
points to a companion model. The thesis supplies a concrete numerical example
of that reverse link: it estimates speed from traffic ahead, then limits the
restriction's acceleration by that estimate. It also describes how restrictions
are embedded in a lane-wise traffic grid. This is stronger support than a bare
statement that an unspecified coupled solver exists.

There is a reason for the speed estimate. The paper represents a moving
restriction by successive stationary restrictions on a grid. Even when the
cumulative traffic count is accurate, this construction can produce artificial
local speed fluctuations. Looking across nearby cells is intended to avoid
feeding those fluctuations back into restriction motion. **This does not mean
averaging away the restriction records.** All distinct positions, speeds,
parameters, birth information and required own traffic history remain retained.

However, an estimate must have a definite meaning. Taking speed from average
density, averaging local speeds, and dividing total flow by total density are
different operations. For two equal road portions with densities 0.01 and
0.10 equivalents/m, a diagnostic triangular FD gives respectively about
8.64, 16.25 and 5 m/s. These are not alternative meter controls or a new
information-hiding example. They show why saying only “average the traffic
ahead” does not finish the motion law. The exact comparison is in the
[mathematical companion](../../../synthesis/rm12/bp_r_stage3/own_motion_math.pdf).

## Why the joined update cannot yet be frozen

The sources support individual ingredients. They do not establish that our
particular combination handles every simultaneous restriction, mandatory
merge and accepted lateral source with one consistent motion/receiving update.
The thesis's passing example explicitly puts restrictions on different lanes
while they cross; it is not a proof for all same-lane coincidences generated
by our approved reset. The stochastic birth example is also not a replacement
for our deterministic E1 rule.

Two analytical checks expose what a completion must preserve:

- **Accurate counts are not automatically accurate motion feedback.** A count
  error can be amplified when estimating density over a shrinking window.
  The journal's prescribed-path count bound does not, by itself, prove that
  the resulting speed estimates or endogenous paths converge. This is a
  limitation of that inference, not proof that the source method diverges.
- **A direct grid transcription can create a temporary restriction where the
  moving path is physically nonbinding.** An entrant already traveling at
  free speed does not hold up following free-flow traffic. Replacing it at
  the merge by a stationary zero-capacity boundary for a whole step can
  temporarily block that traffic. This is a conditional check of that boundary
  transcription, not a blanket criticism of every implementation of the paper.

We therefore cannot silently freeze a density-average predictor plus a
stationary capacity mask as the completed reference. A numerical field is
allowed in the present review; retaining exact records does not require an
exact continuum traffic solution. But the numerical method still needs its
own activation, motion and source consistency qualification. Nor can a
persistent physical lookahead distance be introduced merely to obtain a
convergence argument: that would add a traffic interaction assumption.

## What the clearance and research-question checks establish

There is one further positive result. In this finite, forward-directed CTM
geometry, finite offered and initial mass bound the cumulative mass transported
across forward cell moves.
Every discretionary transfer advances to the next section, and every actual
merge advances into the mainline. Consequently, the cumulative-threshold rule
can create only finitely many new descriptors, even if clearance takes a long
time. This is a bound at the declared finite grid, not a uniform bound as the
grid is refined. It uses the current geometry; it does not prohibit lane changes,
discard small transfers or add a record-count acceptance limit.

Finite births do **not** prove clearance. Traffic can still be held by an
unqualified motion/receiving rule. We have not proved that all interacting
traffic empties, produced a reached pair of metering controls with different
complete exits, or established useful gradients. A finite-time count bound
can bound finite-time TST error; it does not certify the unobserved clearing
tail or the derivative of the objective.

The present status of the research questions is therefore:

| Question/product | Current result | Still missing |
|---|---|---|
| Which information can affect control? | Positions, kinetic state, births and own wave/receiving history have a supported causal role | Necessity relative to strong aggregate/memory rivals; a nontrivial complete-TST control comparison |
| Concrete experimental task | Meter placement, continuous-rate meaning, priority, exact state and sampled reset are selected; source family has positive support | A qualified, determinate joined update and clearance contract |
| Gradient path | Control → admission → approach/merge → births and motion → waves/receiving → exits → TST is conceptually explicit | Event-boundary treatment, gradient correctness and downstream usefulness; Stage 4 remains unopened |

## The next decision: complete the source-to-task method, or accept this partial endpoint

**Problem statement:** the source-first check has finished without a complete
joined recipe. Should we continue with an explicitly identified same-family
method completion, or close/defer this line at its supported partial result?

**Model-chain function:** the completion must turn the retained own state into
one consistent motion, receiving and accepted-transfer update before E1 creates
the next records. It determines future exits and the meaning of every later
gradient comparison.

**Core gap:** the straightforward source-derived candidate is reviewable, but
its activation and feedback qualification remains incomplete. Repairing or
replacing those details cannot be represented as merely copying the supplied
paper. The current Stage 3 protocol reserves new reference-law adoption and
claim changes for the user. No earlier choice about the meter, priority, exact
retention or sampled births needs repeating.

### A — continue with an explicit same-family completion (approved)

Keep the present physical task and exact information. Complete one fixed-step
own update using the source's lane-wise KW/CTM and constrained-motion family.
Start from the concrete candidate in the
[technical assessment](../../../synthesis/rm12/bp_r_stage3/own_motion_qualification.md#concrete-source-derived-candidate-not-adopted),
and resolve its two exposed defects before proposing adoption: define the
speed estimator without silently adding persistent physical anticipation, and
make restriction activation consistent with moving-relative flow and the
nonbinding limit. Then join N.A's single receiving resource, accepted source
attachments, simultaneous records and E1; finish clearance/TST qualification.
Every departure from literal source numerics must be labeled as our adaptation.

**Pros:** directly addresses the remaining gap while preserving the approved
task and its strong information-retention endpoint. The source ingredients and
new checks give a concrete target for the completion. It does not depend on a
favorable hidden-information case or waive inactive equivalence.

**Cons:** this becomes original mathematical source-to-task completion work,
not only literature extraction. The existing theorems do not certify it; the
result may remain partial or expose a genuine incompatibility. No complete
law, clearing guarantee or useful-gradient result can be promised.

**Dependencies/consequences:** retain M.A, N.A, G1, E1, ACT.A and the current
comparison guardrail. Return to the smallest affected global decision if a
new physical interaction, clock, approximation of records or acceptance change
is required. No production development or experiment is included. The bounded
completion plan is below; its preparation does not adopt its missing laws.

### B — accept the source-grounded partial endpoint and defer completion

Record the model family and its causal state/control path as feasible to
investigate, while closing this continuation as an incomplete joined task.
Keep the explicit source-derived defects and missing evidence in the handover;
do not promote this formulation to a research-ready experiment. Decide any
later reopening after discussion, rather than claiming that the mechanism or
exact information has been refuted.

**Pros:** accurately separates what the literature establishes from what would
be our contribution. It yields a defensible closure without inventing a
coupling law or weakening the comparison criteria.

**Cons:** leaves the intended task and its control/gradient questions unresolved.
It provides no new evidence that a compact model is sufficient or that the
current line is impossible.

**Dependencies/consequences:** requires an explicit scoped closure/disposition
at Q/G3. It does not automatically open Stage 4, another branch, a pulse task,
implementation or experiments. Existing accepted subresults remain valid.

**Provisional recommendation: A.** The supplied and nearest-cited sources give
positive support for the physical family; the remaining obstruction is a
specific unqualified update, rather than evidence that exact retention or the
metering task is methodologically unavailable. B remains a legitimate partial
closure if original method completion is to be deferred.

## Approved bounded plan

1. **Bind one traffic-to-motion update.** Specify the estimator's support,
   averaging operator, time phase and downstream-end treatment; qualify
   moving restriction activation using free-flow and arriving-queue checks.
2. **Complete the conservative shared step.** Handle all existing records and
   accepted transfers together; retain N.A's single resource and E1's subsequent
   reset. Check coincidences and one-sided source/count attachment analytically.
3. **Qualify the task's endpoint.** Prove clearance or a sufficient integrable
   tail and assess a genuine common-meter effect on complete exits/TST. Return
   at any required physical-law amendment, or with a bounded disposition.

Detailed [source audit](../../../extraction/rm12/bp_r_stage3/own_motion_source_audit.md),
[assessment](../../../synthesis/rm12/bp_r_stage3/own_motion_qualification.md),
[equations](../../../synthesis/rm12/bp_r_stage3/own_motion_math.pdf) and
[work report](work_report.md#2026-10-08-supplied-journal-and-own-motion-qualification)
are supporting records. **S3-G2-Q.J is closed as A; B is unselected.**
The motion/contact continuation executes the first local part and reaches
Q.J.K, kinetic timing; neither new timing law is adopted. Full Q adoption and final G3 closure remain
pending. There is no outstanding source-input or actuator approval gate.
