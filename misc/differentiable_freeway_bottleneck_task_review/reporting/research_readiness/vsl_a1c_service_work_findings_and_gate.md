# One service account can join sharing and merging difficulty; speed needs a causal rule

**Current O-R qualification, 2026-10-15:** the user selects recent-mass
renewal, closing RE-O1. R-E and current-state S-E-P remain. The bounded
recovery candidate/analytical pass is complete at **OR-Q1**: physical
update/state, local causal coupling, derived positive service and clearance
bounds, and a regular full-cohort family with A delay and active retirement.
This does not establish realistic parameters, the whole original action
range, applied MP6 or useful gradients. The complete joined review and
Step 3 remain open; J4 follows review of this checkpoint. Earlier reports
retain delivery-time meaning. No implementation or traffic experiment.

[Selected renewal, analytical evidence and recovery checkpoint](vsl_or_recovery_qualification_and_checkpoint.md)

[Executed S-E model, reachable contrast and current allocation gate](vsl_se_admission_findings_and_gate.md)

[Latest configuration check, refined options and S-E selection](vsl_se_fixed_queue_configuration_response.md)

## The model shape that can now be written

A compact unified description is possible at the service interface.
Imagine one service budget and a traffic-dependent amount of work needed
to admit one unit of A or E. A difficult E entry can consume more of the
budget than an ordinary A passage. If the streams are similarly easy to
serve, their costs can be comparable. Recent interactions may still affect
the account after the traffic causing them has crossed the line.

For a concrete allocation module, suppose two waiting streams receive equal
shares of **service work**, with unused work returned to the other stream.
Then the stream costing more work receives less physical flow. The same
account determines both the flow split and the total discharge; there is
no independently chosen constant E flow fraction.

The equal-work convention is a **proposed symmetry/fairness assumption**,
not a consequence of conservation or a measured law. Other justified
conventions remain possible. The source-grounded ingredient is conservative
service allocation; the exact state-to-cost and recovery maps are still
constitutive assumptions to qualify.

### What it says through the same illustrative budget

| Conditional state/cost case | Allocation from six work units per second | Traffic meaning |
|---|---|---|
| **A and E each cost one unit per admitted mass** | Three A and three E. | Comparable costs give balanced passage under the proposed fairness convention. |
| **A costs one; E costs two** | Three A and one-and-a-half E. | Harder E admission gives E a smaller flow share and reduces total usable throughput to four-and-a-half. |
| **Intermediate E cost of one-and-a-half** | Three A and two E. | The same rule yields an intermediate split and total flow. |
| **Both cost two** | One-and-a-half A and one-and-a-half E. | Balanced sharing can coexist with strongly reduced total service. |

These are exact static work-account examples, not traffic parameters,
measured cost values or a simulation. They demonstrate the unified mapping
conditional on its inputs; they do not establish which traffic states
actually produce those costs.

Unlike changing a priority weight alone, a larger E cost can also make
some nominal residual capacity unusable by E. With six work units, an A
offer of two and E cost two, A can pass two and E two: E cannot convert the
four remaining work units into four mass units. No mass is lost; E simply
waits if its offered mass exceeds its feasible admission.

**One account still means one account.** The internal costs and allocation
are rules for consuming its common budget, not independent service ceilings
attached to past vehicles. Its physical throughput reading depends on the
mix being admitted. Work capacity must not be mislabeled as vehicle flow,
and low outflow due to low demand is not a service loss. Current admission
cost and retained recovery must describe distinct portions of the interaction,
or be combined in one justified mapping; the arithmetic alone does not prevent
charging the same physical burden twice.

## The new finding: a queue flag cannot silently select its own speed

To use this module, we must predict the actual traffic conditions that set
admission cost. A tempting minimal closure is: E has the advised/free speed
while its queue is empty, but receives a lower congested speed from its
discharge rate as soon as it is queued. Greater mismatch then makes E more
costly and lowers its discharge further.

The analytical check finds a concrete problem with that closure. Under the
same constant local offers and empty queue, one valid continuation remains
free. Other continuations spontaneously start a queue at any chosen time;
once the queue exists, the slower speed and lower discharge sustain it.
Nothing in the proposed differential rules chooses that starting time.

In traffic terms: **“a queue makes the entry slow” and “slow entry sustains
the queue” do not by themselves decide whether and when a queue starts.**
This does not require an external slowing seed, exclude merging-induced
queueing or revive the old F/D choice. It requires a causal state/entry rule
inside the model. A simulation update must not make that scientific choice
implicitly through its time step, an epsilon queue or an unrecorded fallback.

The example uses an illustrative speed-cost relation and temporarily holds
the recovery budget fixed to isolate the entry-state closure. It is not
the selected complete M2 law, not a reachable H1/MP6 witness, and not a
theorem that every algebraic speed-dependent point model is nonunique.
Adding a recovery account does not by itself supply the missing branch rule;
the fully coupled law still needs its own proof.

## What the source recheck establishes

Demand/supply node models provide usable conservative allocation templates.
They do not automatically identify physical insertion speed. A saturated
lane demand can stay at capacity while actual boundary conditions differ.

Jin, Gan and Lebacque's capacity-drop model explicitly supplies a boundary
selection rule and proves its Riemann solution. Its existence illustrates
why that rule is part of the scientific model; its phenomenological drop
and proof are not transferred to our history-dependent node.

[Primary manuscript, §2.1–2.2 and §6](https://arxiv.org/pdf/1310.2660)

Leclercq et al. relate insertion speed to flow under a declared congested
regime. That selected relation does not choose the finite-cohort transition
from initially free entry to a queued state.

[Primary manuscript, §2 and §3.2](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6)

Chevallier and Leclercq's inspected work distinguishes insertion decisions
and relaxation; its congested-merging framework uses an insertion-rate
description. It supports examining how admission and recovery fit together,
not importing a full microscopic algorithm or its numerical parameters.

[Primary publisher abstract/introduction, access limited](https://www.sciencedirect.com/science/article/abs/pii/S0968090X09000096)

The earlier empirical relative-speed and congested-sharing evidence remains
conditional. No source read here supplies a ready-made, finite, homogeneous-
upstream A1-C task or determines the new work coefficients.

## Gate A1-C-S1: how do the point's traffic states evolve?

**Direction choice now closed: S-E first.** The original problem compared
equilibrium boundary speeds with explicit causal regime transitions against
additional finite-rate aggregate speed dynamics. The user accepts S-E.
Qualify it with the existing fixed A/E waiting balances and retained
travel/storage/recovery histories; no queue-position states are implied.

**Function in the chain.** This closes the state input to the unified
admission/work/recovery component. The state determines admission difficulty;
admissions and queues then change that state. It sits in J1–J2 of the
approved three-part review and supplies the input needed for J3 recovery.

**Core gap.** The user selected traffic-conditioned A1-C and now S-E's
qualification direction, not its exact speed/admission law.
The natural queue-based instantaneous completion tested here is insufficient
without a rule choosing its evolution. The choice affects traffic memory,
the meaning of speed, transition timing, derivatives and the source of the
comparison's information. It is not a numerical implementation preference.

### S-E: equilibrium speeds, with an explicit causal regime rule

Keep the first-order boundary description. When a stream is unqueued, use
its compatible free branch; do not switch it to a congested branch merely
because that alternative would sustain a queue. A specified physical
admission restriction or service shortfall must trigger queue formation.
Once queued, use the qualified congested branch until its stated clearance
condition returns it to the free regime. Specify simultaneous events and
prove the complete law has a unique causal continuation.

This rule would reject the arbitrary queue births in the diagnostic. That
is a local consequence, not a full A1-C proof. It still needs a real
conditional entry/opportunity rule, not a fixed low insertion speed for E.
The diagnostic's speed-only cost is not itself the final compulsory-merge law.

- **Pros:** retains the existing first-order approach interpretation and
  few continuous states. Boundary-selection rules have a source precedent.
  It can preserve the current point/storage interface without spatial cells.
- **Cons:** speed is an equilibrium boundary approximation and may change
  abruptly at a regime transition. The triggering/clearance rule carries
  scientific meaning and may produce hysteresis. It must be specified and
  checked; invoking a standard solver or M1's proof is insufficient.
- **Dependencies/consequences:** Type 2 G3 state/transition semantics.
  Known initial regime stays fixed; no hidden disturbance or numerical
  tolerance may select a branch. Sensitivity must account for transition
  timing. Full entry/recovery and MP6 remain after this direction choice.

### S-V: retain local aggregate speed dynamics

Give the relevant local approach/entry speeds a predicted aggregate state
with explicit acceleration, deceleration, entry and clearance rules. Queue
presence constrains that state but does not instantaneously assign its
speed. Actual initial speeds must be known, and empty or changing traffic
populations must have defined state semantics.

This can describe a short obstruction whose effect builds and recovers
over time, even before a long queue exists. It remains a macro point
component if only aggregate local conditions are retained. It is not an
instruction to introduce CTM cells or individual vehicle following.

- **Pros:** represents finite-rate speed adjustment explicitly and can keep
  physically relevant memory across brief waiting and recovery episodes.
  It avoids making a queue flag the sole instantaneous speed switch.
- **Cons:** introduces additional continuous dynamics and parameters. A
  meaningful averaging/head-of-stream interpretation, mass-changing updates
  and their relation to the first-order terminal need qualification. A
  velocity ODE alone does not guarantee safe admission, uniqueness or MP6.
- **Dependencies/consequences:** Type 2 G3 local motion/state amendment.
  Unknown initial kinematics would reopen G2; a spatial requirement or new
  longitudinal propagation would require its own explicit decision. H1
  and the objective do not change automatically.

### Direct comparison through a short E obstruction

| Question | S-E: equilibrium plus causal regime rule | S-V: aggregate speed dynamics |
|---|---|---|
| **What describes E just after entry is obstructed?** | A specified transition selects the applicable equilibrium boundary branch. | A speed state responds over its specified physical adjustment time. |
| **What additional information persists?** | Queue/regime history and the selected recovery record. | Those records plus the justified speed state. |
| **What prevents arbitrary queue birth?** | An explicit admissible transition rule, proved as part of the node. | The initial-value dynamics must determine it; their proof is still required. |
| **Can the shared service rule cover intermediate traffic states?** | Yes, through its state-dependent law; transitions need not be smooth. | Yes, through the evolving state and the same kind of service law. |
| **Does either force E to slow every time?** | No. | No. |
| **Does either require spatial cells or microscopic cars?** | No. | No, unless later qualification exposes such a need and reopens scope. |

**Selected first direction: qualify S-E.** It is the smaller
amendment to the existing first-order stack, and the failure of the naive
queue-flag rule does not prove a causal first-order closure unavailable.
If the intended task needs finite-rate approach-speed memory that S-E
cannot defensibly reproduce, return explicitly to S-V. The user now accepts
S-E as the first qualification direction; S-V remains unselected. The fixed
configuration narrows S-E to explicit empty/waiting/clearance and boundary-state
rules at one A/E line, retaining T1 histories and one shared recovery account.
This does not prove a stationary physical jam or sufficient queue-only state.

## Progress, MP6 and stopping status

| Approved work | Established in this pass | Not yet established |
|---|---|---|
| **Admission/discharge** | An explicit unified work-allocation module with unique flows for fixed inputs; its matched/mismatched and residual-service limits. A specific instantaneous speed completion has a nonunique queue-birth diagnostic. | Physical state-to-work map and selected, well-posed speed/transition closure. |
| **One shared recovery account** | The module can consume one account with sufficient internal state; prior influence need not be a separate per-entry constraint. | Exact recovery/overlap and a justified partition from current admission burden. |
| **Joined qualification/MP6** | Conditional demand/work-budget feasibility, storage/TST compatibility and a bounded-work/finite-loss sufficient clearance bound. | Complete-law uniqueness, actual finite-loss bound, reachable consequential all-action regime, information/action/gradient or SUMO evidence. |

**M2-A1's direction choice is closed by user approval of revised A1-C.**
The original pass stopped at **A1-C-S1, Type 2 G3**. The user subsequently
accepts S-E at direction scope. The fixed-queue check is now complete;
exact S-E admission, boundary-state and recovery qualification remains the
next work. A new state or interface meaning still requires user approval;
source/units/algebra transcription is Type 1. The direction closure does
not establish a complete law or remove the diagnostic's causal-rule gap.

The approved three-part review and original Step 3 are still in progress.
No complete primary model is frozen. H1, finite storage, the primary demand
domain, known initial information, local completion and S-P→S-L remain.
No positive information/action result is inherited from S13 or M1; no
interior optimum, full lane state or gradient advantage is required.

[Analytical module, exact queue-birth diagnostic and conditional bounds](../../synthesis/research_readiness/vsl_a1c_service_work_and_speed_closure.pdf)

[References viewed, source/adaptation boundary and access limits](../../extraction/research_readiness/vsl_a1c_source_and_adaptation_audit.md)

[Selection and precise approval scope](vsl_a1c_selection_and_scope.md)

[Files, commands, checks and next allowed action](vsl_a1c_service_work_work_report.md)
