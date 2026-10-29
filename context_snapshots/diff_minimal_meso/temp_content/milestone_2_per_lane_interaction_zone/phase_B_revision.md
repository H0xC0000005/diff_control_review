# Milestone 2 Phase B revision record

Status: **Milestone-global backbone closed; component-local discussion active**  
Decision date: **2026-09-04**

## Closed inherited contracts

Milestone 2 retains the agreed series decomposition (`U_a` upstream aggregate LTM plus `Z_a` downstream per-lane interaction zone), cumulative-mass/rank bins, an exact ordered route-mass ledger as semantic/update authority, fixed structural lane commitment, continuous vehicle-equivalent mass, and no clipping or silent reassignment. The M2 resolved-removal-plan seam remains exact and policy-neutral; M3 owns exact-FIFO versus bin-scale partial-FIFO service behavior and any lossy canonicalization.

## Closed global decisions

### G1 — Candidate A: geometry-authoritative physical partition

Author whole-link and interaction-zone physical geometry plus compatible triangular-FD primitives in a meso-owned wrapper. Derive `U_a` parameters for the residual upstream length, per-lane `Z_a` storage from geometry and jam density, and the grid layout from physical storage and the configured mass-bin resolution. Grid dimensions do not determine road length. If the zone spans the whole link, omit/bypass `U_a`; a zone longer than the physical link is invalid.

### G2 — Candidate A: homogeneous LTM boundary with fixed commitment

Reuse the accepted aggregate LTM equations over `U_a`. Transfer its eligible ordered mass conservatively into each entry's single precommitted lane, bounded by that lane's receiving capacity. Continue the stable scan past an entry blocked from its own lane so other independently committed lanes remain accessible; never search alternative lanes or balance load. Track explicit zone service eligibility, prohibit same-step admission/discharge, retain rejected mass upstream, and transmit storage restriction backward causally.

M3 may replace the passive-accessibility/no-cross-lane-blockage policy. It does not replace the M2 LTM propagation, fixed-commitment seam, conservative U/Z transaction, delay eligibility, or spillback infrastructure.

### G3 — Candidate A: fixed equal-mass lattice with partial capacity masks

Use one configured mass-bin width per scenario, fixed padded tensor shapes, explicit per-bin capacity/masks including partial final bins, and an atomically rebuilt cached grid. The ledger remains authoritative. Changing bin resolution changes representation fidelity, not physical lane storage or road geometry.

### G4 — revised Candidate A: movement-exclusive neutral service domain

Principal M2 service fixtures use only full-length node-reaching lanes, exactly one movement per lane, no lane starts/ends within the zone, no lane changing/reassignment, and only pre-update service-eligible resident mass. Aggregate movement quotas are replayed through deterministic capped/proportional same-movement lane bookkeeping and exact prefix removal plans. Shared-lane head blocking, pocket accessibility/overflow, intermediate merges, and cross-movement blockage are unrepresentable in the neutral domain and remain M3 responsibilities. Ordinary finite storage, entry/discharge capacity, signal service, downstream supply, and upstream spillback remain active M2 physics. Short lanes may appear only in isolated geometry/storage/ingress tests without behavioral claims.

### G5 — Candidate A under delegated authority: two-layer equivalence evidence

Use a validation-only matched split-domain aggregate comparator to isolate representation/coupling, plus a separately reported comparison with the original unsplit M0 link to characterize subdivision effects. Reference-only flow must not become a production dependency. The comparator must mirror the closed G1/G2 equations and indexing.

### G6 — Candidate A: fixed-structure piecewise differentiation evidence

Validate reverse-mode AD, JVP/directional derivatives, and central finite differences along the continuous ledger mass/timing to route-to-movement projection to overlap/rebinning to grid to storage/service/output path. Route IDs, positions, movement/lane labels, order skeletons, topology, and active-set signatures remain structural and nondifferentiated. Compare derivatives only under stable signatures; do not add smoothing or surrogate gradients.

## Dependency result and reopen rule

The choices are mutually compatible. G1 supplies geometry-derived storage/delay inputs to G2 and capacity masks to G3; G4 holds M3 behavior inactive; G5 mirrors G1/G2; and G6 validates the continuous path. A component-local decision may not alter these contracts. Evidence of conflict reopens the smallest affected global decision and its dependents explicitly.

## Next Phase B activity

Discuss and close component-local questions serially in dependency order, Components 2.1 through 2.6. Then perform a final global/component consistency audit before requesting Phase C approval.
