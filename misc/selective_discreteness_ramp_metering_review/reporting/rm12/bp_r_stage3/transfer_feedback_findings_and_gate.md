# Transfers can share the restriction's field; late-arriving traffic exposes a sending choice

**Subsequent decision and execution, 2026-10-08:** the user approves T.A
and rejects an extra held rate limit without supporting evidence. Q.J.F.T
is closed; T.B unselected. The dependent continuation establishes amount
exhaustion and coupled local allocation examples, then reaches the distinct
Q.J.F.P allocation question. The T.A/T.B comparison below is the preserved
historical rationale, not an unresolved current gate.

[Current result and P.A/P.B decision](quota_allocation_findings_and_gate.md)

Date: 2026-10-08. The user approved and opened the four-step transfer
continuation. **There is a constructive local positive, followed by one
methodological decision. The complete forward bridge is not yet closed.**

The positive is about actual traffic, rather than compatible pictures alone.
Through traffic and traffic changing from an adjacent lane enter a section
containing a slow restriction. The restriction creates a queue. When the
queue reaches the section's entrance, it reduces entry. The accepted flows,
the queue, the restriction's motion and its traffic-count label all agree
with the same evolving field. A second case serves both requests fully.

This also extends locally to the ramp: its approved fixed share and the
non-ramp through/lateral group spend the receiving allowance once. We retain
two distinct old restrictions and can attach two newly eligible effects to
the completed field at the next regular update. **This is an analytical
certificate for specified states and one interval, not a reached control
experiment or the entire joined model.**

## What the concrete case establishes

In the constrained example, a 30 m section has a slow effect initially 1 m
from its entrance. It moves at 5 m/s. Initially the entrance can receive
about 0.643 vehicle equivalents/s. After 0.2 s, the restriction's backward
queue wave reaches it; receiving falls to 0.375. Both competing streams
therefore reduce their accepted entries. The receiving history is derived
from the traffic waves; it is not supplied independently.

Over the one-second interval, 0.429 equivalents enter. The ending queue and
boundary counts account for exactly that mass. With a second, faster effect,
the field also retains its separate queue and the empty gap between them.
Neither effect record owns extra population. In the available-receiving
case, the lower requests are fully served and the queue stays away from
the entrance.

The ramp extension preserves fixed priority, unused-share reallocation and
the approved proportions within the non-ramp group. It does not give ramp,
through traffic and lane-changing traffic separate receiving budgets.

## Why the now-closed temporal decision was needed

The source CTM recipe says how much traffic **wants to advance during a
regular timestep**, using a cell's average density. A richer field can also
say **when that traffic can physically reach the exit**. Those are different
questions. The old uniform-cell recipe does not uniquely specify how its
sampled request should operate after we retain that internal layout.

Consider a 30 m ramp approach with 0.45 equivalents near its upstream end
and empty road ahead. Keep the meter closed during the present second;
downstream receiving is ample. Its average-density sending request is 0.45
equivalents for that second. The own KW field, however, cannot deliver
traffic to the merge until 0.9 s. It can discharge at most about 0.064
equivalents before the next regular update.

Two reasonable completions differ even here:

- Treat 0.45 as a **total request allowance**. Once traffic arrives, it may
  use physically available capacity until that allowance is spent. This
  example discharges about 0.064 equivalents.
- Treat it as a **held rate of 0.45 equivalents/s**. Once traffic arrives,
  that sampled rate still limits discharge. This example discharges 0.045.

Both can conserve mass and respect the own field. They produce different
queues, accepted-transfer counts and potentially different next-clock effect
births. For example, if the ramp's previous accepted-entry counter is 0.94,
the first completion crosses the next birth threshold and the second does
not. The birth rule itself is unchanged.

This is a diagnostic of the numerical/source interface, not a proposed
hidden-information scenario or evidence of controller benefit. Nor does it
refute CTM: the native coarse CTM step approximates the internal layout.
Ordinary numerical approximation remains allowed. What is not justified is
declaring these two richer completions equivalent without choosing and
qualifying their transfer meaning.

## The decision: what does the sampled request constrain?

**Problem statement — Q.J.F.T, Type 2 / user.** When the own traffic field
delays discharge inside a regular interval, does the sampled request constrain
the total transferred mass, or its instantaneous rate as well?

**Assumed model-chain function.** The request enters the donor sending and
shared-node allocation, before paired transfers update the field and E1
creates effects. Its interpretation changes what motion, receiving, counts
and future effects see. It is not a change to the upstream meter actuator.

**Core gap.** The source's finite-step desired masses and constant-step flow
calculation coincide in its original sampled cell recipe. They no longer
uniquely determine an internal causal discharge history on a nonuniform
field. The two explicit completions above are not the same forward map.
The exact numerical values are consequences, not a cost criterion.

### T.A — sampled mass requests, discharged when physically available

Keep the regular request-phase observations, choice fractions and desired
movement masses. Track each movement's unspent request through the interval.
Actual discharge must also respect the donor field, shared receiving and
the approved IT/N.A allocation. Do not retry lane choice or reassign an
unused movement request inside the interval. A request is a numerical claim
on possible service, not a packet owning population or a new meter.

**Pros:** preserves the source's stated desired number of advancing moves;
lets late-arriving traffic use available road capacity; avoids imposing a
second rate limit just because the interval started with traffic far away.
The single-exit example has a complete causal realization.

**Cons:** this is a declared richer-field adaptation, not a published
drop-in implementation. Multiple donor/target ports still need an explicit
allocation while requests remain unspent, including depletion and temporary
unavailability. A total allowance alone does not settle those interactions.

**Dependencies and consequences:** qualify that allocation next under
Q.J.F.T's selected semantics. Preserve the sampled choice and birth clocks,
fixed ramp priority, single receiving budget and exact effect metadata. Any
needed new FIFO, rerouting or priority rule must return as its own decision.
Approval would select the qualification direction, not adopt a full solver.

### T.B — held request rates, additionally limited by the own field

Divide each sampled movement mass by the regular interval duration and hold
that nominal request rate. The field can reduce it when traffic has not yet
arrived or receiving is constrained. Missed service is not caught up above
the nominal rate during that interval. Reconsider requests at the next
regular update; preserve N.A and the existing within-group proportions.

**Pros:** stays close to an explicit CTM flux held over a step; supplies a
simple, well-defined nominal-rate interface; keeps regular sampling and
avoids resampling lane choice at internal wave events. It also has a complete
causal realization for the single-exit diagnostic.

**Cons:** can leave usable downstream capacity idle after traffic arrives;
the rate limit changes queues and effect births. It requires qualification
as a numerical sampling consequence, rather than being called an additional
physical bottleneck or assumed equivalent to the source's finer solution.

**Dependencies and consequences:** qualify causal donor availability, shared
allocation and refinement behavior with the declared nominal rate. It does
not justify freezing unobstructed receiving, spending absent traffic or
changing the upstream meter. Full joined evolution remains a subsequent check.

**Recommendation subsequently approved: T.A.** It retains the source's sampled desired
mass meaning and does not add a held rate restriction where the own field
already determines availability. This is methodological reasoning; literature
does not already prove the complete T.A multi-port adaptation. T.B remains a
legitimate explicitly sampled numerical alternative.

T.A/T.B are temporal sending choices. They are different labels from the
earlier moving-boundary A1 / fixed-cell reconstruction A2 / count-wave C
representation candidates. No representation is selected here.

## Scope, evidence and next allowed work

| Approved work | Result at this stop |
|---|---|
| Read the source requests on the richer field | Desired masses, nominal rates and own port availability separated; exact temporal equivalence not established; Q.J.F.T subsequently closed as T.A |
| Actual through/lateral transfer with an old restriction | Two own-field one-interval certificates: fully available and constrained receiving |
| Joined setting | Local ramp priority, two old records, wave interaction and simultaneous E1 attachment checked; arbitrary contacts, crossings and repeated multi-port updates not closed |
| Forward bridge assessment | Partial positive; stop for the changed source-time interpretation, not generic permission to continue |

The original journal defines sampled desired moves and IT allocation. Merge
literature distinguishes finite CTM fluxes from their continuous junction
solutions, including boundary states needed for consistency. Neither result
automatically supplies our full multiple-effect adaptation.

[Lane-changing source, sections 2.1–2.2](https://doi.org/10.1016/j.trb.2005.04.003)

[Continuous merge analysis, sections 3–5](https://arxiv.org/pdf/0810.3952)

After the user selected T.A, its dependent review proceeded to Q.J.F.P.
Select that allocation interpretation before completing shared-donor/depleted
modes and remaining contact, crossing and reset interactions. N.A ramp
priority/grouping/shared receiving, M.A/G1/E1/K.A/T.A remain approved. Q.J.F,
full Q adoption and Stage 3/67 remain open. Clearance, complete-TST metering
response and useful gradients remain downstream. Stage 4 is unopened.

[Mathematics and exact cases](../../../synthesis/rm12/bp_r_stage3/transfer_feedback_math.pdf)

[Technical qualification and question ownership](../../../synthesis/rm12/bp_r_stage3/transfer_feedback_qualification.md)

[Primary source audit](../../../extraction/rm12/bp_r_stage3/transfer_feedback_source_audit.md)

[Analytical and document checks](transfer_feedback_execution_validation.json)
