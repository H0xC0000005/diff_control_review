# Exact-information continuation — source and transfer audit

Date: 2026-10-07. Execution of approved G1 under
[continuation 65](../../../rm12_65_bp_r_stage3_exact_information_continuation.md).
Read the [findings](../../../reporting/rm12/bp_r_stage3/exact_information_findings_and_gate.md)
for traffic meaning. This is a bounded nearest-source audit, not a general
impossibility claim or a source reproduction certificate.

## Methods actually checked

**RM12-S3-A01, supplied Laval/Daganzo 2006 journal.** Re-read Sections 2.1–2.2
and Appendix A, PDF pages 4–6 and 11–12. Continuous lane mass, deterministic
sampled transfer thresholds, zero-relative-passing descriptors and bounded
constrained motion are explicit. The downstream-speed estimate belongs to the
coupled KW problem. The retained particle state need not be replaced by moments.
The text does not give a complete ramp-node insertion/reset recipe for the
approved adaptation. The supplied file and hash are unchanged.
[Original](../../../archive/user_supplied/rm12_bp_r_stage3/Lane-changing%20in%20traffic%20streams.pdf).

**RM0011, 2004 working paper.** Rechecked Sections 2.2–3, PDF pages 4–5,
equations 5–10. It gives donor-lane birth speed and sampled cumulative floor
generation. Mandatory changes are not studied in its local discretionary rule.
It does not fill all ramp insertion/count-association details.
[Institutional original](https://escholarship.org/content/qt8w70q261/qt8w70q261.pdf).

**RM12-S3-S02, Daganzo/Laval RR-2003-2.** Re-read Sections 2–4 and Appendix,
PDF pages 3–7. It retains exact moving-boundary locations/counts, solves frozen
composite Riemann problems and specifies step restrictions. Bulk-field averaging
is a numerical approximation. Its reported multi-coincidence stalling and
suggested trajectory perturbation do not establish an exact adapted birth/node
resolver. No perturbation is adopted.
[Original](https://escholarship.org/content/qt1hp588xx/qt1hp588xx.pdf).
Browser title is erroneous; the PDF cover identifies the report.

**RM12-S3-C01, Daganzo/Laval PWP-2003-10.** Rechecked Sections 1–2.3, 4–5,
PDF pages 4–9 and 16–18. Prescribed-path count convergence is distinct from
pointwise speed feedback. General boundary results require well-posed compatible
data; they do not specify the new metered merge/birth interface.
[Original](https://escholarship.org/content/qt69r4t5pp/qt69r4t5pp.pdf).
Its browser title is likewise wrong; cover/body identify the report.

**RM12-S3-S01, Daganzo PWP-94-12.** Re-read Section 3.2, PDF pages 14–16,
printed pages 8–10. Fixed junction priority plus unused-share reallocation
determines flows from sending/receiving data. It does not determine newborn
moving-constraint insertion. N.A remains approved.
[Original](https://escholarship.org/content/qt9pz309w7/qt9pz309w7.pdf).

**RM8-P01, Laval/Cassidy/Daganzo merge manuscript.** Rechecked Section 2,
PDF pages 1–3. It couples retained accelerating changers to a point ramp merge.
This is positive physical precedent. Its priority calibration is not our N.A
operator, and its account does not bind our finite-approach upstream permission
and complete-clearing objective as one exact model.
[Author-hosted original](https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/f/3571/files/2023/03/merges.pdf).

**RM12-S3-E01, Goatin/Daini/Delle Monache/Ferrara (2023), NHM 18(2), 930–945,
DOI 10.3934/nhm.2023040.** Newly read Sections 2–3, especially equation 2.1,
Definitions 2.1–2.2 and same-lane interactions, PDF pages 2–8. It gives explicit
coupled trajectory/flux and interaction laws; same-lane encounters have a
specified continuation. Its controlled speed caps, passing law and bulk-road
description differ from the accelerating, lane-specific zero-passing reference.
It is evidence that interactions need a rule, not authority to import its rule.
[Publisher PDF](https://www.aimspress.com/aimspress-data/nhm/2023/2/PDF/nhm-18-02-040.pdf).
The PDF and publisher give 17 March 2023; a mirror gives a later date. Use the
primary version. A reference DOI mismatch on the publisher page is not reused.

## Exactness and new reviewer deductions

The new construction retains every distinct descriptor and all own information
needed by the chosen traffic field and speed supports. Numerical approximation
of the existing KW method is separate from information-reduction closure.
No evidence read here proves that exact retention is unacceptable for control.
No storage, runtime or compression requirement is imposed.

The [mathematical companion](../../../synthesis/rm12/bp_r_stage3/exact_information_chain_math.pdf)
derives source-correct cumulative-label bookkeeping, conditional exact-state
equivalence and a local birth-clock example. These are reviewer deductions from
conservation and declared clocks, not published theorems for the joined ramp
task. Exact source correction does not itself solve a simultaneous point
source/path event. Nor does conditional equivalence qualify clearance or gradients.

The next proposal binds when an actual transfer activates a restriction and how
it attaches to the conserved traffic count. Source sampled births and an
event-resolved extension are distinguished explicitly. Neither is silently
adopted by G1's exact-state approval.

## Coverage and access

Twelve actual queries in five batches are in
[search log](../../../search/rm12_bp_r_stage3_exact_information_queries.csv).
[Source activities](../../../screening/rm12_bp_r_stage3_exact_information_sources.csv)
record seven technical reads, a new limited-access lead, discovery exclusions
and the two previously unavailable originals. No further attempt was made to
retrieve either of those originals.

Laval's 2004 thesis was located as an author-upload listing but its full methods
were not read. Dymski's thesis generated search snippets; two library PDF opens
failed, and author-linked network chapter opens failed. These are discovery/
access limits, not technical evidence for adopting a new network solver. A
priority-solver preprint, second-order models, relaxation and microscopic
insertion models were discovery only. No new original was downloaded, no source
figures inspected, and no traffic simulation or empirical calibration performed.
