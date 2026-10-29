# RM9-R1 source/measurement review work report

Date: 2026-10-05. Status: **Executed to UG4-O; stopped for user discussion.**
R1 evidence deliverable is finished; observer adoption/G1 closure is not.
Approved G0/G2 and UG1–UG3 remain unchanged. R2 has not started.

## Authorization, scope and result

The user explicitly authorizes R1 until the next user gate. Applied the accepted
method-first/no-extra-lanes/strong-history plan. Read current branch protocol,
handoff, inherited design/source records and repository context without adopting
implementation-compatibility restrictions. Interactive instructions override
old feedback; no new feedback request was present in the global inbox.

Executed five targeted searches, followed primary measurement research and FHWA
documentation, and rechecked existing FB0030 locally/web. Added four source IDs
with version/selected-section limits. Produced metric/observation/task evidence,
initialization/ramp/causal indexing requirements, PDF/TeX and C29–C32 claims.

The current CTM does not uniquely realize a physical detector passage speed in
congestion. A newly viable section-aligned Candidate C avoids the historical
cell-to-face identification but retains explicit representative FD equilibrium
and exact-section-observation assumptions. Recommend C for the first conditional
methodology benchmark; A and P retain their strongest viable forms. All remain
unapproved. Definitions do not establish a useful hidden state or field fidelity.

## Files created and updated

Created:

- `extraction/rm9_r1_measurement_source_audit.md`: primary evidence and channel/task matrix.
- `extraction/rm9_r1_observation_claims.md`: C29–C32, provenance and limits.
- `archive/metadata/rm9_r1_source_access_record.md`: source access/version record.
- `synthesis/rm9/rm9_r1_observation_contract_audit.tex` and `.pdf`: mathematical explanation.
- `reporting/rm9_60_r1_observation_findings_and_gate.md`: expanded C/A/P gate.
- This work report and `reporting/rm9_r1_document_validation.json`.

Updated search/screening CSVs, README, RM9 protocol, active handoff, formulation
inventory, detailed and brief continuation plans, historical findings navigation
and dialogue. Existing PDFs/source versions and user feedback are preserved.
No production model, slide, configuration, dependency, root AGENTS/PLANS or
milestone plan was changed. Preexisting root AGENTS/PLANS edits remain untouched.

## Commands and validation

Source work: batched rg/cat/sed reads; web searches/open/find on primary sources;
local pypdf extraction of existing FB0030. Used apply_patch and Python csv
append with ID/schema guards. Default Python lacked pypdf; reused the existing
`differential_sim` interpreter rather than installing anything.

Build:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/rm9_r1_observation_latex misc/selective_discreteness_ramp_metering_review/synthesis/rm9/rm9_r1_observation_contract_audit.tex

Copy and document checks:

    /home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/rm9_r1_validate.py

Validation checks: new/updated local links; CSV widths/unique IDs and four
new source/five query references; current gate/pending/deferral wording; PDF
page text/section completeness; final LaTeX warning/overflow scan; exact
Fraction arithmetic for the explanatory section-weighted mean/inverse and
the distinct passage-weighted mean. These are document/formula checks, not
traffic runs, numerical derivatives or G3/G4 validation.

An initial long history equation and justified table caused box warnings;
shortened notation and ragged-right cells corrected them. Final PDF has five
pages, with no LaTeX warnings or overfull/underfull boxes. Pypdf content checks
passed. No local PDF raster renderer is available; no visual rendering claim.
Full validation details are in [JSON](rm9_r1_document_validation.json).

## Assumptions, remaining risks and next action

Source metrics are evidence; representative FD speed, exact section observation
and any cell-to-face approximation are proposed model assumptions. No lane
symmetry, noise, private forcing, weaker history or favorable parameter tuning
was adopted. Candidate C changes the support of an unapproved speed proposal;
it requires a G1 decision and must not be silently treated as measured passage.

Initialization and concrete site/ramp geometry still need coherent task binding;
a fully known deterministic initial state is a sufficiency boundary, not a
hidden-information witness. The estimation source's no-lane-change assumption
prevents direct transfer. No reviewed source closes the entire strong-history/
useful-action/gradient chain. Field observation fidelity remains separate.

Next allowed action: discuss/adopt C/A/P at UG4-O, then complete compatible
G1 geometry/history transcription before R2. No R2/extension, successor,
SUMO installation, simulator, numerical gradient test or VSL restart is opened.
