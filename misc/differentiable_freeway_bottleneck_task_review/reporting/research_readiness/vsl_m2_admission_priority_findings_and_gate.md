# A queued through lane: must the ending lane wait, or may it be given room?

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

[Fixed queues, refined S-E and approval scope](vsl_se_fixed_queue_configuration_response.md)

[Current selection and precise approval scope](vsl_a1c_selection_and_scope.md)

[Current executed findings and new state-closure gate](vsl_a1c_service_work_findings_and_gate.md)

**Feedback 7 revision, 2026-10-15:** the exclusion/allocation findings
below remain valid, but a fixed positive quota is no longer the preferred
full behavioral closure. Revise A1-C toward traffic-conditioned usable
entry and shared service/recovery. A variable weight alone may leave
residual E admission unchanged. M2-A1 stays open; no amendment or exact
law is approved. The original hand case and PDF remain conditional references.

[Current conceptual response, evidence limits and candidate revision](vsl_feedback7_traffic_state_response.md)

Date: 2026-10-15. The user approved the three-part admission/discharge →
shared recovery → joined qualification plan and confirmed that E slowing
is conditional. **That review has begun and is paused at a narrow terminal
admission choice. The full three-part pass is not complete.**

## What the opening check establishes

The next model can remain a pair of physical approach queues feeding one
point, with one shared service account retaining recovery information.
There is no finding here requiring a spatial merging zone, CTM cells,
individual vehicles or automatic slowing of E.

The immediate issue is more specific: **does the continuing stream merely
have preference, or does it have an absolute claim on service whenever its
queue is nonempty?** The inherited exact terminal rule means the latter.
That is stronger than ordinary language such as “A has priority.”

When A is queued, its boundary demand can consume the whole effective
service budget. The rule gives that budget to A first. E receives zero,
even if E is waiting at the lane end. Reducing the meter does not make room
for E: A continues to take the whole smaller budget until its queue clears.
This follows directly from the inherited strict allocator, made explicit
in the conditional M1 reference, independently of how the new meter remembers
recovery. M1's exact law remains an unselected conditional reference.

That behavior is a coherent **passive, strictly yielding E model**. It can
still have conditional E waiting/slowing and continuing-traffic delay from
earlier slow entries. It is not incapable of coupled merging. What it cannot
represent is **letting E through while an A queue is still present**, whether
the physical opportunity comes from an existing gap or from A making room.
Calling that latter behavior part of the same model would silently change
the allocator.

## The same traffic episode under both interpretations

Consider a moment with A queued, E ready to merge, and shared effective
service of 600 vehicle-equivalents per hour. This is a hand case, not a
simulation or proof that the as-yet-unformed M2 reaches this state from empty.

- With the inherited strict rule, A receives all 600 and E waits.
- With a limited E claim during contention, an illustrative allocation is
  450 to A and 150 to E. A still receives preference, but E can enter while
  A remains queued. Those numbers illustrate the rule; they are not proposed
  parameters or a calibrated merge ratio.

Both allocations use the **same 600**. Sharing is not itself a capacity drop.
If an admitted E group actually enters slowly, its physical influence may
subsequently reduce the shared meter. The model must qualify that speed and
recovery separately; the allocation ratio cannot stand in for either.

In a benign case with ample service for both arriving streams, both rules
pass all available traffic. Limited sharing does not require queues, braking
or a fixed slow speed for every E passage. If one stream has little demand,
its unused allocation goes to the other.

## What the source recheck adds

A published first-order merge template explicitly separates a shared service
limit from the priority used to divide it. Its spare service is redistributed,
so a priority parameter need not impose a fixed completed merging proportion.
We can inspect that allocation without adopting its phenomenological
capacity-drop law. The exact transfer into M2 would remain a declared adaptation.

[Jin, Gan and Lebacque, merge equations (15), printed pp21–22](https://arxiv.org/pdf/1310.2660)

The behavioral literature also distinguishes free, forced and cooperative
merging. That supports examining cooperation as real traffic behavior, but
does not validate a particular aggregate priority weight for our task.

[Hidas (2005), inspected publisher abstract and introductory excerpts](https://www.sciencedirect.com/science/article/pii/S0968090X04000671)

The primary SUMO lane-changing paper describes speed adjustments by both
the merging vehicle and obstructing traffic. That is a behavior precedent,
not evidence that the proposed restricted point geometry already implements
it. Native junction correspondence still needs qualification after the
primary admission meaning is fixed.

[Erdmann, lane-changing model, §1.4.3](https://elib.dlr.de/89233/1/SUMO_Lane_change_model_Template_SUMO2014.pdf)

## The model that can be formed, and its remaining gap

The source-supported shape is a **conditional admission-and-recovery point
model**: available E/A traffic competes under a declared admission rule;
actual departure kinematics determine whether an entry creates a genuine
restriction; one aggregate account carries its remaining influence. Ordinary
queueing and forced interaction remain compatible cases of that model.

The opening audit supplies exact allocation modules for strict priority and
limited sharing, proves their different queued-A behavior and checks the
unchanged physical interfaces conditionally. It does not yet supply a full
M2 constitutive law. Two guardrails matter for the next part:

**A queue identifies waiting, not a unique insertion trajectory.** A
congested fundamental-diagram branch is a possible boundary-speed description
when its regime is justified; it is not automatically the lateral entry speed.
Neither a service-equivalent speed nor low observed flow alone supplies that
missing behavior.

**Following a slow entry is not automatically a second disturbance.** If
the meter has already slowed A, feeding every resulting slow A departure
back as another independent moving-bottleneck loss may repeat the same
restriction. The analytical note makes that feedback visible. A separately
justified startup or acceleration effect remains reviewable; no blanket A
penalty is adopted.

## Gate M2-A1, revised: traffic-conditioned admission and service

**Problem statement, revised after feedback 7.** Should the primary retain
the restricted passive contract or qualify traffic-conditioned admission
and effective service/recovery? A numerical fixed-share choice is no longer
presented as a sufficient physical answer.

**Assumed function in the model chain.** Component 6 follows H1's unchanged
preparation and finite-terminal eligibility. It must join predicted traffic
state, usable entry and one effective shared service/recovery account to
determine actual A/E departures. Those departures determine queue areas;
the entry-speed/recovery dependence remains to be closed causally.

**Core gap.** Literal strict priority excludes E during A backlog, but
a positive quota merely redistributes a budget. It does not establish
E's ability to use nominal spare service or the interaction's current and
continuing burden. The physical target must join traffic state, admission,
discharge and shared recovery. A changed terminal contract remains Type 2
G3; this does not revive the withdrawn F/D origin choice.

### A1-S: retain strict A-first service; E uses only the remainder

Keep the current terminal allocator. E can wait, enter through residual
service when A demand permits, and leave a recovery influence after a slow
entry. If A is queued, E waits until A's queue clears. Finite-cohort clearance
can still be possible; this is not a proof of permanent E starvation.

The strongest version qualifies a causal aggregate opportunity/entry-speed
rule for those permitted E passages, rather than treating every E as slow
or claiming that residual capacity identifies physical gaps. It retains
ordinary congestion and forced waiting together, as feedback 6 requires.

- **Pros:** preserves the approved allocation exactly and makes the fewest
  contract changes. It has transparent priority semantics and remains a
  useful strict-priority reference. It needs no microscopic gap realization.
- **Cons:** deliberately omits E passage while A is queued, including
  cooperative gap creation. More detailed recovery memory cannot repair
  that omission. E may wait through a whole A backlog; the external mapping
  must preserve or explicitly test that restriction rather than call it
  ordinary cooperative merging.
- **Dependencies and scientific consequences:** no priority amendment.
  Conditional entry speed, any additional admission restriction, recovery
  and clearance still need qualification. Restrict any behavioral claim
  accordingly; do not identify this whole allocator with natural SUMO behavior.

### A1-C revised: traffic-conditioned admission and shared service

Qualify one terminal rule that distinguishes slow E beside fast A,
comparable slow approaches, intermediate and benign conditions. Predicted
traffic state must explain usable E entry and actual kinematics, alongside
the effect on the singleton effective-service/recovery account. E may pass
during A backlog where the qualified interaction permits it; no fixed quota,
universal monotonic speed penalty or automatic E slowdown is imposed.

The previous constant-weight form remains an exact allocation template and
serious simpler rival. Under a fixed 600-unit budget, unqueued A demand of
450 leaves E 150 under either a one-quarter or one-tenth weight. Therefore
varying priority alone may not describe incompatible entry into apparent
spare service. This is a static check, not a numerical traffic scenario.

- **Pros:** directly addresses traffic-dependent merging within the selected
  point component and one account. Preserves the possibility of aggregate
  representation without new spatial cells or individual gap trajectories.
  Retains strict and fixed sharing as explicit restricted cases/rivals.
- **Cons:** the joint state/opportunity/kinematics/recovery closure is not
  supplied by an allocation formula. Similar queues do not guarantee equal
  speeds, equal shares or a slightly greater E cost. Additional assumptions
  and parameter provenance must be qualified rather than tuned for control
  benefit; macro sufficiency remains unproved.
- **Dependencies/consequences:** the same terminal G3 discussion, not another
  component/stage. A changed admission/service law needs confirmation;
  H1's own-lane priority, cutoff, finite storage, initial information, primary
  domain and local endpoint remain fixed. Current and continuing influence
  must not be charged twice. Unknown initial state or privileged future
  information returns to G2. Matched information comparisons share the
  physical law/parameters; published model-form rivals keep disclosed native
  semantics. No SUMO model is forced to reproduce these numerical departures.

### Direct comparison after feedback 7

| Traffic question | A1-S: strict remainder | Fixed-share template | Revised A1-C |
|---|---|---|---|
| **E entry during A backlog** | Excluded. | Allowed by a positive reserved weight. | Allowed where the qualified traffic interaction permits it. |
| **Slow E beside fast A** | Priority alone does not explain compatibility. | Weight alone does not explain compatibility. | Explicit admission/service dependence to qualify. |
| **Comparable slow approaches** | E still waits for A backlog to clear. | May represent a qualified approximately stable sharing regime. | Comparable sharing is a hypothesis; total capacity may remain reduced. |
| **Benign passage** | Can be undisturbed. | Can be undisturbed. | Must allow an undisturbed limit; no automatic E penalty. |
| **Status** | Inherited restricted contract/reference. | Exact template and simpler rival. | Provisional preferred qualification target, unselected. |

**Provisional recommendation, revised:** traffic-conditioned A1-C. Establish
the physical admission/service target before freezing a constant quota.
This is a candidate revision, not approval of a formula or a terminal-priority
amendment. The full feedback-7 response states the source support and limits.

## What the joined checks establish at this stopping point

| Approved chain | Result now established | Still unresolved |
|---|---|---|
| **1: admission and departure** | Strict exclusion and reference sharing calculations remain valid. Feedback 7 shows why usable entry and service need traffic-conditioned qualification. | Revised M2-A1 target, exact opportunity/entry-speed and shared-service law; no constant quota or universal mismatch rule approved. |
| **2: shared recovery** | One shared account remains sufficient as an interface; admission priority and capacity reduction are different functions. Slow A flow is not by itself a newly established loss source. | Exact recovery update, interaction/overlap closure, independent A mechanism if any, sufficient memory. |
| **3: joined qualification and MP6** | Both reference allocation modules respect demands and one shared budget. Conservative departures preserve the existing storage/TST interfaces. A finite total service-loss budget gives a sufficient clearance bound. | No complete state-dependent M2 uniqueness, finite-loss proof, reachable consequential MP6 regime, information/action/gradient or SUMO qualification is established. |

The all-action no-ordinary-overload condition remains unchanged. The queued
hand case diagnoses the allocator; it is not an unapproved overloaded primary
scenario or a claim of reachability from the known empty start. No strong
aggregate/history, ending-statistic, P-E/M1 or equal-information search rival
is removed. No interior optimum or full-lane-state advantage is assumed.

**Ownership/status after feedback 7:** M2-A1 remains Type 2 G3, with the
terminal admission/service candidate revised and unselected. The reviewer
qualifies source/physical law; the user confirms changed scientific meaning.
Source/unit/algebra bookkeeping is Type 1 and cannot select it. CP-D2/M2,
P-H/C-P, H1 and S3-M1/S3-M2 stay closed in their existing scope. The approved
three-part pass and Step 3 remain in progress. No full replacement, priority
amendment, new state law or fixed physical limit is approved here.

[Analytical audit: exact allocation, kinematic guardrails and conditional joined bounds](../../synthesis/research_readiness/vsl_m2_admission_priority_audit.pdf)

[References actually viewed and access limits](../../extraction/research_readiness/vsl_m2_admission_priority_source_audit.md)

[Work, checks, preserved artifacts and next allowed action](vsl_m2_admission_priority_work_report.md)
