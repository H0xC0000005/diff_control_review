# A point merge can have physical queues; its service law is the remaining choice

**Subsequent decision, 2026-10-15:** the user selected P-H, closing CP-D1.
The resumed pass delivers a concrete recovery-work node at CP-D2's exact-law
confirmation gate. The text below preserves the first pass and its then-open
choice; it no longer means that P-H/P-E selection is pending.

[P-H approval and scope](vsl_ph_selection_and_scope.md)

[Current model, analytical findings and confirmation gate](vsl_ph_recovery_work_findings_and_gate.md)

**C-P's bounded terminal review is opened and substantively begun,
2026-10-14.** The first source/interface pass is complete at VSL-CP-G1.
It establishes a coherent candidate interface and conditional storage/time
checks. It does not complete the coupled-law sprint or all of Step 3.
The first genuine choice is how the node represents the loss of service:
a compact rule for the observed capacity reduction, or a causal representation
of slow entry and recovery. Neither exact law is adopted.

The traffic picture is now clearer. E and A approach the same compulsory
boundary on finite physical lanes. A slow E entry can restrict A's service.
Both lanes may then hold traffic. Vehicles stop contributing to local TST
when they cross the choke, but any continuing service restriction must be
predicted rather than erased at that crossing. H1 still supplies the prepared
arrival streams; a new spatial preparation region is not required by the
first interface checks.

[Opened review plan, questions and stop conditions](vsl_cp_qualification_review_plan.md)

[Accepted C-P direction and choke-line objective](vsl_step3_coupled_point_decision.md)

## What model can now be formed at the interface level?

A **two-queue physical terminal with coupled point service** is a viable
architecture. Retain the existing lane entrance/departure histories, physical
stock, minimum-travel eligibility and sending/storage limits. Replace A's
automatic departure with a jointly determined A/E departure rule. A record
of service restriction or past admissions may be added if the selected law
needs it. That record is predicted state; it is not extra traffic mass or
future reference information.

For example, suppose E enters at a low speed. A's available service falls,
so a queue can form in the continuing terminal lane. If the influence remains
after that E entry, the selected state must keep it until its stated recovery
rule releases it. Simply setting E's remaining mass to zero must not silently
reset a restriction whose physical cause still persists.

| Interface | Direct requirement and finding |
|---|---|
| **Inputs** | H1's E/A/B entrance histories, the shared physical parameters/advice and known initial terminal/service state. No future receiving trace is supplied. |
| **Predicted state** | E and A eligible queues and physical stocks; only the additional service state/history justified by the selected closure. B retains its independent reference behaviour unless a separate reason requires reopening it. |
| **Outputs** | Conservative, physically eligible lane departures; resulting terminal receiving and complete local cohort time. Continuing priority is compatible with A delay when shared service is restricted. |
| **H1 handoff** | The old sufficient total-mass/storage bound still protects the handoff for any admissible departures. Its proof did not require immediate A service. |
| **Objective** | Keep road travel plus all eligible queue areas, now including A. Post-line vehicle-time remains excluded; service influence is not discarded. |

This forms the shared interface, not the missing constitutive law. The latter
must determine the available service and actual departures causally, prove
clearance, and supply its parameter/entry-speed interpretation.

## The source finding that prevents a premature equation choice

The inspected point-merge mechanism does not need a spatial *insertion*
zone. Leclercq, Laval and Chiabaut's 2011 conference paper examines entry
at one location followed by limited acceleration; passing counts are obtained
from that motion and wave propagation. The source's zero insertion length
does not mean zero approach/storage or no downstream influence. Its capacity
formulation describes mean discharge over an insertion process, rather than
our whole finite-cohort update and clearance law.

[Inspected 2011 primary paper text](https://www.researchgate.net/publication/251530773_Capacity_Drops_at_Merges_an_endogenous_model)

Leclercq et al.'s 2016 manuscript likewise derives effective mean capacity
from insertion headways, entry speeds and acceleration. Its discussion
distinguishes mean discharge from time-varying flow. Substituting the current
continuous E flow into a mean formula is therefore a new approximation;
it does not automatically retain a completed entry's transient influence.
The old H1/T1 boundary counts also do not specify an individual insertion
speed. That speed/history mapping is still part of the coupled-law review.

[Inspected 2016 manuscript, point case and discussion](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6)

There is also a strong simpler model. Jin, Gan and Lebacque supply a first-order
node with reduced capacity under congestion, including a merge extension.
Its purpose is to reproduce capacity reduction and waves. The authors state
that the reduction magnitude is calibrated and the underlying merging
mechanism is not explained. It is a serious compact rival, not an inferior
baseline merely because it lacks vehicle trajectories.

[Inspected point-capacity model and merge extension](https://arxiv.org/pdf/1310.2660)

These sources support point coupling, but they do not provide one already
qualified continuous-mass, finite-population C-P law. A priority split alone
represents competition for service, not necessarily the reduction caused by
slow entry. A selected instantaneous mean formula must not gain a recovery
law through a numerical lag or an unapproved smoothing rule.

## What the analytical interface checks establish

**H1 can remain protected while A queues.** In the accepted conservative
domain, the entire cohort fits inside one terminal lane's jam storage.
Each lane's cumulative entries are at most that total. Therefore its physical
vacancy stays positive even if its departures slow or temporarily stop.
This is a sufficient analytical restriction, not a general spillback solver
or a native SUMO admission result.

**Complete time must now charge A's delay.** The travel-plus-queue identity
extends directly when conservative departures replace immediate A service.
The extra term is A's eligible queue area. Service memory is not counted as
another vehicle queue. The new identity says where the costs belong; it
does not determine their magnitude or the best advice.

**Compact initial information can remain sufficient conditionally.** If the
new service state starts in a known empty condition, and its causal law is
uniquely determined from the predicted histories, the same initial ending
scalar reconstructs the inputs and future state. This is an interface
deduction. Existence/uniqueness of that law and the old action/gradient
certificate are not established by it.

**Clearance remains a law-specific obligation.** A positive lower bound on
total departure flow whenever eligible traffic remains is sufficient to
clear a finite cohort. A capacity state that can stay shut does not inherit
the predecessor's positive-service proof. The selected law must supply its
own bound or another valid clearance argument.

[Conditional mathematics and precise limits](../../synthesis/research_readiness/vsl_cp_interface_foundations.pdf)

| Opened question | Core answer from this pass | What remains |
|---|---|---|
| **CP-Q1: service origin** | Point coupling has both mechanism-based and phenomenological source precedents. They make different physical/evidence commitments. | Select the closure philosophy at the gate below before exact transcription. |
| **CP-Q2: retained influence** | Past completed entry may remain relevant. Current queues and mean insertion rate are not automatically a valid recovery state. | Specify the entry-speed and finite-time state/update rule for the selected closure; a one-scalar recovery reduction is not proved. |
| **CP-Q3: storage/accounting/MP6** | A/E terminal queues fit the existing storage/time interfaces under the stated conservative conditions; immediate A service is unnecessary for handoff protection. | Exact coupled service, well-posedness, clearance and an applied domain remain unqualified. |
| **CP-Q4: information/gradient/reference** | Known empty state plus an autonomous unique law would preserve compact initialization. A queue contributes to the full derivative and SUMO must judge service independently. | Recheck the amended action/sensitivity results and native mapping; no gradient or traffic usefulness is tested. |

## VSL-CP-G1: what kind of compact service law are we qualifying?

**Problem statement, CP-D1.** Should C-P's primary node represent observed
capacity reduction directly, or retain a causal slow-entry/recovery mechanism
in continuous service state/history?

**Assumed model-chain function.** This is component 6's missing map from
prepared arrivals and previous admissions to present shared service and
conservative departures. The output feeds existing terminal queues and the
fixed choke-line objective. Neither choice adds a recovery-time objective
or changes C-P's point location.

**Core gap.** C-P selected the physical location, through-traffic coupling
and local completion convention. It did not select an effects-only capacity
closure, or approve averaging the source vehicle process into a transient
continuous law. The differences affect what speed, entry state and history
mean in the model and what its gradients can claim.

### P-E: represent the capacity-reduction effect directly

Use a conservative priority node with a declared reduced shared capacity
under a congestion/activation condition. E and A can queue and their queues
feed physical propagation. Its retained activation/congestion state determines
whether service has recovered. Keep the native source form as a baseline;
any adaptation that ties activation to E or changes priority must be explicit.

In a short burst of E traffic, this model judges service using its selected
activation state and calibrated capacity. It need not reconstruct the speed
and acceleration of each completed entry. An A backlog can persist after
E leaves; that does not establish equivalence to slow-leader recovery.

- **Pros:** compact, continuous and directly compatible with demand/supply
  propagation. It has a strong published precedent and can represent reduced
  throughput and A delay without a new spatial preparation model.
- **Cons:** it does not explain the speed/recovery mechanism. Activation,
  capacity magnitude and priority need provenance, and source switching can
  be discontinuous. It may reproduce mean capacity while missing finite-burst
  timing. No smoothing or favourable capacity calibration is preapproved.
- **Dependency and consequence:** Type 2 G3/evidence interpretation. Selecting
  it as primary would explicitly make C-P a phenomenological interaction
  benchmark. The mechanism-based source and native SUMO still constrain
  development qualification; claims about inserting-speed causation narrow.

### P-H: retain causal slow-entry/recovery service history

Qualify a continuous service state or temporal history driven by completed
E admissions and a declared entry-speed/recovery relation. Past admissions
can continue to restrict present A/E departures. The physical terminal holds
traffic; the additional record holds influence, without converting mass to
individual cars or storing longitudinal trajectories in H1.

For the same short E burst, recent slow entries can leave a service restriction
after E's measured completion; a sufficiently recovered history need not
leave the same restriction. The number and form of continuous states must
be derived or explicitly qualified, rather than assuming one state is enough.

- **Pros:** matches the user's causal emphasis while keeping C-P's point
  accounting and elementary upstream model. It separates ending mass waiting
  to merge from the remaining influence of traffic already admitted.
- **Cons:** the inspected mean-capacity formulas do not provide this exact
  finite-time reduction. Entry speed, response duration and interactions need
  a defended constitutive law. Uniqueness, clearance and sensitivity are open;
  it must not be sold as exact adoption of the source particle mechanics.
- **Dependency and consequence:** Type 2 G3 service/state qualification, with
  G2 only if an unknown initial state is introduced. Keep the native-event
  source as physical evidence and the simple capacity-drop node as a rival.
  If a continuous temporal reduction fails, stop before adopting particles,
  spatial recovery or a widened objective.

**Provisional recommendation: P-H.** It best preserves the accepted emphasis
on slow compulsory entry affecting continuing traffic, including influence
after completion. P-E remains a mandatory strong simpler rival and is a
viable primary if its effects-only interpretation is explicitly accepted.
Neither law nor branch is selected here. No exponential kernel, recovery
parameter, node priority share or numerical scenario is proposed as fixed.

CP-D1 is Type 2 under G3, owned by the user for methodological selection and
the reviewer for source qualification. S3-M1 and S3-M2 remain closed; this
is a dependent service-law choice within their accepted scope. Type 1
transcription follows the selected physical contract.

The initial source/interface pass is finished at this gate. The complete
C-P terminal-law review and Step 3 remain open. MP6 has conditional storage
and accounting support, not a complete admitted coupled law or calibrated
traffic regime. Step 4, code, installations, experiments and the ramp line
remain unopened. Stop here for CP-D1; do not proceed through the new
methodological choice automatically.

[References actually viewed and their limits](../../extraction/research_readiness/vsl_cp_source_and_interface_audit.md)

[Work, commands and checks](vsl_cp_opening_work_report.md)
