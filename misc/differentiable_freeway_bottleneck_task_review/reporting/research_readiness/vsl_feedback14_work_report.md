# Feedback 14: work and preservation record

Date: 2026-10-21. **Scope questions answered; active recommendation corrected.**

Read feedback 14 and rechecked the approved short plan, feedback-13 response,
active source/flow report, source audit, hand-check status and dialogue.
The intended goal is a complete source-backed task answering the same RQs,
with the accepted VSL model as a reference and limited adaptation preferred.
Functional identity is not required. The prior plan already permitted this;
the last backtrack-first recommendation overweighted literal source reuse
before evaluating the smaller allocator completion.

The response preserves the analytical findings while narrowing their
implication: direct transcription is not ready, but limited adaptation has
not been shown infeasible or too complex. It withdraws the backtrack-first
recommendation, prioritizes allocator assessment and retains backtracking as
a fallback. LF1 remains the substantive traffic-rule question rather than a
strategic approval needed before reviewing allocators. No exact allocator,
source repair or new backbone is selected.

Added the response, this work record and static verification. Updated the
active findings/recommendation, source audit's interpretation notice, README
and successor dialogue. Added only `(answered)` to feedback heading 14,
preserving every other byte of user text. Historical work/validation records
keep their delivery-time meaning. All existing model/source/proof equations,
PDFs and LaTeX sources remain unchanged, including both accepted compact
report artifacts and the new hand-check note. Root files are preserved and
this task writes nothing to urban.

Assumption: feedback 14 asks for the purpose check, its consequences for the
findings and corrected review direction. It does not ask this answer to
execute another literature review or adopt an allocation formula.

Used `sed`, `tail`, `rg`, `git status --short`, `apply_patch`, and Python
standard-library hashing/JSON/path checks. No external search or new paper
reading is needed for these scope questions. Snapshot:
`/tmp/vsl_feedback14_before.json`.

The first preservation check detected a final newline added by the patch
tool to the feedback inbox. Removed that single appended byte after an exact
comparison; the only remaining inbox change is the answered marker.

```bash
python3 /tmp/vsl_feedback14_checks.py
git status --short
```

[Static checks](vsl_feedback14_validation.json)

No source or mathematical claims are newly proved, no formula-heavy artifact
is changed, and no LaTeX build or scientific test is required. No simulator
code, dependency installation, traffic/gradient/SUMO/optimization experiment,
agent launch or external message occurs. VSL Step 4 remains closed; separate
historical acceptance records and the closed ramp line are unchanged.
The next substantive action is a bounded allocator assessment, stopping at
its result or a consequential unresolved traffic-rule choice.
