# S07.90 — Reachable near-drop preparation review work/check report

Date: 2026-09-29. Status: **Executed to S07-UG1 / DG-R4; Candidate A approved
and S07 subsequently closed.** S06 was closed before S07 opened.

## Work performed

Reconstructed the accepted geometry, response, demand, observation, matching,
accounting and preparation contracts. Derived strict and nominal arrival times,
final-400 m residence, low/peak cohort transition, nominal snapshot populations,
lane-specific quota rates and a localized balanced contrast bank. Inspected the
minimum official/primary material needed for departure, insertion-capacity and
strategic-anticipation claims. No general literature expansion was performed.

Created S06's closure; S07's approved protocol; LaTeX/PDF analysis; source/method
audit; query/access logs; findings/gate; and this report. Synchronized the living
inventory, dialogue, README, ordered sequence, recap and document registry.

## Assumptions and calculations

Arithmetic uses the accepted 2,400 m approach, region start 2,000 m, base front
position 5 m, 100 km/h road target, nominal 95 km/h baseline-response target,
2.6 m/s² acceleration and the fixed intended departure schedule. Advice-aware
times and region populations are nominal free-flow planning screens. They do not
bound native delay and are never described as SUMO results.

The recommended bank keeps all lane assignments common except one balanced
six-vehicle block, uses six permutations, and evaluates three decision times for
18 prefixes. The block indices were chosen inside the intersection of the final-
400 m residence windows under both nominal entry-speed conventions. Exact match,
actual occupancy and action relevance remain future empirical questions.

## Commands and sources

Commands: `find`, `sed`, `rg`, `git status`, one-off read-only Python arithmetic,
`latexmk -pdf -interaction=nonstopmode -halt-on-error`, pypdf text/page checks,
CSV/Markdown/link validation and `apply_patch`. New discovery used four bounded
web queries and official/primary opens recorded in the S07 logs. No package
installation, dependency change, provider/server command, simulation, model code,
traffic run, detached process or gradient calculation.

Sources: current official SUMO vehicle/type/route, insertion, road-capacity and
vehicle-speed documentation; Erdmann's 2015 primary LC2013 manuscript reused from
S06. Rolling documentation supports capability/risk statements, not a future
installed-version claim.

## Validation

- Independent Python recomputation of every reported timing and snapshot count.
- LaTeX build with two passes; formula PDF retained beside source.
- PDF page count and searchable-text extraction with pypdf.
- LaTeX log checked for errors, unresolved references and overfull boxes.
- CSV headers/row counts/IDs checked; registry paths/keys checked.
- Package-wide local Markdown links checked.
- Navigation/status audit confirms S06 closed and S07 stopped at DG-R4.

PASS results: strict/nominal times independently recomputed as 71.820000,
77.161880, 74.093684, 79.435565 and 14.413355 s; snapshot counts reproduced as
2/1, 4/4, 9/4, 16/12, 17/17, 16/16 and 17/17 for desired/zero insertion at
80/120/200/210/220/240/260 s. All three six-vehicle blocks fall inside the
intersection of the two nominal residence windows, and all six patterns contain
exactly two assignments per lane.

The PDF has four pages and 8,322 extracted text characters. PDF/TeX SHA-256 are
respectively `d39a303dc4bc10d65bf391fcdb1f5739d6797c9ecb226a0b743af5443da4ba32`
and `11b46a77e685dd70bd6f13d15c344b055f75e1920de27dc922492e4d5cdd0337`.
The LaTeX log has no error, warning, unresolved reference or overfull box.
Query/access logs each have four valid rows; the registry has 32 unique existing
paths including three S07 primary entries; 315 local Markdown links have zero
broken targets. Independent raster rendering was unavailable, so PDF validation
used LaTeX layout diagnostics plus pypdf page/text inspection. No numerical
traffic or gradient test applies.

## Remaining risks and next allowed action

Current native documentation suggests strategic anticipation can cover the whole
approach. Therefore exact history equality may fail even for the localized block.
Desired-speed insertion reduces an avoidable source bottleneck but is synthetic
and must be frozen explicitly. A positive future prefix match would not prove
lane occupancy alone is causal or sufficient; preparations also alter gaps/order.

Review [S07 findings/S07-UG1](s07_20_reachable_preparation_findings_and_gate.md)
and choose/adjust DG-R4. No experiment or later sprint starts automatically.

## Post-gate candidate synchronization

The user's staged A-then-B question exposed a materially distinct viable
candidate. Synchronized DG-R4 findings, inventory and dialogue without treating
the discussion as approval. The new ladder pre-registers both banks but permits
B only after A preserves exact history and loses all lane contrast. An A history
mismatch, an A nonzero contrast, subjective contrast size, or later negative
action evidence cannot trigger B. This clarification changes no evidence,
contract, budget or execution authorization.

## Subsequent closure

The user approved Candidate A, retained Candidate B only for possible later
manual agreement, rejected automatic fallback, and instructed continuation to
the next user gate. [S07 closure](s07_99_reachable_preparation_sprint_closure.md)
records the accepted boundary; S08 owns later planning.
