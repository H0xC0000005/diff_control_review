# S12.20 — Advice–merge–service findings and user gate

Date: 2026-09-30. Status: **Closed; G4-A approved and AMR-A accepted.**
Parent: [approved S12 plan](../../s12_00_analytical_advice_merge_service_admission_review.md).
Evidence: [source audit](../../extraction/s12_advice_merge_service_source_audit.md)
and [mechanism matrix](../../synthesis/s12/s12_mechanism_admission_matrix.md).

## Decision summary

The bounded screen found one analytical family that can pass the intended
lightweight threshold:

> conservative per-lane first-order flow with endogenous mandatory lateral
> demand, finite target-lane receiving shared by longitudinal and lateral
> entrants, and a nonnegative extra gap/spacing cost for lane changes.

This family is compatible with a permanent three-to-two lane drop and continuous
traffic mass. It breaks the S05 fixed-service premise without selecting one
favorable coefficient: whenever mandatory ending-lane demand is positive and
target receiving binds, lane state changes the feasible allocation and hence
realized service. Common VSL can affect the time-varying lane-wise sending,
receiving and transfer opportunity.

Under working-default G4-A the provisional verdict is:

> **AMR-A — admit this family for a later, separately approved analytical
> model-contract and derivation plan.**

This is a model-class result. S12 has not proved an exact matched-history pair,
a different best action, the necessity of lane contrast, a full gradient chain
or empirical validity.

## What “admit M2” means

Admission is permission to formulate and test one analytical model class in a
later review. It is not acceptance of M2 as true, necessary, calibrated or
sufficient to answer the project-wide research question.

The distinction is:

1. **Model-family legitimacy:** Are the state, flows and service interaction
   recognizable traffic mechanisms with primary-source support? M2 passes.
2. **Obstruction escape:** Does the family remove a premise that made the fastest
   action universally optimal in S05, without assigning an outcome-favorable
   coefficient? M2 passes structurally.
3. **Information-to-decision result:** Can two reachable cases with exactly the
   same strong aggregate history require different useful common VSL actions
   under complete accounting? M2 has not established this.
4. **Gradient result:** Does the retained state provide a correct and useful
   derivative path? M2 has not established this.

Thus, “AMR-A” means that further analytical work is methodologically warranted.
It does not mean that the core result is likely, or that a mesoscopic simulator
should be implemented.

## M2 task formulation at the admitted level

The later analytical task would use the following fixed outer contract:

- **geometry:** a permanent three-to-two lane drop;
- **action:** one upstream time-varying speed advice applied uniformly to all
  lanes;
- **continuous state:** per-lane traffic mass/density and the mass that must
  leave the ending lane;
- **structural metadata:** lane existence and the mandatory ending-lane
  permission, held fixed rather than differentiated;
- **transition:** longitudinal sending plus paired conservative lateral transfer
  from the ending lane to a continuing lane;
- **service mechanism:** same-lane and lane-changing traffic compete for finite
  target-lane receiving space, with lane changes permitted to require more space
  than ordinary following;
- **observer:** total density, flow, speed, cumulative counts and their full
  predecision spatial history, without lane decomposition;
- **decision score:** complete affected-cohort time/delay through common
  clearance, including source/approach waiting; and
- **comparison claim:** determine whether equal-observer preparations can produce
  different useful actions, while retaining a strong aggregate capacity-drop
  alternative.

S12 does not freeze the exact lane-change demand law, receiving priority rule,
VSL response law or parameter interval. Those are the first decisions of the
possible successor model-contract review.

## The sufficient reason for admission

### 1. The mechanism is directly represented in conservative traffic models

Carey, Balijepalli and Watling model per-lane CTM conservation, mandatory
lane-changing demand and competition for target-lane receiving capacity. Their
gap-acceptance factor makes lane-changing traffic consume additional receiving
space. FB0030 independently provides paired conservative lateral transfers and a
lane-drop application. These sources support the mechanism's traffic meaning,
not merely a verbal conjecture.

### 2. The service channel is endogenous rather than attached afterward

In the source family, same-lane inflow and lateral inflow share one finite
receiving constraint. Semantically, the constraint has the form
`same-lane flow + gap factor × lateral flow ≤ target-lane receiving`.
When mandatory lateral demand is positive and receiving binds, changing the lane
allocation or transfer demand changes which flows can be realized. Downstream
service is therefore produced by the evolving lane state; it is not a fixed
capacity selected from the hidden-state label.

This is the precise premise change relative to S05. S05's fastest-action result
requires one advice-independent service process. M2 does not have that service
process once common advice changes lane-wise approach state and transfer
opportunity. The proof of universal fastest-action dominance therefore cannot be
carried over unchanged.

### 3. The escape is structural, not selected by fitting a favorable result

M2 needs an ordinary operating regime—positive mandatory ending-lane demand and
binding finite receiving—and a sign restriction that lane changing consumes no
less space than ordinary following. It does not require a particular fitted
value, a selected best action or a prescribed capacity benefit. Within that
regime, lane composition enters the feasible-flow constraint for every admissible
positive gap cost.

The effect may still be too small, have the wrong sign or leave all states with
the same best action. Those are accepted future null results. Admission relies
only on removal of the fixed-service theorem, not on assuming a benefit.

### 4. The hidden-state argument is coherent but intentionally incomplete

M2 applies lane-wise receiving and priority operations before lane aggregation.
Those operations generally cannot be reconstructed from a contemporaneous total:
the same total mass can place different amounts in the ending and continuing
lanes, creating different lateral demand and receiving competition. S05 already
shows that lane allocation can be hidden during an early homogeneous
preparation.

What is not known is whether two such preparations remain reachable with the
same **entire** strong spatial aggregate history when M2's near-drop interactions
are active. That exact joining construction is the main missing proof, not an
assumption made by S12.

### 5. Common VSL compatibility is supported but not closed

The common-VSL lane-drop study and FB0039 show that a common speed restriction can
be associated with changed lane preparation or lane-changing activity. In M2,
VSL can enter the lane-wise sending/density evolution that determines lateral
demand and receiving competition. This supplies a non-circular candidate path
from action to service.

The literature does not provide one validated common-VSL response law joined to
M2's finite-receiving equations. The successor review must specify this join and
may conclude that common lane-uniform advice cannot move it enough to matter.

### 6. The class has an aggregate limit and explicit failure tests

M2 reduces toward an ordinary aggregate first-order model when mandatory
transfer vanishes, receiving does not bind or lanes are effectively homogeneous.
It must be rejected for the hidden-information claim if:

- common VSL cannot affect its lane/transfer inputs;
- the strong aggregate history determines every consequential input;
- complete accounting restores a common best action; or
- an aggregate state-dependent-capacity model reproduces the action ranking.

These failure routes prevent admission from becoming an unfalsifiable assertion
that lane detail must matter.

## M2 status against the research questions

| Research question or product | M2 status after S12 | Missing result |
|---|---|---|
| What hidden information could matter? | **Candidate identified:** lane allocation, mandatory lateral demand and lane-specific receiving competition. | A reachable exact strong-history collision in the consequential near-drop regime. |
| Can hidden information alter controller results? | **Mechanism possible:** hidden lane state can alter endogenous service, so S05 no longer rules out an action split. | A complete-accounting example with different useful common VSL actions. |
| Is lane contrast necessary? | **Open.** M2 shows a lane-sensitive family, while aggregate capacity drop remains viable. | Demonstrate that the strong aggregate countermodel cannot reproduce the relevant ranking. |
| Is the task formulated? | **Outer contract formed; internal equations unfrozen.** | Lane-change demand, receiving priority, VSL response, parameter bounds and exact witness construction. |
| Is there a gradient path? | **Only a candidate path:** advice → lane-wise flow/transfer → receiving/service → total delay. | Exact component derivatives, active-set treatment, finite-difference correctness and downstream usefulness. |
| Should M2 be implemented? | **No implementation admission.** | Successful analytical contract and evidence at later gates. |

It is therefore fair to say that M2 survives the lightweight negative filters,
with one qualification: S12 also provides a positive structural reason—finite
lane-wise receiving competition—to believe the model class can escape the known
obstruction. It survives as a **testable candidate**, not as an answered core
research question.

## Results against G1–G3

### G1-A — permanent three-to-two lane drop

**Passed as the analytical domain.** FB0030 and the lane-drop VSL study directly
support conservative lane-resolved modeling and common VSL in this geometry.
The analytical family needs no temporary event or on-ramp actuator.

### G2-A — bounded mechanism portfolio

The common screen separated five mechanism families:

- particle/gap relaxation is physically strong but would require a substantive
  continuous-mass adaptation;
- conservative mandatory transfer with finite receiving/gap cost is admissible;
- optimized lateral-flow control has an actuator mismatch;
- perceived-density capacity drop may collapse to an augmented aggregate state;
  and
- aggregate capacity-drop/hysteresis is a strong aggregate countercandidate.

Only the conservative finite-receiving family passes all lightweight structural
tests. This avoids choosing among equations because of a desired outcome.

### G3-A — exact strong-history target

**Coherent at admission; still unproved as a certificate.** Lane-wise receiving
and mandatory-transfer operations occur before aggregation, so total density,
flow and counts do not algebraically determine them. The literature also shows
that single-lane surrogates can miss aggregate outflow/travel-time behavior when
systematic lane changing is material.

S05 supplies an information collision in an early homogeneous subcase. A later
derivation must join that collision to the near-drop receiving regime while
preserving the entire declared aggregate history. S12 does not silently promote
the coherent separation argument into that missing exact witness.

## What has and has not been established

| Claim | S12 status |
|---|---|
| A conservative lane-resolved function class exists | Established for model admission. |
| The class can make service depend on action-conditioned lane state | Structurally established. |
| The S05 fixed-service dominance proof applies unchanged | Rejected for the admitted class. |
| Aggregate state-dependent capacity is a viable competitor | Established. |
| Exact same-strong-history near-drop preparations exist | Not established. |
| The preparations select different useful common VSL actions | Not established. |
| Lane contrast is necessary relative to every aggregate closure | Not established. |
| A correct/useful combined gradient exists | Not reviewed or established. |

## S12-UG1 / AMR-R1 — deferred G4 decision

### Problem statement

What evidence threshold should turn the completed structural screen into S12's
final verdict?

### Assumed model-chain function

A later task would freeze equations for common VSL to change lane-wise approach
and mandatory transfer, for finite receiving/gap cost to change service, and for
that service to affect complete-accounting action ranking. It would construct an
exact strong-history witness and audit the aggregate countermodel.

### Core gap

The sources and structural audit support the function class and show why the S05
fixed-service theorem no longer applies. They do not supply the exact reachable
matched-history witness or useful-action split. The decision is whether those
belong in the next full analytical study or must already be proved at admission.

### Candidate A — retain the source-bounded structural threshold

Require the source-bounded inputs/outputs, conservation, aggregate limit,
falsification conditions and coefficient-independent escape completed by S12.
On this standard, close S12 as **AMR-A** and permit a separately planned full
analytical contract.

**Pros:** Matches the agreed lightweight role. It admits one narrow family only
after conservation, actuator, aggregate-equivalence and obstruction checks. The
later study still has explicit null outcomes and cannot assume the desired split.

**Cons:** The admitted class is assembled from compatible evidence across
sources; no source demonstrates the complete common-VSL information chain.
Substantial analytical work may still end with no exact witness or useful action.

**Dependencies and consequences:** The next task must freeze equations and prove
or refute the exact strong-history and action-ranking claims before any gradient
work. S12 admission itself authorizes none of that work.

### Candidate B — require the full certificate now

Require the exact reachable matched-history pair, complete action ranking and
accounting proof as the S12 pass condition. The present record then does not pass;
S12 closes without admission.

**Pros:** Prevents a follow-on model contract unless the central result is already
known to hold.

**Cons:** Collapses model admission and the full derivation into one gate. It
would reject the branch for work intentionally assigned to the successor study,
rather than for a defect in the identified mechanism family.

**Dependencies and consequences:** Candidate B closes S12 without opening a full
analytical plan. The approved freeway sequence may then consider ramp-metering
task admission, but only after a separate user instruction.

### Candidate C — admit any plausible source-supported mechanism

Accept lane-change disturbance, relaxation or capacity-drop plausibility without
the structural tests.

**Pros:** Keeps the broadest range of future mechanism choices open.

**Cons:** Repeats evidence already available before S12 and does not protect the
review from actuator transfer, aggregate equivalence or favorable parameter
selection. It provides no stable basis for equations.

**Dependencies and consequences:** Multiple incompatible families would remain
open, forcing the next plan to redo S12's selection. This standard weakens the
current evidence discipline.

**Provisional recommendation: Candidate A.** It answers the intended admission
question while preserving the exact witness and useful-action distinction as
claims to prove, not assumptions.

## Gate question

Select **G4-A**, **G4-B** or **G4-C**. Selecting A closes S12 with AMR-A and makes
a full analytical model-contract plan the next *eligible* action. Selecting B
closes the analytical branch at admission. No successor task starts
automatically.

## User decision and closure

The user approved **G4-A**, accepted M2 as feasible for targeted further review
and closed S12 with **AMR-A**. Candidate B's full-certificate burden was not
adopted as the admission threshold, and Candidate C's plausibility-only standard
was not adopted.

The user inserted a separately gated S13 targeted M2 analytical-contract and
certificate review before the planned ramp-metering review. This closure does
not approve S13 equations or derivation; S13 stops first at its plan gate.
