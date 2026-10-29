# S11.20 — Temporary-closure recovery admission findings and user gate

Date: 2026-09-30. Status: **Closed; G4-A approved and TCR-E accepted.**
Parent: [approved S11 plan](../../s11_00_temporary_closure_recovery_admission_review.md).
Evidence: [source audit](../../extraction/s11_temporary_closure_recovery_source_audit.md)
and [admission matrix](../../synthesis/s11/s11_temporary_closure_recovery_admission_matrix.md).

## Decision summary

The temporary-closure domain is credible, but the default admission threshold is
not met. The evidence supports three neighboring facts:

1. a fixed lane reopening can have a noninstantaneous, lane-resolved recovery;
2. lane-uniform work-zone VSL can change lane-change activity and mobility; and
3. lane-change anticipation, gaps, relaxation and waves can affect discharge.

No inspected primary source joins them. In particular, none shows that hidden
lane/gap/order state **at a fixed reopening** changes transient service after
conditioning on the declared strong aggregate history, or that the resulting
change selects a different useful common VSL action. Composing separate contexts
would create a testable hypothesis, not an established mechanism chain.

Under the working-default G4-A, the result is therefore:

> **TCR-E — evidence inconclusive; do not admit a full Option 3 protocol on the
> current source basis.**

This is narrower than a mechanism impossibility. Lane/gap/order effects remain
physically plausible, and recovery remains a meaningful scenario. The missing
joins are precisely the result that a later empirical protocol would have to
assume or test.

## Results against the approved questions

### G1-A — removable one-lane obstruction

**Pass as a task domain.** Official work-zone/VSL sources and incident-recovery
studies support a fixed temporary mainline restriction and recovery phase. The
simple three-lane domain remains preferable to a temporary event stacked on the
permanent drop because it isolates recovery.

### G2-A — exact strong-history information target

**Coherent but unresolved.** Relational gap, leader and lane-change-memory
variables are finer than aggregate density/flow/speed. Full spatial aggregate
history can nevertheless reveal waves, queue state and some preparation effects.
No source provides an exact collision, an observer residual study or a minimum
hidden state after conditioning on that history. S11 found no justification for
weakening the comparator.

### G3-A — declared metric set

The evidence supports retaining the set, then assigning distinct roles:

- **primary decision candidate:** all-cohort total system time or total delay
  through common clearance;
- **secondary operational measure:** queue-clearance time or duration;
- **mechanism diagnostic:** time-resolved post-reopening discharge/throughput;
- **required guardrail:** queue length plus residual/unfinished demand;
- **supporting diagnostics:** speed, speed variance and lane-change activity.

This recommendation follows the evidence rather than freezing a target at S11
opening. It still prevents metric shopping: a later protocol must freeze the
roles before outcomes are observed. Clearance or throughput alone cannot support
a useful-control claim because they can hide displaced waiting or unfinished
traffic.

### G4 — evidence standard

G4 was intentionally deferred to this gate. The full candidate discussion below
includes the new cross-context option exposed by the completed audit.

## Why the S05 obstruction still matters

If reopening merely restores an aggregate capacity and advice only shifts when
traffic arrives, complete accounting provides no supported reason for a slower
common advice to beat the fastest feasible action. A useful distinction needs an
advice-dependent service channel.

The literature makes that channel plausible but does not close it. VSL can alter
lane-changing; lane-change gaps and relaxation can alter discharge; and recovery
can be transient. The sign is not guaranteed: one lane change can create a short
flow surge and later generate a disturbance. No source identifies the combined
state-to-service law at reopening or shows that a strong aggregate history misses
it. Selecting a favorable recovery capacity would assume the desired result.

## Gradient boundary

A fixed reopening time is not by itself fatal to differentiation. A continuous
state and smooth recovery-service law with a stable active set can be handled
piecewise across the known event time. Sending/receiving switches and exact
clearance time require directional or event-time care. Hard lane permissions,
lane assignments, accepted/rejected lane changes, leader/order switches and
queue-emptying changes are hybrid boundaries where pathwise derivatives may be
undefined or uninformative.

This classification establishes only where a later gradient review would look.
Because S11 did not establish the decision path, it does not establish a combined
or useful gradient.

## S11-UG1 / TCR-R1 — deferred G4 decision

### Problem statement

What evidence threshold should determine whether the current cross-context
mechanism is enough to admit a full temporary-closure protocol?

### Assumed model-chain function

A later protocol would need common VSL to change preparation, hidden state at the
fixed reopening to change transient service, and that service change to alter the
complete-accounting action ranking relative to a strong aggregate-history
controller.

### Core gap

The bounded review found primary support for the neighboring links in different
settings but not for their transfer into one chain. It also found no direct
strong-observer comparison. The decision is whether task admission requires
those joins to be source-supported or may treat them as hypotheses for a later
test.

### Candidate A — retain the mechanism-and-obstruction threshold

Apply the working default: do not admit a later protocol unless the critical
state-to-reopening-service path is supported without assigning a favorable
coefficient, and the strong-history information question remains defensible.
With the current record, close S11 as **TCR-E evidence inconclusive**.

**Pros:** Preserves the evidence discipline used to close the permanent-drop
review. It prevents separate VSL, lane-change and recovery findings from being
mistaken for a joint causal result. It retains negative/inconclusive evidence and
does not weaken the aggregate comparator.

**Cons:** Direct literature on this exact conjunction may be intrinsically sparse.
The branch closes before a protocol can test a physically plausible mechanism.

**Dependencies and consequences:** Option 3 ends at task admission unless new
direct evidence is supplied. The approved sequence may next consider the
lightweight analytical Candidate B because that branch openly constructs and
audits a service coupling rather than attributing it to the reopening literature.

### Candidate B — require a complete certificate during admission

Require an exact matched-history pair, a full common-action ranking distinction
and complete accounting before admission.

**Pros:** Gives the strongest protection against a speculative follow-on and
would make admission decisive.

**Cons:** It turns an admission review into the analytical or empirical study it
was meant to precede. The current evidence cannot meet it, and the original plan
identified it as disproportionate.

**Dependencies and consequences:** Close or defer Option 3 with a stronger unmet
burden. Reopening it would require a separately approved constructive or
empirical study.

### Candidate C — admit a composed cross-context hypothesis

Treat the separate evidence as enough to motivate a full protocol whose purpose
is to test the unverified joins. Label the state-to-reopening-service link and
strong-observer failure as hypotheses rather than premises.

**Pros:** Uses the strongest available evidence and allows a direct test of the
precise missing transfer. It does not falsely claim that the literature already
contains the full chain.

**Cons:** It relaxes G4-A. The later protocol begins without a source-supported
joint path and could spend substantial effort testing a mechanism that aggregate
history already captures. The service sign and useful-action distinction remain
open.

**Dependencies and consequences:** A later plan must preregister the possible
null outcomes, preserve the strong observer, forbid hand-selected favorable
recovery coefficients, freeze metric roles before outcomes and stop before a
gradient review unless a useful decision distinction is found.

**Provisional recommendation: Candidate A.** It matches the user's stated default
and the current review's evidence standard. The result is a bounded inconclusive
closure, not a claim of aggregate sufficiency or physical impossibility.

## Gate question

Select G4-A, G4-B or G4-C. Selecting A closes S11 with TCR-E and leaves the
lightweight analytical Candidate B as the next separately planned branch.
Selecting C admits a full Option 3 protocol under explicitly hypothesis-first
status. No further review, experiment or successor sprint starts automatically.

## User decision and closure

The user selected **G4-A**, accepted the partial result and failure of the core
admission question, and instructed S11 closure. TCR-E is the final S11 verdict.
Candidate C was not selected; no temporary-closure experiment or full protocol
is admitted. The user separately authorized opening the next planned analytical
branch as S12, subject to its own plan gate.
