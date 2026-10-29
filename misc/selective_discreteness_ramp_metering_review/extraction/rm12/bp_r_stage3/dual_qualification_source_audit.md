# A-primary/B-companion pass — primary-source audit

Date: 2026-10-07. Execution authorized under
[arrangement 62](../../../rm12_62_bp_r_stage3_dual_review_arrangement.md).
Primary sources only support the technical findings. This is a bounded citation
and equation audit, not a systematic literature census or a simulation study.

## Source facts newly examined

**RM10-P01, 2011 proceedings body, Sections 2.1–2.2 and conclusion.** The
author-uploaded text includes point and extended insertion cases. Its
uncongested-ramp branch assigns entrants the main-road mean speed; the congested
branch couples ramp flow and speed. Its mean supply calculation is not a
qualified transient law for donor-speed births in this task.
[Author-uploaded original](https://www.researchgate.net/publication/251530773_Capacity_Drops_at_Merges_an_endogenous_model).

**S12A005, 2016 manuscript, Section 2 equation (1), Sections 3 and 5.** A
point-insertion renewal construction connects the backward characteristic and
an accelerating entrant to long-run service. Distributed insertions introduce
wave/void interactions. These distinctions motivate the reviewer derivation
below; the paper does not establish that derived extension for our task.
[Institutional manuscript](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6).

**RM10-P02, 2016 multilane paper, Modeling Framework, printed pp. 2–4.** Its
coupled capacities use a constant-acceleration mean calculation, consecutive
nonoverlapping discretionary/mandatory areas, and congested-branch flow-to-speed
relations. This is an active-bottleneck calculation, not a general changing-rate
update for the existing lane-exchange reference.
[Institutional original](https://repository.tudelft.nl/file/File_d4844cb9-1115-47ab-ab36-443cc0ca7df4).
PDF screenshots of printed pp. 3–4 were attempted; at least the latter failed
with a cache error. No reliable figure inspection is claimed. Decision-critical
claims here use readable text, equations with unambiguous supports, and the
independent reviewer derivation; no ambiguous typesetting is silently corrected.

**RM0010, 2013 author preprint, Section 4 and Section 6 equation (15).** Its
conservative density update and fixed-priority merge are dynamic. Reduced
receiving is triggered by demand exceeding ordinary supply, with a calibrated
drop fraction. The authors explicitly distinguish this phenomenological law
from detailed transition-region acceleration/lane-changing mechanisms.
[Author preprint](https://arxiv.org/pdf/1310.2660).

**RM12-S3-A01, supplied 2006 journal, Section 2 and Appendix A.** Re-read the
local conservation/receiving and motion equations from the unmodified PDF.
The free acceleration depends on speed; traffic downstream also limits motion.
No constant acceleration, source-bin replacement, or sampled birth interpolation
is adopted. [Supplied original](../../../archive/user_supplied/rm12_bp_r_stage3/Lane-changing%20in%20traffic%20streams.pdf).

**RM0011, 2004 working-paper Section 3.** Rechecked the sending-lane initial
speed and actual-transfer descriptor construction, keeping this antecedent
distinct from the final journal.
[Institutional original](https://escholarship.org/content/qt8w70q261/qt8w70q261.pdf).

**RM12-S3-S01, 1994 network CTM, Section 3.2.** Reopened the original and
retained the previously qualified fixed-priority/unused-share allocation.
[Institutional original](https://escholarship.org/content/qt9pz309w7/qt9pz309w7.pdf).
RM0003 was opened for background only; no fresh control theorem is used.

## Reviewer deductions and their limits

The [mathematical companion](../../../synthesis/rm12/bp_r_stage3/dual_qualification_math.pdf)
derives a conditional local renewal mean using a bounded monotone free-motion
path; an inactive limit; a unique scalar priority/receiving fixed point; a
counterexample to matching acceleration solely by recovery duration; B's
fixed-trigger service plateau; and conditional startup mismatch of the proposed
present-entry A mean as well as B. These are reviewer deductions under stated
assumptions, not published theorems for the joined multilane reference.

The point construction does not prove that spatially separated insertions or
multiple interacting constraints can be represented by one renewal clock. A
donor speed is not inferred from accepted flow by blindly selecting the
congested FD branch. Birth/input statistics must come from each model's own
declared state/support. No reference-state oracle is permitted.

## Search and preservation

Three executed queries in one batch are recorded in the
[new query log](../../../search/rm12_bp_r_stage3_dual_queries.csv). Deduplicated
method reads, background/access limits and in-place reuse are recorded in the
[activity log](../../../screening/rm12_bp_r_stage3_dual_sources.csv).
Secondary search hits were discovery leads only. No new full text was archived;
the archived/supplied originals and prior search/validation snapshots are
unchanged. Neither unavailable RM12-S3-A03 nor the previously inaccessible
RM12-S3-Q01 was pursued. No experiment, calibration or gradient evaluation.
