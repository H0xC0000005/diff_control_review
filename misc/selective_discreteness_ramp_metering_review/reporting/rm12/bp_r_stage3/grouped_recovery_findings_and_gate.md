# Remembering recovery by groups: what can safely be grouped?

Date: 2026-10-07. You approved the expansion to position and speed groups
(M1/option A). The bounded review is complete to a choice about the actual
grouping rule. The traffic task and its physical mechanism remain unchanged.

**Subsequent user decision:** G1 / option A is approved, with the exact-information
chain first. Storage/processing cost and useful compression are not acceptance
criteria for that pass. Distinct restrictions may all be retained. Approximation
is not opened. [Continuation 65](../../../rm12_65_bp_r_stage3_exact_information_continuation.md)
records this clarification; the candidate comparison below is the historical
decision inventory, not an outstanding G selection.

The approved exact-state pass is now performed to
[Q-E insertion/reset discussion](exact_information_findings_and_gate.md).
Q-E is subsequently closed as E1; the
[sampled-insertion findings](sampled_insertion_findings.md) record bounded
reset/prescribed-path qualification. Full joined feedback remains partial;
E2 is unselected. Reduction follows exact-chain qualification. The earlier
concurrent coarse-comparator requirement is deferred.

**The expansion is useful, but a spatial group is not yet a complete recovery
model. We can justify sharing a record when restrictions have identical motion
and traffic effects. Averaging nearby but different restrictions requires an
additional approximation that has not been adopted.**

## The traffic meaning

Think of two recovering slow groups on a stretch of freeway. One meets slow
traffic ahead; the other has room to accelerate. Remembering where each speed
occurs helps predict their different recovery. Remembering only the average
speed and a separate average position can lose that association.

The state expansion gives us a way to retain the association. But if one spatial
group covers both traffic conditions, assigning everyone the group's average
position and speed can lose it again. The issue has moved from **whether the
state may contain spatial recovery information** to **how grouping preserves
the information needed for motion and traffic service**.

This example explains the problem; it is not a newly established full traffic
scenario with a different optimal metering decision.

## What this review established

There is a safe conditional case. If two restriction records have the same
lane, exact position, motion state, vehicle parameters and the same condition
on traffic passing their location,
they can share one evolving record. Identical restrictions impose the same
condition twice; counting that condition twice does not make it stronger.
Their traffic mass remains in the ordinary traffic field and is counted once.
The record's multiplicity is bookkeeping, not extra population or capacity cost.

This conclusion requires a well-defined coupled source update. We have not
assumed that all births in a cell occur at the same position, resolved all
coincidences, or produced the complete joined traffic model. In some scenarios
every restriction could still need its own record. This is a defensible
equivalence rule, not proof of broadly compact recovery.

There is also a concrete limit to simple grouping: even two groups with the
same count, mean position and speed can send different amounts across a group
boundary next time. The within-group arrangement can matter. This is a checked
local update example, not proof that all richer summaries or approximations fail.

## What the literature adds

Distribution-based traffic dynamics and compact moment models are established
families. Their closures use specific interaction and approximation assumptions;
they are not ready substitutions for this reference's recovery rule.
[Gong/Piccoli/Visconti](https://arxiv.org/pdf/2007.14655),
[Helbing/Greiner](https://arxiv.org/pdf/cond-mat/9806126).

Moving-restriction methods also show how trajectory-specific conditions couple
to traffic service. They support the coupling question, rather than a rule that
adds separate average penalties from every group.
[Daganzo/Laval](https://escholarship.org/content/qt1hp588xx/qt1hp588xx.pdf),
[Simoni/Claudel](https://arxiv.org/pdf/1701.01026).

The scoped finding is therefore **partial support for a group representation,
with no qualified rule yet for combining distinct nearby restrictions under
the whole current task**. This is not a negative verdict on all compact models.

## Why this is now a decision

**Problem statement:** should the first concrete grouping rule preserve the
source exactly wherever grouping is certified, or should we introduce an
explicit approximation to achieve broader compression?

**Function in the model chain:** groups remember motion after actual merges;
their own update determines where restrictions act; the conservative traffic
coupling determines service, exits and total system time. The meter and objective
are unchanged.

**Core gap:** a cell count or average does not determine the missing within-group
arrangement. Supplying a representative arrangement changes predictions.
Preserving the full arrangement avoids that choice but may retain nearly all
the detailed state. Approval to expand the state did not choose between these
scientific consequences.

### G1 / option A — preserve the source and group only certified equivalents

Use the identical-signature rule as the first concrete grouping contract.
Here a signature means all the motion and traffic-service data determining
a restriction's behavior, not its personal identity.
Distinct motion/service signatures remain distinct. Every group evolves from
its own traffic and source motion rule. Broader merging or permanent deletion
needs a certificate that the source response is preserved; proximity or current
inactivity alone is insufficient.

**Pros:** adds no average-path or capacity-penalty assumption; preserves the
existing inactive requirement wherever source equivalence is established;
provides a clear check for the proposed representation and its own update.

**Cons:** compression may be small or absent, and state size can grow with
distinct disturbances. It supplies an equivalence anchor, not by itself a strong
coarse competitor or an information-loss/control witness. Joined source events
and clearance still need qualification.

**Dependency/consequence:** approve this grouping contract for the next source-
coupling qualification, not a completed compact model. Keep the genuinely
reduced comparator obligation explicit. Do not manufacture coincident births
or hide a detailed solver behind a compact-state name to meet it.

### G2 / option B — define an approximate within-group reconstruction

Choose a justified joint position/speed projection and an explicit rule for
the arrangement represented inside each group. Derive transport and traffic
service from that model's own reconstruction; assess its errors and inactive
behavior. Means, profiles or several representatives are possibilities to
justify, not choices already selected here.

**Pros:** can merge distinct nearby states and supply a genuinely smaller model;
has precedents in distribution/moment modeling; permits a meaningful test of
how representation resolution affects control predictions.

**Cons:** introduces a new reconstruction assumption and possible activity,
transport and service bias. Small position/speed errors do not yet give a
whole-task system-time or gradient error bound. A new approximation may still
fail the current inactive requirement.

**Dependency/consequence:** the concrete projection, reconstruction, update,
service law and calibration domain need a reviewable proposal. This route does
not waive T1; a conflict must reopen that smallest requirement separately. A
future refinement cannot recover lost member information from the reference.

### G3 / option C — accept and park this bounded partial result

Retain the conditional exact grouping and local projection limits, but leave
the whole compact recovery model unresolved.

**Pros:** records an honest evidence boundary without adding an unsupported
closure or narrowing the task to make grouping work.

**Cons:** leaves the current research-ready comparison unfinished; it gives no
control-relevant information gap or useful-gradient result.

**Dependency/consequence:** parks this attempt if selected. Final Stage 3
disposition is a separate user decision; no other review or experiment opens.

**Provisional recommendation: G1 first.** It is consistent with the preference
to avoid extra modeling assumptions. Its limited compression must remain an
explicit result, not be called a successful coarse model. If genuinely reduced
recovery remains unsupported, discuss G2 or a bounded disposition before
introducing an approximate reconstruction.

## Position and evidence limits

| Research obligation | Status after this pass |
|---|---|
| Fairness of expanded state | Joint spatial/kinetic information has a clear function; own inputs remain required. |
| Concrete grouping | Conditional identical-signature rule supported; adoption pending. |
| Broad compact recovery/service | Not established for distinct nearby restrictions. |
| Complete system-time control response | Not established; local update differences are insufficient. |
| Useful gradients | Not established; separate later review. |

**M1 is approved and its bounded pass is performed. S3-G2-Q-G is closed as
G1, Type 2/user; G2 and G3 are unselected.** Concrete whole-model adoption and final
Stage 3 closure remain pending. Stage 4 and experiments remain unopened.

Optional support: [technical assessment](../../../synthesis/rm12/bp_r_stage3/grouped_recovery_qualification.md),
[source audit](../../../extraction/rm12/bp_r_stage3/grouped_recovery_source_audit.md),
[mathematical companion](../../../synthesis/rm12/bp_r_stage3/grouped_recovery_math.pdf)
and [work report](work_report.md). The facade can be read without the proofs.
