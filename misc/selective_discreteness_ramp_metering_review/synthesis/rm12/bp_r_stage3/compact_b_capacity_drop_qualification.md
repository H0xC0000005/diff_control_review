# Companion B — dynamic capacity-drop qualification

Date: 2026-10-07. **Dynamic diagnostic candidate supported; full inactive
admission not passed.** B was reviewed during the same authorized pass as A.
Sources: [primary audit](../../../extraction/rm12/bp_r_stage3/dual_qualification_source_audit.md).
Equations/proofs: [mathematical companion](dual_qualification_math.pdf).

## What B predicts

B carries its own road/ramp queues and propagates traffic through the common
finite approach. At the merge, it tests demand against ordinary receiving.
When that test activates the calibrated drop, it shares the resulting receiving
with the approved fixed priority. It requires neither individual accelerating
constraints nor a new penalty timer.

The conservative node bounds survive this supply modification. Demands are
not exceeded, receiving is spent once, and unused priority shares can be used
by the other stream. Continuous paired transfers preserve population. Native
single-node evidence does not certify the adapted multilane grouping or the
joined reference's motion/count integration.

## New control-response finding: distinguish a ceiling change from sharing it

If the drop trigger stays active and ordinary receiving stays above the dropped
capacity, B has a fixed service ceiling. With enough traffic available to use
it, changing ramp demand reallocates ramp/mainline service but leaves total
merge output unchanged at that instant. This is a direct deduction from the
native operator, with explicit conditions in the PDF.

Therefore B's metering benefit must be sought in a changed trigger, receiving,
availability, future queue evolution, or later exit history—not assumed from
the fact that the ramp award changes. It is not a theorem that every metering
schedule gives the same TST. A finite ramp approach can delay entries and change
when the trigger turns on/off. Downstream travel and lane states may also make
the exit history differ while local output is equal.

An upstream meter cannot instantaneously turn off the trigger if ramp traffic
already near the merge continues to request entry. This makes the approach
state essential even for B; a direct command-at-merge substitution would test
a different control task.

## Inactive behavior: a narrower pass does not erase the failure

With no ramp demand, mainline demand no greater than full ordinary receiving,
the trigger is off and the ordinary node is recovered. This correct narrow
limit does not imply agreement whenever the reference has no active descriptor.
The earlier 90-versus-80 receiving example remains valid as a local check.

A second local check in the PDF uses full downstream receiving, mainline demand
at capacity and a small positive ramp request. Native B immediately drops the
ceiling. An initially descriptor-free sampled reference with sufficient space
can still use the ordinary node before its first transfer threshold is reached.
This identifies a possible onset mismatch without downstream crowding. It is
a conditional local-update comparison, not a demonstrated complete control
trajectory, calibrated task or proof of a field-model defect. Global reachability
and the chosen birth timing still require qualification.

No parameter, trigger patch or inactive-criterion waiver is adopted. A failed
mechanism-matching check does not prohibit diagnostic review; it does prevent
certifying B as a matched reduction under the unchanged criterion.

## Fixed calibration and claims

The drop fraction is physical/model calibration held fixed across intervention
schedules. It is not the merge priority, a ramp speed control, or a new
service-equivalence multiplier. Calibration can use a later declared common
training/held-out protocol; per-intervention fitting is excluded. No numerical
value is selected by the normalized hand checks.

**Disposition:** retain B as the companion. It provides a concrete independently
dynamic explanation and a useful fixed-trigger comparison. Its failure may be
trigger/constitutive error; it does not prove necessary identity. Its success
would establish only scoped predictive sufficiency before separate gradient
checks. Any definitive admission despite the known mismatch needs an explicit
later acceptance decision. The transient admission issue is now shared with the proposed present-entry A
mean. B remains the companion; this is not a reopening of A+B coordination.
