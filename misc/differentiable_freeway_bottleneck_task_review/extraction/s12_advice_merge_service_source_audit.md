# S12 source audit — advice, merge state and endogenous service

Date: 2026-09-30. Scope: bounded primary-source review for S12 model-class
admission. E3 means selected full methods/results were inspected; E2 means the
claim is limited to a primary abstract or institutional record. The
[query log](../search/s12_advice_merge_service_query_log.csv) and
[access log](../search/s12_advice_merge_service_access_log.csv) record new work.

## Evidence needed

S12 does not ask whether lane changes can disturb traffic somewhere. It asks
whether a conservative mechanism class can support this specific path:

`common lane-uniform VSL → lane-resolved approach/mandatory transfers → finite
receiving or endogenous service → complete-accounting action response`.

The class must also have a coherent state distinction beyond total density,
flow, speed, cumulative counts and their full predecision history. At this stage
an exact matched-history witness is reserved for a later derivation; physical
plausibility without a structural escape is insufficient.

## S12-S1 — Laval and Daganzo lane-changing void mechanism

[Institutional primary record](https://its.berkeley.edu/publications/lane-changing-traffic-streams),
DOI 10.1016/j.trb.2005.04.003. The model treats lane changers as particles whose
insertion creates voids, reducing flow and reproducing capacity-drop phenomena.
This directly supports a lane-change-to-service mechanism and a relaxation-scale
state finer than ordinary link totals.

It is not the preferred S12 class. The particle mechanics exceed the intended
continuous-mass first-order refinement, and the source has no common-VSL or
strong-observer comparison. Converting it into a conservative mass closure would
be a substantive new model rather than bounded adoption.

## S12-S2 — Carey, Balijepalli and Watling finite-receiving CTM

[Institutional author manuscript](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf),
DOI 10.1007/s11067-013-9193-7. The paper extends CTM conservation lane by lane,
lets mandatory traffic transfer laterally, and explicitly allocates finite target-
cell receiving capacity between longitudinal and lateral entrants. Its behavioral
dimensions include where mandatory demand arises and how much spacing a lane
change needs relative to ordinary following.

This is the strongest structural basis found for S12. The source reports that
lane-changing assumptions can change aggregate outflow and travel time and that
a single-lane surrogate can miss important congestion behavior. The relevant
mechanism is conservative: lateral outflow from a donor is lateral inflow to a
receiver, and all movements are capped by sending/receiving limits.

The paper itself uses two-lane, single-link examples and no VSL controller. S12
therefore admits its **function class**, not its numerical examples or behavioral
coefficients. Common-VSL reachability must be supplied by the existing common-
limit evidence and by a later explicit action-to-demand/receiving contract.

## S12-S3 — Pan et al. mandatory/discretionary mesoscopic model

[Primary indexed record](https://trid.trb.org/View/1411058),
DOI 10.1016/j.trc.2016.05.002. The model uses lane-specific fundamental diagrams,
motivation/urgency levels and demand-supply reaction rules for lateral and
longitudinal propagation. Its calibrated weaving case reports both lane-balance
and capacity-drop effects.

This supports the existence of a continuous mesoscopic lane-change family and
guards against treating all lateral flow as beneficial. The inspected evidence
does not provide the exact equations needed for adoption, and the weaving/lane-
control setting does not close common-VSL reachability or observer separation.

## S12-S4 — Srivastava and Jin lane-drop capacity mechanism

[Official institutional record](https://its.uci.edu/research_products/conference-paper-a-lane-changing-cell-transmission-model-for-modeling-capacity-drop-at-lane-drop-bottlenecks/).
The lane-drop CTM raises perceived density according to lane-changing intensity
and combines this with a downstream acceleration-region demand law. It shows a
compact first-order route from lane-change activity to reduced bottleneck
throughput.

This is useful corroboration, but not a stand-alone admitted family: the result
uses calibrated intensity and an aggregate perceived-density closure. Its
consequential state may be recoverable by an augmented aggregate observer, and
the source does not provide the common-VSL information comparison.

## S12-S5 — Leclercq et al. analytical merge-capacity mechanism

[Institutional primary record](https://repository.tudelft.nl/record/uuid%3Aeb7471c0-8b30-4ee4-a7ce-d748bf2f7c1e),
DOI 10.1016/j.trc.2015.06.025. The work analytically connects lane changing and
relaxation to endogenous effective merge capacity. It supports the proposition
that service need not be an action-independent number.

The native domain is an active freeway merge with on-ramp flow. Translating its
inputs to an ending mainline lane under common VSL would require a new mapping.
It therefore supports the mechanism family but does not independently pass the
S12 actuator/domain screen.

## Reused permanent-drop and common-VSL sources

- [FB0030](n2_source_studies/FB0030.md) supplies paired conservative transfers,
  density-driven incentives, target-lane constraints and field validation at a
  lane drop. It does not supply a VSL ranking, and its full branch/denominator
  scheme is not adopted.
- [S06-S3](s06_reference_mechanism_source_audit.md) studies a permanent
  three-to-two lane drop with common segment VSL. Its microscopic model links
  lane changes and bounded acceleration to capacity drop, while its CTM
  crosscheck prescribes an aggregate density-triggered capacity drop. It is
  actuator/domain support, not an information certificate.
- [FB0039](rb_source_studies/new_lane_evidence.md) shows that one fixed limit
  across lanes can affect lane distribution and lane-changing activity. At equal
  occupancy its lane-flow fractions are almost insensitive in the reported data,
  so it is also counterevidence against assuming a strong response.
- [FB0038](rb_source_studies/new_lane_evidence.md) shows that spatially spreading
  mandatory merging and balancing continuing lanes can help in one three-to-two
  configuration. Because it directly controls lateral fractions and disables
  natural lane changing, it establishes a mechanism boundary rather than the S12
  common-VSL path.

## Aggregate countercandidate

[FB0022](https://doi.org/10.1111/mice.13492) combines cumulative link inflow/
outflow, time-varying VSL effects and traffic-state-dependent capacity drop at a
lane drop. The paper explicitly classifies the model as macroscopic and excludes
individual lane changing/overtaking. This is a credible way to make service
action- and state-dependent without hidden lane state.

Accordingly, an endogenous service law alone cannot pass S12. The admitted
family must retain per-lane receiving competition or another variable whose
effect is not determined by the strong aggregate state/history.

## Evidence-chain judgment

| Link | Evidence | S12 judgment |
|---|---|---|
| Common VSL → lane preparation | S06-S3 and FB0039; mixed magnitude/sign | Supported as reachability, not a fixed response law. |
| Lane state → mandatory lateral demand | FB0030, S12-S2, S12-S3 | Direct support for continuous lane-resolved models. |
| Lateral demand → finite receiving/service | S12-S2; corroborated by S12-S1/S4/S5 | Direct structural support; several incompatible closures. |
| Service → complete outcome | S12-S2 reports outflow/travel-time effects; FB0038 counts origin waiting | Supported in neighboring models; exact S12 action ranking unproved. |
| Hidden state beyond strong history | S05 collision plus lane-wise nonlinear receiving structure | Coherent separation argument; consequential exact pair still missing. |
| Useful common-VSL action split | No inspected source | Reserved for later derivation; must not be claimed at admission. |

## Source-bounded admission conclusion

One narrow composite family survives the screen: **conservative per-lane CTM/
LTM flow with endogenous mandatory lateral demand, finite target-lane receiving
shared between longitudinal and lateral entrants, and a nonnegative extra spacing
cost for lane changes**. Common VSL may affect lane-wise sending, density and the
time available for feasible transfers; the mechanism then makes realized service
depend on the evolving lane state rather than on an exogenous capacity alone.

The family is bounded by the cited sources, but no single source contains the
whole S12 chain. Admission therefore authorizes a later analytical contract to
state and audit the join. It does not authorize fitted coefficients, claim a
useful action split, or establish the necessity of lane contrast.
