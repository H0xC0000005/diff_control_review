# S-E admission review: viewed references and adaptation boundary

Date: 2026-10-15. Selected-section source review. No downloaded-paper archive,
traffic simulation, calibration or source numerical experiment was performed.

## Primary sources inspected in this pass

| Reference | What was inspected | Support and limit |
|---|---|---|
| [Carey, Balijepalli and Watling (2013), *Extending the Cell Transmission Model to Multiple Lanes and Lane-Changing*, DOI 10.1007/s11067-013-9193-7](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf) | Reopened §5 R1/A1 and R2/R3 allocation passages, PDF pp9–12. | Own-lane priority and receiving-work allocation are source ingredients. S-E-P's regime switch and both candidates' equal-work cooperative template are adaptations. R2 is demand proportional, not equal work. No native CTM or discrete source update is adopted. |
| [Jin (2015), *Continuous formulations and analytical properties of the link transmission model*, arXiv:1405.7080](https://arxiv.org/pdf/1405.7080) | Reopened primary preprint; §3 empty-link demand/queue/vacancy and boundary-node interpretation, plus §6 invariant versus non-invariant merge comparison, equations (43)–(45). | Retain T1 eligibility/storage and check node compatibility. The source stationary example is distinct from our transient work-graft test. It neither selects P/W nor proves their switched history law. |
| [Leclercq, Knoop, Marczak and Hoogendoorn (2016), *Capacity drops at merges: New analytical investigations*, DOI 10.1016/j.trc.2015.06.025](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6) | Rechecked §1 assumptions, §2 point case and §3.2 congested-entry speed/flow relation. | Congested insertion-speed and recovery interpretation is conditional. It does not select free-approach priority, prove a transient mode law or derive the trial mismatch work. Its mean-capacity result is not used as a full finite-time departure model. |
| [Jin, Gan and Lebacque (2013 preprint), *A kinematic wave theory of capacity drop*, arXiv:1310.2660](https://arxiv.org/pdf/1310.2660) | Reopened primary manuscript and rechecked boundary-selection context; no new native-law adoption. | Explicit selection belongs to a complete node. Its phenomenological capacity drop and Riemann uniqueness result do not qualify this state/recovery node. |
| [Chevallier and Leclercq (2009), *Do microscopic merging models reproduce the observed priority sharing ratio in congestion?*, TRC 17(3), 328–336, DOI 10.1016/j.trc.2009.01.002](https://www.sciencedirect.com/science/article/abs/pii/S0968090X09000096) | Publisher search-returned abstract, introduction and section snippets; direct publisher open failed. No full algorithm or full-paper reading claimed. | Distinguishes free-approach insertion and congested priority sharing; motivates treating allocation and relaxation jointly. It does not establish exact equal-work sharing in free traffic or our free-A protection rule. |

## Neighboring formulations screened, not adopted

| Reference | Screen and limit |
|---|---|
| [Akçelik and Chung (1994), *Calibration of the bunched exponential distribution of arrival headways*, Road and Transport Research 3(1), 42–59; author-hosted revised reprint](https://www.sidrasolutions.com/media/158/download) | Opened title/abstract and headway-model context; search-returned gap-capacity equation screened. A headway-based opportunity model requires declared critical/follow-up gaps and headway assumptions. No distribution, capacity floor or native gap law is adopted; no calibration/data/figure analysis was done. |
| [Leclercq, Marczak, Knoop and Hoogendoorn (2016), *Capacity Drops at Merges: Analytical Expressions for Multilane Freeways*, DOI 10.3141/2560-01](https://journals.sagepub.com/doi/10.3141/2560-01) | Publisher abstract and institutional search extract screened. The spatial/multilane extension is not the selected compact point task; no complete equations or native algorithm inspected. |

Other incidental search hits were not substantive readings or scientific
support. Earlier empirical relative-speed and merge-ratio sources retain
their prior access limits; they were reused rather than reported as newly
read complete papers.

[Earlier empirical/source qualifications](vsl_feedback7_traffic_state_source_audit.md)

## Deductions and trial assumptions

- **Source-supported ingredients:** continuous boundary counts, sending/
  receiving constraints, explicit allocation choices, congested branch
  interpretation and the possible continuing effect of slow passage.
- **Proposed constitutive family:** immediate E maneuver work plus an
  A-flow-weighted positive relative-speed cost. Its sign, coefficients and
  representative speed identification are not empirical conclusions.
- **Proposed allocations:** S-E-W uses equal service work with redistribution;
  S-E-P protects an unqueued A offer and uses that cooperative template when
  A queues. Neither is a verbatim native source algorithm or approved law.
- **Own exact findings:** monotone feasible queued-E root under a declared
  sufficient coefficient bound; guard-based exclusion of the prior arbitrary
  births; distinct strict local queue onsets at the accepted H1 front; no
  consistent strict mode for a naive demand-proportional binary-demand graft.
  That last finding does not reject native CTM or proper invariant-node rivals.
- **Conditional interfaces:** storage/TST and finite-loss clearance survive
  admissible departures; a marked E-kernel bound does not supply the full
  joint A/E account, overlap law or switched-model uniqueness.

The H1 example is reused at its original analytical status. No numerical
scenario was selected for an interior optimum, no traffic was stepped, and
no positive information/action or useful-gradient result was produced.

[Plain findings and expanded allocation gate](../../reporting/research_readiness/vsl_se_admission_findings_and_gate.md)
