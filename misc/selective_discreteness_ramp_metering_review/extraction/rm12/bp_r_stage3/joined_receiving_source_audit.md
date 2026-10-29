# Joined receiving and own-motion source audit

Date: 2026-10-08. Q.ACT A approved; continuation 67 step 2 investigated up to
the source/input checkpoint. [Readable findings](../../../reporting/rm12/bp_r_stage3/joined_receiving_findings.md).
Eight searches in four batches; primary text only supports technical findings.
No new paper file downloaded and no traffic experiment.

| Source | Actual access/location | Bounded finding |
|---|---|---|
| RM12-S3-A01, supplied 2006 journal | Existing full local PDF/text; Sections 2.1.2, 2.2, Appendix A and bibliography, PDF 4–6, 11–13 | Ordinary CTM requests use current densities; constrained motion instead names a numerical downstream-speed estimate over the ensuing interval and cites Daganzo/Laval 2005b. Separate donor lane-choice speed from this estimate. |
| RM12-S3-S02, RR-2003-2 | [Full institutional PDF](https://escholarship.org/content/qt1hp588xx/qt1hp588xx.pdf), Sections 2–4 and Appendix A, PDF 4–7 | Counts and waves for prescribed linear path segments; motion hooks do not uniquely specify the adapted node's own-speed rule. Pairwise stepping has stated coincidence limits. |
| RM12-S3-C01, PWP-2003-10 | [Full institutional PDF](https://escholarship.org/content/qt69r4t5pp/qt69r4t5pp.pdf), Sections 2.3, 4–5, PDF 8–12, 16–19 | Prescribed-path count contraction and numerical approximation; count accuracy alone does not establish pointwise speed-feedback accuracy. Do not equate this report with verified full-journal access. |
| RM12-S3-V03, Daganzo 2006 NHM | [Full publisher PDF](https://www.aimspress.com/aimspress-data/nhm/2006/4/PDF/1556-1801_2006_4_601.pdf), Sections 2.1, 5 and Appendix A | Prescribed-path variational consistency supports the isolated receiving calculation's lineage. General endogenous multilane linkage is a separate qualification. |
| RM12-S3-J01, Daganzo/Laval 2005, TRB 39(1), 31–46 | [Institutional journal record](https://its.berkeley.edu/publications/numerical-treatment-moving-bottlenecks); publisher full/abstract routes failed | Metadata describes an endogenous extension; the journal's complete algorithm was not read. This is an input target, not technical evidence that the adapted joined task is solved. |
| RM12-S3-M02, Simoni/Claudel 2017, TRB 104, 238–255, DOI 10.1016/j.trb.2017.06.010 | [Author-uploaded full text](https://www.researchgate.net/publication/318699176_A_fast_simulation_algorithm_for_multiple_moving_bottlenecks_and_applications_in_urban_freight_traffic_management), manuscript Sections 2.5 and 3.1–3.4, pages 8–14; author and lab publication lists cross-checked | Multiple endogenous restrictions have a concrete later algorithm, but its maximum-speed/passing specification differs. Section 3.3 introduces encounter approximation to terminate stepping. Neither that approximation nor its method is adopted. |

The M02 source is the author's own manuscript text, not later citing abstracts
on the same ResearchGate page. PDF-equation glyphs in the HTML extraction are
poor; use explicit prose for the encounter qualification, not invented formula
transcription. Publisher access to M02 also failed. No figures inspected.
The paper's algorithm is evidence against equating one pairwise stall with
general mathematical impossibility, not a proof of exact retained-chain closure.

## Reviewer deductions, not newly quoted literature results

The backward-wave arrival relation, saturated receiving envelope, delayed
speed response, idle-then-burst response and conditional node bookkeeping are
derived in the [mathematical companion](../../../synthesis/rm12/bp_r_stage3/joined_receiving_math.pdf).
They use an isolated source-free triangular-FD road with a prescribed forward
zero-passing path and compatible boundary data. This removes own-motion and
source feedback **for a diagnostic only**; no such task restriction is adopted.
They are not a reached metering witness, calibrated acceleration, full model
theorem or useful-gradient result. The positive receiving result cannot be
iterated through omitted E1 births and lateral transfers.

## Decision and access limits

Q.ACT is closed as A. ACT.B remains a distinct unselected approach; ACT.C is
deferred backtracking, not concurrent review. No further actuator approval is
requested. The nearest missing input is J01's complete own-motion method.
SRC.A recommends checking it first; SRC.B would explicitly declare additional
same-family construction if it remains unavailable. Both precede full-law
adoption; the accessible evidence does not select an unstated estimator.

The two old unavailable originals were not retried. No bibliography snippet,
institutional abstract, secondary survey, publisher search snippet or failed
page is treated as a full-method read. The browser gives incorrect generic
titles to C01/S02; covers and bodies verify their identity. See the
[query log](../../../search/rm12_bp_r_stage3_joined_receiving_queries.csv)
and [activity log](../../../screening/rm12_bp_r_stage3_joined_receiving_sources.csv).
