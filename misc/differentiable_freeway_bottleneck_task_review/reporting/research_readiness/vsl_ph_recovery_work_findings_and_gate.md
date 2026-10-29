# A slow merge leaves a temporary restriction on the point's service

**Current continuation:** M2 is now user-selected and CP-D2's direction
choice is closed. The exact M1 note remains a conditional reference. M2's
first source/speed pass reaches CP-M2-D1: what creates the first restriction
under the inherited empty start? No replacement law or demand-domain change
is approved. Earlier notices below retain their delivery status.

[Current M2 findings and activation gate](vsl_m2_first_restriction_findings_and_gate.md)

**Feedback 5 clarification, 2026-10-15:** both directions can use one shared
service reading. The exact law described below is now M1, retained as the
conditional reference. The updated provisional recommendation is to qualify
M2's traffic-dependent update; its exact law and any additional A-discharge
effect remain unapproved. CP-D2 and Step 3 stay open.

[Current mental model, qualifications and revised comparison](vsl_feedback5_shared_service_meter_response.md)

**P-H is user-selected; CP-D1 is closed, 2026-10-15.** The resumed review
has formed and analytically checked one concrete candidate. The basic
traffic picture is unchanged: H1 prepares the lane streams, a finite terminal
holds their physical queues, and remaining E traffic must merge at the choke.
The new part is that a completed slow entry leaves a temporary service
restriction. Later A and E traffic encounter that restriction until it fades.

This completes the resumed **candidate-formulation and analytical-check
pass**, at VSL-CP-G2. The exact reduction is proposed for confirmation, not
silently approved by the selection of P-H. The full terminal amendment and
Step 3 remain open. No simulator or traffic experiment was run.

[P-H approval and preserved boundaries](vsl_ph_selection_and_scope.md)

## The model that can now be formed

Think of two physical approach queues sharing one exit. A still has priority
when both want to leave. What changes is the amount of service available
to share: recent slow E entries can reduce it below the ordinary ceiling.
Priority determines who receives the available service; it does not restore
service lost behind an already admitted slow entry.

For example, an E burst can pass the measuring line before a later group of
A traffic arrives. In the old model, that completed E burst leaves no burden
on A. In this candidate, the later group can encounter a restriction left by
the burst and wait before the line. If it arrives after recovery, that
restriction has disappeared. Neither case charges the completed E traffic
for its own subsequent travel.

The proposed rule has three parts. First, a representative slow insertion
accelerates until it no longer constrains the baseline service ceiling.
Backward traffic waves translate that recovery into a time profile of
service loss at the point. Second, actual completed E mass leaves copies
of this profile, weighted continuously by mass. Their remaining losses add
against the finite service budget. Third, A takes priority within the
remaining budget and E receives the residual. Both can queue when service
is insufficient. A record older than the finite recovery duration is removed.

The retained record is **recent E departure history**, not a list of cars,
physical positions or an extra queue. One scalar memory is not asserted to
be exact. Ordinary lateral merging remains forbidden in the terminal.

| Part of the stack | Old member | Proposed P-H change |
|---|---|---|
| **H1 early preparation** | Homogeneous, receiving-limited E-to-A transfer, followed by a fixed cutoff. | Retained, including its physical opportunity scale and the protected handoff. |
| **Component 6: forced point service** | A leaves immediately; each E departure consumes an instantaneous enlarged work amount. | Recent E admissions reduce shared service during recovery. A receives priority within that service and may wait. The old extra E work factor is removed, avoiding a second charge for the same effect. |
| **Terminal storage and accounting** | Physical lane stock and eligible queues; original member has no A queue. | Same histories and storage interfaces; include A's eligible queue in complete local TST. Memory is not vehicle mass. |
| **Control, observations and endpoint** | One bounded common advice, compact initial lane information, completion at the choke. | Retained. The new service history is predicted from a known empty initial condition. |

## What is physically supported, and what is our approximation?

The point-insertion source describes a slow inserting vehicle with bounded
acceleration and backward waves. Its point-case cumulative capacity expression
provides the basis for an isolated recovery profile. It does not supply the
continuous superposition used here. The new profile and proofs are explicit
deductions/adaptations, rather than adoption of the complete source model.

[Primary point-case basis: Leclercq et al., 2016, §2](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6)

**The important new assumption is how many recovery effects combine.** This
candidate adds their service-loss demands and lets the finite budget fall to
zero when those demands exhaust it. It does not reconstruct interactions
between individual leaders, voids and waves. That makes the model compact
and analytically manageable, but is its main physical qualification risk.
It is a proposed constitutive approximation, not an established literature
law for this finite continuous cohort.

A second explicit assumption is a shared representative insertion speed and
acceleration. These describe the recovery prototype. They are not an actual
Eulerian exit-speed field inferred from the current queue, nor known SUMO
measurements. All parameters remain fixed across advices and observers. With
the inherited fixed baseline ceiling, the prototype profile is also fixed
across advices: advice changes preparation, arrival timing and the resulting
admissions. This candidate does not additionally claim a direct advice-to-
insertion-speed law. Adding that law would require its own evidence.

## Direct answers from this pass

| Review question | Core finding | Evidence limit |
|---|---|---|
| **CP-Q1: what creates the service loss?** | A slow insertion leaves a finite restriction while it accelerates. The candidate spreads the loss over later service instead of charging only the E entry at completion. | The isolated profile has a kinematic-wave basis; its continuous overlap rule is a proposed adaptation. |
| **CP-Q2: what information must persist?** | Keep the completed E mass admitted during the last recovery window. Its age determines the restriction that remains now. The initial record is empty and the record is generated causally. | No exact one-scalar reduction or traffic-state-derived insertion-speed field is established. |
| **CP-Q3: is there a complete mathematical terminal?** | For the stated continuous law there is a unique causal departure process, conserved mass, respected sending/storage, and finite full-cohort clearance. A can queue; H1 remains protected by the inherited conservative storage domain. | These are analytical results for this candidate, not native traffic validation or approval of its physical closure. |
| **CP-Q4: what survives for information and gradients?** | Aggregate information plus the initial ending scalar still reconstructs the full candidate under symmetry and known empty memory. The gradient must include the effect of E admissions on future service and A waiting. | The old positive action/gradient certificate does not transfer. No new decision split, derivative computation or useful-gradient result is claimed. |
| **MP6: can early limitation and a consequential forced merge coexist?** | A nonempty conditional family can have active H1 receiving limitation and positive A waiting under the same law, while satisfying storage and clearing in finite time. | This is a symbolic existence construction, potentially requiring slow recovery and ample storage. It supplies no empirical parameter range, interior optimum or SUMO admission. |

The clearance result does not rely on inserting an artificial positive
capacity floor. A large overlap can temporarily stop service, but finite
admitted mass leaves only a finite total recovery burden. The node therefore
cannot remain shut forever. The mathematical note gives the bound and the
separate existence/uniqueness argument.

A caution helps interpret the A-delay finding. Slow merging does not make
A wait in every demand pattern. With constant A demand, initially empty
memory and strict A priority, this fluid rule can reduce E admissions enough
to protect A. H1 supplies increasing A demand as early transfers accumulate;
that later demand can encounter earlier recovery restrictions. The candidate
permits the required coupling without asserting an inevitable shockwave.

[Exact law, proofs, limiting cases and MP6 construction](../../synthesis/research_readiness/vsl_ph_recovery_work_contract.pdf)

## What this means for the remaining comparison review

The model has gained temporal service state, not an extra initial information
privilege. A+E and G remain equivalent for this conditional member. A compact
scalar predictor, full lawful aggregate-history inference, one-dimensional
search, analytical/finite-difference gradients and the simple capacity-drop
node remain serious rivals. A steady-flow limit of the candidate even
reduces to an effective enlarged E work factor; the distinctive issue is
whether timing of the recovery matters for the finite cohort.

SUMO S-P must generate its own insertion speeds, braking and service. It must
not be scripted to reproduce this loss profile. Its role is to test whether
the reduced point law predicts useful advice with the same preparation cutoff
and local endpoint. S-L remains the later transfer test with additional native
terminal gap opportunities. The accepted ladder is unchanged. Neither
reference admission nor the amended information/action/sensitivity evidence
is complete in this pass.

## VSL-CP-G2: what updates the one shared service meter?

**The common traffic picture is one effective service ceiling shared by A
and E.** Ordinary passage uses current service; a physical disturbance may
also leave a restriction on later service. Recent influences and recovery
determine one current reading. Several history contributions do not mean
several independent service constraints.

The user's feedback 5 sharpens the actual choice: what determines the loss
and recovery of that single reading? It also adds a physical question about
slow A discharge, which cannot be resolved merely by observing an A queue.
The queue can be a consequence of the existing restriction; a second loss
needs an additional mechanism. One current reading is likewise not proof
that one scalar state can predict its future recovery.

**M1 — a representative E response.** This is the exact conditional model
above, formerly Option 1. Each admitted unit of E leaves a common fading loss;
those losses add to one shared restriction. A uses the available service and
can queue but creates no separate recovery burden. Its assumptions simplify
entry-speed and overlap dependence.

- **Pros:** complete equations with analytical conservation, storage,
  uniqueness and clearance support; a compact exact reference.
- **Cons:** actual boundary kinematics do not change the per-unit response;
  independent slow-A recovery and richer overlap behaviour are not explained.
- **Consequence:** retain as an unapproved conditional primary candidate and
  strong reference, with its proofs confined to its own exact law.

**M2 — a response tied to the traffic being discharged.** Refine the earlier
Option 2 into a shared-meter qualification target: relate new restriction and
recovery to admitted amounts, relevant insertion/crossing speeds and the
existing disturbance. A and E feed the same account where a distinct physical
contribution is justified. This is an unresolved law, not a new completed model.

- **Pros:** directly addresses the traffic-dependent update in the user's
  picture while keeping one point/service interface. A justified A effect
  can enter that same account.
- **Cons:** speed meaning, sufficient recovery state, overlap and causal
  feedback remain to be qualified. A queue is not automatically another
  capacity penalty, and M1's analytical guarantees do not transfer.
- **Consequence:** further bounded G3 review is needed before exact-law
  acceptance. No new spatial model or observation privilege is preapproved.

For the same slow E burst followed by queued A traffic, both have one reading.
M1 obtains it from the timing/amount of E and the common response. M2 seeks a
supported update from boundary kinematics and recovery, including A only for
an additional identified mechanism. After E stops, M1's recent E history still
fades; M2's corresponding recovery law is not specified yet.

**Updated provisional recommendation: qualify M2, retaining M1 as the exact
conditional reference.** This revises the previous Option 1 recommendation
because feedback 5 asks the model to account for discharged traffic and speed,
not only to use a single common service ceiling. The single-meter interface
alone already fits M1. No M2 equation or A penalty is adopted by this response.

[Full conceptual explanation, direct comparison, Pros/Cons and limits](vsl_feedback5_shared_service_meter_response.md)

**CP-D2 remains open, Type 2 under G3.** Its question is which inputs and causal
recovery rule should govern the shared service reading. The user owns the
methodological choice and the reviewer qualifies its law. A new independent
A-discharge burden is proposed for assessment, not approved by CP-D1's E-driven
selection. Unknown initial state would reopen G2; broken H1 protection reopens
its G3 interface; a wider endpoint reopens G4/S3-M2. None is adopted.

The M1 analytical candidate pass remains complete; M2's exact law is unresolved.
S3-M1/S3-M2 remain closed. The terminal amendment and the full Step 3 remain
open. Stop at the revised CP-D2 choice. Step 4 and simulator/experiment work
remain unopened.

[Papers viewed and exact adaptation boundaries](../../extraction/research_readiness/vsl_ph_source_and_adaptation_audit.md)

[Original M1 analytical work and checks](vsl_ph_work_report.md)

[Feedback 5 response work and verification](vsl_feedback5_work_report.md)
