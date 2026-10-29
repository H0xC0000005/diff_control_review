# MP6 physical review: viewed references and limits

Date: 2026-10-16. Reference list for **MP6-Q1**. Two previously reviewed
papers and one official documentation page were rechecked in selected
passages; no new full-paper review, data extraction or empirical replication
is claimed. Older literature is reused through the linked source audits.

| Viewed reference | Reading scope this pass | Support and limit |
|---|---|---|
| [Carey, Balijepalli and Watling, *Extending the Cell Transmission Model to Multiple Lanes and Lane-Changing*, author manuscript labeled 2013; DOI 10.1007/s11067-013-9193-7](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf) | Section 5 receiving/headway interpretation and neighboring priority passages; manuscript pp8–9. | Supports extra receiving work and separate allocation choices. Does not establish our speed-mismatch coefficient or separation from recovery. No CTM algorithm adopted. |
| [Leclercq, Knoop, Marczak and Hoogendoorn (2016), *Capacity drops at merges: New analytical investigations*, TRC 62, 171–181; DOI 10.1016/j.trc.2015.06.025](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6) | Introduction; Section 2 point-case assumptions, equation (1) and accompanying interpretation; Sections 3.1–3.2 interactions and congested insertion-speed assumption. | Supports bounded-acceleration insertion and restricted equilibrium speed reasoning. The square-root boundary quantity is not physical vehicle speed. Our capped profile and continuous recent-mass renewal are adaptations. Illustration parameters are not a calibrated joined range. |
| [SUMO, official *Road Capacity* documentation](https://sumo.dlr.de/docs/Simulation/RoadCapacity.html) | Computing Headways and Further headway effects; retrieved 2026-10-16. | Constant-speed Krauss spacing supports the earlier stationary correspondence only. Native variation and insertion effects prevent treating that ideal curve as measured transient capacity. No installed version or runtime was inspected. |

## Review deductions, rather than borrowed findings

The queued A-only tail equality, conditional work-identification rank test,
preparation-scale confounding and evidence dependency order are our analysis
of the selected equations. They are not conclusions attributed to these
papers. Exact algebra checks do not establish statistical identifiability
under noisy native data, availability of informative tails, absence of
duplicate physical effects, or applied MP6.

No numerical source value was imported into task configuration. No source
supports the full W-F/S-E-P/R-E/O-R law as a published complete model. The
new admission contract preserves that distinction and the one common
parameter set, independently native reference and held-out boundaries.

[Previous forward source audit](vsl_wf_forward_source_audit.md)

[Prior recovery and overlap evidence](vsl_re_overlap_source_and_adaptation_audit.md)

[Strong aggregate/history/scalar rivals and evidence gaps](vsl_successor_baselines_and_evidence_gaps.md)

[Plain findings and checkpoint](../../reporting/research_readiness/vsl_mp6_physical_findings_and_checkpoint.md)

[Mathematical identification note](../../synthesis/research_readiness/vsl_mp6_physical_identifiability.pdf)
