# Feedback 20 evidence-debate work record

Date: 2026-09-15

> Historical work record. Feedback 21 subsequently accepted the negative role verdict, closed RM4, and opened the RM5 colleague-report scope gate.

## Outcome

Completed the requested evidence collection and debate without opening B1-P formulation. The active recommendation is that B1-P should not be the primary orthogonal parallel task; it may be preserved as an optional post-M3 transfer/ablation fixture. RM4 remains open at the user decision gate.

## Files created

- `synthesis/feedback20_evidence_debate.md`
- `reporting/feedback20_user_gate.md`
- `discussion/feedback20_response_record.md`
- `archive/metadata/feedback20_sources.md`
- `archive/full_text/RM0024.pdf`
- `archive/full_text/RM0025.pdf`
- this work record

## Files updated

- `README.md`
- `review_protocol_plan.md`
- `reporting/d1_user_gate.md` (marked historical/superseded; content retained)
- `reporting/current_handoff.md`
- `archive/manifest.csv`
- `screening/records.csv`
- `extraction/evidence_matrix.csv`
- `extraction/claim_source_map.md`
- `search/search_log.csv`
- `search/coverage_map.md`

No project file, source, test, configuration, milestone file, closed sibling review, or user feedback file was modified. Existing tracked modifications to `AGENTS.md` and `PLANS.md` were observed and left untouched.

## Evidence operations

- Read feedback entry 20 and the current D1 synthesis/gate/status records.
- Searched scholarly, publisher, arXiv, FHWA, NCHRP, Berkeley and author-repository sources for:
  - mesoscopic/DTA/event-based ramp-metering simulation;
  - adjoint, sensitivity, smoothing and automatic-differentiation ramp/freeway methods;
  - strong aggregate control alternatives and microscopic/hybrid scope boundaries.
- Inspected the full text of Reilly et al. (RM0024) and Goatin et al. (RM0025), plus bounded method/abstract evidence for RM0026–RM0030.
- Downloaded two public full texts into the approved archive. The first RM0024 endpoint returned an HTML challenge and was replaced with the valid Berkeley Connected Corridors PDF before manifest entry.

## Commands and checks

- `rg`, `sed`, `find`, `tail`, and `git status --short` for feedback/package/status inspection.
- `curl -L --fail` with approved network escalation for the two public PDFs.
- `file`, `sha256sum`, and pypdf page/title extraction for archive validation.
- Python `csv.DictReader` validation for all four updated CSV indexes.
- Python Markdown local-link resolution for the new/updated primary reading files.

Results:

- manifest: 28 rows, no duplicate IDs;
- screening records: 28 rows, no duplicate IDs;
- evidence matrix: 28 rows, no duplicate IDs;
- search log: 36 rows, no duplicate query IDs;
- RM0024: readable 23-page PDF, expected title phrase found, checksum matches manifest;
- RM0025: readable 33-page PDF, expected title phrase found, checksum matches manifest;
- seven primary Markdown files checked, zero broken local links;
- stale active-status search found only the deliberately retained historical E1 text beneath the superseded warning in `d1_user_gate.md`.

No simulation, code test, numerical experiment, LaTeX build or project implementation was run because none belongs to this review response.

## Assumptions and evidence limits

- "Differentiable ramp metering" was interpreted broadly enough to include exact discrete adjoints, smooth gradient methods and automatic differentiation, while keeping their derivative contracts separate.
- Abstract/method-level records were used only for high-level classification, not equation adoption.
- The pass is targeted and role-decisive, not an exhaustive systematic ramp-metering review. It supports rejection of B1-P for the specified role, not a universal nonexistence claim about all possible freeway tasks.

## Remaining risk and next action

The role conclusion is a recommendation pending user approval. The next allowed action is the user's F20-A/F20-B/F20-C decision in `feedback20_user_gate.md`. No formulation, new task-family search, closure, implementation or project amendment may begin automatically.
