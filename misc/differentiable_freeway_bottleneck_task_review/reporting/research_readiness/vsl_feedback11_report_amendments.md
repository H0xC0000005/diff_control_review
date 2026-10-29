# Feedback 11: a traffic-first explanation of the existing VSL model

Date: 2026-10-20. **Requested report revision completed for user reading.**
All ten numbered items are answered individually. The feedback-11 tab stays
unmarked for further rounds. Changes remain red until the user explicitly
requests normal color. The methodology target is now 3.5 pages excluding
references; main text remains nominal 10 pt.

[Revised PDF, changes in red](../../synthesis/research_readiness/vsl_compact_methods_report.pdf)

[Retained LaTeX source](../../synthesis/research_readiness/vsl_compact_methods_report.tex)

[Equation/source coverage and reading limits](../../extraction/research_readiness/vsl_compact_report_source_and_coverage_map.md)

## Direct answers and report changes

| Item | Answer / core improvement | Report location |
|---|---|---|
| **1** | The original questions are distinct: what omitted information changes traffic service; whether it changes useful speed advice; whether the complete gradient predicts useful interventions. Each is a separate bullet, without assuming a positive result. | Part 1 |
| **2** | This is explicitly one permanent three-to-two lane drop, one specified finite cohort and one constant common advice. MA1–MA5 separately state the representation, advice response, lane coupling, point-service closure and recovery memory. No numerical scenario or new assumption is invented. | Part 2 |
| **3** | The literature motivates conserved traffic, finite receiving and state-sensitive discharge. Capable aggregate/history models already address VSL/capacity drop, while lane models supply additional traffic state. The specific matched-information/control/full-gradient comparison still needs its declared observations, complete objective and peers. The paragraph ends with this task's criteria, including lawful inference, the sufficient compact peer and scalar search. | Part 2, “Why this test” |
| **4** | The source/adaptation statement now touches the defining equation: conservative transfer/receiving, terminal travel, forced work and isolated recovery. Study-defined closures are identified at the same point. Gradient corrections retain their specific source; our joined deductions stay separate. | Parts 2, 3.1–3.4, 5 |
| **5** | The reader first pictures E traffic finding early room in A, residual E being forced to merge at the choke, and a slow discharged entry continuing to restrict followers while it recovers downstream. The four components then have a traffic meaning before their formulas. | Part 3 introduction |
| **6** | The service formula is already concrete. Solve its specified work equation for E discharge when E queues; the A flow, A speed and allocated E work are given by the selected sharing branch. The previous braces meant multiplication. An explicit dot and equality now remove that ambiguity; no new function is left to choose. | Part 3.3, equation 5 |
| **7** | Removed the procedural sentence about rates outside an interval and negative-time values. Empty cohort-count history remains a meaningful initialization statement, introduced after explaining terminal travel. The finite cohort and its entry interval still define the same arrivals. Other revised sections now lead with behavior rather than update instructions. | Part 3.2 and component introductions |
| **8** | The report now calls the lane quantity a representative boundary speed. “Mark” was bookkeeping terminology, not a claimed conventional traffic term. Free and queued speeds retain their existing definitions; the queued value is an equilibrium closure, not a newly tracked vehicle trajectory. | Parts 2, 3.3, 3.4, 5 |
| **9** | A queue forms when arrivals cannot pass; after the last waiting traffic has passed, immediate passage resumes if feasible, including equality. New arrivals determine current demand after a rate change. Clearing a queue does not erase the separate recovery effect of traffic already served. | Part 3.3 after the table |
| **10** | Recovery now begins with the traffic effect on following A/E traffic. The equivalent boundary speed describes service recovery caused by downstream acceleration and backward-wave propagation. The loss is explicitly the part of undisturbed A/E service still unavailable at the choke. Crossing times, discharged mass ranks, insertion speeds, the recent-mass reading and its shared budget are defined in words. | Part 3.4; notation also clarified in Parts 2 and 5 |

Two distinctions prevent a methodological misunderstanding. First, the
service function is fully specified; the unknown is the flow solving it.
The explicit multiplication dot changes presentation only. That equation
is needed when E queues, while the free-E branches remain in the same table.
Second, the physical mechanism behind recovery is downstream acceleration,
but its square-root quantity is an equivalent boundary-flow speed. Calling
it the actual downstream acceleration trajectory would change its meaning.
The revised paragraph preserves the accepted isolated-point interpretation
and identifies exactly whose service is reduced and where.

The Part 2 chain is a synthesis of inspected literature ingredients and
the accepted research contract. It is not a universal published checklist,
a blanket finding that peer models are inadequate, or a modeling-novelty
claim. Permitted histories may reveal the lane split and all lawful inference
remains allowed. The compact peer and same-model scalar search remain
serious comparisons rather than results assumed to fail.

## Changes, provenance and preservation

Changed the current report source/PDF, source/coverage map, report plan,
four entry-point notices, progress and dialogue. Feedback 11 gains only an
answered token on each of its ten item lines; no user wording is rewritten.
The underlying accepted global-assumption statement, AS1–AS3 mathematics,
source studies and evidence remain unchanged.

The report retains 11 equation groups and the complete four-branch service
table. Ten displayed groups are unchanged byte for byte. Equation 5 prints
the already defined work function with an explicit multiplication dot and
its existing allocated-work equality; its traffic law is unchanged. All
physical coefficients, branch conditions, objectives, information rights,
compact-peer equality and regular sensitivity retain their definitions.

The bibliography now has seven IEEE entries. The extra short-report citation
is Wei, Han and Wang's already reviewed strong aggregate VSL/history/capacity-
drop model. Rechecked its publisher abstract, cumulative-state scope and
publication metadata; no source model is adopted. Rechecked Leclercq's
point expression and equivalent-speed note, and Jin–Jin's primary abstract/
metadata as additional context. Reading limits are retained in the source map.

Saved the 466 pre-edit package hashes and exact feedback text in
`/tmp/vsl_feedback11_before.json`. Exact pre-amendment source/PDF/map bytes
are in the [v2 archive](../../synthesis/research_readiness/vsl_report_versions/v2/README.md).
Earlier report versions, build logs and validation records are preserved.

## Build and verification

Used existing `pdflatex`, `xcolor.sty`, `cite.sty`, and the installed review
Python/pypdf environment. No dependency was installed. Inspected repository
context, roadmap, feedback, accepted question/assumption/model/source records,
the current source/PDF and Git status using `sed`, `rg`, Python and
`git status --short`. No production implementation milestone is opened.

Two final LaTeX passes, from `synthesis/research_readiness/`:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/vsl_feedback11_latex vsl_compact_methods_report.tex
```

[Retained final build log](vsl_feedback11_report_build.log)

Artifact checks:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_feedback11_report_checks.py
git status --short
```

[Verification results](vsl_feedback11_report_validation.json)

Checks cover equation/table preservation, the ten response items, red text
in PDF drawing instructions, conventional speed notation, adjacent source
credit, resolved IEEE citations/DOI links, 10 pt main type, embedded fonts,
main-methodology extent excluding references, local document links, feedback
token-only edits and protected file hashes. PDF text and layout geometry
are inspected; no raster visual inspection is claimed. The conceptual
traffic introduction stays together on a page. The final build is free of
warnings and overfull/underfull boxes. No font shrinking is used.

**Results: passed.** Four physical A4 pages contain about **3.38 pages of
methodology excluding references**, within the 3.5-page target. All 13 fonts
are embedded; the main type remains nominal 10 pt. Actual PDF text drawing
instructions confirm red changes on every page. All seven IEEE citations
and DOI links resolve, ten equation groups match v2 exactly, and the
service table is unchanged. All 575 local links and 22 heading anchors
across the nine changed/new Markdown documents pass. Nine existing package
files changed, seven were added, none were deleted, and all 457 protected
artifacts plus the v2 copies pass their hash checks. Feedback changes are
exactly the ten individual answered tokens; the tab remains open.

Pagination inspection exposed a separated model heading/mental picture;
an explicit page break keeps them together. Color-content assertions use
kerning-normalized PDF word strings while retaining the actual RGB check.
Neither correction changes a scientific or reporting criterion.

## Assumptions, status and next allowed action

No new scientific assumption or methodological choice is needed for these
amendments. The accepted conditional model and evidence boundaries remain
in their archive; the user-requested compact report still omits a separate
limitations discussion. No simulator code, package installation, traffic/
ODE run, optimization, AD/numerical-gradient or SUMO experiment occurs.

This report revision stops for user reading and further item-level feedback.
Overall Step 4, the historical Step 3 formal-closure record, urban work and
optional SUMO status are unchanged. The next allowed action is a requested
editorial correction, normal-color conversion when explicitly requested,
or a separately opened companion item; none starts automatically.
