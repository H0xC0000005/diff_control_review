# Milestone 2 component-question crosswalk — draft

Status: **Advisory draft; no component decision is made here**  
Prepared: **2026-09-15**

## How to use this crosswalk

This file maps the review findings in the companion supplement to the existing
Milestone 2 Phase B component-question inventory. It identifies where a future
planning agent should test a candidate for compatibility with the accepted
downstream task. It does not amend candidate text, endorse a component candidate,
or add a parallel decision process.

The active serial closure order remains Components 2.1 through 2.6. Review
traceability should be checked within that order and again in the final
global/component consistency audit.

## Crosswalk

| Review finding | Existing owner(s) | Methodology-side check during the existing decision | Required outcome before Phase C |
|---|---|---|---|
| RF-M2-01: scenario semantics remain explicit and reusable | C2.1-Q1, C2.1-Q3, C2.5-Q1 | Verify that lane order, permissions, route/movement maps and scenario groupings are explicit, jointly permutable, and not hard-coded to one four-leg layout | The later symmetric four-leg/four-group fixture is expressible and rotation-testable through general structures |
| RF-M2-02: neutral refinement has an identifiable comparator | C2.5-Q2, C2.6-Q1, C2.6-Q3 under G5 | Keep the matched split-domain comparator separate from the original unsplit M0 comparison; label both and retain their configuration/provenance | Representation neutrality cannot be confused with link-subdivision error |
| RF-M2-03: all physical mass can be counted once for later TST | C2.2-Q1, C2.3-Q3, C2.5-Q1, C2.5-Q3, C2.6-Q3 | Expose disjoint physical ownership and route/location transitions; mark grid and ledger as synchronized views, not additive accounts | A later objective can count source and network mass once without behavioral reconstruction or double counting |
| RF-M2-04: continuous derivative path and active signatures | C2.2-Q1, C2.3-Q2, C2.3-Q3, C2.4-Q3, C2.4-Q4, C2.6-Q2 | Ensure continuous tensors remain connected and each structural/active change is diagnosable; keep labels and topology nondifferentiated | Reverse AD, JVP and central finite differences can be compared on stable signatures without smoothing |
| RF-M2-05: M2→M3 service seam remains policy-neutral | C2.2-Q3, C2.3-Q2/Q3, C2.4-Q2/Q3, C2.5-Q1/Q3 | Preserve exact ledger authority and a resolved-removal-plan/application boundary; avoid assuming the eventual policy is necessarily one scalar prefix; measure fragmentation without lossy repair | M3 can select exact or approved bounded bin-scale behavior without rewriting physical ownership/coupling |
| RF-M2-06: comparison seams exist without later baselines | C2.5-Q1/Q2, C2.6-Q1/Q3 | Preserve common scenario inputs, explicit refined/unrefined dispatch, comparable outputs, and independent reference evidence | Later baselines can be added as separate realizations without becoming M2 production dependencies |
| RF-M2-07: ramp metering is not a parallel task | Scope audit across C2.1–C2.6 | Reject requirements introduced only for freeway lane change, weaving, capacity-drop hysteresis, ramp control or independent speed behavior | No M2 interface or acceptance burden is justified solely by the closed ramp branch |

## Question-specific notes

### Component 2.1 — topology, geometry, and storage

- **C2.1-Q1:** the selected composition root should retain general network and
  refined-link identity. The review does not require a four-leg-specific wrapper.
- **C2.1-Q2:** the downstream task does not justify new lane-specific fundamental
  diagram physics in M2. Geometry/storage expressiveness should not be confused
  with activating bay blockage behavior.
- **C2.1-Q3:** permission completeness and canonical lane order are the principal
  carriers of RF-M2-01. A rotation/permutation test must transform permissions,
  route-to-movement mappings, commitments, and result interpretation together.

### Component 2.2 — exact lane-local state and commitment

- **C2.2-Q1:** distinguish physical ownership from synchronized views. Continuous
  ledger mass/timing needed by later projection and accounting must remain on the
  graph.
- **C2.2-Q2:** commitment remains structural in M2. The future task does not
  authorize behavioral lane choice or reassignment here.
- **C2.2-Q3:** exact adjacent merging is allowed, and fragmentation telemetry is
  useful. The component must not decide the later within-bin homogenization or
  defragmentation policy.

### Component 2.3 — cumulative-rank grid

- **C2.3-Q1:** bin resolution changes representation resolution, not physical
  storage or scenario geometry. No numerical resolution is fixed by the review.
- **C2.3-Q2:** overlap/incidence changes belong in the active signature. The
  application interface should be able to consume a future resolved removal plan
  without embedding the plan-generating policy.
- **C2.3-Q3:** if the grid is cached, it remains a deterministic view of the exact
  ledger. It cannot be counted again in total system mass.

### Component 2.4 — internal physics and feedback

- **C2.4-Q1/Q2:** preserve physically matched capacity/storage assumptions needed
  by the split-domain comparator. Do not tune them to force equality with the
  unsplit finite-step trace.
- **C2.4-Q2/Q3:** neutral M2 service may use only the closed movement-exclusive,
  no-blockage contract. Keep eligibility and removal application modular so M3
  can replace the plan-generating policy.
- **C2.4-Q4:** numerical handling must report invalid storage/conservation states;
  it must not clip away discrepancies that later TST accounting would hide.

### Component 2.5 — rollout composition

- **C2.5-Q1:** reserve immutable scenario identity and authoritative histories for
  source, aggregate-region, lane-zone, downstream, and completion mass. This is
  readiness for the later clearance-complete objective, not a requirement to
  implement that experiment now.
- **C2.5-Q2:** explicit refined/unrefined dispatch is also the clean seam for
  later representation comparisons. Do not run two physical owners and reconcile
  them after the fact.
- **C2.5-Q3:** conservation evidence should be sufficiently disaggregated to
  detect double ownership and route/location swaps, while remaining derived
  diagnostic state.

### Component 2.6 — reference and evidence harness

- **C2.6-Q1:** the independent oracle floor should cover the new physical
  partition, overlap, admission, eligibility, and one-step conservation. It need
  not implement the later task or another full simulator.
- **C2.6-Q2:** extend the accepted derivative scan with local structural
  signatures; interpret only stable-signature rows as smooth derivative checks.
- **C2.6-Q3:** record which comparator was used, all resolved physical inputs,
  signature/tolerance evidence, and physical ownership totals. Avoid claims of
  downstream usefulness at M2 closure.

## Final consistency-audit questions

Before a future Phase C request, the ordinary Milestone 2 consistency audit
should be able to answer all of the following without relying on this supplement
as an authority:

1. Can a general structural API express and rotate the intended four-leg task
   fixture without hard-coded cardinal directions or group count?
2. Is matched split-domain neutrality reported separately from comparison with
   the original unsplit Milestone 0 link?
3. Can every released mass unit be assigned to exactly one physical location or
   completion state while ledger/grid views remain non-additive?
4. Is the continuous local path testable by AD, JVP, and central differences
   under an explicit stable signature?
5. Can Milestone 3 replace only the service/removal-plan policy while retaining
   M2 physical ownership, conservative coupling, and exact ledger authority?
6. Are later baselines and richer evaluators attachable without entering M2
   production behavior?
7. Has ramp metering remained an excluded task rather than a hidden source of
   new requirements?

A negative answer should be handled through the existing component question or,
if necessary, an explicit reopening of the smallest affected global contract.
This supplement itself cannot resolve the conflict.
