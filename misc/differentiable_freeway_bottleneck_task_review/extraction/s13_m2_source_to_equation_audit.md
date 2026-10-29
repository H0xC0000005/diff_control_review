# S13 M2 source-to-equation audit

Date: 2026-09-30. Scope: targeted reuse of primary sources already inspected in
S05/S12. No broad discovery search was needed. This audit separates direct
source structure, bounded analytical adaptation and original deduction.

## Contract summary

S13 reduces the three upstream lanes to two analytical groups: the ending lane
and the continuing-lane group. The reduction retains the state relevant to
mandatory transfer while avoiding lane-specific control. One common VSL sets a
shared longitudinal travel speed through a fixed preparation zone. Conservative
lateral transfer can occur while traffic traverses that zone. Traffic still in
the ending lane at the choke consumes extra target-lane receiving work.

The contract is a conditional analytical member of the admitted M2 family. It is
not a transcription of one paper, a calibrated model or a claim that the same
functional forms hold empirically.

## Source map

| Contract element | Evidence basis | S13 use | Boundary |
|---|---|---|---|
| Per-lane continuous conservation and paired lateral transfer | [FB0030 study](n2_source_studies/FB0030.md), equations 1–4 and 12–22 | Ending-lane outflow is exactly continuing-lane inflow; total mass is invariant. | The complete published incentive/branch system is not adopted. |
| Mandatory lane-end incentive and spatially distributed transfer | FB0030 equations 6–11; [Carey et al. author manuscript](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf), mandatory-demand scenarios | Positive ending-lane mass transfers progressively in a fixed preparation zone. | S13's constant active-branch transfer rate is an analytical specialization, not a reported calibration. |
| Finite target receiving and neutral proportional allocation | Carey et al., sections 4–5, especially gap factor and priority rule R2 | Same-lane and lateral demand share finite receiving in proportion to effective demand. | Exact zero-demand conventions are supplied by S13; alternative priority rules are outside the certificate. |
| Extra receiving work for lane-changing traffic | Carey et al., section 5: lane-changing headway ratio and receiving constraint | Remaining ending-lane mass has receiving-work factor greater than one at the choke. | The factor is a conditional class parameter, not an empirical estimate adopted from the paper. |
| Common VSL at a permanent three-to-two lane drop | [S06 source audit](s06_reference_mechanism_source_audit.md), S06-S3 | One lane-uniform speed controls traversal time through the preparation zone. | The paper's microscopic calibration and finite-horizon discharge objective are not adopted. |
| Common limits may affect lane preparation | S06-S2 and [FB0039 extraction](rb_source_studies/new_lane_evidence.md) | Supports reachability of a common-speed/lane-state path. | Effect magnitude and sign are mixed; no direct response coefficient is imported. |
| Strong aggregate VSL/capacity-drop alternative | [FB0022](https://doi.org/10.1111/mice.13492) and prior evidence register | Defines the concrete aggregate countermodel class. | It is not assumed to contain hidden lane allocation. |
| Exact early information collision and fixed-service obstruction | [S05 analysis](../synthesis/s05/rb_certificate_analysis.pdf) | Supplies the predecision equal-history handoff and theorem that M2 must escape. | The near-drop action result is an original S13 deduction. |

## Adopted state and units

| Symbolic role | Unit | Status |
|---|---|---|
| Total affected cohort mass | veh-eq | Common and observed. |
| Ending-lane fraction | dimensionless | Hidden structural preparation state; differs between paired cases. |
| Ending/continuing mass | veh-eq | Continuous differentiable state after the decision. |
| Preparation-zone length | km | Common fixed geometry. |
| Lane-uniform advice speed | km/h | Only action; common to all lanes. |
| Zone traversal time | h | Determined by length divided by advice speed. |
| Active-branch lateral transfer rate | 1/h | Common positive class parameter. |
| Choke receiving-work rate | veh-eq/h | Common finite service parameter. |
| Lane-change receiving-work factor | dimensionless | Common class parameter greater than one. |
| Per-cohort mean total time | h/veh-eq interpreted per vehicle equivalent | Primary complete-accounting outcome. |

## Direct adoption, adaptation and original deduction

### Direct structural adoption

- continuous lane masses;
- paired conservative lateral transfer;
- mandatory lane-end demand;
- finite target receiving;
- gap-weighted lateral receiving demand; and
- neutral demand-proportional allocation in a binding-receiving regime.

### Bounded analytical adaptations

1. **Ending versus continuing groups.** Two continuing lanes are aggregated only
   after assuming symmetry within that group. Ending-lane mass remains explicit.
2. **Constant transfer-rate branch.** Over one fixed preparation zone, the
   density/geometry-driven transfer law is restricted to a positive constant-rate
   linear branch. This provides a deterministic continuous-mass analogue of
   repeated CTM lateral transfer. It is not claimed as a universal behavioral law.
3. **Batch handoff at the choke.** A common-speed cohort reaches the choke after
   the same traversal time within each action. A homogeneous proportional service
   phase then clears the complete cohort. This isolates service workload without
   introducing vehicle order.
4. **Gap work rather than microscopic gaps.** The gap factor counts additional
   receiving work and does not model individual headways or particles.

### Original S13 deductions

- the exact strong-history spatial handoff from S05 into the fixed preparation
  zone;
- the closed-form complete-accounting objective;
- the open parameter conditions yielding different optimal common actions;
- positive observer-only minimax regret; and
- the conditional conceptual gradient-direction result.

These are review deductions, not findings attributed to the cited papers.

## Conservation and zero-state audit

The lateral law removes and adds identical mass, so ending plus continuing mass
is constant. At zero ending-lane mass, lateral flow is exactly zero without a
ratio or fallback. At zero gap surcharge, the service workload reduces to total
mass and every state selects fastest advice. At zero transfer rate, the model
returns to an action-independent hidden-state service workload and the S05
arrival-dominance logic reappears.

No clipping, stochastic sampling, integer rounding, hidden mass deletion or
outcome-selected capacity branch is used.

## Evidence limits

The source record does not validate the constant transfer-rate specialization,
its numerical range or the batch/proportional choke as a field model. It also
does not show that an actual freeway common VSL produces the analytical action
split. S13 can therefore establish a conditional existence certificate within a
source-bounded M2 class, not empirical necessity, calibration or universal lane-
contrast value.
