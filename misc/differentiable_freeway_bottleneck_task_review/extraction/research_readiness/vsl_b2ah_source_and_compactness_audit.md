# A-H source and compactness audit

Date: 2026-10-13. Scope: a bounded review of whether travel histories and
one receiver stock can close P1's *upstream* early merging. This is not a
traffic experiment, a simulator design, a calibration or a full literature
survey. “Inspected” below distinguishes primary text read in this pass,
previously audited primary text reused here, and abstract-only leads.

## Primary texts inspected or reused

| Source | Material inspected | Direct support and exact limit |
|---|---|---|
| [Yperman, Logghe and Immers (2005), *The Link Transmission Model*](https://www.mech.kuleuven.be/cib/verkeer/dwn/pub/P2005C.pdf) | Original PDF abstract and §§1–3; earlier B2-A extraction reused. | Homogeneous-link boundary cumulative counts and node sending/receiving. Interior mandatory lane changes under one common VSL are not derived. |
| [Jin (2015), *Continuous formulations and analytical properties of the link transmission model*](https://arxiv.org/pdf/1405.7080) | Primary preprint §2.2 on initial density plus boundary cumulative flows and the LTM relation. | Reconstruction of a homogeneous link needs declared initial and boundary conditions. It is not a one-stock theorem for a link with distributed internal lateral source terms. |
| [Carey, Balijepalli and Watling (2013), *Extending the Cell Transmission Model to Multiple Lanes and Lane-Changing*](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf) | Primary manuscript §4 desire cases, §5 R1 and Algorithm A1, and discussion of unfinished lane changes; earlier B1/B2 audits reused. | Eager or distance-based desire, local target-cell receiving, own-lane-first priority, unfulfilled requests and later opportunities. It does not derive one pooled receiver stock for the entire preparation area. Its numerical illustrations use R2, not an R1 calibration. |
| [Carey (2021), *The cell transmission model with free-flow speeds varying over time or space*](https://pure.ulster.ac.uk/ws/portalfiles/portal/85807280/TRB_2018_842_R2_as_uploaded_to_TR_Part_B_on_2020_04_29.pdf) | B2-A's previous primary-paper audit and half-speed reference case reused. | A current-stock fractional release can give unphysical free-flow exit timing; entry-time memory is a correction ingredient. This paper does not join that correction to upstream lane changing or certify congested VSL operation. |
| [Jin (2021), *A link queue model of network traffic flow*](https://arxiv.org/pdf/1209.2361) | Primary preprint abstract, introduction, link conservation discussion and conclusion. | A link-level occupancy can drive a useful demand/supply approximation. The source explicitly distinguishes link-queue internal dynamics from CTM/LTM; it gives no native distributed mandatory-lane-change closure for P1. |

The [official record and abstract of van der Gun, Pel and van Arem
(2018/2019)](https://research.tudelft.nl/en/publications/the-link-transmission-model-with-variable-fundamental-diagrams-an/)
was inspected, but the full PDF was not accessible through the web reader.
Its abstract reports variable fundamental diagrams, within-link density
reconstruction and a VSL/dynamic-lane-management demonstration. We use
only that scope statement: neither its detailed algorithm nor a lateral
merge reduction is inferred from the abstract.

Searches also found other lane-changing, reservoir and VSL papers. Their
snippets were treated as leads, not as evidence for the present gate. The
accepted [B2-A full reference list](vsl_b2a_compact_closure_source_audit.md)
and earlier [B2 source audit](vsl_b2_source_and_reduction_audit.md) remain
available; this list identifies what this pass actually used.

## The compactness check in traffic terms

**Motion subproblem.** In the inherited S13 free-flow branch, a finite
cohort has one entrance time and all its mass shares the chosen physical
speed through fixed geometry. The lane-end arrival time follows from its
travel clock. That is a special compact case. The B2-A half-speed example
already ruled out replacing this clock with repeated fractional release of
the current stock. If early service causes longitudinal waiting, the
waiting/release history must be retained and counted, so the common clock
cannot be presumed after P1.

**Own-demand subproblem.** Local R1 consumes target receiving with target
traffic that actually reaches the opportunity during the accounting
interval. Total target mass is measured in vehicle equivalents; local
receiving and own demand are rates or amounts per interval. A physical
entry/passage profile, a finite footprint, or an endogenous release queue
is needed to relate the mass to that local demand. S13's simultaneous
analytical batch leaves this upstream relation unspecified. A sample
arithmetic comparison at a local opportunity is:

| Same target total | Passage of target mass | Own demand per second | Receiving work per second | Work left before lateral requests |
|---:|---|---:|---:|---:|
| 4 veh-eq | even over 2 seconds | 2 veh-eq/s | 3 work/s | 1 work/s |
| 4 veh-eq | even over 8 seconds | 0.5 veh-eq/s | 3 work/s | 2.5 work/s |

This is a dimensional hand example, not a claim that either profile is
empirically correct. If each lateral unit consumed two work units and
donor requests were available, the spare budgets would permit at most
0.5 versus 1.25 lateral veh-eq/s. That calculation shows why target
stock alone cannot supply R1's own-demand input. A-H's proposed travel
history may distinguish the profiles, once the task declares one.

**Location subproblem.** A donor at one early opportunity cannot spend
unused receiving at a remote opportunity at that instant. Equally large
target stocks with different internal concentrations can therefore have
different local receiving. This is a conditional counterexample to an
unrestricted one-stock reduction, not to a tightly restricted homogeneous
cohort model. A complete entrance and exit history can reconstruct some
internal state when a homogeneous link has no internal sources and its
initial condition is specified. Early lane changes themselves are
internal inflows to the target lane and outflows from the donor lane.
Knowing their total without their physical location need not reconstruct
local service; storing every transfer location/time can erase A-H's
compact advantage. This is our inference from conservation and the
sources' different interfaces, not a theorem stated by a cited paper.

**Choke subproblem.** Residual ending-lane mass must still obtain finite
service at the permanent lane end. None of the upstream compactness
arguments decides that law. Nor does avoiding the travel-time tail prove
S13's proportional batch mean remains valid after P1 creates varied
arrival and waiting times.

## Consequences for the scientific comparison

An admitted entrance profile or receiver statistic is part of the initial
information contract. It cannot be provided to A-H from post-action
reference trajectories while withholding the same available aggregate
history from strong simpler rivals. A homogeneous whole-window service
budget could define a small theoretical model, but its local-to-aggregate
step is an analytical adaptation requiring explicit G3 approval and a
separate MP6 domain review. A few fixed internal service interfaces
preserve local R1 more directly but add spatially indexed information;
their number and placement affect the physical task and cannot be chosen
merely to fit results. No source inspected here establishes a positive
action split, calibrated speed response, derivative correctness, or
independent gradient usefulness for either route.

[Decision-facing finding and VSL-B2AH-G1](../../reporting/research_readiness/vsl_b2ah_history_service_findings_and_gate.md)
