# S12.80 — Advice–merge–service decision dialogue

Date: 2026-09-30. Status: closed dialogue; G4-A and separate S13 approved.

## User clarification request

The user found the sufficient reason for admitting M2 difficult to identify and
asked whether admission means that M2 merely survives lightweight negative
literature filters, how it relates to the review questions, and what remains
missing.

## Clarified interpretation

M2 is admitted as a **testable analytical model class**, not accepted as the
answer to the core information-to-decision question. It passes four admission
levels:

1. primary sources support conservative per-lane mandatory transfer, finite
   receiving and additional gap demand;
2. the class is compatible with the permanent lane drop and can expose its inputs
   to a common VSL through lane-wise sending/density evolution;
3. binding receiving makes service endogenous to lane state, removing the S05
   fixed-service premise without fitting a favorable coefficient; and
4. applying lane-wise receiving operations before aggregation gives a coherent
   reason that relevant state may be hidden from aggregate totals/history.

The class does **not** yet pass the decision or gradient levels. Missing work is
an exact reachable same-strong-history near-drop pair, a complete-accounting
different-useful-action result, a test against the strong aggregate capacity-
drop alternative, frozen internal equations/parameters and any gradient
correctness/usefulness evidence.

Therefore “survives negative filtering” is substantially correct, provided it
is paired with the positive structural finding: M2 contains a source-backed
finite-receiving mechanism that actually invalidates the known obstruction. It
survives as a candidate worthy of the next analytical gate, not as a confirmed
scientific conclusion or implementation target.

The expanded rationale and task mapping are now incorporated into the
[findings](s12_20_advice_merge_service_findings_and_gate.md) and
[mechanism matrix](../../synthesis/s12/s12_mechanism_admission_matrix.md).
G4 remains undecided.

## Clarification: S05 versus S12/M2

The two studies use the same permanent lane-drop motivation, common lane-uniform
VSL actuator, strong aggregate-history comparator and complete delay accounting.
They differ in the model class and in what the review is trying to establish.

| Dimension | S05 analytical construction | S12 M2 admission candidate |
|---|---|---|
| Immediate purpose | Try to build an exact information-loss/useful-action certificate and identify why it succeeds or fails. | Decide whether a source-bounded endogenous merge/service class is sufficiently defensible to deserve a full certificate attempt. |
| Preparation state | Homogeneous free-flow subcase in which conservative lateral transfers cancel after lane aggregation; hidden ending-lane mass can remain. | Lane-resolved near-drop mass, mandatory lateral demand and continuing-lane receiving competition remain dynamically active. |
| Bottleneck service | State-specific service may differ, but it is fixed with respect to the chosen advice. | Realized service is generated from advice-conditioned lane state, lateral demand, finite receiving and gap cost. |
| Role of common VSL | Changes cumulative arrival timing; a fastest action pointwise dominates arrivals. | Can change lane-wise sending/density and transfer opportunity, which can change the service sequence itself. |
| Dominance result | With advice-independent work-conserving service and complete accounting, the fastest feasible action is common best. | The advice-independent-service premise is absent, so the S05 theorem cannot be transferred; no opposite ranking has yet been proved. |
| Hidden-information result | Exact aggregate-history collision is constructed only in an early simplified branch; consequential near-drop persistence is missing. | Lane-wise receiving gives a coherent consequential variable beyond totals, but the exact same-history near-drop collision is still missing. |
| Equation status | Restricted arrival/service equations are sufficiently fixed to prove the obstruction. | Only the outer function class and invariants are admitted; lateral-demand, priority, response and parameter contracts are unfrozen. |
| Evidence method | Top-down analytical construction plus a proof of impossibility inside the restricted class. | Bottom-up primary-source mechanism screen plus conservation, actuator, aggregate-limit, obstruction and falsification audits. |
| Parameter role | No service parameter can make slower advice necessary while the fixed-service/arrival-dominance assumptions hold. | A broad source-motivated regime is retained—positive mandatory demand, binding receiving and positive extra gap cost—without choosing an outcome-favorable value. |
| Aggregate alternative | The obstruction shows that hidden state plus different fixed capacity is insufficient. | An aggregate state-dependent capacity-drop model is retained as an explicit competitor to lane-resolved M2. |
| Endpoint | Partial negative result: information can be hidden, but fixed service cannot convert it into a useful-action distinction. | Conditional positive admission: a model family can bridge that logical gap, but the exact decision result remains future work. |

The causal structures are therefore different:

- **S05:** `advice → arrival timing`, while hidden state selects an
  advice-independent service process;
- **M2:** `advice → lane-wise approach/transfer → receiving allocation →
  endogenous service`.

M2 does not replace or contradict S05. It is a direct response to S05's stopping
finding: the next viable class must make service depend jointly on advice and
lane-state evolution. S05 supplies the obstruction and information-side starting
point; M2 proposes the smallest literature-backed mechanism class that removes
the obstruction's fixed-service premise.

## Clarification: lane-uniform action and action-dependent service

The user proposed the shorthand that S05 has fixed per-lane service while M2's
per-lane VSL changes lane occupation, redistributes it laterally and thereby
changes per-lane service. The causal intuition is close, with two corrections:

1. S05 does not require a separately fixed service for each physical lane. It
   assumes that, for each hidden state, the work-conserving bottleneck service
   process is fixed **with respect to the selected advice**. Hidden states may
   have different service curves, but changing VSL changes arrivals only.
2. M2 retains one **lane-uniform** VSL; it does not introduce lane-specific speed
   controls. The common advice may indirectly change lane-wise sending, density,
   the timing/feasibility of mandatory merging and hence lane occupation. The
   resulting endogenous lateral redistribution then competes with same-lane flow
   for finite receiving space and can change realized bottleneck service.

The corrected shorthand is:

> S05: common VSL changes arrivals while service is action-independent. M2:
> common VSL may change lane-resolved approach and mandatory-transfer state, and
> finite shared receiving lets that state change endogenous service.

“May” remains essential. S12 admits this causal path as a model-class
possibility; it has not yet fixed or proved a common-VSL response law that creates
a sufficient lane-contrast change or a different useful action.

## Prospective continuation after M2 admission

The user concluded that M2 appears feasible for further exploration and asked
whether to extend S12 by amendment or open a further stage seeking stronger
answers to the core review questions.

### Problem statement

S12 has completed model-family admission. The remaining work changes the
scientific burden: it must freeze equations, construct an exact strong-history
witness and prove or refute a complete-accounting action distinction. Continuing
without a new boundary could make AMR-A look like the result it only authorizes
testing.

### Assumed model-chain function

The successor would formalize
`common lane-uniform VSL → lane-wise sending/mandatory transfer → finite
receiving allocation → endogenous service → complete delay`, while comparing
against a strong aggregate capacity-drop model.

### Core gap

M2 lacks a frozen VSL-response law, mandatory-transfer law, receiving priority,
parameter class, reachable exact same-history pair and useful-action result. More
generic literature is unlikely to close these joins by itself; the next work must
combine targeted source support with an explicit analytical contract.

### Candidate A — amend S12 and continue evidence collection

Keep S12 open and add a broader search/derivation amendment.

**Pros:** Maintains one document lineage and can seek additional sources before
committing to equations.

**Cons:** Blurs model admission with certificate construction, weakens the
meaning of the reached gate and risks another unbounded literature search. The
current source gap is mainly a missing join, not an absence of neighboring
mechanisms.

**Dependencies and consequences:** S12 scope and stop conditions would need
explicit reopening. AMR-A could not close until the larger work finished.

### Candidate B — close S12 under G4-A and open a separately gated S13

Treat AMR-A as the completed admission result. S13 first freezes a minimal
source-to-equation contract and then, only after approval, attempts the analytical
certificate or obstruction.

**Pros:** Preserves the distinction between “worthy of study” and “proved.” It
supports global-first choices for the response law, receiving priority,
parameter class, observer, accounting and aggregate countermodel. It gives clear
early stop conditions if any join cannot be defended.

**Cons:** Adds a planning gate before derivation and may still close negatively
after the model contract is specified.

**Dependencies and consequences:** Requires G4-A closure of S12, followed by an
S13 Phase-A proposal. The S13 plan should not authorize implementation,
simulation or gradients.

### Candidate C — close S12 and start a certificate derivation immediately

Select equations and attempt the exact construction without a separate contract
review.

**Pros:** Shortest route to a mathematical result.

**Cons:** The choice among priority rules, VSL response laws and parameter
classes changes scientific meaning. Direct derivation risks choosing a closure
because it yields the desired action split.

**Dependencies and consequences:** Would require explicitly waiving the planning
gate and accepting a greater risk of equation selection bias.

**Provisional recommendation: Candidate B.** S12 has answered the admission
question; S13 should test the admitted family rather than enlarge S12.

### Minimum S13 aims

1. Freeze the smallest continuous-mass M2 equations and map every adopted term to
   source evidence or an explicitly labeled new assumption.
2. Define how one lane-uniform VSL reaches lane-wise sending, mandatory transfer
   and receiving without becoming lane-specific or direct lateral control.
3. Construct or rule out a reachable pair with identical declared strong
   aggregate history at the consequential near-drop state.
4. Include the fastest feasible action and complete all-cohort accounting; prove
   a different useful-action result or a typed obstruction.
5. Test whether an aggregate state-dependent capacity model reproduces the same
   ranking before attributing value to hidden lane state.
6. Stop before gradient analysis unless the decision distinction is established.

S13 should close early if the action-to-lane join requires unsupported behavior,
the strong observer determines the M2 state, complete accounting restores one
common best action, or an aggregate countermodel reproduces the result.

## User decision

The user selected the recommended boundary: **G4-A closes S12 with AMR-A**, and
a targeted S13 is inserted before ramp-metering review. S13 is opened only for
planning and must stop at its next discussion/approval gate.
