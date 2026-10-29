# Resolve the shared traffic representation before selecting another coupling repair

Date: 2026-10-08. Response to feedback 26 in the review feedback inbox.
Discussion and candidate revision only; no representation change adopted.
K.A timing remains approved. Q.J.F and Stage 3 remain open; Stage 4 unopened.

**Your root-cause concern is justified. We should qualify a representation in
which the traffic field and moving restrictions describe the same traffic,
rather than accept an unexplained discrepancy between them.** The demonstrated
failure is specifically whole-cell averaging that discards the empty interval
between retained restriction positions. It is not a proof that all CTM-based
methods conflict with moving restrictions.

There is also an important location distinction: the current accelerating
restrictions are created from actual lane entry and move in the receiving
main lane. Changing the ramp representation alone does not remove that
mainline conflict. Your proposed replacement of their mainline effects by a
service-accounting model could avoid tracking that conflict, but then the
accounting law must establish which physical effect it preserves.

## 1. What is right about the diagnosis, and what needs narrowing

CTM is already macroscopic: it represents continuous traffic mass in spatial
cells and numerically approximates kinematic-wave traffic. It does not require
individual vehicles or integer mass. A moving restriction can have a real-valued
position inside a cell; our selected motion already allows that. Therefore the
problem is not that a restriction cannot move continuously unless CTM is removed.

The problem is that one cell total cannot describe every within-cell pattern.
In the established example, traffic lies behind the slow record, with an empty
gap between it and a faster record. Uniform cell reconstruction erases that
gap even though both records retain count labels saying no traffic lies between
them. The coarse field and exact metadata now describe different spatial states.
Keeping mass globally correct does not resolve that inconsistency.

Think of the field and records as two views of the same road. If one view says
the gap is empty and the other puts traffic there, the next motion calculation
does not have a declared common state. We should either represent the gap or
justify a complete approximation to the shared dynamics. A tolerance alone does
neither. Your rejection of unqualified error is recorded; it is not interpreted
as prohibiting every ordinary numerical approximation.

The earlier counterexample remains a local diagnostic, not proof that a real
metering policy necessarily reaches those exact initial records. Nor is it a
complete negative result for a CTM family. The closed results are bounded
bookkeeping/local-wave results; the whole CTM reference has not been closed.

## 2. Can we discard CTM, and where would that matter?

Yes: the review has no requirement to preserve ordinary CTM merely because
earlier work used it. The scientific backbone is conserved macroscopic traffic,
finite storage/receiving, causal propagation and the selected merging mechanism.
Fixed uniform spatial cells are one way to realize that backbone. Keeping the
controller and E1 birth clock regular does not require uniform cell averaging.

The literature supports this distinction. Daganzo's original CTM describes a
discrete counterpart of continuum traffic equations. Jin's continuous LTM
formulates link sending/receiving from cumulative flows. Daganzo's variational
traffic formulation admits moving constraints, while distinguishing prescribed
paths from the harder case in which the same traffic determines their motion.
These establish alternative families, not our full task's readiness.

[Primary evidence and scope](../../../extraction/rm12/bp_r_stage3/feedback26_representation_source_audit.md)

Three interpretations of your proposal have different consequences:

| Proposed change | What it achieves | What remains |
|---|---|---|
| Replace only ramp CTM by a continuous spatial macro approach | Can preserve ramp travel, queue storage and delivery to the merge without ramp cell averaging | Existing restrictions still move inside mainline cells; the demonstrated gap remains there |
| Use a continuous count/wave field wherever the restrictions act | Removes the obligation to reconstruct their surroundings from whole-cell totals alone; preserves the moving-effect mechanism | Own-motion feedback, transfers, priority and encounters still need a joined solution |
| Keep mainline CTM and convert a merged restriction into a service-accounting state | Could avoid a separate moving path inside a uniform cell if that path is no longer needed by the new law | Must derive entry/speed, influence location and duration, interactions and disappearance of the penalty; it changes the current mechanism unless equivalent |

Replacing ramp CTM by a spatial KW/LTM representation is feasible in principle.
Replacing it by a featureless queue is another change: finite travel and spatial
spillback are no longer automatically preserved. Conventional boundary-only
LTM also does not automatically include internal moving constraints; it needs
an extension or a different local wave/count solver.

The current IT lane-transfer rule uses source sections, target-section entries
and a next-section advance. A representation change must state how these
requests and transfers are transcribed. Removing the grid while copying a
grid-dependent rule unchanged is not a complete method. Fixed physical transfer
sites could remain; genuinely continuous distributed transfers need their own
supported law. Neither is selected here.

There is a further distinction at the meter. In the accepted rate-controlled
task, admission grants entry to a finite approach; it does not set a launch
speed or create an accelerating restriction at the meter. E1 creates records
at actual receiving-lane entry, after completed transfers. Tracking admitted
fluid groups through the ramp could be bookkeeping. Giving them leading-vehicle
launch/interaction dynamics introduces an additional physical mechanism and
would need explicit qualification of M.A/E1, rather than being a pure CTM swap.

Likewise, a restriction currently does not own an extra packet of traffic mass.
Mass between compatible count locations can be measured, but several distinct
records may share a count and have zero mass between them. Assigning an arbitrary
positive packet to each would change the representation and double-count traffic.

## 3. Is A a defensible bridge or merely an adaptation?

A has a sound local meaning: **do not average across a retained traffic boundary
whose count difference matters.** The restriction locations become part of the
field representation. Equal adjacent counts retain vacuum; other intervals have
the density allowed by their mass and length. This addresses the information
loss at its source rather than adjusting a label after averaging.

There is a reviewed moving-boundary numerical precedent: S02 keeps counts at
both fixed mesh points and moving bottleneck locations, reconstructs between
those locations, and evolves them through local wave problems. Thus A has a
method-family basis; it is not justified only by conserving total mass. Our
completed proof, however, establishes only a compatible reconstruction at one
update. It does not establish our full adapted evolution.

To justify A as a complete bridge, the same compatible field must determine
restriction motion and accepted fluxes, then produce the next compatible field.
Contact/coincidence, finite receiving, all transfers and inactive restrictions
must fit that evolution without clipping counts or inventing mass. The numerical
step must satisfy its own stability conditions. The next flux rule cannot
simply reuse the original uniform-cell rule after adding interior boundaries.

Changing the field basis where the moving effects occur can therefore itself
be a root-level remedy. “Adaptation” and “root change” are not necessarily
opposed. A boundary-aware numerical method and a continuous count/wave reference
may be two realizations of the same physical formulation, rather than competing
physical hypotheses. Neither requires exact solution of every continuum detail.

My previous A recommendation was too narrow if read as selecting the local
reconstruction before qualifying that full representation. I withdraw that
automatic recommendation. A remains a viable candidate; B's unqualified
compatibility tolerance is not an accepted resolution. The new representation
and service-accounting alternatives are in the revised living inventory.

## The recommended next discussion and evidence target

First define the common KW-with-moving-restrictions state independently of
ordinary CTM: which traffic counts, positions, speeds and interfaces must agree?
Then compare a boundary-aware numerical realization (A) with a continuous
count/wave realization (C) against that same state and physical mechanism.
They can share a reference/implementation relationship. The purpose is a
concrete viable joined update or a clearly identified remaining obstruction,
not a general proof for every freeway model.

Keep your ramp-plus-mainline-service-accounting proposal (D) as a distinct
candidate. Review it as a potential mechanism change or demonstrable reduction,
not presume its equivalence because the representation mismatch disappears.
In particular it must not impose a lasting service penalty when no restriction
is physically active, a defect already found earlier on this branch.

No further review execution is opened by this answer. The user asked to discuss
the idea first; no candidate, altered birth rule or accounting law is adopted.
The detailed inventory records dependencies and smallest reopen conditions.

[Revised living decision inventory](joined_step_findings_and_gate.md)

[Work report](work_report.md#2026-10-08--feedback-26-representation-diagnosis-and-candidate-revision)

[Document and scope verification](feedback26_representation_validation.json)
