# VSL-B1: source and interface qualification

Date: 2026-10-13. Status: **Selected primary-source review and reduction
diagnostics complete; no whole source model or replacement equation admitted.**

This supports the decision-facing report. The review reused accepted S13,
S12/S06 and VSL-R1 evidence, then rechecked the decision-critical primary
methods. It is not a new literature-wide novelty/absence survey.

[Traffic model, interface consequences and gate](../../reporting/research_readiness/vsl_b1_lane_change_model_and_gate.md)

## Primary evidence inspected

| Source and access | Selected locations | Bounded evidence used | Remaining qualification |
|---|---|---|---|
| Carey, Balijepalli and Watling, institutional submitted manuscript, 26 PDF pages; web text | PDF pp. 5–8, classes/conservation and §4; pp. 9–12, receiving, R1/R2, eq. 9 and Algorithm A2 | One-way mandatory desire, finite adjacent receiving, gap allowance, proportional or same-lane priority; unsatisfied demand can remain at the final cell | No native common-VSL permanent three-to-two boundary; cell motion, priorities, class/FIFO restrictions and population closure need qualification |
| Nagalur Subraveti, Knoop and van Arem, existing archived FB0030 primary article, 24 PDF pages; local text | PDF pp. 5–12, printed pp. 1760–1767; equations 1–4, 6–22; pp. 21–22 for sensitivity context | Lane conservation; density/lookahead and route incentives; sending-based lateral demand; receiving and longitudinal-flow coupling | Original branch, zero-state and combined-budget cautions preserved; changing speed is not a qualified VSL intervention or useful derivative |
| Wei, Han and Wang 2025, publisher full text; web | §§1.2–2.1; boundary-speed cohorts, cumulative counts, downstream supply and node capacity-drop context | Concrete strong aggregate-history/VSL challenger | Different source laws are not inserted into the matched information ladder; no successor derivative or native equal-history witness certified |
| Roncoli, Papageorgiou and Papamichail 2014, primary six-page IFAC paper; web | §§2–3, printed pp. 4179–4181; density/flow states, lateral-flow controls, constraints 5–11 and objective | Continuous multi-lane control precedent already in the accepted predecessor screen | Lateral flow is directly controlled, not endogenous under one common speed; 2015 journal extension remains metadata-only in the reused record |
| Zhang et al. 2023, institutional 44-page manuscript; web | §4.1, PDF pp. 14–16; §§4.2–5, PDF pp. 18–23; reuse S06 qualifications | Permanent three-to-two VSL relevance with microscopic interaction and aggregate explanation | Calibration at 100 km/h, low-limit extrapolation and different action/objective restrict transfer to this task |

[Carey primary manuscript](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf)

[FB0030 primary archive](../../archive/full_text/FB0030.pdf)

[Wei primary methods](https://onlinelibrary.wiley.com/doi/full/10.1111/mice.13492)

[Roncoli primary proceedings](https://skoge.folk.ntnu.no/prost/proceedings/ifac2014/media/files/1657.pdf)

[Zhang primary manuscript](https://ira.lib.polyu.edu.hk/bitstream/10397/92568/1/Zhang_Optimization_Speed_Freeway.pdf)

## Native models and proposed restriction are different things

**Carey as a principal candidate.** Its simple mandatory-demand alternatives and
explicit receiving allocations make it the provisional anchor for a bounded
reduction proposal. The candidate restriction would consider ending-lane
traffic that all needs the adjacent lane; after transfer, the cohort has the
same downstream destination. That could remove distinctions between traffic
classes that no longer affect service. It does not certify that total lane
masses replace spatial occupancy or all relevant chronology. Carey's source
discusses FIFO labeling and a proportional simplification; exact ordered
metadata is not automatically part of this proposed restricted task.

The source permits unsatisfied transfer demand at the final cell. It therefore
does not, by itself, specify that every member of the proposed finite cohort
eventually merges and exits a permanent lane drop. A lane-end holding/transfer
boundary must be explicitly qualified before adoption. This is a completeness
obligation, not a finding that the source model loses mass.

**FB0030 as a separate structural/domain check.** Its lateral demand is a share
of sending, and its final flows couple lateral and longitudinal transfers.
It supplies a native lane-drop application, but its larger incentive system
cannot be added to Carey's allocation without a new declared model. The
published receiving branch at theta = 1 differs from its lower-branch limit;
empty-density expressions and shared donor/receiver budgets remain unqualified.
No repair, clipping, smoothing or new capacity branch was supplied in B1.
The repository/copyright year 2019 and article-header year 2020 are preserved.

**Speed response remains a global adaptation.** Carey chooses cell length using
free-flow motion per time tick; FB0030 also states a speed-dependent grid/CFL
relation. Varying common advice must not silently change physical geometry,
the meaning of a transfer fraction or the number of opportunities. A future
fixed-grid interpretation needs an explicit longitudinal/action law and
appropriate numerical bounds. Reusing a free-flow-speed parameter as advice
without declaring its effect on capacity, receiving and actual progress is
not sufficient. This review chooses none of those adaptations.

## Original reduction diagnostics

The examples in the linked mathematical note are deductions, not published
case results, calibrated claims or traffic runs:

- **Receiver distinction:** equal ending and combined continuing mass can
  coexist with different adjacent receiving under a standard occupancy-based
  receiving relation. This is a local snapshot/interface counterexample, not
  an equal-full-history or different-optimal-action witness.
- **Symmetry persistence:** an initially balanced continuing pair can become
  unbalanced when only the adjacent lane receives mandatory transfer. An
  exact grouped closure needs a compensating condition, not just initial symmetry.
- **Time accounting:** two simultaneous classes with identical final work can
  have different complete population time under different allocations. The
  proportional half-clearance expression requires its stated batch/allocation
  conditions.

[Editable mathematical source](../../synthesis/research_readiness/vsl_b1_interface_examples.tex)

[Mathematical examples, PDF](../../synthesis/research_readiness/vsl_b1_interface_examples.pdf)

## Interface contract ledger at the gate

| Contract | Evidence now established | What is proposed or still open | Ownership / smallest return |
|---|---|---|---|
| Continuous mandatory transfer | Source structure and paired conservation are credible | One exact desire, sending and allocation/update scheme | Type 2, VQ3-T/G3 |
| Adjacent receiving | Consequential receiver distinction can defeat unrestricted combined-mass closure | Restricted equivalence or smallest continuous augmentation | Type 2, VQ3-P/G3; initial information under G2/VQ2 |
| Preparation/exit connection | Scalar sufficiency requires receiving/timing restrictions | B1-L would permit local receiving and time-resolved flow exchange, including consequential feedback | Type 2, VQ3-P/S/G3; no current source/Python API commitment |
| Early/late accounting | Receiving cost at both locations can affect total time | Consistent spare-upstream/constrained-exit domain, or represented costs in both regions | Type 2, VQ3-S/G3; complete objective remains G4 |
| Departures | Final work and clearance do not determine general mean time | Retain qualified batch or carry relevant within-cohort chronology | Type 2, VQ3-P/S; G4/VQ4 consistency |
| Common action and domain | VSL lane-drop and aggregate-control precedents exist | One coherent advice-to-demand/motion map, fixed geometry, boundary closure and common action range | Type 2, MP6 through VQ3-P/T/S and G3 |
| Observation / sufficient statistic | S13 scalar equivalence remains exact | Receiver augmentation may be sufficient; new-model sufficiency and reachable history matching not proved | Type 2, G2/VQ2 after the traffic contract |
| Source indices, units and record format | Selected locations recorded | Exact transcription after global contracts close | Type 1, C1-Q1/C2-Q1; physical repairs return to the affected global contract |

MP1–MP3 establish the proposed transfer/state meaning; MP4–MP5 check its
accounting and timing consequences; MP6 checks those conditions jointly.
This internal order does not approve any scientific amendment. No global
choice is delegated to a notation, source transcription or implementation detail.

## MP6 evidence boundary and possible reopening

The structural candidate is sufficiently concrete to propose its next contract,
but the applied task is **not admitted**. Required joint evidence concerns:
the same finite population and fixed geometry; a common intervention mapping;
receiver/grouping sufficiency; upstream cost and downstream feedback; lane-end
holding and eventual clearance; and a declared range/branch interpretation
for sensitivities. A useful state-dependent action distinction is an outcome
to assess, not a constraint used to select the model.

If local reduction cannot satisfy these together without a large spatial or
behavioral program, return to G1's elementary role. If receiving-state inputs
are not observable/inferable under the proposed initial information, return to
G2. If an attempted simplification omits action-dependent time or changes the
physical derivative, return to G4. Source/adaptation conflicts first return to
the smallest VQ3-P/T/S contract, before expanding scope.

## Access and inspection limits

Carey, Wei, Roncoli and Zhang were read through primary web text. Attempts to
obtain Carey screenshots of PDF pages 11–12 returned web Internal Error; no
rendered-equation certification is claimed. Source R2 is used as a provisional
allocation lineage, not whole-algorithm certification. FB0030 pages were
extracted with installed `pypdf` 6.15.0. No new full text or dependency was
installed/archived. Selected rechecks do not certify every source equation,
boundary or all forward reference cases.

[Earlier source join audit](vsl_r1_primary_source_join_audit.md)

[Accepted S13 source/adaptation record](../s13_m2_source_to_equation_audit.md)

[Accepted domain evidence and counterevidence](../s06_reference_mechanism_source_audit.md)

[Previously inspected control predecessors](../n2_source_studies/feedback23_amendment_predecessors.md)
