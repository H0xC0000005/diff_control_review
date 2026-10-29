# RM6 source-transfer audit — ramp action, hidden target-lane receiving and service

Date: 2026-10-01. Scope: bounded reuse of the closed ramp corpus and the later
S12–S13 finite-receiving evidence. No broad discovery search or new source
download was needed.

## Historical ramp evidence retained

| Evidence | Established result | RM6 consequence |
|---|---|---|
| RM0024, first-order coordinated ramp discrete adjoint | Time-dependent ramp-control gradients and finite-difference verification exist in a macroscopic freeway model. | Generic differentiable ramp control is prior work and must be a strong baseline. |
| RM0025, multiclass network discrete adjoint | Piecewise exact numerical gradients exist for multiclass conservation laws with merges, diverges and buffers. | Classes, route memory and buffers cannot be presented as new solely because they are differentiated. |
| RM0002 and the historical control screen | Strong aggregate/structured ramp controllers can be near-optimal under their declared assumptions. | The comparator cannot be a memoryless weak controller. |
| RM0009 FIFOQ and RM0016 destination-aware control | Route-composition memory and destination-aware aggregate state are credible alternatives to exact order. | Any lane/order claim must survive route-aware and compressed-state baselines. |
| FB0008/FB0009 and FHWA ramp guidance | Fair feedback, coordinated nonlinear MPC, finite ramp storage, queue override and spillback are established concerns. | Ramp queue and storage belong in every candidate and outcome; they are not the missing selective state. |
| Closed D1/B1-P audit | A non-overlap order construction is coherent but repeats the downstream ordered-service hypothesis and is not representative of ordinary overlapping merge traffic. | RM6 does not revive B1-P or use bookkeeping serialization as physical merge order. |

## New transferable evidence since the historical closure

The later VSL review inspected a continuous lane-resolved merge/service family:

- Carey, Balijepalli and Watling model conservative per-lane CTM transfer,
  mandatory lateral demand and finite target receiving shared by longitudinal
  and lateral entrants, with a gap/headway factor for lateral traffic.
- Nagalur Subraveti, Knoop and van Arem provide paired conservative lateral
  transfer, lane-end incentives and target-lane receiving constraints.
- Laval and Daganzo, Srivastava and Jin, and Leclercq et al. independently
  support lane-change/merge activity changing effective service or capacity;
  Leclercq's native context is an active freeway merge.
- S13 then showed analytically that a continuous finite-receiving member can
  make hidden merge preparation decision-relevant for common VSL. That proof is
  not a ramp-metering result, but it removes the earlier presumption that only
  microscopic gap sequences can represent a consequential merge penalty.

These sources are mapped in the
[S12 audit](../../differentiable_freeway_bottleneck_task_review/extraction/s12_advice_merge_service_source_audit.md)
and [S13 audit](../../differentiable_freeway_bottleneck_task_review/extraction/s13_m2_source_to_equation_audit.md).

## RM6 evidence chain

| Link | Evidence status | Boundary |
|---|---|---|
| Infrastructure meter → ramp demand/release history | Direct and mature in ramp-control literature. | Does not itself create a resolution gap. |
| Mainline lane state → target-lane receiving/merge work | Direct structural support in continuous lane-resolved models. | Exact safe-gap sequences and microscopic lane changes are not adopted. |
| Metered lateral demand + mainline target demand → endogenous service | Structurally supported by finite-receiving models and active-merge capacity literature. | Priority, parameter range and exact response law remain unfrozen. |
| Hidden target-lane state under road-total history | Algebraically coherent and supported by the S05/S13 information logic. | No ramp-specific exact reachable-history pair has been constructed. |
| Hidden state → different useful meter action | Plausible but not established. Metering changes lateral demand directly, yet complete all-stream accounting may restore a common best release policy unless merge interference changes service enough. | Requires a separately approved analytical formulation/certificate. |
| Hidden state → useful gradient | Only a candidate path. | No ramp-specific derivative or independent usefulness result. |

## Representation implication

The smallest consequential state may be a scalar target-lane merge-pressure or
receiving-work statistic. Full lane state is not justified merely because the
mechanism is lane-resolved. A fair future ladder is:

1. strong aggregate/multiclass ramp state and history;
2. the same state plus a merge-pressure statistic;
3. target-lane versus remaining-mainline grouped state; and
4. fuller lane state only if the compressed closure fails.

## Source judgment

The historical assertion that realistic ramp-specific value necessarily needs
microscopic behavior is now too strong. A conservative continuous-mass
finite-receiving family is available for analytical testing. The historical
conclusion that generic ramp gradients and aggregate queue control are mature
remains unchanged.

The literature does not supply one jointly validated model that combines the
declared strong observer, hidden target-lane preparation, infrastructure meter,
complete all-stream objective and different optimal actions. RM6 can therefore
admit a task family for further analytical review, not claim that the core ramp
question is answered.
