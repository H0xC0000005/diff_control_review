# Compact event/recovery memory — bounded primary-source audit

Date: 2026-10-07. T1 execution under [continuation 63](../../../rm12_63_bp_r_stage3_event_memory_continuation.md).
Primary facts are separated from reviewer deductions in the
[assessment](../../../synthesis/rm12/bp_r_stage3/event_memory_qualification.md).

## Source facts used

**RM12-S3-A01, supplied final 2006 journal.** Re-read PDF pp. 3–6 and 11–12:
Section 2.1 has paired continuous lane transfers; Section 2.2 creates particles
from cumulative transfers separately for each origin-cell/lane/target-lane
stream. Appendix A limits desired motion by immediately downstream traffic,
updates desired speed from the realized speed, and advances position. Its
acceleration parameter's maximum vehicle speed is distinct from KW free speed.
This supports event bookkeeping and explains why birth age alone does not
determine constrained recovery. It does not publish the compact summary now
sought. [Unchanged supplied PDF](../../../archive/user_supplied/rm12_bp_r_stage3/Lane-changing%20in%20traffic%20streams.pdf).

**S12A005, Leclercq/Knoop/Marczak/Hoogendoorn, author manuscript of the 2016
paper, DOI 10.1016/j.trc.2015.06.025.** Re-read abstract, Section 2, Section 4.3
and conclusion. Accurate mean capacity with suitable mean parameters does not
establish transient flow accuracy; wave/void interactions and upstream dynamics
receive separate treatment. This is evidence against dismissing compact means
solely because heterogeneity exists. It supplies no qualified event/recovery
service law for our whole changing-rate task.
[Institutional original](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6).

**RM10-P04, Laurent-Brouty/Costeseque/Goatin, HAL-02155131v4 (2020 author
version; SIAM 2021).** Re-read Sections 2–3, Theorem 1 and interaction-time
definition. The model retains accelerating leaders and ends their active
restriction at interaction with preceding traffic or attainment of limiting
speed. Its motion is constant-acceleration, initialized from density jumps;
the theorem is not for repeated ramp births or the supplied nonlinear CM.
It is evidence for location-sensitive activity, not a timer transferable by
name. [Author-uploaded original](https://www.researchgate.net/publication/346438282_A_Macroscopic_Traffic_Flow_Model_Accounting_for_Bounded_Acceleration).

**RM12-S3-T01, 2018 IFAC antecedent of RM10-P04.** Newly read Sections 1.2,
2.1–2.2, and theorem scope. A scalar traffic field and leader motion are
coupled; the active/inactive test uses local traffic along the trajectory.
The single-jump proof and uniform constant-acceleration/no-overtaking assumptions
do not qualify our multiple-birth ramp reference. This is a narrower antecedent,
not a second independent validation of the 2021 result.
[Author-hosted six-page original](https://www-sop.inria.fr/members/Guillaume.Costeseque/Laurent-Brouty-Costeseque-Goatin-2018.pdf).

**RM9-L03, Srivastava 2016 dissertation.** Re-read Chapter 3.3.1, Chapter 4.6,
and Chapter 5.4. A modified congested demand can represent acceleration/recovery
with aggregate density; its lane-drop geometry and acceleration mapping have
declared simplifying assumptions. The merge extension remains future work.
This keeps a strong compact alternative visible, without declaring its native
law a matched reduction of our event reference.
[Institutional original](https://escholarship.org/content/qt7dx478g4/qt7dx478g4.pdf).

## Deductions made in this pass

The new [analytical companion](../../../synthesis/rm12/bp_r_stage3/event_memory_math.pdf)
contains source-timing phase bookkeeping; a source-sampled free-motion recurrence;
a limited clipped-speed moment obstruction; and conditional descriptor relabeling
invariance. These are reviewer deductions. They do not prove a reachable
equal-history task pair, a universally impossible finite summary, a complete
spatial compact law, or useful control gradients.

The free-motion result is a checked subcase, not an adopted restriction of the
task. A distribution retaining every restriction's position/speed removes names
but not detailed configuration; it is an equivalence endpoint, not compactness
evidence. No additive disturbance penalty or exponential recovery timer is
inferred from these sources.

## Search and access

Six actual queries in two batches are in
[event-memory query log](../../../search/rm12_bp_r_stage3_event_memory_queries.csv).
The [read/access log](../../../screening/rm12_bp_r_stage3_event_memory_sources.csv)
records five technical sources and the two retained unavailability boundaries.
Other search results were discovery leads only; no secondary technical claim
is used. Existing source IDs are reused; T01 names only the newly read 2018
antecedent. No full text was downloaded, source PDF altered, traffic experiment
run, or unavailable original pursued. Text/equations were read; no new figure
inspection is claimed.
