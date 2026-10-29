# S11.00 — Temporary-closure recovery task-admission review proposal

Date: 2026-09-30. Status: **Closed; G4-A approved and TCR-E accepted.**
Parent: [S10 closure](reporting/s10/s10_99_vsl_methodology_review_closure.md)
and [approved successor ordering](synthesis/s10/s10_post_closure_next_step_plan.md).

## Decision and scope of this proposal

S10 closed the permanent-lane-drop methodology review. Feedback 25 selected
temporary lane-closure recovery as the first planned successor. S11 is a new,
methodology-only **task-admission review**: it asks whether reopening supplies a
defensible physical path from hidden near-zone state to a different useful
lane-uniform speed-advice decision. It does not assume that path exists.

Approval of this proposal would authorize documentary review and bounded
analytical auditing through S11-UG1 / TCR-R1. It would not authorize a simulator,
SUMO or other traffic execution, calibration, controller construction, numerical
experiment, differentiable model, gradient calculation or full experimental
protocol.

## Opening approval record

On 2026-09-30 the user approved G1-A, G2-A and the revised G3-A and authorized
S11 execution through the next user gate. G4-A was retained as the working
default, while final selection of the evidence standard was explicitly deferred
to the end of S11. The review therefore applies G4-A provisionally and returns
G4 with the completed evidence audit at S11-UG1 / TCR-R1.

## Scientific purpose

The permanent-drop review found that hidden lane information plus fixed,
advice-independent service is insufficient: if advice only changes arrival time,
the fastest feasible advice can remain a common best action. A fixed exogenous
reopening introduces a time-varying recovery phase without changing the VSL
actuator. S11 will determine whether that phase offers a source-grounded mechanism
that escapes the obstruction, or merely adds recovery accounting already handled
by strong aggregate models.

The admission question is:

> Can a fixed, exogenous lane reopening create a source-supported path from
> hidden near-zone lane/gap/order configuration to recovery discharge and a
> different useful upstream VSL decision under the same declared strong
> aggregate history?

## Verified starting point

The following are inputs, not claims to rediscover:

1. **Recovery is operationally material.** The archived FB0006 incident report
   separates effects during a blockage from effects after clearance. FHWA also
   treats the period from reopening to ordinary flow as incident recovery.
2. **Aggregate recovery control and sensitivity already exist.** FB0021 uses an
   aggregate kinematic-wave model for an exogenous temporary bottleneck, restores
   capacity when the event ends, includes delay through complete queue clearance
   and derives analytical parameter sensitivities. Recovery-tail accounting,
   reopening and speed sensitivity are therefore not standalone novelty.
3. **The strong aggregate alternative remains mandatory.** Aggregate models can
   represent queue size, waves, capacity restoration, speed response, cumulative
   counts and complete recovery history. S11 may not use a memoryless or
   incident-unaware comparator.
4. **The S05 obstruction remains a check.** If post-reopening service is fixed
   and hidden state only changes arrival timing, the proposed decision distinction
   has not escaped arrival dominance.
5. **Lane/gap/order effects are mechanism candidates only.** S06 establishes
   urgency, safety-gap and lane-redistribution precedents, without proving a
   beneficial sign, a minimum state or advice-dependent recovery service.
6. **Gradient claims remain downstream.** A hybrid reopening event can create
   event-sensitive or nonsmooth responses. Forward relevance, decision relevance,
   internal derivative correctness and independent gradient usefulness remain
   separate claims.

## Fixed boundaries

- The control remains a fixed-zone, lane-uniform infrastructure speed advice;
  no lane-specific limit, lane-change command, ramp meter or vehicle trajectory
  control is admitted.
- Closure and reopening time, location and usable-lane count are exogenous and
  identical across compared states and actions.
- Demand, route population and known future inputs are shared. No action may
  receive credit by delaying uncounted traffic beyond the horizon.
- The comparator receives the declared strong spatial aggregate state and its
  full predecision history. Approximate matching or a deliberately weak observer
  is not introduced in this admission review.
- Hidden state initially means the unresolved lane/gap/order/leader/lane-change-
  memory bundle. Lane occupancy alone is not presumed sufficient.
- Conservation, complete source/approach/recovery accounting and the distinction
  among forward, decision and gradient evidence are retained from S10.

## Explicit non-goals

S11 will not choose numerical geometry, demand, event duration, advice values or
acceptance tolerances for an experiment. It will not reproduce FB0021, claim
recovery as new, prove an exact native history collision, select a minimum
mesoscopic state, derive a complete gradient, or evaluate field effectiveness.
It will not turn reopening time or lane availability into a control variable.

## Global question inventory

All four questions are Type 2 because each changes the task, observer, decision
contract or interpretation of a later gradient. Source-extraction details are
local review work and may not silently alter these contracts. Discussion order is
TCR-G1 → G2 → G3 → G4.

### TCR-G1 — What temporary-closure domain is being admitted?

**Problem statement:** A temporary lane closure can mean a removable obstruction
on an otherwise unchanged road, a temporary restriction layered onto a permanent
drop, or a detailed work-zone taper. These do not share the same service and
recovery mechanism.

**Assumed model-chain function:** The event creates a bounded restriction, then
restores lane availability at a fixed time. Pre-reopening advice affects arrivals
and preparation; the state present at reopening may affect subsequent discharge.

**Core gap:** The approved ordering names temporary recovery but does not freeze
the physical domain. Combining a permanent drop with a temporary event creates
two bottlenecks; adopting a taper adds geometry and lane-changing assumptions not
needed for the first admission test.

**Candidate A — removable one-lane obstruction on an otherwise three-lane
homogeneous freeway (provisional recommendation).** During the fixed event, one
lane is unavailable over a bounded bottleneck region; at reopening, the original
three-lane availability returns. Preserve the current upstream common-advice
meaning and treat warning/taper details as later reference-model obligations.

**Pros:** Isolates recovery, provides a real capacity transition and avoids
stacking it on the permanent drop. It is closest to the incident-recovery sources
and leaves lane/gap/order state meaningful at reopening.

**Cons:** Synthetic geometry omits work-zone taper details and field operations.
Restored nominal capacity can make aggregate queue mass dominate the recovery
unless a defensible transient state-to-service mechanism exists.

**Dependencies/consequences:** This is a new scenario, not an amendment to the
closed permanent-drop result. Event schedule and nominal before/during/after
capacity must be common inputs; state-dependent transient discharge cannot be
assumed.

**Candidate B — temporary obstruction upstream of the permanent three-to-two
drop.** Retain the prior permanent narrowing and add a time-limited restriction.

**Pros:** Reuses the old geometry and can study interaction between recovery and
the downstream lane drop.

**Cons:** Two bottlenecks confound recovery, hidden state and advice effects. A
positive result would be harder to attribute and the aggregate comparator would
need a more complex coupled calibration.

**Dependencies/consequences:** Requires a new two-bottleneck information and
accounting contract. It is not a small continuation of S10.

**Candidate C — explicit work-zone taper and reopening operation.** Model the
physical taper, warning region and reopening procedure as the task domain.

**Pros:** Strongest operational interpretation and direct relation to work-zone
practice.

**Cons:** Geometry, compliance, taper behavior and reopening operations can
dominate the state-resolution question. It is too broad for first admission
unless the simple obstruction is shown scientifically inadequate.

**Dependencies/consequences:** Requires additional operational sources and later
calibration; likely a separate domain review.

### TCR-G2 — What information claim is retained?

**Problem statement:** Should S11 retain the exact strong-history information-
loss target, or lower the claim to performance under one approximate observer?

**Assumed model-chain function:** The controller observes the same declared
spatial aggregate history for compared preparations before selecting common
advice. Hidden reopening state can matter only if the comparator cannot already
recover the relevant distinction.

**Core gap:** Reopening may amplify lane/gap/order differences, but pre-reopening
queues and speeds may also reveal them. Recovery relevance alone does not
establish lost aggregate information.

**Candidate A — retain the exact strong-history target, but audit only its
plausibility at admission (provisional recommendation).** Require any later
positive claim to preserve the S10 observer boundary. During S11, determine
whether sources and causal structure leave a coherent possibility; do not claim
or numerically search for an exact pair.

**Pros:** Preserves the accepted intrinsic-information question and prevents
recovery from winning against a weak observer. Keeps a future result comparable
to the closed VSL review.

**Cons:** The admission result remains conditional; an exact reachable pair may
later fail. Strong history may encode much of the reopening state.

**Dependencies/consequences:** A future empirical protocol would still need an
outcome-blind exact-match construction. Failure at admission does not prove
aggregate sufficiency.

**Candidate B — change to a bounded approximate-observer value claim.** Specify a
strong observer family and ask whether compact lane-aware input improves recovery
decisions within a declared error envelope.

**Pros:** More practical if exact histories are rarely equal and can quantify
incremental sensor value.

**Cons:** Changes the research claim to model/observer adequacy and introduces
fitting, residual and fairness contracts. It can manufacture value through a poor
observer.

**Dependencies/consequences:** Would reopen the information claim and should be a
separate successor, not a fallback inside S11.

### TCR-G3 — Which metric candidates can support a useful recovery decision?

**Problem statement:** Clearance time, post-reopening throughput and total delay
can rank advice differently. A short recovery metric can reward moving queues or
unserved demand outside the score.

**Assumed model-chain function:** Common advice changes arrivals and preparation.
Candidate metrics expose different consequences of that chain: total system
time/delay covers the affected cohort, clearance time covers recovery duration,
transient discharge/throughput covers service dynamics, and residual queues
check incomplete accounting. Whatever role each metric ultimately receives, the
evaluator must count the entire affected population until clearance or apply a
complete terminal residual.

**Core gap:** Existing sources establish recovery-tail importance but do not yet
show which metric is decision-grade for this particular hidden-state/VSL chain.
Fixing a primary metric before the evidence audit would be premature; leaving the
set unbounded would permit outcome-driven metric selection.

**Candidate A — review a declared metric set under a fixed complete-accounting
guardrail (provisional recommendation).** Audit total system time/delay, clearance
time, transient discharge/throughput and residual queue or terminal cost. For
each, record its operational meaning, source support, susceptibility to horizon
or queue-shifting artifacts, and whether it can support a useful-decision claim
or only diagnose the mechanism. The S11 findings will recommend primary,
secondary and guardrail roles at TCR-R1. A later full protocol must freeze those
roles before observing experimental outcomes and must compare the full common
action set rather than only seek a two-action reversal.

**Pros:** Lets the documentary evidence determine which measures are suitable,
while preserving complete accounting and making recovery mechanisms inspectable.
It avoids prematurely treating one metric as decision-grade.

**Cons:** S11 cannot make a final useful-decision claim until the metric roles are
selected. The audit must resist adding measures merely because they yield a
favorable result.

**Dependencies/consequences:** New materially distinct metrics found in sources
must be added to the inventory with their rationale and failure modes. Advice
menu, numerical horizon and tolerances remain for a later protocol. Any later
decision claim must use identical event/demand inputs and complete accounting.

**Candidate B — preselect all-cohort total system time as primary, with recovery
decomposition.** Include source waiting, approach time, event-period delay,
post-reopening delay and residual queues; retain clearance and discharge as
diagnostics.

**Pros:** Preserves comparability with S10, has a clear welfare interpretation
and strongly limits horizon gaming or queue shifting.

**Cons:** It fixes a primary target before S11 establishes how the cited recovery
literature measures operational relevance. A long horizon can dilute a localized
recovery effect.

**Dependencies/consequences:** Numerical clearance and residual rules remain for
a later protocol.

**Candidate C — preselect clearance time or post-reopening throughput as
primary.** Center the decision claim on the recovery phase, with broader costs as
secondary checks.

**Pros:** Sensitive to reopening dynamics and operationally intuitive when rapid
restoration is the stated agency goal.

**Cons:** Can reward shifting queues or delay outside the scored region or time.
Without complete-accounting guardrails it cannot support the project's useful-
control claim.

**Dependencies/consequences:** It is admissible only if sources justify the
operational target and the full-cohort accounting reports any displaced cost.

### TCR-G4 — What evidence is sufficient to admit a later full review?

**Problem statement:** Requiring a complete matched pair and useful gradient now
would turn task admission into an experiment; accepting recovery relevance alone
would repeat established aggregate prior art.

**Assumed model-chain function:** Admission must identify a conservative,
source-supported path from pre-reopening advice and hidden state to transient
recovery service, then show why a strong aggregate history does not trivially
close that path. It also classifies the later derivative boundary.

**Core gap:** No reviewed work currently supplies the joint path. A mechanism can
be physically plausible yet circular if a favorable state-dependent discharge
term is simply assumed.

**Candidate A — mechanism-and-obstruction admission screen (working default;
final selection deferred to S11-UG1).** Admit a later protocol only if the review finds at least one
primary-source-supported transient state-to-discharge mechanism, traces a
non-circular common-advice path, survives the S05 fixed-service check, and leaves
a coherent strong-history information question. Classify smooth, fixed-active-
set, event-sensitive and discontinuous derivative regimes without constructing a
gradient.

**Pros:** Strong enough to exclude recovery-only novelty and invented favorable
dynamics; attainable within methodology-only scope. Negative and inconclusive
results remain useful.

**Cons:** A passing result is still conditional and does not prove an exact pair,
action distinction, minimum state or gradient usefulness.

**Dependencies/consequences:** A pass returns to a user gate before a full
protocol. Failure closes Option 3 with a typed reason and informs whether the
analytical fallback remains meaningful.

**Candidate B — require a complete information-to-decision certificate during
S11.** Do not admit the task without a proved or observed matched pair and action
distinction.

**Pros:** Prevents a weakly motivated follow-on and would give decisive evidence.

**Cons:** Exceeds task-admission scope, likely requires a new model or empirical
reference, and collapses several gated claims into one review.

**Dependencies/consequences:** Would require explicit authorization for a much
larger analytical or empirical study.

**Candidate C — admit a hypothesis from a composed cross-context mechanism.**
Permit separate sources to establish that VSL can alter preparation, lane/gap
state can alter discharge, and post-reopening recovery is transient, even if no
source or matched analysis establishes the joint chain in the S11 domain.

**Pros:** Uses the strongest available evidence without demanding a complete
certificate at task admission. It can motivate a later protocol that directly
tests the missing transfer.

**Cons:** The transfer across work-zone VSL, active-bottleneck lane-change and
post-incident recovery contexts is itself the critical uncertainty. Admission
would mean “plausible hypothesis worth testing,” not a source-supported path, and
could import a favorable service effect that the S05 obstruction warns against.

**Dependencies/consequences:** A later protocol would need to label the
state-to-reopening-service link and strong-observer failure as hypotheses, not
established premises. Choosing C changes the original G4-A admission threshold.

## Bounded review method

1. Reconstruct the event, actuator, observer, accounting and obstruction
   contracts from S01–S10. Reuse FB0006, FB0011, FB0021 and the S06 mechanism
   sources before new discovery.
2. Conduct a bounded primary-source search only for missing links: temporary
   mainline lane closure plus VSL; lane/gap/order effects on discharge immediately
   after reopening; transient capacity recovery; and derivative treatment of a
   fixed exogenous reopening event. Log queries, access and evidence limits.
3. Build a claim/source matrix separating operational recovery, aggregate
   recovery capability, hidden-state mechanism, advice coupling, observer
   recoverability, decision relevance and gradient status. Add a metric-role
   table for total delay/system time, clearance, transient discharge/throughput
   and residual queues, plus any materially distinct source-supported candidate.
4. Trace the causal chain
   `common advice → arrivals/preparation → hidden state at reopening → transient
   receiving/service → candidate recovery and all-cohort outcomes`. At every
   link, state whether support is direct source evidence, a conditional deduction
   or absent.
5. Reapply the S05 obstruction with the same aggregate queue, event schedule and
   known inputs. Do not escape it by assigning a favorable capacity to the hidden
   state. Identify the smallest additional physical premise, if any, supported by
   sources.
6. Audit whether the strong aggregate history can observe or reconstruct the
   proposed mechanism. Preserve unknown-input qualifications and do not relax to
   approximate matching.
7. Classify derivative regimes around fixed reopening and state-dependent
   discharge. This is a feasibility map, not a derivation or usefulness result.
8. Produce S11 findings and stop at S11-UG1 / TCR-R1.

## Admission criteria and verdicts

Option 3 is **admitted for a later full protocol** only if all of the following
hold:

1. the temporary-closure domain and same VSL actuator are supported without
   importing direct lane or vehicle control;
2. at least one primary source supports a conservative transient link between
   reopening lane/gap/order state and realized receiving or discharge;
3. common advice can affect that state through a source-supported path rather
   than a chosen favorable coefficient;
4. the mechanism is not already exhausted by aggregate queue, restored capacity
   and full history under the declared observer;
5. at least one source-relevant metric can support a decision claim while the
   complete-accounting guardrail exposes any displaced cost; and
6. the derivative boundary can be classified without claiming that a useful
   gradient already exists.

The findings must assign one verdict:

- **TCR-A — admit:** the complete admission criteria pass; return for approval of
  a full information/decision protocol.
- **TCR-B — forward-recovery only:** a hidden state can affect recovery, but no
  supported useful-advice distinction is available; do not proceed to a gradient
  review.
- **TCR-C — aggregate closure:** supported recovery effects are represented by a
  strong aggregate history/state for the admitted domain.
- **TCR-D — mechanism obstruction:** no non-circular source-supported mechanism
  escapes fixed-service arrival dominance.
- **TCR-E — evidence inconclusive:** the key source or observer implication
  remains unresolved; state the smallest missing evidence and whether the
  analytical fallback is still meaningful.
- **TCR-F — gradient-boundary warning:** decision relevance is supported but the
  derivative is event-sensitive or unsuitable; preserve the positive decision
  result and route the next review to hybrid/nonsmooth sensitivity or a
  non-gradient controller rather than automatic fallback.

## Outputs

If approved, S11 will produce:

- `extraction/s11_temporary_closure_recovery_source_audit.md`;
- `synthesis/s11/s11_temporary_closure_recovery_admission_matrix.md`;
- search/access logs only if new discovery is performed;
- `reporting/s11/s11_20_temporary_closure_recovery_admission_findings_and_gate.md`;
- `reporting/s11/s11_90_temporary_closure_recovery_work_report.md`; and
- synchronized sequence, registry and decision records.

A formula-heavy conditional argument, if required by the evidence, will be
retained as LaTeX source and PDF under `synthesis/s11/`. No empty role files or
implementation artifacts will be created.

## Stop conditions

Stop before findings only for a decision-critical inaccessible source, an event-
domain ambiguity that changes the scientific interpretation, or evidence that
the route requires a different actuator or controlled reopening time. At the
ordinary endpoint, stop at S11-UG1 / TCR-R1 regardless of verdict. Do not draft a
full experiment, begin the analytical fallback, reopen ramp metering or start
S12 automatically.

## S11-PG1 — Opening decision record

The provisional recommendation is the complete Candidate A set:

- G1-A: removable one-lane obstruction on an otherwise three-lane freeway;
- G2-A: retain the exact strong-history target at admission;
- G3-A: review the declared metric set under a complete-accounting guardrail and
  recommend metric roles at TCR-R1; and
- G4-A: mechanism-and-obstruction admission screen.

This approval froze the bounded methodology-only review through S11-UG1. Revisions
to the event domain, information claim, metric-selection rule or admission
standard require explicit reopening of the smallest affected TCR global decision.

**Opening gate closed:** S11 execution was authorized. The completed review now
stops at S11-UG1 / TCR-R1, where G4 returns for its deferred decision.

## Closure record

The user approved G4-A after reviewing the completed matrix and accepted the
partial result and failure of the core admission question as sufficient closure.
S11 therefore closes with **TCR-E: evidence inconclusive**. No full temporary-
closure protocol is admitted. This result does not establish aggregate
sufficiency or physical impossibility and does not invalidate the separately
planned analytical advice–merge–service branch.
