# Report revision: inherited backbone and concentrated movement adaptation

2026-10-22. **Historical hierarchy revision; followed by feedback 15.**
Its last PDF/LaTeX, including the plain-language exit correction, are
preserved as v4. The current [feedback-15 revision](vsl_feedback15_report_amendments.md)
adds assumptions and semantic explanations within the new three-page budget.
The user agrees with the inherited-Han description and asks to make the
few-dependency design explicit in the report. This is an authorized
presentation/attribution revision, with no change to equations or methods.

[Hierarchy PDF](../../synthesis/research_readiness/vsl_literature_report_versions/v4/vsl_literature_backbone_review_report.pdf)

[Adjacent LaTeX](../../synthesis/research_readiness/vsl_literature_report_versions/v4/vsl_literature_backbone_review_report.tex)

[Final build log](vsl_literature_backbone_review_hierarchy_build.log)

[Document verification](vsl_literature_backbone_review_hierarchy_validation.json)

## What the reader now sees

The prominent construction paragraph presents one Subraveti lane framework,
following its adoption of Han's congestion approach and completing/adapting
that formulation for the VSL task, plus one Carey-led movement replacement.
The hierarchy table separates the principal framework, inherited budget
lineage and movement adaptation. The thesis clarifies the backbone;
Wright supports allocation. The two aggregate alternatives remain
comparison-only. This is an explicit effort to concentrate independent
additions, not a claim that a globally minimal construction has been proved.

Section 3.2 identifies the full-budget interpretation as our completion,
including the omitted extra density-order sending switch, and keeps the
Han 2017 nominal/VSL source credit. The shared receiving mapping remains
an adaptation. The exact assembled variant remains ours, not an
author-certified Subraveti implementation.

Section 3.4 presents Carey's R3/A3 sharing and fallback as the movement
principles, extended to the selected three-lane composition. Wright is
explicitly supporting; no general Wright junction model is imported.
Equation (5) is now amber as an adapted Carey rule, with nearby cyan
supporting citation preserving Wright's actual contribution. The equation
itself is unchanged. Normalization, allocation/fallback sequencing and
mandatory lane-end closure remain explicit. They are not all geometry-only
changes or an unchanged published Carey algorithm.

The stronger palette, B/A/D/S relationship labels, three-section structure,
causal diagram, all eight numbered equations, inline mathematics, assumptions,
information/gradient definitions and eight IEEE bibliography entries remain.
The main text is about 2.39 pages at 10 pt, within 2.5 excluding references;
the PDF has three pages. No standalone evidence-boundary Section 4 is added.

## Files and preservation

Update the live PDF/LaTeX, package README, selected structure under
`temp_content/vsl_review_report/`, source-first overview and successor dialogue.
Mark the previous color work record historical and point its artifacts to
the byte-preserved v3 archive. Add the v3 README and this work/build/check
record. The earlier v1/v2 archives, accepted old VSL report, selected model,
analytical proofs, source audits and user feedback remain untouched.

[Preceding v3 PDF/LaTeX](../../synthesis/research_readiness/vsl_literature_report_versions/v3/README.md)

[Source-first explanation](vsl_literature_backbone_peer_work_overview.md)

[Han adoption and exact-variant evidence](../../extraction/research_readiness/vsl_congestion_join_sources_and_adaptations.md)

[Carey/Wright overlap and adaptation boundaries](../../extraction/research_readiness/vsl_allocator_sources_and_adaptations.md)

No new literature search or full-paper reading is claimed. Reuse the
preceding primary-source clarifications and the accepted H/LF1 decisions.

## Build and document checks

Verify `/usr/bin/pdflatex` is installed; use the existing LaTeX packages and
the installed Python/pypdf tools. Inspect with `rg`, `sed`, `cat` and
`git status --short`; edit with `apply_patch`. Use Python file tools to
snapshot 594 existing files and copy the prior PDF/LaTeX without changing
their bytes. No dependencies or environment settings are modified.

Build twice:

```bash
pdflatex -interaction=batchmode -halt-on-error -file-line-error -output-directory /tmp/vsl_literature_report_hierarchy4/latex /home/zpz/repos/diff_minimal_meso/misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_literature_backbone_review_report.tex
```

Copy the built PDF beside its source and the final log to the link above.
Run the document-only checker:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_literature_report_hierarchy4/document_checks.py
git status --short
```

Check display/inline mathematics and bibliography against archived v3 after
removing style wrappers only; verify equation/citation numbering, source-role
wording, color use, unchanged palette, contrast, embedded fonts and local
links. Measure the main-text end from the LaTeX save-position marker and
inspect extracted text/positions for layout. The final log has no warnings
or overfull/underfull boxes. No PDF rasterizer is available; no rendered-PDF
visual audit is claimed. The changed role of Equation (5)'s color is checked
in the actual PDF drawing operators. This is not traffic/gradient testing.

The verifier records exact counts, hashes and protected-file results in the
JSON above. Root AGENTS.md, PLANS.md and memo.txt contain pre-existing user
changes and remain untouched. No simulator, configuration, experiment,
implementation milestone, separate urban work or closed ramp work is changed.

## Status and next allowed action

The report revision is delivered for user reading. Analytical review remains
complete, with report/JM1 acceptance still separate. Its empirical fidelity,
positive action-information value and useful gradients are not established
by this presentation revision. The next allowed action is bounded report
feedback/revision. No review stage, experiment or implementation starts.

**Plain-language wording follow-up, 2026-10-22.** The user asks to replace
“Free A/B outlets complete trips.” Write that trips end when traffic leaves
the modeled road through A or B, assuming no downstream congestion blocks
the exit. Also describe the boundary flow as traffic leaving the modeled
road. This is wording only: service constraints and equations are unchanged.
Keep before-edit copies in `/tmp/vsl_outlet_wording5/`; rebuild twice with
the command above and rerun the document checks. Update the current page
extent and final log/verification. User review remains the next action.
