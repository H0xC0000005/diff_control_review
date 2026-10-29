# H1: source support, analytical adaptation and limits

Date: 2026-10-13. Scope: homogeneous upstream receiving/transfer qualification
and its compulsory lane-end interface. No traffic rollout, simulator
implementation, calibration or gradient-usefulness experiment was performed.

## References viewed in this pass

This is the reference list of papers viewed, rather than a collection of full
PDFs. Older source lists remain linked for the preceding passes.

| Paper | Inspected locations and use | Limit |
|---|---|---|
| [Carey, Balijepalli and Watling (2013), *Extending the Cell Transmission Model to Multiple Lanes and Lane-Changing*, DOI 10.1007/s11067-013-9193-7](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf) | Author manuscript §2 / PDF p4, §4 / p7, §5 R1 / pp9–10 and Algorithm A1. Rechecked fundamental-diagram, eager-demand and receiving-work context. | Supports local own-lane priority and gap-weighted residual acceptance. Does not derive this finite-footprint homogeneous VSL reduction or its terminal queue. Source cell movements are diagonal to the next cell; the proposed same-location continuous exchange is an adaptation. |
| [Jin (2021), *A link queue model of network traffic flow*, primary preprint arXiv:1209.2361](https://arxiv.org/pdf/1209.2361) | Introduction and §7 conclusion, including comparison with kinematic-wave models. | Supports keeping a compact occupancy model as a serious rival. Its distinct internal dynamics do not establish exact physical footprint discharge. |
| [Jin (2015), *Continuous formulations and analytical properties of the link transmission model*, primary preprint arXiv:1405.7080](https://arxiv.org/pdf/1405.7080) | §2.2 on initial density and boundary cumulative flows; source retained as a reduction check. | Boundary history does not by itself remove initial-profile or internal lateral-source requirements. The H1 construction is not an exact LTM reconstruction theorem. |

Earlier inspected variable-speed timing evidence is reused through the existing
audits, not reported as a newly viewed fourth paper:

[A-H reference list and compactness audit](vsl_b2ah_source_and_compactness_audit.md)

[B2-A reference list and the free-flow discharge-tail finding](vsl_b2a_compact_closure_source_audit.md)

[Accepted S13 source-to-equation audit](../s13_m2_source_to_equation_audit.md)

No new full-text access or algorithm claim is made for van der Gun et al.; its
earlier official-abstract-only restriction remains in force. Source numerical
illustrations are not an R1 calibration for this candidate.

## What is borrowed and what is newly assumed

| Candidate ingredient | Provenance and status |
|---|---|
| Continuous mass; demand/supply limits; own-lane-first service; gap-work distinct from transferred mass | Established source ingredients, reused in an explicitly adapted setting. |
| Common VSL changes the free-flow slope of a triangular diagram, with fixed wave parameter and jam density | A declared analytical response family. Its internally admissible free-flow domain is proved; empirical response and parameter provenance are not supplied. |
| Uniform finite initial footprint, common across actions; initial continuing symmetry | A proposed H1 member that supplies finite physical density and arrival timing. It changes S13's initial batch meaning and is not adopted by merely selecting H1's review direction. |
| Uniform local lateral source and fixed physical interaction length | H1 adaptation. R1's algebraic receiving-work inequality carries over; its repeated physical opportunity/rate scale is not identified by the source. No numerical grid change is used to generate a speed effect. |
| Donor offer bounded by progress through that interaction scale | Explicit rate analogue. It is not the native CTM stock request divided by an arbitrary numerical interval, nor a claim that the original diagonal-movement algorithm is unchanged. |
| Homogeneous lane-density invariance while all motion remains free flow and the boundary accepts arrivals | A mathematical deduction from the proposed transport/source equations. The proof is conditional, not a claim that real merging preserves a uniform profile. |
| Initial ending scalar reconstructs adjacent density under initial symmetry | A deduction within the candidate. It does not supply a reachable equal-aggregate-history witness or prove differing best actions. |
| A nonblocking terminal makes all exit times their physical arrival times | A conditional reference limit. If receiving binds, storage and upstream influence remain unqualified. |

## Audited deductions and hand checks

The mathematical note gives the unit table, source/work limits, nonnegative
density invariant, free-flow barrier, footprint edges, arrival histories and
whole-cohort conservation identity. Its branch solutions distinguish a donor
limit from a residual-service limit. They are analytical reference expressions,
not numerical traffic trajectories.

The eight-work-unit illustration is an exact receiving-work check. With a
two-unit donor offer and a gap weight of two, own flow of two leaves six work
units and accepts two lateral mass units; own flow of six leaves two and
accepts one. Consumed work is six and eight respectively. The accepted mass
is two and one, not four and two. Equal total continuing density can accompany
different adjacent densities by exchanging initial density with the other
continuing lane, but that asymmetric construction is outside the retained
initial-symmetry member and is not an information witness for it.

Changing to distance as the independent variable reveals a useful limit:
if receiving capacity divided by common speed is unchanged, the proposed
early-merging evolution per unit distance is unchanged. More physical time
does not then mean more preparation. The triangular diagnostic changes this
normalized headroom with speed. That is a conditional model effect, not a
universal measured speed–merging relation.

For the no-blocking member, total arrivals conserve the entire initial mass,
and mean completion time is the mean initial distance to the lane end divided
by speed. The fastest action follows independently of lane composition. This
checks the scientific limit rather than manufacturing a positive split.

## MP6 admission and reopen conditions

The note demonstrates existence of an internally consistent analytical
no-blocking domain, including a sufficient terminal-work bound across the
whole advice range. It establishes no calibrated or independently evaluated
traffic regime. A delay-producing member needs an arrival-aware lane-end
service contract and an account of any upstream influence. A point-queue
approximation cannot be admitted by omitting its storage or influence.

Failure of that no-wait branch does not prove every homogeneous compact model
impossible. A proposed compact holding model returns to G3/VQ3-P/T/S and G4;
initial footprint observability returns to G2. H2/B remains deferred. No source
or mathematical finding in this pass authorizes introducing position-resolved
state, revising the objective, or claiming gradient usefulness.

[Main findings and original system-interface gate](../../reporting/research_readiness/vsl_h1_homogeneous_window_findings.md)

[Mathematical candidate and reference checks](../../synthesis/research_readiness/vsl_h1_homogeneous_window_contract.pdf)
