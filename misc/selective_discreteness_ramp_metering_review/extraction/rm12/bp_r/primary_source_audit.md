# BP-R — source/task transfer audit

Date: 2026-10-06. Bounded Stage 2 source/static review under the
[approved protocol](../../../rm12_50_bp_r_stage2_protocol.md).
Source selection is evidence work, not adoption of equations, particle events,
geometry, controllers or numerical settings. No papers are redistributed.

## Access-qualified primary evidence

| ID / inspected version and link | Selected location and source result | Transfer qualification |
|---|---|---|
| RM8-P01; 2005 conference manuscript / 2007 chapter, [author-hosted original](https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/f/3571/files/2023/03/merges.pdf) | Sections 2–4, especially Figure 6: lane-wise kinematic waves plus bounded-acceleration lane changers; field/model evidence connects metering, queue regimes and discharge. Figure 6 distinguishes two regimes with the same ramp inflow but different ramp queuing. | Point ramp, zero acceleration-lane length and increased ramp boundary capacity representing priority are source assumptions. Demand after detector queuing is extrapolated. Neither public exact forcing nor finite-cleared all-stream TST is certified. A queue/speed-aware compact rival can distinguish the Figure 6 regimes; this is not fine-identity necessity. Lane-change bans are an additional actuator, not imported. |
| RM0011; 2004 working paper, [institutional original](https://escholarship.org/content/qt8w70q261/qt8w70q261.pdf) | Sections 2–3 and selected applications: fluid lane exchange is followed by quantized lane-change events; a changer's acceleration and downstream constraints determine its moving obstruction. Section 3 permits deterministic cumulative-floor events; Poisson sampling is optional. | Continuous background traffic does not make event generation a continuous-mass mesoscopic law. The working-paper applications are lane drops/moving obstructions, not a complete local ramp/TST comparison. Reference-only use or a continuous adaptation would need explicit qualification; neither is adopted here. |
| RM0003; Cao/Nilsson/Coogan 2021 arXiv v1, [original](https://arxiv.org/pdf/2106.10347) | Sections II–IV, equations 3–7, Proposition 1/Theorem 1: density plus retained congestion mode changes service; rate permissions and ramp inventories are explicit. MPC costs count road and ramp inventories. Conditional two-cell control analysis and later controller comparisons support a compact-memory mechanism. | Actual entry is demand/permission limited in the printed update; joint mainline/ramp receiving and finite ramp spillback need qualification. Restricted demand can produce unbounded ramp queues. Throughput and inventory-cost claims require the accounting caution below. Comparisons change controllers/horizons, not just representation under common open-loop actions. |
| RM0001; Gomes/Horowitz 2006, [original ACTM paper](https://horowitz.me.berkeley.edu/Publications_files/All_papers_numbered/80J_Gomes_TRC06.pdf) | Section 2 equations 3–13; Section 4 equations 18–20 and cooling discussion: section inventories, ramp queues, permissions, actual entries, receiving/storage/allocation, and travel-time accounting. Fixed routing and empty-terminal assumptions can remove the distance term from its objective. | Corridor optimization with twenty meters is not our one-ramp richer-family test. Cooling approximates emptying because the discrete model can retain asymptotically diminishing inventory. Accounting/receiving precedent is not permission to splice its law into a different source and call the result validated. |
| RM10-P01; **2011 proceedings body**, [author-uploaded original](https://www.researchgate.net/publication/251530773_Capacity_Drops_at_Merges_an_endogenous_model) | Sections 2.1–2.2 and 4–5: endogenous mean capacity accounts for inserting acceleration and headway statistics, separating congested/uncongested ramp regimes. In the latter, actual insertion demand and assumed entry speed affect the capacity calculation. | Body is Procedia 17, 12–26, DOI 10.1016/j.sbspro.2011.04.505; journal landing metadata is not the inspected version. Mainline is congested and the merge active. Field comparison selects stable periods; stop-and-go effects remain outside the mean closure. This is a substantive compact rival, not a complete transient rate rollout. |
| S12A005; **2016 author manuscript**, [institutional original](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6) | Sections 4.3 and 5/Figure 5: mean-characteristic estimates closely approximate effective mean capacity in tested regimes, while heterogeneous dynamics show varying local flow despite similar means. | DOI 10.1016/j.trc.2015.06.025; keep the 2014 antecedent separate. Steady active-merge insertion, fixed wave/entry-speed assumptions and statistical approximations are limits. Different transients motivate an adequacy question; they do not establish common-rate TST/action differences, exact mean equality, or failure of every dynamic compact closure. |
| RM10-P02; 2016 published paper, [institutional original](https://repository.tudelft.nl/file/File_d4844cb9-1115-47ab-ab36-443cc0ca7df4) | Printed pp. 1–3, Modeling Framework: analytical lane capacities and insertion flow are coupled recursively; mandatory and discretionary transfers occupy consecutive nonoverlapping areas. | DOI 10.3141/2560-01. A lane-aggregate mean-capacity competitor, not a lane-blind one. Spatial partitioning is an approximation. No additional lanes or geometry is adopted; dynamic common-rate fidelity is unestablished. |
| RM0014; related 2004 report / 2005 journal, [report location](https://escholarship.org/content/qt30s46939/qt30s46939.pdf) | **Prior RM8 Sections 3–5 extraction reused**: isolated-merge metering/recovery and occupancy feedback context. | Fresh fetch attempts failed; no fresh full-method read claimed. The prior evidence remains qualified by [RM8 extraction](../../rm8_source_studies/isolated_merge_and_hybrid.md). No new certificate follows from failed access. |
| RM12-RP01; Kim/Cassidy 2012, [publisher-indexed original](https://www.sciencedirect.com/science/article/abs/pii/S0191261512000860) | Indexed abstract/introduction and selected section snippets: a metering strategy influences recurring discharge recovery on a 3-km site; higher average discharge and shorter ramp queues are reported. | DOI 10.1016/j.trb.2012.06.002. Direct full-text opens failed; methods were not obtained. Multiple on-ramps and uncontrolled scope differences prevent transfer as a one-ramp matched certificate. Context only. |
| RM12-RP02; Guin/Laval 2011 GDOT report FHWA-GA-10-0722, [institutional report text](https://dlg.usg.edu/record/dlg_ggpd_s-ga-bt700-pr4-bs1-bc6-br34-b2011-belec-p-btext) | Selected printed pp. 21–24 and documentation page: explicitly discusses ramp-delay transfer and the unresolved system-delay balance for capacity-drop interventions. Report's own planned optimization was not completed because valid streaming data were unavailable. | Institutional machine-extracted text, selected passages only. Its literature review corroborates an accounting caution, not independent replication of the cited field results or a completed optimization certificate. Corridor/software proposals are not adopted. |

## Accounting caution: distinguish exits from their timing

RM0003's text associates maximizing an unweighted horizon total of exits with
minimizing accumulated inventories. That equivalence does not hold in general
under fixed arrivals: the former asks how many have left by the endpoint; the
latter also depends on when they left. The printed inventory cost is a useful
precedent; the throughput theorem is not automatically a TST theorem. This is a
reviewer accounting deduction under the inherited conservation contract, not a
new traffic law or a blanket rejection of the source's conditional results.

For illustration, ten units present initially and all leaving after one minute
versus after two minutes give the same eventual exit total but different system
time. This is an accounting example, not a proposed freeway witness. For our
fixed finite population, compare the full exit histories and count all waiting,
including traffic unable to enter the modeled road. Clearance/tail treatment
must be declared; an endpoint throughput gain or finite-horizon queue decrease
does not settle the required objective.

## Coverage and stopping rationale

Eight actual queries in three combined batches are recorded in
[the query log](../../../search/rm12_bp_r_query_log.csv). Ten deduplicated sources
are qualified in [screening records](../../../screening/rm12_bp_r_records.csv):
eight reused and two new. Seven reused sources received selected fresh method
reads; RM0014 retains its prior extraction only. Source versions and failed
fetches remain explicit. Secondary catalogues helped locate originals; no
technical conclusion rests on them.

The nearest frontier now covers physical intervention, compact memory,
spatial/receiving/accounting, endogenous mean closure and transient limitations.
It does not supply a joined positive study certificate. Expanding to unrelated
CAV, VSL, reinforcement-learning, emissions, multi-ramp or timing tasks would
change scope rather than complete this bounded admission pass. Stop at BPR-G3
with the qualified result; source absence is not a universal impossibility proof.
