# Source audit for the autonomous alignment ladder

Date: 2026-10-08. Eight queries in four batches; 26 web open/find operations.
Search hits are leads; positive source claims below use primary body/abstract
content actually inspected. No source automatically adopts a joined task law.
Publisher access errors are logged, not interpreted as unavailable mathematics
or as a SUMO/input gate. No paper download or external message was required.

[Search record](../../../search/rm12_bp_r_stage3_alignment_ladder_queries.csv)

[Operation/screening record](../../../screening/rm12_bp_r_stage3_alignment_ladder_sources.csv)

## Supplied task lineage (read locally)

**A01, Laval and Daganzo (2006), Lane-changing in traffic streams**, supplied
final journal, DOI 10.1016/j.trb.2005.04.003. Read Sections 2.1.1–2.1.2,
equations 1–14, and Appendix A. The continuum section distinguishes desired
lane-changing demand, through demand, receiving and a competition operator.
The numerical section ties longitudinal cell size to u times timestep and
oriented choice fraction to the timestep. Target competitions are proportional
to the oriented requests; transfers advance once. Appendix A computes motion
from own downstream traffic and desired kinetics. This is positive source
lineage, not proof that a direct pointwise trace lift preserves its finite-step
semantics. Request-speed support remains the approved preceding-period Edie
convention; it is not replaced by point FD speed here.

[Supplied journal](../../../archive/user_supplied/rm12_bp_r_stage3/Lane-changing%20in%20traffic%20streams.pdf)

**J01, supplied On the numerical treatment of moving bottlenecks**, final
16-page journal, DOI 10.1016/j.trb.2004.02.003, previously verified. Its
prescribed-path/count treatment and own-motion lineage remain prior evidence.
This pass does not reinterpret a count estimate as a full endogenous theorem.

[Supplied numerical-treatment journal](../../../archive/user_supplied/rm12_bp_r_stage3/On%20the%20numerical%20treatment%20of%20moving%20bottlenecks.pdf)

## Numerical field/motion families

**S02, Daganzo and Laval (2003), Moving Bottlenecks: A Numerical Method that
Converges in Flows**, RR-2003-2, 14 pages. Sections 2–4 use counts at fixed
and moving points, constant density between them, and composite-Riemann
updates. Section 4 identifies stalling at certain multiple coincidences and
suggests trajectory perturbation. This supports A1's family, not the complete
zero-passing K.A/port extension; perturbation is not adopted. Browser title
metadata are erroneous; the actual PDF cover/body confirm source identity.

[Primary report](https://escholarship.org/content/qt1hp588xx/qt1hp588xx.pdf)

**DG14, Delle Monache and Goatin (2014)**, A front tracking method for a
strongly coupled PDE-ODE system with moving density constraints in traffic
flow, DOI 10.3934/dcdss.2014.7.435. Primary abstract supports a moving-mesh
field coupled to downstream-dependent restriction motion. Abstract-level
family support only; no transfer of its theorem to this task.

[Primary publisher page](https://www.aimsciences.org/article/doi/10.3934/dcdss.2014.7.435)

**CDG17, Chalons, Delle Monache and Goatin (2017)**, A conservative scheme
for non-classical solutions to a strongly coupled PDE-ODE problem, Interfaces
and Free Boundaries 19, 553–570, DOI 10.4171/IFB/392. Read Sections 1–3:
fixed-mesh discontinuity reconstruction, conservative fluxes and coupled
motion. Source assumes strictly concave flux (its example is quadratic), one
bus and positive reduction parameter. It reports isolated-shock exactness
and numerical general convergence; no rigorous general convergence theorem
there. This admits A2 as a promising family, not an unchanged task solver.

[Primary full text](https://ems.press/content/serial-article-files/36595)

**SC17, Simoni and Claudel (2017)**, A fast simulation algorithm for multiple
moving bottlenecks and applications in urban freight traffic management,
TRB 104, 238–255, DOI 10.1016/j.trb.2017.06.010. Author-uploaded primary
full text, Sections 2–3/Algorithm 2 inspected after publisher access failed.
Triangular-FD count calculations include endogenous multiple restrictions;
Section 3.3 resolves possible crossing/Zeno stalling using approximate
fixed-step trajectories. This is useful multiple-interaction evidence, not
certification of our exact retained-count/K.A/source interface. It overlaps
the earlier M02 lineage rather than newly resolving that earlier limit.

[Author-uploaded full text](https://www.researchgate.net/publication/318699176_A_fast_simulation_algorithm_for_multiple_moving_bottlenecks_and_applications_in_urban_freight_traffic_management)

## Continuous representation and its limits

**V03, Daganzo (2006)**, On the variational theory of traffic flow: well-posedness,
duality and applications, NHM 1(4), 601–619. Prescribed moving restrictions
and count/wave duality support C as a reference family. Endogenous multi-lane
coupling needs separate conditions. An implicit operator with externally
given paths does not close the required feedback.

[Primary full text](https://www.aimspress.com/aimspress-data/nhm/2006/4/PDF/1556-1801_2006_4_601.pdf)

**JIN15, Jin**, Continuous formulations and analytical properties of the link
transmission model, arXiv:1405.7080; published TRB 74 (2015), 88–103.
Section 6 explicitly distinguishes invariant junction models from direct
non-invariant proportional merging in continuous LTM. It also notes that
different interior states can make the corresponding rules equivalent in
continuous CTM. Therefore a failed direct LTM substitution does not refute
CTM or prove that a source-equivalent continuous completion is impossible.
This is the main qualification for the new node diagnostic.

[Primary full text](https://arxiv.org/pdf/1405.7080)

**LP21, Liard and Piccoli (2021)**, On entropic solutions to conservation laws
coupled with moving bottlenecks, CMS 19(4), 919–945. Sections 1.2–1.3 and
Theorem 1.1 give single-bottleneck existence under a smooth strictly concave
FD/motion setting. Remarks 1.1–1.2 explain why naive convergence of one-sided
traces in earlier proofs may fail and provide a repaired argument. This
supports taking coupled field/motion seriously, not transplanting a theorem
to triangular-FD multiple records, K.A and the sourced metering network.

[Primary publisher PDF](https://intlpress.com/api/bgcloud-front/resource/pdf/volume/1806261872028504065-1806261872028504065-76ddf6ddc1152a68b4b1a09558bf8154.pdf)

**BCLMP18, Bretti et al. (2018)**, Two algorithms for a fully coupled and
consistently macroscopic PDE-ODE system modeling a moving bottleneck on a
road, Mathematics in Engineering 1(1), 55–83, DOI 10.3934/Mine.2018.1.55.
Sections 1–2 use a spatially modulated flux and density-dependent bottleneck
motion, with assumptions allowing cars to pass it. That changes our
pointwise zero-passing/motion mechanism. Not adopted as a neutral representation
swap merely because it treats multiple bottlenecks.

[Primary full text](https://www.aimspress.com/fileOther/PDF/MinE/Mine-01-01-055.pdf)

## Unqualified further lead

**NODE25, Extended macroscopic node model for multilane traffic**, TRB 195
(2025), 103208, DOI 10.1016/j.trb.2025.103208. Indexed primary abstract/text
suggests lane-based node and lane-choice/invariance work. Both direct primary
opens failed. Not used as proof, not recommended as a ready substitute;
its approach-lane equilibrium/assignment setting may differ from our IT.

[Primary publication lead](https://www.sciencedirect.com/science/article/pii/S0191261525000578)

## Evidence judgement

There are genuine field/motion methods, so a representation mismatch is not
a demonstrated impossibility of macroscopic moving effects. The original
local constructions are distinguished from source results in the mathematical
companion. No audited source or completed construction supplies the entire
approved field/record/node/IT/E1 loop. Missing qualification is reported as
such; it does not establish failure of every A/C extension or the core research
question. A2 is newly explicit in the living inventory; no full-target winner.
