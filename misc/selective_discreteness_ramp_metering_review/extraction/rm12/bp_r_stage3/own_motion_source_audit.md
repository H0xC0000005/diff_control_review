# Supplied journal and nearest own-motion source audit

Date: 2026-10-08. Source-first SRC.A executed; access checkpoint resolved.
[Readable result](../../../reporting/rm12/bp_r_stage3/own_motion_findings_and_gate.md).

## Actual access and identity

| ID | Access and inspected locations | Qualification |
|---|---|---|
| RM12-S3-J01 | User-supplied *On the numerical treatment of moving bottlenecks*, Daganzo/Laval, TRB 39 (2005), 31–46; DOI 10.1016/j.trb.2004.02.003; all 16 PDF pages' extracted text, Sections 2–5 and references | Full journal access now verified. PDF SHA256 `efa3ee8b5aa9c647bcab685960f99c580dcf56f393f0548555ddd6b5c26afece`. No source bytes renamed or changed; figures not visually inspected. |
| RM12-S3-A01 | Existing supplied *Lane-changing in traffic streams*, 2006, Appendix A, PDF 11–12 | CM uses a numerical own downstream-speed estimate for the ensuing interval; desired acceleration updates from realized speed. Lane-choice speed support is a separate estimator. |
| RM12-S3-D04 | [Author-uploaded Laval 2004 thesis PDF](https://www.researchgate.net/profile/Jorge-Laval/publication/35936658_Hybrid_models_of_traffic_flow_impacts_of_bounded_vehicle_accelerations/links/54e764500cf2cd2e0293f478/Hybrid-models-of-traffic-flow-impacts-of-bounded-vehicle-accelerations.pdf), 110 PDF pages; targeted text: printed 30–32, 34–37, 41–46, 49, 60–61, 88–92 | CFM minimum-speed rule; CTM capacity embedding; speed from a forward density average; lane-specific zero-capacity embedding; continuous transfer with stochastic descriptors; passing example uses different lanes. Relevant methods read, not a full-thesis read. |
| RM0011 | [Institutional 2004 multilane working paper](https://escholarship.org/content/qt8w70q261/qt8w70q261.pdf), title/cover, Sections 2–3, bibliography and Appendix | Confirms it is *Multi-Lane Hybrid Traffic Flow Model*, not the separately cited *Impacts of Roadway Geometry on Capacity*. Does not independently supply the complete adapted mandatory-node feedback. |
| RM12-S3-S02 | [Existing RR-2003-2 institutional PDF](https://escholarship.org/content/qt1hp588xx/qt1hp588xx.pdf), identity/method route rechecked | Already qualified prescribed/frozen paths and pairwise coincidence limits. Browser generic title is incorrect; existing cover-based identification retained. No new full-method result asserted from this re-open. |

The separately cited geometry manuscript was not obtained. Its title/year
varies between the journal and the working paper. The thesis is a directly
cited, author-uploaded primary alternative for the targeted method check;
it is not relabeled as that manuscript. The previously unavailable originals
remain unavailable and were not retried.

## What J01 proves, and what it explicitly separates

Sections 2–3 establish count-solution contraction and a trajectory staircase
error bound for prescribed paths/capacities. The piecewise case has count
error at most 3 P kappa Delta-x, with P depending on the prescribed data and
trajectory. Multiple coincident stationary restrictions use the minimum
capacity, not additive deductions. The paper discusses extensions by
approximation; these are not a theorem for our joined endogenous source/node
task or its derivatives.

Its Q is downstream trace flow at an active moving bottleneck, while Q-r is
relative passing flow. They are different variables. Zero passing on one lane
gives an adjacent void with zero downstream trace flow, while following flow
can be positive. Neither is the full boundary receiving for arbitrary demand.
The earlier delayed/slack receiving diagnostics remain conditional.

Section 4 compares prescribed paths in CTM, including two restrictions and
prescribed acceleration. It uses an isosceles FD to isolate particular numerical
errors; this is not a freeway calibration to import. Count-based finite-region
performance continuity does not establish complete clearing or gradient
convergence.

Section 5, printed 44–45, expressly separates traffic-to-motion from the main
proof. It describes a cited feedback extension with averaging ahead and nearby
restriction status. The reason for averaging is artificial grid-induced speed
fluctuation. Thus the previous request's expectation of a full own-motion
recipe *inside this journal* was too strong; the received original corrects
that expectation. It is not evidence that the source is useless or the model
family fails.

## Nearest feedback transcription and limits

D04 Sections 3.2–3.3 connect constrained acceleration to a CTM traffic-speed
estimate. Section 4.5 applies it lane by lane and blocks incoming through/lateral
flows at the projected restriction. Appendix A.2 illustrates a queue encounter
and passing via another lane. Section 5.2.1 distinguishes continuous transferred
mass from discrete stochastic descriptors. No stochastic rule, instant
restriction lane change, or single-pipe passing capacity is adopted here.

The extracted equation (3.6), printed 32 / PDF 43, appears to pair a factor
1/4 with inclusive summation limits i through i+4. A screenshot fetch failed;
no visual glyph confirmation is available. We do not silently attribute an
exact four-/five-cell indexing correction to the author. The review candidate
uses an explicitly normalized spatial integral, labeled as an adaptation.
The discrepancy is a transcription limit, not a claimed theorem failure or
a separate user gate about typography.

Own-speed density averaging is not Edie's lane-choice/flow-to-density speed.
The numerical normalization and support, time ordering and boundary treatment
must be declared before a concrete reference is frozen. A physical lookahead
of fixed length and a mesh-dependent numerical window have different limits.

## Reviewer deductions

The [companion](../../../synthesis/rm12/bp_r_stage3/own_motion_math.pdf) derives:
count-to-window-speed error amplification; a conditional free-speed boundary
staircase mismatch; a finite-birth bound for the admitted forward-directed
geometry; finite-time TST and derivative limits. These are analytical checks,
not published claims of model failure, reached traffic-control scenarios,
experiments or gradient evidence. No uniform-endogenous-trajectory theorem is
inferred from the prescribed-path bound.

## Search/access record

Eleven actual queries in four batches. Source routes and failed access are
separated in the [query log](../../../search/rm12_bp_r_stage3_own_motion_queries.csv)
and [activity log](../../../screening/rm12_bp_r_stage3_own_motion_sources.csv).
The initial ResearchGate thesis link failed; the canonical author-uploaded
PDF route succeeded. The faculty-linked lab homepage failed. Two thesis
screenshots failed. These failures do not negate the readable primary text.
No new PDF was downloaded through a shell command, no source-access credentials
were requested, and no traffic experiment was run.
