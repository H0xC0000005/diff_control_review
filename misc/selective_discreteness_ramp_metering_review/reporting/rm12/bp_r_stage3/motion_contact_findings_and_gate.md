# A merger can follow its own traffic; the remaining choice is how recovery uses time

**Current status update, 2026-10-08:** Q.J.K is closed as K.A by user approval;
its synchronization retains the component stack. Conditional joined bookkeeping
and a local exact-anchor reconstruction are now established. The current shared
decision is Q.J.F, field/count compatibility (A recommended; neither candidate
adopted). Full endogenous joining, clearance and complete-TST response remain
partial. Stage 3 open; Stage 4 unopened. The following earlier findings and
candidate discussion are preserved as historical evidence, not reopened gates.

[Current findings and field/count decision](joined_step_findings_and_gate.md)


Date: 2026-10-08. Your option A is approved and its analytical continuation
has produced a bounded positive result. RM12 Stage 3 remains open.

**We can now describe a consistent local response without averaging over an
arbitrary road length: a slow merger holds back faster traffic, but follows
an already slower queue without adding another service penalty.** Keeping
several restriction records at exactly the same point is also locally
consistent; they do not need invented vehicle spacing or extra traffic mass.
This establishes more than source-family plausibility, although the complete
metered, lane-changing model is still unfinished.

## The traffic meaning of the result

Think of a slow entrant with empty road ahead. It moves according to its
current recovery speed. Faster traffic catches up behind it, while a gap opens
ahead. If it catches a queue already moving more slowly, it joins that queue's
motion. It must not pass through it, and the model must not subtract a second
capacity penalty merely because the entrant's record still exists.

The local mathematical construction handles those cases through traffic waves:
boundaries between different traffic states move at speeds determined by mass
conservation. It also reproduces the harmless free-speed case. This provides
an analytical reference for checking a numerical KW/CTM field; it does not
require abandoning the spatial macroscopic backbone.

Suppose two records start together, one recovering more slowly than the other.
The slower one can hold back traffic while the faster one moves into the gap
ahead. Both still have the same traffic-count label because the gap contains
no traffic. We can retain both kinetic descriptions without pretending that
each record is another vehicle. This result concerns a local segment with
held desired speeds; it does not justify deleting the faster record later.

The physical ingredients are grounded in the supplied constrained-motion
journal and the primary moving-bottleneck literature. The local wave proof
and the example below are deductions made in this review, not a claim that
the literature has proved our complete joined task.

[Source support and its limits](../../../extraction/rm12/bp_r_stage3/motion_contact_source_audit.md)

## A concrete example shows what the update must remember

An existing restriction moves at 15 m/s toward a queue initially 20 m ahead.
The queue moves at 5 m/s. It catches the queue after two seconds, then follows
it. After four seconds it has traveled 40 m. Its average speed was 10 m/s,
but its speed at the end is 5 m/s.

Those are different pieces of information. The average tells us how far it
traveled. The ending speed tells us how much recovery it still needs. Using
10 m/s for both would give it an unjustified head start in the next
acceleration update. Using 15 m/s throughout crosses the queue; using 5 m/s
throughout slows it before the queue is reached.

The distinction also changes the waves behind it. In this diagnostic, the
slowdown reaches the entrance only at second eight. A straight path at the
average speed has the same four-second endpoint but a different entrance-flow
history. Thus endpoint agreement alone does not close motion and receiving.
The four seconds are an explanatory window, not a prescribed CTM timestep;
an interior contact can also occur within a shorter, CFL-compatible step.

This does not prove the source's single-speed numerical approximation is
unusable. A numerical scheme may approximate these events. It must then
qualify that motion and wave error; exact record retention does not require
an exact continuum field. The positive construction gives a local reference
against which such an approximation can be assessed.

This is a local analytical example, not a pair of ramp-meter policies or a
complete total-system-time comparison. Future births and lane changes remain
part of the admitted full task.

## What this establishes for the research question

The exact-state line now has a constructive local result: own traffic can
determine motion, restriction activation and coincident-record compatibility.
The result keeps the meter placement, continuous mass, fixed merge priority,
exact information and sampled births. It does not establish that all this
information is necessary against a strong aggregate/memory competitor.

The next pieces remain the shared update with actual lane transfers, correct
count attachments where transfers meet old restrictions, clearance or an
integrable clearing tail, and a reached metering change that affects complete
exits and total system time. Gradient correctness and usefulness remain later
questions. Stage 4 is unopened.

## The genuine modeling choice now exposed

This is **S3-G2-Q.J.K**, a new timing/adoption decision. Your earlier Q.J-A
approval to push the completion is recorded as closed; it is not being asked
again. No further paper reading or source-access approval is needed here.

**Problem statement:** how should a restriction's kinetic state evolve when
its own traffic changes partway through a regular simulation interval?

**Model-chain function:** this state determines its next recovery motion,
which creates waves and receiving for subsequent traffic. Position and ending
speed must belong to the same own traffic history.

**Core gap:** the source's sampled numerical update uses one speed for both
interval travel and the next acceleration increment. The resolved contact
shows why that single value cannot represent both exactly. Completing the
model as a contact-resolved reference requires declaring how braking and renewed
acceleration fit inside the regular clock. Alternatively, retain the source's
one-speed numerical approximation and qualify its errors explicitly. This
chooses the reference timing/accuracy contract, rather than another source route.

### A — resolve contacts, retain the regular recovery clock (recommended)

Let the restriction slow as soon as its own traffic requires it. Integrate
that motion for distance and store its true ending speed. Refresh positive
acceleration at the next regular update, from the ending speed. If a queue
disappears earlier, it waits until that update to accelerate again. New E1
records still begin after completed transfers at the regular update.

**Pros:** preserves the current sampled recovery schedule on intervals without
contacts; fixes crossing a slower queue and incorrect kinetic memory; retains
regular public updates, exact records and the existing birth clock. It makes
the smaller amendment among the two contact-resolved kinetic completions.

**Cons:** renewed acceleration can wait for the next update, so recovery has
a timestep dependence. Internal traffic contacts must be resolved consistently
with the own field. This is our declared adaptation, not a full source theorem.

**Dependencies/consequences:** explicitly amend CM/Q's single-speed interval
transcription and ending-speed phase before freezing. M.A, N.A, G1 and E1
remain fixed. Internal wave resolution does not require asynchronous meter or
birth decisions. Then join source/receiving and qualify clearance/full TST.

### B — resolve contacts and advance recovery continuously

Use the source acceleration function continuously between contacts. Brake
when required by the own queue, and begin accelerating again immediately after
it releases. Public meter and E1 times can still remain regular.

**Pros:** avoids waiting for the next update after release and gives motion
and ending speed from one continuously evolving kinetic history. It is a
legitimate use of the supported acceleration family.

**Cons:** changes the existing free-motion recurrence even when there is no
queue; it therefore broadens the reference change. The coupled field/source
qualification is still missing and cannot be inherited from the local proof.

**Dependencies/consequences:** explicitly reopen the sampled kinetic
transcription within M1/Q and its dependent comparisons. Meter placement,
priority, exact retention and E1 births remain unchanged. No cost argument
or approximation requirement favors either candidate.

### C — retain one sampled speed and qualify its numerical errors

Keep the source recurrence: one speed determines interval travel and the next
desired speed. Use the explicit own density-window predictor already audited,
with a moving-relative field treatment instead of the unqualified stationary
zero-capacity mask. Treat its interior-contact errors as numerical errors to
be measured and bounded against the new local construction. This does not
compress records or add a physical lookahead rule.

**Pros:** retains the sampled kinetic transcription and a concrete source-style
numerical approach; ordinary numerical field/motion error is allowed. The new
contact solution gives it a sharper mathematical test than count accuracy alone.

**Cons:** its predictor remains unqualified for the adapted task. The local
result does not prove that its endogenous motion, wave and clearing errors
vanish, nor that its derivatives are adequate. It cannot be adopted simply
because the source used related numerics.

**Dependencies/consequences:** declare a numerical accuracy/convergence contract
at Q and qualify the predictor/relative field jointly before source/node joining.
No existing guardrail is weakened by selecting this review route; a failed
check returns to Q. M.A, N.A, G1 and E1 remain fixed.

**Provisional recommendation: A.** It addresses the exposed physical gap while
keeping the approved regular recovery schedule as far as possible. B remains
a viable alternative if continuous recovery timing is the intended reference;
C preserves more literal source numerics but still needs feedback-error qualification.
Neither timing law is adopted. The pause is at this changed scientific contract,
after the constructive local result, rather than at another procedural gate.
C remains admissible for further qualification; the local contact result does
not refute it or establish that exact event resolution is mandatory.

The technical material is optional for understanding this finding:

[Mathematical explanation](../../../synthesis/rm12/bp_r_stage3/motion_contact_math.pdf)

[Qualification and exact proposed phases](../../../synthesis/rm12/bp_r_stage3/motion_contact_qualification.md)

[Work report](work_report.md#2026-10-08-qj-a-approved-local-motion-and-contact-completion)

[Verification record](motion_contact_execution_validation.json)
