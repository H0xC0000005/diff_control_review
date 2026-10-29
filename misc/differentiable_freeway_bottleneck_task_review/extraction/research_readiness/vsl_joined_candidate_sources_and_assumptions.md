# Joined member: source credit, global assumptions and local conventions

2026-10-21. **LF1/LF2 selected; bounded qualification delivered at JQ1.**
This pass uses existing primary evidence rather than importing a new traffic
model. The numerical member, finite-domain conventions and new analytical
results are separated from source formulations and empirical claims.

## References actually used and reading scope

**[1]** H. H. S. Nagalur Subraveti, V. L. Knoop, and B. van Arem, “First
order multi-lane traffic flow model – an incentive based macroscopic model
to represent lane change dynamics,” *Transportmetrica B: Transport Dynamics*,
vol. 7, no. 1, pp. 1758–1779, doi: 10.1080/21680566.2019.1700846.
Repository/copyright 2019; article header 2020, as previously recorded.

[Archived final university PDF](../../archive/full_text/FB0030.pdf)

Reread the extracted primary text for printed pp. 1762–1764, equations 6–11,
and the route-distance discussion around the later FD/calibration section.
The framework uses a displayed additive incentive and density/lookahead
preferences. Route and courtesy have geometry-dependent activation; the
text restricts courtesy to free conditions and explicitly permits zero
congestion keep-right bias. Follow the displayed additive equation with its
unit density baseline, rather than replacing it by the cubic route term.
The source text motivates leftward restriction; its printed index condition
is not copied as the literal impossible general condition “target < 1.”
Directions are stated physically in the concrete member.

The source's numeric route distance 750 m is reused as a review default.
Its heterogeneous site FD, calibration and original adjusted-flow rules are
not inherited. No source code or new empirical evidence was accessed.

**[2]** H. H. S. Nagalur Subraveti, *Lane-specific Traffic Flow Control*,
Ph.D. dissertation, TU Delft, 2021,
doi: 10.4233/uuid:e405a549-b1fe-4fa1-8090-4429612359d9.

[Institutional dissertation](https://repository.tudelft.nl/record/uuid:e405a549-b1fe-4fa1-8090-4429612359d9)

Reread local chapter 4 text around PDF pp. 64–65, equations 4.4–4.5: weights
2:2:1 and the additive density/incentive construction. The original article
does not specify all finite-end averaging conventions. Our treatment of
missing E cells and outlet ghosts is explicit below, not attributed to the
author as an erratum or recovered implementation.

**[3]** Y. Han, Y. Yuan, A. Hegyi, and S. P. Hoogendoorn, “New extended
discrete first-order model to reproduce propagation of jam waves,”
*Transportation Research Record*, vol. 2560, pp. 108–118, 2016,
doi: 10.3141/2560-12.

[Primary accepted manuscript](https://pure.tudelft.nl/ws/files/10502816/New_Extended_Discrete_First_Order_Model_to_Reproduce_Propagation_of_Jam_Waves_TRR.pdf)

**[4]** Y. Han, A. Hegyi, Y. Yuan, S. Hoogendoorn, M. Papageorgiou, and
C. Roncoli, “Resolving freeway jam waves by discrete first-order model-based
predictive control of variable speed limits,” *Transportation Research Part C:
Emerging Technologies*, vol. 77, pp. 405–420, 2017,
doi: 10.1016/j.trc.2017.02.009.

[Primary accepted manuscript](https://pure.tudelft.nl/ws/files/45432235/AAM.pdf)

Reused the just-completed H source qualification and its common-FD bounds.
The complete source laws and VSL interpretation were read in the preceding
pass, not newly downloaded or experimentally tested here. H is now selected.

[Exact previous source locations and limitations](vsl_congestion_join_sources_and_adaptations.md)

**[5]** M. Carey, C. Balijepalli, and D. Watling, “Extending the cell
transmission model to multiple lanes and lane-changing,” *Networks and
Spatial Economics*, vol. 15, pp. 507–535, 2015,
doi: 10.1007/s11067-013-9193-7. Online publication 2013.

[Institutional manuscript](https://eprints.whiterose.ac.uk/id/eprint/77315/)

**[6]** M. A. Wright, G. Gomes, R. Horowitz, and A. A. Kurzhanskiy, “On node
models for high-dimensional road networks,” *Transportation Research Part B:
Methodological*, vol. 105, pp. 212–234, 2017,
doi: 10.1016/j.trb.2017.09.001.

[Primary author preprint](https://arxiv.org/html/1601.01054)

Reused the selected allocation contract and prior primary-method reading.
No new reading or general-node certificate is claimed. Positive fixed
priority sharing and unused-share return support the component; the
three-lane composition, donor normalization and forward fallback remain an
explicit adaptation. It need not maximize unrestricted throughput.

[Previous actual reading scope and adaptation boundary](vsl_allocator_sources_and_adaptations.md)

No newly found paper or secondary technical source supplies this pass's
information, residual-value or complete-derivative proofs. Those are review
deductions from the selected model. Search results and inaccessible sources
are not used as additional evidence.

## Global assumption set for the declared member

| ID and status | Assumption and scientific role |
|---|---|
| **JA1 — selected model contract** | Continuous vehicle-equivalent stocks, fixed finite geometry, a common triangular FD and selected H budgets. No integer traffic or microscopic ordering is introduced. |
| **JA2 — declared member default** | A finite cohort is initialized inside the road independently of advice; there are no later arrivals. The task starts at this decision state. This supports the full remaining-time objective without an uncounted external holding queue. |
| **JA3 — declared member default** | The road ends at the lane-drop line with free A/B outlets. Completion occurs on crossing that line. Ghost densities represent that boundary, carry no mass and are not a downstream recovery zone. The proof does not claim behavior of a congested downstream road. |
| **JA4 — declared member default** | One positive constant common advice is chosen at the reset and held. All observers share its bounds. Nominal critical density, physical cells and reference priorities do not change with advice. |
| **JA5 — selected model contract** | Old-state one-row forward/diagonal movements; shared donor and receiver limits; equal positive reference-capacity priorities; attempts with forward fallback; final E must merge or wait. These are the dependencies of the conservation/progress proof. |
| **JA6 — declared objective** | Count every unfinished unit from the decision to the common exit. The infinite-sum population-time is represented exactly by a finite prefix plus its derived residual value, not by deleting residual mass. Pre-decision travel is outside the remaining-time objective and action-independent. |
| **JA7 — evidence/derivative contract** | Differentiate the complete objective on regular finite branch traces. Native switching may remain discontinuous. Correctness, information value, optimizer benefit and physical fidelity require separate evidence; none follows merely from finite derivatives. |

JA2–JA4 and the concrete numeric defaults are exposed for the JQ1 review,
not silently frozen as empirical configuration. The new analysis is
conditional on them. They use the earlier completion-at-choke preference
without requiring functional identity to the accepted old model.

## Local definitions resolved within the selected direction

| Detail | Concrete convention and provenance |
|---|---|
| **Grid/action example** | Ten 100 m rows, 6 s updates, common nominal 60/20 km/h FD with jam density 150 veh/km and 10% maximum drop; advice 30–60 km/h. This extends the preceding illustrative FD, not a calibrated or positive-result search. |
| **Finite lookahead** | Use 2:2:1 weights. For E omit nonexistent downstream E cells and renormalize existing weights. For continuing A/B use the free outlet's zero-density extension. This is a finite-domain convention, not a new obstacle or fake jam. |
| **Displayed incentives** | Retain the additive unit density baseline plus source route, keep-right and courtesy terms. Route bias applies to E-to-A; courtesy applies to A-to-B in the approach. The last-E forced connection overrides a mere desire fraction, as already selected. |
| **Origin mode and direction** | Classify the current origin density using nominal critical density. Use the source's allowed zero keep-right term in congestion; in free conditions apply its ratio restriction for leftward moves/rightmost entry. Free A may cooperate toward B within the route zone. These direction/mode conventions make the chosen member explicit. |
| **Empty traffic** | Zero donor stock means zero requests; do not evaluate density ratios. No numerical epsilon, extra smoothing, probabilistic decision or mass truncation is inserted. |
| **Initial diagnostic pair** | All three penultimate cells at critical density, last E at 120, last A/B at 60/90 or 90/60, all earlier cells empty. Both members have identical E and A+B profiles and total initial mass. These are root initial conditions, not a reachability assertion from identical hidden histories. |

These details finish a concrete proposal inside the accepted framework. They
are not empirical findings or proof that every native branch is behaviorally
accurate. If changing them affects the accepted information/control/physics
contract, record that scope change rather than treating an implementation
adapter as authority.

## Derived findings, hypotheses and exclusions

**Derived here:** a valid same-observation service/next-state contrast; exact
equivalence of the one-statistic and full observers on the diagnostic pair;
eventual unconstrained service and finite full remaining population-time;
an exact residual expression; a full regular-trace derivative with both
residual-state and direct-speed terms. The progress proof permits arbitrary
admissible desire fractions and therefore does not assume incentive smoothness.

**Hypotheses, not assumptions:** positive attainable action value from lane
information; richer lane fields outperforming a compact statistic on a
broader family; numerical gradient correctness and usefulness; physical
fidelity of the adapted flow/finite-domain model. The diagnostic may have
zero optimal-action gap even though service differs.

**Outside this qualification:** continuing arrivals, unknown external queues,
blocked downstream traffic, heterogeneous FD mapping, repeated advice/feedback,
absolute unobservability under histories, new speed-mismatch/recovery dynamics,
and microscopic order. SUMO remains optional. The old S13/asymmetric task
certificates and monotone-queue claims do not transfer automatically.

[Readable findings and review checkpoint](../../reporting/research_readiness/vsl_joined_candidate_findings_and_checkpoint.md)

[Complete mathematical definition and proofs](../../synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.pdf)
