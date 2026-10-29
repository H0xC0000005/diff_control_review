# Pack navigation refactor work report

Date: 2026-09-17. Pack-maintenance task only, not a new scientific sprint.
Current review status remains S05 at pending DG-AC1 / DG-R2.

## Requested change and assumption

User requested names/metadata exposing report order and sprint relationships.
Use stable sprint IDs plus document-role slots while retaining semantic suffixes
and original N1/N2/Route B/gate identifiers. Scope is primary reports and root
plans; evidence archives/registers and technical/mathematical annexes retain
their names. Shared dialogue IDs identify origin, not an exclusive coverage period.

## Changes

Renamed23 primary documents:19 reporting files and four root plans.
Added a sprint/role heading and predecessor/gate/index metadata to each.
Updated package filename/path references mechanically. Added00_review_sequence.md
and review_document_registry.csv; README points to the new reading guide.
No extra development phase or scientific sprint, result, approval or model change.
Earlier console links using the old canonical filenames are now obsolete;
the registry provides their new targets. No duplicate draft/alias files created.

## Commands and checks

Read-only rg --files, rg --no-ignore reference search, sed, git status;
existing Python standard-library snapshot/hash/metadata checks; apply_patch for
all moves, reference updates and new navigation files. An initial attempt to
collect all document text exceeded the output limit; discarded that truncated
response, then used compact hashes and bounded per-file line metadata instead.
No partial edit or missing evidence resulted. No installation or traffic run.

PASS:23 unique renames and registry rows; each new target exists exactly once,
and the old primary paths are absent.58 Markdown documents/232 local links
resolve; all explicit sprint anchors resolve. Eleven unique decision-inventory
IDs and the pending DG-AC1 status are preserved.

PASS: reversed the filename substitutions and newly added navigation in memory
and compared all56 original documents with their baseline hashes. All substantive
text matches. Two documents lost one trailing blank line during apply_patch
moves (the Route B protocol and Feedback23 amendment); explicitly accounted for
that EOF-only normalization. The initial stricter byte check flagged those two
formatting differences, not a scientific-content change. README's deliberate
reading-guide addition and prefix-convention update are separately reversed in
this comparison. All other original document bodies reconstruct byte-for-byte.

PASS: all37 original non-Markdown evidence/artifact files and all10 snapshot
context/feedback files remain byte-identical. Existing tracked AGENTS.md/PLANS.md
changes remain untouched; git status shows only those pre-existing modifications.
No archived source, PDF/.tex, query/claim data, approval or experiment cap changed.

Traffic/code/gradient tests are not applicable to this naming-only refactor.
Source/decision risks remain as recorded in S05; next allowed action is user
review of that existing gate. Earlier console filename links are obsolete;
use00_review_sequence.md and its registry for current canonical targets.

## 2026-09-30 sprint-directory cleanup

After S10 closure, the user requested a flatter and more readable ownership
hierarchy before opening S11. Grouped all 41 report files under `reporting/s01/`
through `reporting/s10/`, with this package-maintenance record under
`reporting/shared/`. Grouped all 20 synthesis artifacts under their owning
`synthesis/s01/`, `s02/`, `s03/`, `s04/`, `s05/`, `s07/`, `s08/` or `s10/`
directory. Filenames were retained. Added a README at each directory root with
the ownership map and future placement rules; no empty sprint directories were
created.

Updated Markdown links relative to both moved sources and moved targets across
the repository, then updated literal package-relative, repository-relative and
absolute path mentions in text records and slide notes. Updated current paths in
the document registry while preserving its historical `previous_path` entries.
The migration performed 61 moves, 347 Markdown-link rewrites and 103 literal
path replacements. SHA-256 checks confirmed all four moved PDF artifacts were
byte-identical.

Final validation found 428 links in package Markdown and 434 repository Markdown
links targeting this review package, with no broken target. The registry retains
46 unique existing current paths. No old flat `reporting/sNN_...` or synthesis
artifact path remains in searchable text, and the two directory roots contain
only their placement READMEs. `git diff --check` reported no whitespace errors.
No scientific statement, decision status, source archive, experiment setting,
simulator, controller or gradient result was changed. S10 remains closed, and
S11 remains ready but unopened.
