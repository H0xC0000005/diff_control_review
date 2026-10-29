# T1 continuation: joined-model review work report

Date: 2026-10-14. Task: execute the remainder of the original VSL-B2/Pass 2
review after the user selected T1. This is a methodological review and document
build, not simulator development or a traffic experiment.

## Outcome and status

A single H1/T1 contract now joins the initial cohort, early opportunity and
receiving, preparation handoff, physical terminal histories/storage, forced
service, full departures and complete TST. A scaled algebraic family shows
active early receiving and positive forced waiting together, with no
terminal restriction of H1. Conservation, restricted well-posedness and
finite clearance are derived in the mathematical note.

**The planned Pass 2 evidence review is finished at VSL-B2-G1's exact-contract
confirmation gate.** The user selected T1's finite physical section, described
handoff and restricted own-lane-first direction. The assembled exact H1/T1
laws and domain await confirmation before freeze. No original Pass 3 work
was opened and no additional shared choice was needed.

## Assumptions and qualification refinement

Retain H1's homogeneous uniform footprint, ideal constant common preparation
speed, local uniform lateral source, fixed physical opportunity scale and
triangular diagram family. Initial continuing symmetry and empty terminal
histories preserve scalar sufficiency. T1 ends early sources at the terminal
entrance and puts compulsory completion at its downstream point.

Retain fixed work factors and strict continuing priority in the one-queue
member. Add conservative exit-work ceilings no greater than the slowest
action's lane capacity, alongside the already reviewed ordinary-load and
storage bounds. This narrows the qualification domain to make the exit
receiver compatible across actions; it adds no state or mechanism.

The algebraic coefficients demonstrate compatibility, not calibration,
a chosen scenario, an observer witness, an interior optimum or control
usefulness. Outside the declared domain, the smallest affected shared
contract must be reopened rather than clipping mass or adding queues.

## Files changed

New artifacts:

- Reporting: vsl_t1_joined_model_and_gate.md; vsl_t1_work_report.md;
  vsl_t1_validation.json.
- Synthesis: vsl_h1_t1_joined_contract.tex and its compiled PDF.

Current-status and interpretation updates:

- Package README.md and vsl_successor_00_opening_plan.md.
- Synthesis: vsl_feedback1_core_model_candidates.md and
  vsl_successor_methods_outline.md.
- Reporting: vsl_review_progress.md, vsl_r1_modeling_problem_inventory.md,
  vsl_k2_forced_merge_findings_and_gate.md, vsl_h1_homogeneous_window_findings.md,
  vsl_b2_p1_joined_service_review_plan.md, vsl_successor_opening_dialogue.md.
- Extraction: vsl_k2_terminal_source_and_interface_audit.md, including the
  continued viewed-paper list and exact source/adaptation limits.

All paths above are inside the review package. S13 mathematics/PDF and its
closure, the urban closure, the ramp closure and the user's feedback inbox
remain unchanged. Pre-existing root edits to AGENTS.md, PLANS.md and memo.txt
were observed and left alone.

## Commands and source access

Read the existing context, plans, feedback and applicable review records with
rg and sed/cat. Read-only git status identified unrelated existing root edits.
Re-viewed the three fully accessible primary papers named in the terminal
audit with the web tool. Checked Jin's primary preprint and publisher metadata;
other returned search leads were not used as new reviewed papers.

Verified the installed pdfTeX 1.40.25, TeX Live 2023/Debian, with
pdflatex --version. Built from the review-package directory using:

    mkdir -p /tmp/vsl_t1_latex
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory /tmp/vsl_t1_latex synthesis/research_readiness/vsl_h1_t1_joined_contract.tex

Run the same build command a second time for final outlines, then copy:

    cp /tmp/vsl_t1_latex/vsl_h1_t1_joined_contract.pdf synthesis/research_readiness/vsl_h1_t1_joined_contract.pdf

The first build exposed two text-width warnings. Rephrased only the affected
assumption/bibliography prose and rebuilt. No equation changed. Section
symbols were also written as words to retain clear searchable source text.

Verification uses the existing differential_sim Python environment and
installed pypdf 6.15.0:

    /home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_t1_latex/validate.py

The scratch validator checks document links/anchors, strict PDF parsing and
text extraction, the LaTeX log and exact rational coefficient/reference
arithmetic. It contains no time stepping, traffic integration, parameter
search, optimization, autograd or finite-difference traffic calculation.
No dependencies were installed.

## Verification results

Verification passed: 269 local Markdown links and 13 heading anchors across
16 artifacts; strict parsing and text extraction on all six PDF pages; a
clean final LaTeX log; exact joint-domain coefficient and preparation-branch
arithmetic; and the reused isolated terminal pulse references.
The reference family has front residuals 7/20 and 125/352 times the reference
density, and positive initial fast terminal queue growth 581/1760 in its
normalized mass-rate units. These checks substantiate the algebra, not a
traffic simulation or action preference.

The initial PDF-heading check encountered a kerning space in the extracted
word “Well-posedness.” The scratch check now normalizes whitespace before
matching the same required headings. No PDF content, scientific criterion
or equation was weakened to pass it.

Final verification is recorded in the linked machine-readable record.
The full conservation, scalar reflection, finite-storage and TST statements
are analytical deductions in the PDF; documentation checks are not presented
as simulator validation. Raster visual inspection is not claimed.

[Verification record](vsl_t1_validation.json)

## Remaining scientific limits and next allowed action

Sources support ingredients, not joint field calibration of the uniform
footprint, opportunity scale, early cutoff, speed response, priority and work
factors. The selected no-spillback/ordinary-load domain is conservative.
A queue and a preparation response do not establish an interior optimum,
a hidden-state action split or useful gradients. The scalar rival remains
capable of reproducing the whole proposed model.

The current action is confirmation of the assembled conditional contract
at the original gate. After confirmation, the next allowed task is opening
Pass 3's matched-observer and evidence review. It has not started; no simulator
implementation, installation, traffic experiment or ramp work was performed.

[Conceptual result and confirmation gate](vsl_t1_joined_model_and_gate.md)

[Combined mathematical contract](../../synthesis/research_readiness/vsl_h1_t1_joined_contract.pdf)
