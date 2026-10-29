# BP-I Stage 1 — work and verification report

Date: 2026-10-06. Methodology/source review complete at BPI-G3; closure and
successor selection pending. [Findings and gate](findings_and_gate.md) is the
current handoff. [Document verification](document_validation.json) records checks.

## Files and work

Created the operational source audit under `extraction/rm12/bp_i/`, domain/premise
assessment under `synthesis/rm12/bp_i/`, and findings, work report and verification
under `reporting/rm12/bp_i/`. Added executed-query and qualified-source CSVs in
the existing `search/` and `screening/` directories. Updated RM12 protocol,
roadmap/comparison status, branch README, RM11 handoff pointer and RM12 dialogue.
Historical reports and dated verifications remain unchanged. Root project files,
feedback, code, configs and results were not changed.

Commands/tools: `rg`, `rg --files`, `cat`, selected `sed`/`head`/`tail` reads,
`git status --short`; primary web searches, opens, citation-link followups and
one failed PDF screenshot; documentation `apply_patch`; standard-library Python
creation/checking of CSVs and verification JSON. Web queries are recorded
verbatim with domain filters and access-qualified outcomes. Failed fetches were
followed through nearest primary alternatives; inaccessible methods are not
counted as full reads. No binaries or datasets were downloaded.

## Assumptions, checks and limits

The source choice is a reviewer default, not adoption of actual lane count,
source controller, sampled driver dynamics or proposed detectors. Public shared
inputs/knowledge, conservation, receiving/storage, common rates and complete TST
remain inherited requirements. Unreported information is not assumed absent.

Verification checks CSV schema/IDs, query-to-source references, local navigation,
current question/status consistency, required artifacts, and the unchanged
tracked-project boundary. All required Stage 1 assertions are traceable or
explicitly unsupported. No traffic, gradient, optimization, SUMO, scientific
implementation tests, dependencies or delegated work were required/performed.
Verification does not establish observability, control benefit or useful gradients.

**Passed:** 21 query rows across six combined search batches; eight unique,
access-qualified source rows (three reused, five new); resolved query-source
references; 73 local links across ten current documents; complete protocol
question inventory. The tracked status still contains only pre-existing root
AGENTS/PLANS changes. The initial scope checker stripped leading git-status
whitespace and misread the first path; preserving raw prefixes and rerunning
that check corrected the procedural error. No acceptance condition changed.

The principal risk is incomplete operational initialization/access evidence.
The result is evidence-limited with a supported input distinction, not a field
impossibility theorem. BPI-E1–E3 are complete as bounded evidence work; G2 was
not activated; G3 is pending. The next allowed action is user discussion of
the result and successor claim. BP-R and all later stages remain unopened.
