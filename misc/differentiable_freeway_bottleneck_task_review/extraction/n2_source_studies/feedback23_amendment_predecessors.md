# Feedback23 amendment — supplementary predecessor screen

Date: 2026-09-17. Brief targeted primary-source review; no exhaustive novelty
clearance. No paper-access request is needed for these bounded claims.

## FB0034 — Roncoli/Papageorgiou/Papamichail 2014

Primary full six-page IFAC proceedings paper:
https://skoge.folk.ntnu.no/prost/proceedings/ifac2014/media/files/1657.pdf
Inspected cover/abstract and sections2–3, printed4179–4181.
Continuous per-segment/per-lane density and ramp queue; longitudinal, lateral and
ramp flows are control variables. A constrained quadratic program is translated
into speed and lane-changing instructions for equipped traffic.
Overlap: continuous multi-lane model-based speed control.
Boundary: jointly controlled lateral flow is not endogenous merging under the
same shared advice; no native-autodiff or external advice-gradient claim adopted.
2015 journal extension DOI10.1016/j.trc.2015.05.011 verified through Aalto
institutional abstract/metadata only; not full-method equivalence certified.

## FB0035 — Goatin/Göttlich/Kolb 2016 (online2015)

DOI10.1080/0305215X.2015.1097099.
Primary 29-page author copy: https://d-nb.info/1265990972/34
Section3.2/PDFpp10–11 Algorithm2 and equations29–30: discrete-adjoint speed/ramp
objective gradients. Aggregate LWR road densities and queues, piecewise-constant
time controls. Explicit smoothing requirement for nondifferentiable discretized
equations. Section5/PDFp25: discretization-dependent outcomes and limitations
of first-order models for some objectives.
Overlap: gradient-based speed-limit optimization is prior work.
Boundary: not exact unsmoothed closure certification or a lane-state necessity
experiment. Grid effects are a confound, not evidence that lane information
is necessary. Do not mix equation numbers/results from other manuscript versions.

## FB0036 — Poole/Kotsialos 2016

DOI10.1016/j.trc.2016.07.008, TRC71:356–381.
Title: Second order macroscopic traffic flow model validation using automatic
differentiation with resilient backpropagation and particle swarm optimisation
algorithms.
Primary publication/indexed author-PDF abstract:
https://www.sciencedirect.com/science/article/pii/S0968090X16301152
https://durham-repository.worktribe.com/OutputFile/1395060
Indexed abstract reports ADOL-C integration with METANET and RPROP/PSO parameter
calibration. Only E1 abstract/metadata adopted; direct full PDF retrieval failed,
publisher direct retrieval403. No numerical method detail inferred from citations.
Overlap: aggregate freeway autodiff is established.
Boundary: differentiated target is calibration, not shared-advice gradient
usefulness or minimal lane information. This limited claim does not require
requesting another institutional full-text batch.

## Reviewer synthesis

These sources weaken broad novelty, while neither proving nor disproving the
precise proposed independent-reference retained-information gap. Proposed
matched contrasts and component-necessity tests are reviewer recommendations,
not source findings. Extra lane state, class state or intra-lane order remains
unapproved and its benefit unproved.

