# Primary A — mean-service qualification

Date: 2026-10-07. **Conditional local construction supported; full task port
not qualified.** The user subsequently approves T1; the
[memory qualification](event_memory_qualification.md) adds exact event accounting
and conditional kinetics without adopting a compact service law. Current
discussion is [Q-M](../../../reporting/rm12/bp_r_stage3/event_memory_findings_and_gate.md).
This executes the A work in
[arrangement 62](../../../rm12_62_bp_r_stage3_dual_review_arrangement.md).
Read the [source audit](../../../extraction/rm12/bp_r_stage3/dual_qualification_source_audit.md)
and [derivation](dual_qualification_math.pdf).

## Semantic result

A can ask: if entrants continued arriving at the present rate and speed, how
much service would their acceleration leave for the stream? The answer can be
used in a spatial traffic model whose own queues evolve. The construction is
not intrinsically undefined because actual entry and available service depend
on each other: a useful local fixed-point result can be obtained.

But the published multilane mean formula is not a direct transcription of the
current reference. Copying it would approximate not just retained disturbance
history but also acceleration, spatial interactions and some entry-speed
relations. Those changes need explicit treatment before a primary comparison
can be interpreted.

## New local analytical construction

For a **point-insertion renewal subcase**, use one fixed entry speed and a
bounded nondecreasing free-motion path, approaching the same free speed as the
KW stream. A backward characteristic from the next insertion intersects that
path exactly once. The traffic count along the resulting space-time boundary
gives a conditional mean service.

The PDF derives four useful facts:

1. The intersection and mean service are well-defined. A free-speed bound gives
   a service between zero and ordinary capacity. No artificial capacity clip is
   needed for this particular construction.
2. As entry rate vanishes, the service tends to ordinary capacity; entrants
   already at free speed give ordinary capacity. This is a local inactive
   consistency result, not recovery of every transient with old disturbances.
3. At fixed birth speed, more frequent insertions weakly reduce mean service;
   a uniformly faster free-motion path weakly increases it. Changing metering
   can affect both frequency and speed, so neither fact determines a best rate.
4. Coupling this monotone mean to ordinary receiving and the approved fixed
   priority has a unique scalar actual-entry solution when birth speed is a
   declared pre-update own-model input. This result does not cover a general
   multilane coupled solver or a speed computed implicitly from that flow.

All conservation balances remain continuous. The renewal interval describes
disturbance frequency; it does not floor or integerize admitted/transferred mass.
No numerical root solve, traffic rollout or gradient check was run.

## Final transient check: the local inactive limits are not sufficient

The PDF's final check uses a descriptor-free startup state with a slow queued
ramp donor, sufficient mainline/ramp demand and full ordinary receiving. The
unique point-mean root gives a positive accepted entry and a mean ceiling below
ordinary capacity. In a sufficiently small source bin, those actual transfers
have not yet crossed the first descriptor threshold: the reference still uses
the ordinary node, while A already predicts a penalty. This is a conditional
local onset/averaging mismatch, not a complete control trajectory or a universal
refutation of mean-service models. It does not infer a slow donor speed from a
small free-flow demand.

Therefore zero-entry and free-speed limits do not certify the current entire
transient inactive requirement. Present entry intensity does not tell A whether
an actual restriction is currently absent, active or recovering. A source-
qualified own-model event/memory summary could address this, but none is bound.
Alternatively the mean can be evaluated as an explicitly approximate predictive
rival with that error reported. That requires a comparator-admission decision;
merely choosing a point geometry does not solve the mismatch.

## Why matching only recovery time is insufficient

A single representative acceleration could reproduce the time needed to reach
free speed while giving a different distance traveled during that recovery.
The free-speed distance deficit affects the renewal service. The PDF proves
this distinction using the source's level-road free-motion curve and a linear
curve with the same end speed and duration. Thus a time-equivalent acceleration
is a real constitutive approximation, not a harmless parameter transcription.

This supports deriving the mean from the declared kinetic curve rather than
quietly treating the native constant-acceleration formula as matched. The
continuous curve is an analytical illustration; the original sampled motion
and birth conventions still need consistent binding in the eventual task.

## Independent state and input contract

Retain spatial lane/ramp mass and external waiting. Compute candidate entry
rates, speed inputs and receiving from that model's own state. Keep rate,
approach admission, actual merge entry and final exits distinct. Couple actual
entry and service rather than inserting upstream permission directly into a
capacity formula. Keep public initialization/projection and fixed parameters.

Neither accepted flow divided by density nor a congested-branch inversion is
automatically the donor's physical birth speed. Lane-choice look-ahead speed,
downstream constraint speed and donor birth speed retain their separate roles.
No new speed statistic, estimator support or future correction is adopted here.

## What the point result does not establish

It assumes a repeating local pattern and a free-motion renewal path without
unrepresented downstream/neighbor interference. Finite insertion positions,
bidirectional lane exchanges, wave/void interactions, heterogeneous headways
and old restrictions require their own mean closure. Applying the point result
at every cell would risk charging a disturbance repeatedly; that is not proposed.
The result is not an exact reduction of the adapted source reference and is not
a completed transient law on the existing multilane envelope.

Startup, draining and low-demand branch binding remain necessary. Whole-reference
event integration, full-TST rate leverage, compact sufficiency/insufficiency and
gradient usefulness are not proved. The local monotonicity is not a global
policy-dominance theorem.

**Disposition:** A remains viable. Its local mathematical core has progressed
beyond a named mean-capacity family. Its present-entry version is not admitted
as a matched transient reduction. The immediate choice concerns a qualified
retained-state extension versus predictive-model admission, not geometry alone;
see the [transient-comparison gate](../../../reporting/rm12/bp_r_stage3/dual_qualification_findings_and_scope_gate.md).
