# C-P opening: point-service sources and interface limits

**Continuation, 2026-10-15:** P-H is now user-selected. The resumed source
recheck and explicit recovery-work adaptation are recorded separately below;
this opening audit retains its original reading and decision limits.

[Resumed viewed-reference list and source/adaptation distinction](vsl_ph_source_and_adaptation_audit.md)

Date: 2026-10-14. The user opened the next bounded review after accepting
coupled point merging with choke-line completion. This is the reference
list of papers actually viewed, with reading limits, not a full-paper
download archive. Earlier accepted S12/S13/H1/T1 evidence is reused in place.

## References viewed in this pass

| Reference | Material inspected | Support and limit |
|---|---|---|
| [Leclercq, Laval and Chiabaut (2011), *Capacity Drops at Merges: an endogenous model*, conference version, Procedia Social and Behavioral Sciences 17, 12–26, DOI 10.1016/j.sbspro.2011.04.505](https://www.researchgate.net/publication/251530773_Capacity_Drops_at_Merges_an_endogenous_model) | Primary conference-paper text, abstract and selected §2: point insertion, headways/acceleration, congested versus uncongested entering stream and capacity construction. Publisher search record checked; direct publisher open failed. | Entry at one location can constrain main traffic after crossing. The native analytical inputs include inserting speed and headways, with mean-capacity/traffic-regime assumptions. It is not already an autonomous finite-cohort continuous-mass departure law. |
| [Leclercq, Knoop, Marczak and Hoogendoorn (2016), *Capacity drops at merges: New analytical investigations*, DOI 10.1016/j.trc.2015.06.025](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6) | Primary repository manuscript, selected §2 point case, §3 interaction assumptions, and §5 discussion, printed pp3–6 and 12–13. | Strengthens the physical point-service basis, but mean capacity differs from flow dynamics. No source parameter, insertion distribution or law-of-large-numbers approximation is adopted for the finite task. The requested figure screenshot failed; conclusions rely on inspected text, not extracted figure data. |
| [Jin, Gan and Lebacque (2013 preprint), *A kinematic wave theory of capacity drop*, arXiv:1310.2660](https://arxiv.org/pdf/1310.2660) | Selected §2 boundary flux and explicit phenomenological limit; §6 merge extension, equations (15) and limitation discussion, printed pp20–21. | A strong first-order capacity-drop/priority node rival. The native drop magnitude is exogenous; it does not explain slow-entry recovery. Its priority fraction is not H1/T1's late work factor. A new E-specific activation or history law would be an adaptation. |
| [Jin (2015), *Continuous formulations and analytical properties of the link transmission model*, arXiv:1405.7080](https://arxiv.org/pdf/1405.7080) | Selected demand/vacancy and continuous boundary-history sections, especially §3.1–3.3 and initially empty-link cases; abstract/conclusion on junction assumptions. | Supports physical stock, eligible queue and receiving histories. It does not prove the unspecified C-P node well-posed or identify its slow-entry state. The new conditional bounds are review deductions, not a generic source theorem. |
| [Laval and Daganzo (2006), *Lane-Changing in Traffic Streams*, DOI 10.1016/j.trb.2005.04.003](https://its.berkeley.edu/publications/lane-changing-traffic-streams) | Institutional primary abstract rechecked. | Particle/void mechanism supports causal traffic interaction; no full native algorithm was newly read. Particle dynamics are not silently substituted for the continuous primary. |

The ResearchGate landing metadata for the 2011 item conflates the journal
DOI 10.1016/j.trb.2011.05.007 with a conference-volume description. The actual
text viewed identifies the Procedia conference version; its publisher record
provides DOI 10.1016/j.sbspro.2011.04.505. Preserve that distinction rather
than claim a newly inspected complete journal version.

[Conference publisher record inspected through search](https://www.sciencedirect.com/science/article/pii/S1877042811010640)

[Reused accepted mechanism/source screen](../s12_advice_merge_service_source_audit.md)

[Reused T1 source list and adaptation boundaries](vsl_k2_terminal_source_and_interface_audit.md)

## Direct source support versus proposed adaptation

The physical sources support continuing-service loss from inserting traffic
and point-location treatment. Native mean-flow expressions still require
entry/headway assumptions and are not the selected finite time update. The
phenomenological source supports a strong compact node; its causal explanation
and activation timing are limited by its stated purpose.

Converting the vehicle process to continuous temporal service memory, using
a mean-capacity expression instantaneously, tying a source congestion trigger
specifically to E, or changing its priority are distinct adaptations. None
is approved by merely selecting C-P. The finite node also determines E's
admissions, so its service cannot use an unspecified future insertion schedule
as an oracle. The old late-work factor and a new capacity reduction cannot
both represent the same loss without explaining their separate roles.

No new SUMO API/source probe or model construction was performed. Its accepted
reference role and independently produced native service remain inputs from
the existing audit, not a runtime qualification result.

## Independent analytical interface findings

The new supporting note extends the predecessor's sufficient storage proof
to admissible A/E departures, derives the all-queue local TST identity,
states a sufficient law-specific clearance condition and shows conditional
compact initialization if service memory is known initially and evolves
uniquely from the same histories. These deductions do not choose a node,
assume a one-state reduction, or inherit the old positive action certificate.
They are analytical work, not numerical traffic integration or a native run.

[Conditional storage/accounting mathematics](../../synthesis/research_readiness/vsl_cp_interface_foundations.pdf)

[Traffic findings, model interface and CP-D1 gate](../../reporting/research_readiness/vsl_cp_first_findings_and_gate.md)
