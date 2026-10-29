# K2: forced-merge qualification work and gate record

Date: 2026-10-14. Status: **User-approved K2 executed; bounded evidence pass
finished at the original VSL-B2-G1 terminal-contract gate. Pass 2 remains open.**

## Scope and concrete result

The user approved a compact arrival-aware terminal qualification retaining
H1 and requested an explicit forced-merge model at the next gate. The pass
formed a continuous-mass own-lane-first server with one ending queue, finite
residual receiving, conservative completion, full departures and finite
clearance. It joined the server to finite physical boundary histories under
a restricted receiving/storage domain, rather than assuming infinite holding
or an externally supplied future service curve.

The physical candidate reserves a final reach of the same road length and
ends early transfers at its entry. That exact handoff and priority await
adoption. The alternative is an explicitly virtual terminal approximation
retaining the full H1 opportunity window, with a weaker physical feedback
claim. The report presents these choices and stops. H2/B is not opened.

Two scientific clarifications are retained: S13's proportional-batch choke
was already concrete analytically, although physically unqualified; and a
forced queue alone does not ensure an interior advice optimum. Under a stated
fixed-preparation/fixed-service reference, earlier arrivals weakly improve
whole-cohort TST on the proposed own-lane-first branch.

[Main report and specific adoption gate](vsl_k2_forced_merge_findings_and_gate.md)

[Progress against the original roadmap](vsl_review_progress.md)

## Files changed

Added six artifacts: main findings/gate, source/reference audit, mathematical
`.tex` and PDF, this work report and validation JSON. Updated nine existing
review documents: README, opening-plan and methods notices, MP and living
candidate inventories, original-stage progress ledger, the H1 gate addendum,
the original B2 plan execution disposition and the append-only dialogue.
Exact file paths are in the validation record.

S13 authority, the urban closure, ramp closure, production source, dependencies,
user feedback and traffic results were not changed. Existing root edits in
`AGENTS.md`, `PLANS.md` and `memo.txt` were left untouched.

## Assumptions, ownership and remaining limits

The physical candidate assumes an initially empty terminal reach, fixed
geometry/parameters across actions, no internal early transfers there, initially
symmetric continuing lanes, a positive bounded common free-flow advice, and
the existing H1 homogeneous source adaptation upstream. Its strict receiving
domain keeps the ordinary load serviceable and allows only ending-lane
holding. A finite-storage/backward-history condition keeps terminal admission
from constraining H1; a donor sending limit remains explicit. A positive
forced queue is compatible with those conditions.

The terminal priority/work extension is an analytical adaptation, not a
calibrated zipper, gap-acceptance or generic-node theorem. A cooperative rival
can require an ordinary-stream queue and a different TST contract. The
fixed-preparation speed result applies only to its declared branch, not
arbitrary capacities, priority laws or changed preparation.

Current adoption is Type 2 under G3/VQ3-P/T/S, with G2 geometry/information
fairness and G4 complete accounting/evidence dependencies. The viewed-source
locations and unit transcription are Type 1 details after that global meaning
is accepted; they do not select a terminal region or priority. Exact H1 laws,
applied parameter/response evidence, fresh observer reachability, derivative
correctness and independent useful-gradient evidence remain unqualified.

## Commands and verification

Read repository scientific context, current review plan/results, S13's service
contract and the applicable feedback files. Used `rg`, `sed`, `cat`, `tail`,
`git status --short`, review-only `apply_patch`, and web `open`/`find`/one focused
`search_query`. The source audit lists every substantively viewed paper and
the publisher-extract access limit; search leads were not treated as evidence.

Verified `command -v pdflatex` returned `/usr/bin/pdflatex`. The LaTeX build,
from the review package, used the existing pdfTeX 1.40.25 / TeX Live 2023
toolchain:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -output-directory /tmp/vsl_k2_latex synthesis/research_readiness/vsl_k2_forced_merge_contract.tex
```

Created the temporary output directory first, built twice, and copied the
result beside the `.tex` source. Used installed `pypdf` 6.15.0 in
`/home/zpz/miniconda3/envs/differential_sim/bin/python` for strict parsing and
text extraction from every page. No installation or raster visual inspection
is claimed.

The temporary documentation/reference checker is
`/tmp/vsl_k2_latex/validate.py`; its command from the package is:

```sh
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_k2_latex/validate.py
```

The machine-readable record contains link/anchor checks, PDF page/text and
LaTeX-warning checks, exact receiving-work and pulse/batch TST arithmetic,
and the storage/work-bound reference checks. The general receiving and
earlier-arrival results are analytical proofs in the PDF, not simulator or
numerical-gradient validations. The checker performs no time-stepped traffic
integration, parameter search, optimization, AD or finite-difference experiment.

Verification passed: 244 local Markdown links and ten heading anchors across
the fifteen changed artifacts; strict parsing and readable text on all five
PDF pages; no LaTeX layout/reference warnings; exact-fraction mass/work,
pulse TST (eleven versus sixteen), batch priority TST (five versus six),
stock/eligible-queue and receiving/storage bound checks. These establish
document integrity and hand-reference consistency, not applied traffic
fidelity or useful-gradient evidence.

[Documentation and reference validation](vsl_k2_validation.json)

## Phase and next allowed action

This K2 evidence pass is finished. The original B2 plan has reached a specific
necessary-contract adoption gate, and the larger Pass 2 remains open until
that joined meaning is accepted and consolidated. The next allowed action is
user disposition of physical T1 versus virtual T2, including the proposed
terminal priority. T1 is provisionally preferred for finite physical storage
and receiving meaning. No successor review or construction starts here.

## Post-gate mental-model clarification — 2026-10-14

The user requested the traffic pictures and core additions behind T1/T2.
Updated the main gate report and living candidate descriptions, and appended
the interpretation to the review dialogue. T1 is now introduced as a physical
queueing section with a point merge; T2 as a vertical fluid queue at the
point. Both share the proposed service principle. The explanatory change
does not adopt a model, change an equation or reopen the evidence pass.

Used `sed`, `rg`, `tail`, `git status --short` and review-only `apply_patch`.
Standard-library Python checked 75 local links and eight heading anchors in
these four updated Markdown documents; all passed. No
mathematical, simulator or traffic checks were needed for this wording change;
the existing mathematical PDF and original validation record were preserved.
The scientific assumptions, current gate and next allowed action above are
unchanged.
