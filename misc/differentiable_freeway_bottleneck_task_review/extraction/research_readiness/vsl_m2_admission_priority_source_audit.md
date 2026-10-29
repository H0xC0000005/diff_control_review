# Joined M2 opening: viewed references and inference boundaries

Date: 2026-10-15. Source inspection for the user-approved three-part chain.
This is a reference list, with actual reading limits. Incidental search hits
are not counted as reviewed papers; no full-paper archive is claimed.

| Reference | Material actually inspected | Role and limit |
|---|---|---|
| [Jin, Gan and Lebacque (2013 preprint), *A kinematic wave theory of capacity drop*, arXiv:1310.2660](https://arxiv.org/pdf/1310.2660) | Reopened primary manuscript; §6 merge extension, equations (15a–c) and immediately following limitations, printed pp21–22. | Priority allocation template with spare-service redistribution. Its phenomenological capacity law is not adopted as M2 recovery. It does not calibrate an E priority weight. |
| [Leclercq, Knoop, Marczak and Hoogendoorn (2016), *Capacity drops at merges: New analytical investigations*, DOI 10.1016/j.trc.2015.06.025](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6) | Rechecked §2 point-insertion inputs/cumulative expression, §3.2 regime-conditioned inserting speed, §5 mean-capacity/heterogeneity limitations. No new figure extraction or numerical results used. | Insertion kinematics and recovery need their own meaning. The native insertion process/mean-capacity calculation is not an autonomous finite-cohort M2 update. |
| [Jin, *Continuous formulations and analytical properties of the link transmission model*, arXiv:1405.7080](https://arxiv.org/pdf/1405.7080) | Reopened primary manuscript; reused triangular FD and positive eligible queue/boundary demand passages, especially §2–3. Served manuscript headed 8 June 2022. | Basis for cumulative physical/eligible stock and demand. Boundary regime does not by itself identify the lateral insertion trajectory. |
| [Hidas (2005), *Modelling vehicle interactions in microscopic simulation of merging and weaving*, TRC 13(1), 37–62, DOI 10.1016/j.trc.2004.12.003](https://www.sciencedirect.com/science/article/pii/S0968090X04000671) | Primary publisher search-returned abstract, introduction and section previews. Direct page open failed. Full equations/data were not inspected. | Behavioral distinction between free, forced and cooperative passage. Does not establish our macro allocation, speed map, task parameter or a need to implement microscopic agents. |
| [Erdmann, *Lane-Changing Model in SUMO*, DLR author manuscript associated with the 2014 SUMO proceedings](https://elib.dlr.de/89233/1/SUMO_Lane_change_model_Template_SUMO2014.pdf) | Primary 12-page author PDF; selected §1.2–1.4.3 architecture and strategic speed-adjustment text, especially PDF pp2–4. Full native source/version behavior not audited. | E and obstructing traffic can adjust speed to facilitate a lane change. A behavior precedent, not a certified correspondence for a restricted junction, current binary or the proposed quota. |
| [Pan, Lam, Sumalee and Zhong (2016), *Modeling the impacts of mandatory and discretionary lane-changing maneuvers*, TRC 68, 403–424, DOI 10.1016/j.trc.2016.05.002](https://www.sciencedirect.com/science/article/pii/S0968090X1630033X) | Publisher-returned abstract/highlights and selected introduction. Direct publisher open failed. | Alternative source screen: lane-specific FD/minimum-gap model. Its full spatial algorithm was not inspected or adopted; no evidence here requires spatial expansion. |
| [*Modelling motorway merge: The current practice in the UK and towards establishing general principles*, Transport Policy 24 (2012), 199–210, DOI 10.1016/j.tranpol.2012.07.014](https://www.sciencedirect.com/science/article/pii/S0967070X12001436) | Publisher search-returned abstract/introduction excerpts and bibliographic record; direct open failed. Author metadata not independently checked from the primary record. | Screening context on passive gap acceptance versus interactive motorway behavior. No full model, equation or quantitative claim used. |

The final screened motorway-merge record is retained transparently because
its excerpts were viewed; the response's conclusions do not depend on that
record. A [same-title 2011 conference abstract](https://www.sciencedirect.com/science/article/pii/S1877042811009876) was also returned in the
bibliographic check: Procedia 16, 184–195, DOI 10.1016/j.sbspro.2011.04.441;
it is not substituted for the inspected journal record or counted as a
full conference-paper review. Official SUMO documentation
and source-reference search records were also screened for cooperation;
the cited author PDF carries the behavior claim. No SUMO API, build, binary
version or runtime model was qualified in this pass.

## Evidence versus review deductions

The strict-priority E-blocking result is derived directly from the stored
H1/T1/M1 allocator, not inferred from the microscopic sources. The alternative
uses only the published allocation template with a proposed M2 shared ceiling;
it does not import the source's capacity-drop law or prove physical gap safety.

The queue-speed feedback identity, allocator feasibility checks and sufficient
storage/TST/clearance statements are analytical review deductions under the
conditions stated in the new note. They are not a complete M2 existence,
uniqueness or MP6 certificate. A change in admission priority is not approval
of an insertion-speed map, independent A penalty or recovery overlap law.

[Previous M2/feedback-6 references and access limits](vsl_feedback6_behavior_source_audit.md)

[Earlier P-H/M1 source-to-equation distinction](vsl_ph_source_and_adaptation_audit.md)

[Plain traffic findings and the current terminal-admission gate](../../reporting/research_readiness/vsl_m2_admission_priority_findings_and_gate.md)
