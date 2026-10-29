# A+B findings and S3-G2-Q-T transient-comparison gate

Date: 2026-10-07. **A+B qualification completed; T1 subsequently approved.**
This report records the evidence and candidates at that decision. The user
selects compact-memory qualification while preserving the inactive criterion;
T2 remains unselected. The [current plain-language findings](event_memory_findings_and_gate.md)
record the completed bounded T1 pass and approved M1 expansion. The
[current grouped-state findings](grouped_recovery_findings_and_gate.md)
reached Q-G, now closed as G1 with exact retention first and no cost/compression
criterion. The performed [exact-state pass reaches Q-E](exact_information_findings_and_gate.md),
the insertion/reset proposal, now closed as E1. The
[sampled-insertion findings](sampled_insertion_findings.md) qualify its reset and
prescribed-path route; full joined feedback remains partial. E2 is unselected
and approximation unopened.
The prior concurrent reduced-comparison obligation is deferred. Stage 3 stays
open; Stage 4 and experiments remain unopened.

Read [A qualification](../../../synthesis/rm12/bp_r_stage3/compact_a_mean_service_qualification.md),
[B qualification](../../../synthesis/rm12/bp_r_stage3/compact_b_capacity_drop_qualification.md),
[primary audit](../../../extraction/rm12/bp_r_stage3/dual_qualification_source_audit.md)
and [analytical companion](../../../synthesis/rm12/bp_r_stage3/dual_qualification_math.pdf).

## The result in traffic terms

A's mean calculation is mathematically viable in a local renewal subcase. Its
service bounds, zero-entry/free-speed limits and scalar priority coupling are
supported under explicit assumptions. B is independently dynamic and has a
fixed service ceiling while its drop trigger/receiving stay fixed and demand
is sufficient. Changes in sharing alone do not prove a complete-TST benefit.

But **showing that the average merging penalty disappears as the entry rate
approaches zero does not show that the model applies the penalty at the right
times during startup and recovery**.
During a descriptor-free startup bin, traffic can have permission and actual
entry without yet crossing the source's first descriptor threshold. B can
apply its drop immediately. A's newly derived present-entry mean can also
predict a loss for slow entrants before that first event. Neither local result
proves necessary identity or a complete reachable control trajectory. This is
an onset/averaging difference that must not be attributed solely to omitted state.

### Plain-language clarification — 2026-10-07

The **mean model** estimates service using the present insertion rate and speed,
as if those local conditions persisted. Its queues can still evolve. Its
**zero-entry limit** is a stationary formula check: vanishing insertion rate
recovers ordinary service capacity. It does not establish that old restrictions
disappear immediately when new entries stop.

The **sampled reference** here is the selected finer model, whose moving
disturbance descriptors are born at sampled updates when actual cumulative
transferred mass crosses declared thresholds. Sampling does not mean random
sampling or rounding traffic mass. A **moving restriction** represents a slow
entrant that currently limits following service while accelerating; the descriptor
adds no traffic mass. No binding moving restriction does not mean an empty road
or absence of ordinary congestion/receiving limits.

| Situation | What the distinction means |
|---|---|
| Settled absence of entries and old restrictions | Ordinary service is the expected limit; the local mean passes this weak check. |
| Entry has begun, but the first descriptor threshold has not been reached | The selected reference has no moving restriction yet, while the present-entry mean can already apply a penalty. This is the conditional local startup result. |
| New entry stops while an old slow entrant remains | Zero new entry need not mean recovered service. This illustrates the possible memory issue; a complete recovery trajectory has not been proved. |

The current stronger safeguard asks for no additional merge penalty when the
reference has no binding restriction, under matched ordinary traffic conditions.
It does not require full-model equality in every state. This is a comparison
contract, not empirical proof that the reference's sampling convention is exact
physics. Without separating activation/averaging error from retained-state error,
a finer-model advantage would not establish that retaining more information
caused the advantage. This clarification changed no contract; the subsequent
explicit user selection closes Q-T as T1.

### Scope of the hypothesis: traffic model, controller and transitions

The research hypothesis is that some physically supported merge configurations
need additional retained disturbance information to predict the effect of a rate
change on complete all-stream system time. Being far from an average is not
enough: that difference must change the relevant intervention response and
survive comparison with strong compact models, including independently evolved
spatial queues and appropriate memory/moments. If a small aggregate summary is
sufficient, that is a valid scientific outcome.

PID is a feedback controller, not a traffic aggregation model. It uses measured
error, its accumulated history and its rate of change; it need not explicitly
represent mainline/ramp heterogeneity. Its observations, memory and tuning can
allow it to respond to disturbances. The active task remains open-loop rate
schedule comparison; PID/feedback remain background rather than an adopted
primary comparator. See the [previous methods discussion](../../../synthesis/rm7_g1_ramp_metering_methods_background.md)
and [official PID explanation](https://www.mathworks.com/discovery/pid-control.html).

Starting/stopping actual merge entries illustrates the current-entry mean's
activation/recovery gap; it does not delimit all possible aggregation errors.
Moreover, the meter controls upstream admission, so stopping its permission
does not necessarily stop actual merge transfers immediately. The established
result is a conditional local sampled-onset mismatch. It is neither a proof
that aggregate control is suboptimal nor a guarantee that differentiating a
detailed representation yields an optimal policy. Additional state sufficiency,
complete-TST intervention effects, derivative correctness and usefulness remain
separate unfinished obligations. The reference's event convention is part of
the comparison contract rather than an empirical law assumed to be exact.

| Obligation | A primary | B companion | Shared status |
|---|---|---|---|
| Independent dynamics | Own-state spatial/mean candidate; local scalar coupling supported | Native conservative CTM/node candidate | Same upstream admission, public initialization and complete accounting |
| Local service construction | Conditional same-curve point-renewal mean | Explicit native trigger/priority boundary | Whole multilane port not completed |
| Inactive consistency | Zero-entry/free-speed limits pass; proposed present-entry mean can fail sampled onset match | Narrow limit passes; local receiving/onset mismatches remain | No criterion weakened; no universal family refutation |
| Intervention relevance | Frequency/speed paths identified | Trigger/availability paths; fixed-trigger plateau | Actual exit/TST leverage unproved |
| Core research/gradient claim | Not established | Not established | No numerical traffic or gradient experiment |

## Problem statement — S3-G2-Q-T

For primary A, should we preserve the current transient inactive requirement
and seek a compact mean model with enough independently evolved event/memory
state to satisfy it, or allow a present-condition mean as a predictive rival
whose onset/recovery errors are explicitly evaluated?

## Assumed model-chain function

The upstream meter admits continuous mass into the finite ramp approach.
Actual merge transfers generate the reference's disturbances under its selected
sampling/threshold convention. A compact rival independently evolves spatial
mass and any declared retained state, predicts service and complete exits, and
counts every stream's TST. Its admission standard determines what later model
errors can mean. B remains the companion under either choice.

## Core gap

The existing guardrail requires ordinary matched behavior when reference
restrictions are absent or nonbinding. Present insertion intensity is not an
exact indicator of that condition: new entries may precede the first descriptor,
and old restrictions may remain after new entry ceases. The proposed local
mean has no independent record of either event phase or remaining restrictions.
Its steady limiting checks therefore do not qualify it under the entire
transient guardrail. A smaller geometry does not resolve this distinction.

No complete event/memory-aware mean law has been bound. Adding a phase or
active-state summary changes A's retained information; accepting a known
transient mismatch changes the comparator admission/claim boundary. Both are
methodological decisions rather than numerical tolerances. The local example
must still be checked against the final admitted task and source timing; it
is not a general theorem that every compact mean model fails.

## The two options in ordinary language

These are **T1 and T2**, both concerning primary A's mean model. They are not
the previously approved A-primary/B-companion choice. Both retain the same
reference, upstream meter, conserved traffic and complete system-time objective.

**T1 asks: how little memory does the compact model need to recognize when the
merge restriction actually exists?** The present-rate average is an unfinished
reduction under our current comparison requirement. We seek a small,
source-supported summary of onset and recovery, updated from the compact model's
own transfers and state. The aim is to make it a stronger compact rival before
interpreting an advantage of detailed disturbance descriptors. If that summary
suffices, little additional information may be needed; if it does not, its
remaining failure can motivate a more informative representation. Passing the
inactive requirement alone would still not isolate all causes of error.

**T2 asks: can the current average approximation predict useful control changes
despite imperfect restriction timing?** The mean is a declared predictive model.
An instantaneous onset/recovery mismatch is evidence to diagnose, rather than
an automatic reason to exclude it. Its full system-time response to common rate
changes must still be qualified with fixed calibration and independent dynamics.
It could be adequate for control despite a local mismatch, or could mispredict
which rate changes help. A failure would concern the whole declared approximation;
it would not by itself prove that missing detailed state caused that failure.

For example, in the conditional startup check the reference has not yet created
its first moving descriptor, but the current-entry mean already reduces capacity.
T1 treats this as a gap to resolve before admitting A under the current safeguard.
T2 admits that approximation for predictive assessment, asking whether the early
penalty materially distorts control response. Neither assumes this source
sampling convention is exact physical truth, and neither establishes gradient
usefulness. No traffic evaluation is authorized by explaining T2 here.

## Q-T.1 — preserve the guardrail; qualify a compact event/memory-aware mean A

Keep the reference's motion, sampled transfer/birth convention and current
geometry family. Seek the smallest own-state summary that lets A distinguish
pre-event startup, active disturbance and recovery, while averaging rather than
retaining every trajectory. Candidate information includes public threshold
progress updated from A's actual transfers and a source-qualified active/recovery
summary. These are directions for qualification, not approved timer equations,
identity lists or a promised sufficient set. Initial projection, independent
update, nonbinding removal and effect on service must be explicit. B continues
as a diagnostic family with its mismatches disclosed.

**Pros:** preserves the current mechanism-matching control; makes any additional
retained information an explicit scientific object; avoids confusing a known
averaging/activation bias with evidence that full identity is indispensable.

**Cons:** extends A beyond the present-condition quasi-steady construction.
The least sufficient summary and its closure remain unqualified; no positive
result is guaranteed. Exact onset matching alone would not establish recovery,
TST fidelity or useful gradients.

**Dependency/consequence:** approves the bounded retained-state extension for
review, not a new traffic law. Transient source/state/service qualification
precedes final S3-I3.Q-F binding. An unsupported recovery term or a change to
reference birth physics still returns to its smallest global decision.

## Q-T.2 — admit the present-condition mean as a predictive approximation

Keep the reference and complete accounting unchanged. Explicitly relax only
compact-model admission against every transient inactive state: retain exact
ordinary KW controls and algebraic bounds, but report onset/recovery discrepancies
rather than automatically excluding the mean rival. Compare independently
predicted common-rate exit histories/TST against the reference and B, with
fixed calibration and separate diagnosis of constitutive and state errors.
Do not claim a pure removal-of-state or detailed-identity necessity result.

**Pros:** evaluates a legitimate compact approximation on the behavior it is
intended to predict; permits the current mean construction to advance without
inventing event memory solely to satisfy an exact transient test; preserves B's
distinct explanatory contribution.

**Cons:** weakens the current comparator admission criterion and causal
attribution. A fine-model advantage could reflect the mean service law rather
than missing state. The mean spatial/kinetic port is still unfinished; this
choice does not certify its accuracy or complete the study task.

**Dependency/consequence:** requires explicit acceptance of the criterion/claim
amendment before definitive comparator admission. The reference's unobstructed
limit, mass/storage, physical control, knowledge fairness and full TST do not
change. Per-intervention fitting and a deliberately weak sole baseline remain
excluded. It does not automatically admit B as a matched reduction.

## Fair comparison and provisional recommendation

| Dimension | Q-T.1 | Q-T.2 |
|---|---|---|
| What changes | A's proposed retained-state scope | Compact admission and resulting claim scope |
| Inactive guardrail | Preserved; qualifying summary must satisfy it | Known transient error evaluated explicitly |
| Main scientific question | Which compact independently evolved information preserves response? | How well does this declared approximation predict intervention response? |
| Meaning of the startup mismatch | An unresolved gap before matched admission | A declared prediction error whose control significance must be assessed |
| Possible favorable outcome | A small memory summary is sufficient; detailed trajectories may be unnecessary | Average prediction is adequate for relevant rate changes despite local timing error |
| Meaning of a later detailed-model advantage | Stronger retained-information evidence if other law differences are also controlled | Evidence of better overall prediction; state loss and closure error remain entangled |
| Principal unfinished work | Qualified event/recovery summary and service map | Qualified mean port and interpretable predictive evaluation |
| A+B coordination | Preserved | Preserved |

**Recommendation at the decision: Q-T.1; now approved by the user.** It keeps the current comparison safeguard
and turns the newly exposed gap into a specific retained-information question.
Q-T.2 is also methodologically legitimate under its narrower predictive claim;
it remains unselected. T1 approval is recorded in
[continuation 63](../../../rm12_63_bp_r_stage3_event_memory_continuation.md).

## Ownership, superseded draft and stop boundary

- **S3-G2-Q-R, Type 2/user:** A+B coordination approved and execution opened.
- **S3-G2-Q-T, Type 2/user:** closed as T1; its bounded memory qualification is performed.
- **S3-G2-Q-M, Type 2/user:** closed as M1; bounded grouped-state qualification performed.
- **S3-G2-Q-G, Type 2/user:** concrete grouping/reconstruction contract; open in the current findings.
- **S3-I3.Q-P.S/A/B/C, Type 1/reviewer:** bounded source/static pass performed;
  dependent state or predictive-port qualification follows the T decision.
- **S3-G2-Q, Type 2/user:** final concrete law/claim adoption remains distinct.
- **S3-I1/I2 and S3-I3.Q-F:** event/draining and final binding remain incomplete.
- **S3-G3:** final Stage 3 disposition pending; no Stage 4 opening.

An earlier reviewer draft in this same pass proposed Q-S, choosing point versus
multilane first-task geometry. The final onset check shows that restriction
alone does not settle the comparator's transient admission. **Q-S is withdrawn
as the immediate gate; no user-approved decision is reopened.** Point renewal
remains an analytical subcase, and geometry qualification remains later work.
No one-mainline task is adopted or required.

The [approved protocol](../../../rm12_60_bp_r_stage3_protocol.md) requires:
"If adoption of a new physical/reference/actuator contract is necessary, prepare
concrete alternatives and stop at G2 before treating a candidate as approved."
Its G2 inventory also covers knowledge/acceptance transfers. The A-state or
acceptance alternatives are now reviewable; evidence work preceded this stop.
