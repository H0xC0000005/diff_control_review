# RMD-G1 background source and access note

Date: 2026-10-01. Scope: narrow methods clarification requested by the user.
This is not an exhaustive algorithm/prevalence review or RM8 execution.

| Source | Primary URL / provenance | Inspected material | Use and boundary |
|---|---|---|---|
| FHWA Ramp Metering Primer | https://ops.fhwa.dot.gov/publications/fhwahop14020/sec1.htm | Official HTML §§1.8–1.10 | Operational taxonomy, sensors, coordinated families and release modes; no model-necessity proof |
| FHWA Ramp Management and Control Handbook | https://ops.fhwa.dot.gov/publications/ramp_mgmt_handbook/manual/manual/5_1.htm | Official HTML §§5.3.1–5.3.6 | Operational objectives, queue management, algorithms and actuation; no universal controller optimality |
| Papageorgiou, Hadj-Salem, Blosseville, ALINEA (1991) | https://onlinepubs.trb.org/Onlinepubs/trr/1991/1320/1320-008.pdf | Primary PDF indexed excerpt; direct open failed | Feedback/control lineage only; no new equation-level adoption, no full text downloaded |
| Schmitt et al., RM0002 | https://arxiv.org/pdf/1611.06766 | Public PDF §5.1 eq.13 and conclusion | Integral density-based ALINEA and conditional macro optimality; not universal sufficiency outside assumptions |
| Reilly et al., RM0024 | https://jackdreilly.github.io/papers/adjoint.pdf | Public author manuscript §§5.2–5.3 | Finite-horizon optimization versus repeated MPC; not evidence for local meso necessity |
| Wang et al., PI-ALINEA (2014) | https://sndbx.library.tuc.gr/view/49548?locale=el&show=full | Authors' institutional abstract | Integral versus PI and distant-bottleneck setting; no equation/stability rederivation |

Access limitations: a comparative PI manuscript at
https://dias.library.tuc.gr/view/manf/24482 returned an anti-bot page; the
publisher comparative page returned an internal error. The institutional
abstract above suffices for the bounded lineage explanation. These limits do
not establish an equation-level evidence gap resolution for a future RM8 pass.

The institutional PI record contains inconsistent publisher/issue metadata;
cite the DOI 10.1109/TITS.2014.2307884 and title, without propagating those
inconsistent fields. No new document identifiers were assigned because this
pass supplies background, not newly screened model-adoption evidence.

Reviewer definitions: the optimization targets, proposed sensor contract,
hidden-history implication, derivative paths and pros/cons in the background
brief are review reasoning. Source facts are linked beside their claims.

