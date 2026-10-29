# Allocator assessment: work and preservation record

2026-10-21. **Bounded allocation assessment complete; LF1 behavioral choice
open; full replacement task qualification incomplete.** The latest user
instruction authorizes substantive allocation-first review. It does not
approve a new allocation law or reopen simulator development.

## Work and result

Read the current feedback-14 response, approved short backbone-comparison
plan, native-flow qualification/source audit, earlier component audits,
successor dialogue and relevant repository authority. Read the feedback
inbox, without changing it. Reused the native Subraveti/Han method evidence
and its limitations rather than redoing the earlier full review.

Read primary Carey manuscript methods and Wright preprint methods. The
reference audit distinguishes these from metadata/preview checks of
Tampère/Roncoli and failed retrievals. Carey's public PDF required minimum
network escalation after browser timeouts and a sandbox DNS failure; the
same required download then succeeded. No full paper was added to the
repository archive. Its reading copy and extracted text are in
`/tmp/vsl_allocator_review/`.

Constructed a proposed, source-supported three-lane component with joint
donor normalization, fixed-reference-priority receiving allocation and
forward fallback. The mathematical note proves conditional nonnegativity,
shared sending/receiving limits, conservation, permission and stock/storage
bounds, and states the elementary receiving/headway assumption. It also
gives a counterexample to unrestricted total-flow maximization. Compared
with fixed turning fractions and lane-level FIFO through the same blocked
neighbor example. The source methods do not establish this exact composition
or transfer their general-junction certificates to it.

This is a concrete analytical proposal rather than a simulator
implementation or a full task proof. Static rational calculations check
displayed budget examples only; no time trajectory, traffic calibration,
AD/finite-difference experiment, optimization or SUMO test is run. No seed,
GPU or scientific run configuration is applicable.

## Artifacts and synchronization

Added:

- `reporting/research_readiness/vsl_allocator_findings_and_gate.md`
- `extraction/research_readiness/vsl_allocator_sources_and_adaptations.md`
- `synthesis/research_readiness/vsl_allocator_contract_and_checks.tex`
- `synthesis/research_readiness/vsl_allocator_contract_and_checks.pdf`
- `reporting/research_readiness/vsl_allocator_build.log`
- this work report and `vsl_allocator_validation.json`

Updated existing README, active lane-backbone qualification, its source-audit
continuation notice and successor dialogue. Existing source equations,
earlier hand mathematics and accepted compact report remain byte-identical.
The feedback inbox and root authority/user files remain byte-identical.
No urban files are written. Root pre-existing changes to `AGENTS.md`,
`PLANS.md` and `memo.txt` remain outside this work.

## Commands and verification

Used `rg`, `sed`, `tail`, `git status --short`, primary-source `web.run`,
standard-library Python download/hash/path/JSON utilities, installed pypdf,
exact `fractions.Fraction` arithmetic, `apply_patch` and `pdflatex`.
One failed patch context was corrected without changing the intended scope.

The public source fetch used Python `urllib.request.urlopen` for the exact
Carey institutional manuscript URL recorded in the source audit, saving to
`/tmp/vsl_allocator_review/Carey_2013_author_manuscript.pdf`. No installation
or environment mutation was required. PDF text extraction uses
`/home/zpz/miniconda3/envs/differential_sim/bin/python` (Python 3.11.9,
pypdf 6.15.0). The system TeX toolchain is pdfTeX 3.141592653-2.6-1.40.25,
TeX Live 2023/Debian.

Build command, run twice, with stdout saved to `vsl_allocator_build.log`:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory /tmp/vsl_allocator_review/latex /home/zpz/repos/diff_minimal_meso/misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_allocator_contract_and_checks.tex
```

Copied the resulting PDF beside its `.tex`. Both passes succeed; the final
pass has no warnings, overfull boxes or underfull boxes. The four-page PDF
was text-extracted page by page to verify its contents and final references.
No raster preview tool is installed, so no image-rendered visual inspection
is claimed.

Before-edit snapshot: `/tmp/vsl_allocator_review/before.json` (524 package
files plus root/feedback hashes). Reproducible local verification command:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_allocator_review/checks.py
git status --short
```

The checker compares every prior package-file hash, permits only the four
stated existing-record updates, checks protected root/feedback hashes,
new-document relative links, final LaTeX log/PDF contents and exact rational
hand results. It is a static document/analytical-case check, not traffic or
gradient verification. All assertions pass: 520 prior package files are
unchanged, four existing records are updated, seven artifacts are added,
all new relative links resolve, and the four-page PDF and exact hand cases
pass their checks. The initial checker invocation stopped on a missing
document heading update; synchronizing that heading resolved it without a
mathematical or criterion change. Results are recorded below.

[Static preservation, PDF and hand-case checks](vsl_allocator_validation.json)

## Assumptions, remaining risk and next allowed action

The retained research question concerns omitted A/B lane loading and useful
VSL sensitivity under fair comparisons. The accepted old stack is guidance;
its equations or certificates are not required to transfer. No information
advantage, interior optimum or useful gradient is presumed. The proposed
flow law depends on admissible CTM input budgets and fixed-grid timing;
joining native congestion/capacity-drop and VSL branches must still establish
those conditions. Its transport, priorities, residual handling and endpoint
mapping remain unapproved candidate assumptions. It has no inherited global
maximal-flow, continuum or nodal-invariance guarantee.

LF1 now requires the consequential behavioral selection explained in the
main report. Provisionally recommend attempts with forward fallback. After
selection, qualify that law with VSL/congestion and complete the information,
population-time and derivative contracts. This work stops here. The accepted
VSL report and closed Step 4, separate historical acceptance records, closed
ramp line and urban scope retain their status. No agent, external message,
dependency installation, production file or traffic experiment is involved.
