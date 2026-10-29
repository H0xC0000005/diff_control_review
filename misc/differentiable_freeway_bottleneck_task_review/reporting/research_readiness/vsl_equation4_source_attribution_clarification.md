# Equation 4: established request formation and an explicit normalization choice

2026-10-22. **Source separation approved and incorporated; equations unchanged.**

**User's question.** The conditional normalization is intuitive. Why is
Equation (4) entirely red as defined/derived here, and can literature
support be found?

The red D label originally recorded that the exact joint conversion from
independent lane-change desires to feasible outgoing requests was specified
in this review, rather than transcribed as a complete source equation. It
does not claim mathematical novelty or a lack of related source principles.
However, marking the entire equation red is too coarse: it combines an
adaptation choice, ordinary fraction accounting and a request form already
present in the principal source.

## What the sources support

| Part of Equation (4) | Evidence and justified attribution |
|---|---|
| Request equals sending amount times movement fraction | Subraveti's source Eq. (14), printed p. 1765, already forms lateral demand by multiplying sending demand by the desired lane-change fraction. Our amount-per-step form uses the normalized fraction as input. The request-formation form is retained; the new input conversion remains explicit. |
| Straight share is what remains after the chosen lateral shares | Ordinary accounting once the available movements partition the sending amount. The algebra is standard. The choice of how to assign the lateral shares must still be specified. |
| Preserve jointly feasible desires; proportionally scale them only when their sum exceeds the sending budget | Carey's R2/Eq. (9) and Algorithm A2 already use proportional rationing when requests exceed a common capacity, and satisfy them when they fit. In Carey that capacity belongs to a receiver competing inflows. Applying the same principle to one sender's outgoing requests is our adaptation. No inspected source is certified to contain this exact donor-normalization equation. |

The last distinction matters. Conservation requires the requests to share
one sending amount, but it does not force our particular sharing choice.
Prioritizing one lateral direction would also be possible. The existing
rule preserves relative lateral desires and leaves valid desires unchanged;
it is an elementary, source-supported convention rather than a new
lane-changing theory.

The general split-ratio framing is also described in Wright's introduction
and Section 2.1: a movement fraction expresses which destination an input's
traffic wants to use, while the node separately resolves receiving limits.
That supports the standard request/realization distinction; it does not
identify our exact conditional normalization as a Wright source equation.
Wright remains a supporting reference, not a new essential dependency.

## Consequence for presentation

The revised attribution describes Equation (4) as **source-supported
request formation with an adapted proportional-normalization convention**:
credit the request form to Subraveti, distinguish standard remainder
accounting, and identify the conditional donor normalization as our
adaptation of proportional rationing. It need not be presented as a wholly
new derived traffic law. The request form now uses Subraveti's green and B
label, the remainder uses neutral S styling, and the normalization uses
Carey's amber and A label. Adjacent text explicitly credits R2's proportional
receiving principle and retains responsibility for its sender-side use;
the request form cites Subraveti's source Equation (14). This changes
attribution, not the equation or the claim of which exact algorithm was
published. No verbatim Carey donor-normalization algorithm is asserted.

Carey's R2 is cited here for the proportional-sharing principle at request
formation. The actual receiving allocation in Equation (5) retains the
selected equal fixed priorities and R3/A3 interpretation. No demand-based
receiver priority, general-node guarantee, new source family or traffic
behavior is introduced by this clarification.

## Primary sources and actual reading

1. Nagalur Subraveti, Knoop and van Arem, *First order multi-lane traffic
   flow model—an incentive based macroscopic model to represent lane change
   dynamics*, source Eq. (14), printed p. 1765. Reread the archived primary
   article, PDF p. 10. This is report reference [3].

[Archived primary article](../../archive/full_text/FB0030.pdf)

2. Carey, Balijepalli and Watling, *Extending the cell transmission model
   to multiple lanes and lane-changing*, R2/Eq. (9), Algorithm A2, printed
   pp. 10–11 of the locally read 2013 author manuscript. Reread the existing
   extracted primary text. This is report reference [6]. Browser retrieval
   of the manuscript failed; the available local primary PDF/text supplies
   the method evidence, as in the earlier allocator review.

[Primary manuscript](https://eprints.whiterose.ac.uk/77315/7/Carey%20et%20al%202013_with_coversheet.pdf)

3. Wright et al., *On node models for high-dimensional road networks*,
   introduction/Section 2.1 split-ratio definitions. Reread the primary
   arXiv HTML; this is report reference [8].

[Primary author preprint](https://arxiv.org/html/1601.01054)

A bounded web search for an exact normalization precedent did not produce
an additional qualified method source. Unrelated lane-intention prediction,
microscopic-control and secondary search results are not used as evidence.
No exhaustive literature search or proof of absence is claimed. The
Subraveti publisher fetch failed; its existing archived article was used.

## Work record and status

Read the allocator/source-interface audits and current equations, then
check the primary passages above. Use `rg`, `sed`, installed pypdf text
extraction and the browser for source reading; use `apply_patch` to add
this clarification and append the allocator audit/dialogue. Verify local
links and compare the current report's `sha256sum` before and after. These
three Markdown files were the only edits in that clarification pass. The
PDF/LaTeX were then unchanged. The approved report update is recorded below.

No question is presented through an interactive prompt;
no scientific choice, new method, experiment, implementation, dependency
installation, sub-agent or external message is opened. Analytical review
and pending report/JM1 acceptance keep their existing status.

## Approved attribution-only report update

The user accepts the source separation and instructs incorporating it.
Update the live LaTeX/PDF, this clarification, the feedback-15 amendment
record, allocator source audit and successor dialogue. These six existing
files are the only modifications; add the build log and verification JSON
below. Before-edit copies and a 607-file snapshot are retained under
`/tmp/vsl_eq4_attribution6/`. No further permanent report version is created
for this small annotation change.

Build twice with the installed toolchain:

```bash
pdflatex -interaction=batchmode -halt-on-error -file-line-error -output-directory /tmp/vsl_eq4_attribution6/latex /home/zpz/repos/diff_minimal_meso/misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_literature_backbone_review_report.tex
```

Copy the built PDF beside the source and retain the final log. Check:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_eq4_attribution6/document_checks.py
git status --short
```

Verify all display and inline mathematics against the immediate before-edit
source after removing color wrappers. Check the unchanged bibliography,
equation numbering, palette, local links, protected hashes, main-text limit,
fonts and actual Carey/neutral/Subraveti math colors in the PDF. The model
and all eight numbered equations remain unchanged. The main text still
occupies about 2.92 pages at 10 pt; references occupy the separate fourth
page. No warnings or overfull/underfull boxes occur. No raster PDF visual
audit is claimed. The next allowed action is user reading and bounded
report feedback.

[Updated report](../../synthesis/research_readiness/vsl_literature_backbone_review_report.pdf)

[Attribution update build log](vsl_equation4_attribution_build.log)

[Attribution update verification](vsl_equation4_attribution_validation.json)
