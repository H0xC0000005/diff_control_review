# D1 mechanism evidence: point diverge, cohort FIFO, and the merge-order boundary

Date: 2026-09-15

This note records the source-level basis for the D1 verdict. It separates what the literature establishes from the reviewer's proposed task restriction.

## 1. Source findings

### RM0018 — Wright et al., *On node models for high-dimensional road networks*

Full public preprint: `../archive/full_text/RM0018.pdf`; DOI: `10.1016/j.trb.2017.09.001`.

- PDF pp. 3–4 define a first-order node as a no-storage mapping from per-commodity demands, split ratios, output supplies and input priorities to aggregate input-output flows. Commodity restrictions are proportional; the paper explicitly interprets this as isotropic mixing rather than a realized route sequence.
- PDF pp. 5–6 show why full FIFO at a multilane off-ramp can over-block every lane. Splitting lanes into links creates a lane-assignment and weaving/lane-change problem.
- PDF pp. 9–13 define mutual-restriction intervals. These exogenous lane-geometry parameters interpolate between full FIFO and no FIFO while retaining aggregate movement/commodity flows.
- PDF pp. 24–27 show that merge priorities affect aggregate supply allocation and queue direction. They do not define a physical total order among simultaneously admitted mass from different inputs.

**Use here:** strong first-order partial-FIFO comparator and proof that lane geometry can be represented parametrically at a node. **Not established:** exact cross-input chronology, endogenous lane access, or value of ordered mass.

### RM0021 — Carey et al., *Implementing first-in-first-out in the cell transmission model for networks*

Full accepted manuscript: `../archive/full_text/RM0021.pdf`; DOI: `10.1016/j.trb.2014.04.001`.

- PDF pp. 2–4 distinguish homogeneous proportional mixing from time-labelled route cohorts. Their example shows that proportional mixing can reverse or blur the intended order of two route types even though aggregate flow is conserved.
- PDF pp. 6–8 define finite route/time cohorts: FIFO level 2 tracks entry time to the current cell; FIFO level 3 tracks entry time to the current link. The paper stresses that full route FIFO would require still richer history.
- PDF pp. 15–16 process a diverge from the earliest eligible cohort. If the next route-B mass cannot enter output B, later route-C mass can be stuck behind it unless an immediately eligible cohort contains only C. This is a direct first-order precedent for an order-sensitive point-diverge service rule.
- The same section handles a merge in two stages: first compute the aggregate A-to-C and B-to-C quantities, then process each input's internal cohorts separately. It does not define the combined total order of A and B inside output C when both enter at the same time.

**Use here:** source-backed point-diverge order mechanism and precise comparator hierarchy. **Not established:** a physically unique merge interleaving for overlapping continuous inputs or a differentiable ramp-control experiment.

### RM0022 — Boukhellouf, Buisson, and Chiabaut, *Merging and diverging operations: benchmark of three European microscopic simulation tools and comparison with analytical formulations*

Open-access final article: `../archive/full_text/RM0022.pdf`; DOI: `10.1186/s12544-023-00586-1`.

- PDF p. 2 defines the elementary benchmark as one upstream lane leading to two downstream lanes at a point diverge.
- PDF p. 7 states that FIFO preserves upstream appearance order at the diverging point. The point construction is deliberately chosen so that discretionary lane changing is not triggered.
- PDF pp. 7–8 also warn that real multilane diverges can depart from FIFO because of lane changing, anticipation, and destination-dependent lane use.
- PDF p. 11 reports that all three microscopic tools reproduced the elementary macroscopic diverge diagram and showed no significant diverge capacity drop in that simple case.

**Use here:** a plausible richer-evaluator reference case for an intentionally elementary, no-lane-change point diverge. **Not established:** exact within-cohort order benefit, operational representativeness of a real multilane off-ramp, or a gradient result.

### RM0009 — Salehi, Somers, and Seibold, FIFOQ

Archived preprint: `../archive/full_text/RM0009.pdf`.

- PDF pp. 6–8 add a local vertical queue that tracks excess exiting/non-exiting composition while retaining lane-aggregated LWR links.
- PDF pp. 10–15 demonstrate that route-composition memory can avoid both full-FIFO over-blocking and non-FIFO rerouting, while explicitly acknowledging that the assumed road-width split is not generally realistic.

**Use here:** strong aggregate memory comparator. A result explained by FIFOQ is not evidence that exact order is necessary.

### RM0013, RM0017, and RM0023 — empirical/task context and lane boundary

- RM0013 (Muñoz and Daganzo) reports both one-pipe FIFO blockage and persistent multi-pipe regimes near a congested real off-ramp. It supports the physical relevance of destination composition but rejects any universal fixed full-FIFO or fixed partial-FIFO interpretation for real multilane sites.
- RM0017 (Cassidy) supplies the aggregate causal argument that upstream metering can alter downstream destination composition and delay. It does not establish selective-order necessity.
- RM0023 (Newell) models exiting and through vehicles as separate interacting queues on different lane sets along a freeway section. It is compatible with kinematic-wave reasoning but is not a point-node-only realization; it supports the boundary between the narrow point case and a distributed special-lane model.

## 2. What the evidence jointly supports

The literature supplies three distinct levels that must not be conflated:

1. **aggregate full/partial FIFO:** movement demands, supplies, route proportions, and fixed restriction parameters;
2. **aggregate composition memory:** an extra route-specific queue or time cohort that remembers which class is delayed;
3. **realized ordered service:** route-labelled mass is served in its actual sequence, so an inaccessible head can block later accessible mass.

Level 3 has a first-order point-diverge precedent. It does not require lane changing when the incoming approach is deliberately a single ordered stream. This closes the downstream-mechanism part of RQ1 for an elementary construction.

The remaining physical issue occurs upstream at the merge. Published first-order merge models allocate quantities/priorities; they do not automatically supply a unique combined chronology for simultaneously entering continuous streams. This agrees with the project's closed M1 statement that whole-package serialization is bookkeeping, not physical lane-entry chronology.

## 3. Reviewer construction and its evidential status

The proposed **chronology-safe B1-P** restriction is a review inference, not a copied literature method:

- mainline and metered-ramp eligibility intervals at the merge must be non-overlapping in every admitted scenario;
- actual time then gives an unambiguous combined order without sub-packet interleaving or lane-changing dynamics;
- the merged one-stream link feeds a fixed-supply point diverge whose ordered service follows the Carey-style earliest-cohort semantics;
- route totals, control action, supplies, objective accounting, and physical time step remain matched across exact-order and aggregate comparators.

This is physically coherent as a mechanism-isolating proof case, but it is intentionally not a claim about ordinary continuously overlapping freeway flows. Removing the non-overlap restriction would require a new merge-order contract or richer lateral/microscopic physics.

## 4. Access and uncertainty

RM0018, RM0021, and RM0022 are archived locally and were read in full at the cited sections. RM0023 was inspected through publisher metadata/abstract and is not used alone for a positive task claim. The public Muñoz–Daganzo working-paper mirror timed out during bounded retrieval; the publisher/UC Berkeley record was sufficient for the limited empirical regime statement and no exact equation from it is adopted.

