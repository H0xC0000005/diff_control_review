# Feedback 15: clarify the model's traffic meaning

2026-10-22. **All twelve feedback points addressed in the revised report.**
The user permits three main-text pages excluding references, while asking
for only the necessary extra space. The revision explains the established
model; it adds no traffic rule, source family or methodological decision.
Main text occupies about three pages at 10 pt; eight IEEE references occupy
the separate fourth page. The eight numbered equations are unchanged.

[Revised PDF](../../synthesis/research_readiness/vsl_literature_backbone_review_report.pdf)

[LaTeX source](../../synthesis/research_readiness/vsl_literature_backbone_review_report.tex)

[Final build log](vsl_feedback15_report_build.log)

[Document verification](vsl_feedback15_report_validation.json)

## Individual responses

The user's paragraphs are numbered here for traceability; the feedback
inbox is left unchanged. The following answers explain what the model
already means, and the revised PDF now says it directly.

| ID / status | Feedback | Direct answer and report change |
|---|---|---|
| **F15.1 — addressed** | Assumptions are mixed into the components. | Section 3.2 now lists the core assumptions together: closed cohort/constant advice, common lane physics, exit/full accounting, service/update conventions and sensitivity scope. These reorganize the existing JA1–JA7 assumptions; they are not new assumptions. |
| **F15.2 — addressed** | D and R lack definitions and intuition. | Section 3.3 defines D as the rate a cell can release and R as the rate a target lane can accept from all competing streams. They are rates in vehicle-equivalents per hour; multiplying by the time step gives the amounts available in an update. Departure ability and receiving space jointly constrain movement. |
| **F15.3 — addressed** | Bold component titles should name components. | Sections 3.1–3.7 now have component/topic names. Their opening prose explains the traffic question and function instead of making a question carry the heading. |
| **F15.4 — addressed** | I has no definition or intuition. | Section 3.4 defines it as the dimensionless incentive multiplier for a specific lane change. With a multiplier of one, density differences drive the request. Route urgency, keep-right and cooperation modify that motivation; larger values can sustain a desire even toward a more crowded destination. |
| **F15.5 — addressed** | Finite-end/empty-cell wording is procedural. | Remove the implementation-style list from the compact account. Explain lookahead and incentives through perceived density and urgency. Exact finite-end averaging, mode branches and zero-donor conventions remain in the unchanged companion formulation. |
| **F15.6 — addressed** | “Temporarily omit i” sounds like a boundary condition. | It was only a shorthand for not repeating the road-section index in the local allocation equations. Replace it with direct definitions of origin and destination lane indices, at each section. No physical boundary condition changes. |
| **F15.7 — addressed** | P/b and Eqs. (4)–(5) lack logical meaning. | P is the desired lateral proportion before common limits; b is the assigned fraction of the one sending amount; m is its traffic request. Two 70% requests become 50% each. Then choose a common service level so the receiver is filled or all requests are met; small requests return unused entitlement to others. These are demand formation and feasible service, respectively. |
| **F15.8 — addressed** | Does forward fallback mean queuing? | No. Traffic not served in the first allocation can still advance in its current lane if sending and receiving remain available; that additional straight flow is y. If receiving space also prevents forward movement, it waits upstream. Retained free-flow stock is not automatically classified as a queue. |
| **F15.9 — addressed** | Does E merging make A less able to serve and easier to queue? | It can: E uses part of A's shared exit service, so A's own traffic may have to wait. Accumulation in A can then reduce space for later arrivals and propagate congestion. This is competition followed by state feedback, not an unconditional extra capacity-loss or slow-entry recovery penalty. |
| **F15.10 — addressed** | h and the two TST terms are unclear. | Section 3.6 defines h as the number of cell advances remaining to the exit. The first term counts time spent before the cutoff. The second counts all future travel time of the remaining stock, weighted by remaining distance and divided by advice speed. No unfinished traffic disappears at the cutoff. |
| **F15.11 — addressed** | Why add final-A density? | Section 3.7 describes the reviewed pair: final A has density 60 or 90 vehicle-equivalents/km/lane. That one reading identifies which initial state is present, despite identical E and A+B observations. It is a rival testing whether the entire lane field is needed. Sufficiency is limited to that pair. |
| **F15.12 — addressed** | Scalar search and maximum advice look arbitrary. | One scalar advice makes direct search a strong simple alternative to gradients. With the same information and complete objective, comparison separates missing information from optimizer quality. Maximum advice asks whether optimization beats simply using the highest allowed speed. These are prospective comparison definitions, not executed results or a claim of certified global search. |

## Assumptions and scientific meaning preserved

The global assumption set is reorganized, not reopened:

| Existing assumption | Location in the new presentation |
|---|---|
| JA1: continuous stocks, fixed geometry/common FD | Lane-cell state and common-lane-physics bullet. |
| JA2: action-independent closed initial cohort | Cohort/advice bullet. |
| JA3: completion at the lane-drop line with unblocked downstream road | Exit/accounting bullet and final-E rule. |
| JA4: one positive constant common advice | Cohort/advice bullet and fixed physics. |
| JA5: old-state diagonal movements, shared limits, priorities, attempts and mandatory end | Service/update bullet and movement allocation. |
| JA6: all initial traffic's remaining population-time | Exit/accounting bullet and exact complete objective. |
| JA7: complete derivatives on regular traces, separate evidence claims | Sensitivity bullet and complete-time derivative explanation. |

The source hierarchy remains one Subraveti backbone with inherited Han
budgets and a Carey-led movement adaptation; Wright retains supporting
allocation credit. The stronger palette and B/A/D/S labels remain. The
new prose does not certify the exact variant as an author implementation,
give the whole Wright junction theorem to the component, or establish
positive information/gradient benefit. No experiment is run.

## Files, commands and document checks

Read feedback 15 and the global-assumption/verification contracts. Use
`rg`, `sed`, `cat` and `git status --short` for inspection. Edit with
`apply_patch`; snapshot and archive with Python file tools. Keep the
preceding hierarchy PDF/LaTeX unchanged in the v4 archive. Update the live
PDF/LaTeX, package README, selected structure, source-first overview,
historical hierarchy record and successor dialogue. Add this amendment
record, final build log and verification JSON. User feedback, source
contracts, analytical proofs, older archives, accepted old VSL report and
the separate urban/ramp records are unchanged.

[Preceding report archive](../../synthesis/research_readiness/vsl_literature_report_versions/v4/README.md)

[Existing global assumptions](../../extraction/research_readiness/vsl_joined_candidate_sources_and_assumptions.md)

[Existing information/optimizer contract](../../synthesis/research_readiness/vsl_joined_candidate_verification_contract.md)

Use the installed `pdflatex`, existing LaTeX packages and installed
Python/pypdf. Build twice after the final source edit:

```bash
pdflatex -interaction=batchmode -halt-on-error -file-line-error -output-directory /tmp/vsl_feedback15_report/latex /home/zpz/repos/diff_minimal_meso/misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_literature_backbone_review_report.tex
```

Copy the PDF beside its source and retain the final build log above. Run:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_feedback15_report/document_checks.py
git status --short
```

Snapshot `/tmp/vsl_feedback15_report/before.json` contains 600 existing
files. Check that only the seven intended existing report/navigation files
change and the six expected archival/report files are added. Check all
display equations and bibliography against v4 after removing style wrappers;
inspect the expanded inline definitions and removal of notation-only or
procedural text. Check numbering, feedback coverage, source-role wording,
the unchanged palette, actual PDF colors, embedded fonts, links and page
extent. Keep the sharing explanation with its equation and put references
on a separate page. Final LaTeX output has no warnings or overfull/underfull
boxes. PDF text/positions and drawing operators are inspected; no raster
PDF visual audit is claimed because no rasterizer is installed.

Final verification passes: seven display environments contain the same
eight numbered equations; the bibliography is unchanged; 72 inline
expressions now include explicit definitions. The only omitted old inline
tokens are standalone names for nominal free speed, backward-wave speed
and an unnamed request: their full definitions remain or are made explicit.
The v4 PDF/LaTeX are byte-preserved. All 197 checked local links resolve,
and 593 other snapshotted files are unchanged. The three-page main-text
limit, 10 pt text, four-page PDF, source colors and no-warning build pass.

The verification JSON records exact counts, hashes and environment versions.
No simulator test, traffic trajectory, gradient calculation, optimization,
dependency installation, agent delegation or external message is performed.
Pre-existing AGENTS.md, PLANS.md and memo.txt changes remain untouched.

## Status and next allowed action

Feedback 15 is addressed as a report revision. Analytical review remains
complete; report/JM1 acceptance is still for the user. No new methodological
choice has arisen, and no implementation or further review stage is opened.
The next allowed action is user reading and bounded report feedback.

**Approved source-separation follow-up, 2026-10-22.** Equation (4)'s former
all-red treatment is replaced by Carey-based A styling for proportional
normalization, neutral S for the straight-share remainder and Subraveti B
for request formation. Credit Carey's R2 principle while stating that its
sender-side application is our adaptation; cite Subraveti's source Eq. (14).
Mathematics, information, gradients and model behavior are unchanged.
The [attribution clarification and current checks](vsl_equation4_source_attribution_clarification.md)
record this later annotation pass; the main text remains about 2.92 pages.

## Section 3.7 follow-up: make the validation logic explicit

2026-10-22. **Request addressed as a presentation revision.** The user asks
what Section 3.7 tries to answer and wants its core designs and steps stated
directly. Rename it “Validation design and rival models” and open with the
questions: does hiding A/B loading worsen advice, can one local reading
suffice, and do gradients help choose advice?

The section now explains three comparisons in order. First, keep the same
physical model and complete objective and compare E-plus-A+B information
with separate lane information. Identical reduced observations require a
shared advice; the full observer may distinguish the paired states.
Model-aware inference from admitted histories remains allowed, while action
timing precedes later discharge revealing the split. Second, add only final
A-cell density to test whether the full lane field is needed; the 60/90
reading identifies the reviewed pair, with no broader sufficiency claim.
Third, distinguish derivative correctness from optimizer usefulness: check
the complete derivative against finite differences away from switches,
then compare gradient guidance with direct scalar search and maximum advice
under each information view, using matched initialization and computational
budget. Search remains an approximate reference, not a certified optimum.

These are existing prospective evidence requirements from the comparison
contract, made visible in the compact report. No finite difference, traffic
trajectory or optimization is executed, and no positive information or
gradient benefit is asserted. Mathematical formulas, assumptions, source
attribution and the underlying evidence contract are unchanged.

[Section 3.7 build log](vsl_section37_clarification_build.log)

[Section 3.7 document checks](vsl_section37_clarification_validation.json)

**Work and checks.** Edit only Section 3.7 in the report source; rebuild its
PDF, update this record, the package introduction and the successor dialogue.
Keep before-edit copies and a file-hash snapshot in
`/tmp/vsl_section37_clarification/`. Use the installed LaTeX toolchain and
Python/pypdf; no packages are installed. Build twice with:

```bash
pdflatex -interaction=batchmode -halt-on-error -file-line-error -output-directory /tmp/vsl_section37_clarification/latex /home/zpz/repos/diff_minimal_meso/misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_literature_backbone_review_report.tex
```

Copy the PDF beside its source and retain the final log above. Run the
document-only comparison with:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_section37_clarification/document_checks.py
git status --short
```

Check that all report source outside Section 3.7 is byte-identical, including
eight numbered equations, 72 inline expressions, source colors and eight
IEEE references. Verify a warning-free build, three main-text pages at
10 pt, references on page 4, embedded fonts and working local artifact
links. Inspect PDF text and positions; no raster visual audit is claimed.
Final document checks pass: the main text occupies 2.9974 pages, references
start on page 4, the build has no warnings or overfull/underfull boxes,
174 local Markdown links resolve, and 595 other snapshotted files are
unchanged. Report source outside Section 3.7 is byte-identical. The linked
JSON records exact extent, checks and preserved-file counts. A temporary
checker regex error was corrected before the passing document check;
it required no report or method change.
Analytical review remains complete and report/JM1 acceptance remains for
the user. No methodological choice or new review/implementation stage is
opened; the next allowed action is user reading and bounded report feedback.

## Final colleague-facing cleanup

2026-10-22. The user finds the content satisfying and requests a final
colleague-oriented editorial pass. The live report has the exact new title,
no subtitle, preserved source colors and full-word source attribution in
place of B/A/D/S shorthand. Internal review language, local companion links
and archival bibliography notes are removed. These source notes and the
precise adaptation audit remain in the review package; no source work,
formula, assumption or validation requirement is removed. The preceding
Section 3.7 version is preserved in v5. This is final presentation cleanup,
not new methodological or numerical validation.

[Final editorial work and document checks](vsl_literature_backbone_colleague_finalization.md)
