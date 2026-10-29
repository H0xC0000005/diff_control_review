# S08.90 — Exact-prefix planning work/check report

Date: 2026-09-29. Status: **Closed after explicit approval of DG-R5 Candidate
A.**

## Work performed

Closed S07 with DG-R4 Candidate A and explicitly deferred automatic use of the
broader or staged fallback. Opened S08 as planning only. Transcribed the accepted
preparation into exact IDs, rational intended times, global vehicle indices,
lane arrays, canonical observations, pair enumeration/selection, time-step
variants, provider/readiness boundary, budgets, failure labels and durable-output
requirements. No new literature search was necessary.

## Assumptions and boundaries

Global vehicle IDs are zero-based in intended departure order: 30 low-demand
vehicles precede peak index j. Decimal times shown in the contract are displays;
generation uses `120 + j*(8/9)` exactly before the target configuration's
documented serialization. The existing strong channel and matching meaning are
unchanged. A provider version and its native defaults must be recorded during a
future authorized readiness stage, not assumed here.

The 24-invocation readiness cap is retained from the earlier approved contract;
the narrowed scientific caps are 36 full-dual prefixes or at most 22 staged
prefixes. These are maximum invocations, not permission to use unused budget for
new preparations.

## Commands and validation

Commands: read-only `sed`, `rg`, CSV/Markdown inspection and Python validation;
`apply_patch` for documents and navigation. No web query, dependency change,
provider/server command, installation, implementation, simulation, detached
process, action evaluation or gradient test.

Validation checks exact block/global-ID arithmetic, pattern balance/uniqueness,
pair count, decision/step divisibility, cap arithmetic, document registry and
package-local links. The synchronized package contains six unique balanced
patterns, 18 unique preparations and 15 unordered comparisons per decision
time. All block times and global IDs reproduce the exact rational/index rule;
both decision times are divisible by 0.5 s and 0.25 s. The full-dual and staged
total caps are respectively 60 and 46 invocations after the 24-invocation
readiness allowance. After closure synchronization, the registry has 37 unique
existing paths, including four S08 primary records, and all 337 package-local
Markdown file links resolve. The
future experiment directory is absent, confirming that this review created no
implementation or execution artifacts. Numerical traffic tests do not apply.

## Remaining risks and next allowed action

Native anticipation may prevent every exact pair; desired-speed entry and a
future provider are still synthetic/external choices. Exact pair success would
not establish useful advice or occupancy sufficiency. Implementation must not
repair scientific failure by changing lookahead, physics, patterns or equality.

Review [S08 findings/S08-UG1](s08_20_exact_prefix_planning_findings_and_gate.md)
and choose/adjust DG-R5. No execution begins automatically.

## Subsequent gate clarification

The user ranked methodological soundness and feasibility above exact quantitative
execution cost, with cost relevant only for an algorithmic-complexity change.
The full and staged banks differ only by a bounded constant instance count; the
staged variant additionally introduces a discovery filter. The findings,
contract, plan, inventory and dialogue were synchronized. The user then
explicitly approved Candidate A. S08 is closed; separate authorization is
required to open the exact-prefix readiness and execution continuation.
