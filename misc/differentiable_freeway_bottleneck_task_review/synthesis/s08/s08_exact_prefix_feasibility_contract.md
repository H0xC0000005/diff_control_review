# S08 exact-prefix feasibility contract — proposed

Date: 2026-09-29. Status: **Approved at DG-R5 with the full dual-step bank;
not execution authority.**

## 1. Frozen preparation bank

Retain the accepted synthetic permanent three-to-two narrowing, empty start,
2,400 m approach, final-400 m contrast region, baseline advice 90 km/h, response
gain 0.5, and intended demand schedule. Make these formerly implicit entry fields
explicit:

- `departPos="base"`;
- `departSpeed="desired"`;
- numeric departure lane from the frozen pattern;
- all insertion safety checks active;
- unlimited retained insertion delay; no discard, force insertion or relocation.

Lane 0 is the ending lane. The common six-departure pattern is
`P0=(0,1,2,0,1,2)`. Every intended departure uses P0 cyclically except the one
contrast block named below. At and after decision time, every preparation uses
the same continued P0 sequence. Intended timestamps and vehicle IDs are common;
only the six block lane labels differ.

The six frozen contrast patterns, assigned in chronological block order, are:

| Pattern | Lane sequence |
|---|---|
| P0 | 0,1,2,0,1,2 |
| P1 | 0,2,1,0,2,1 |
| P2 | 1,0,2,1,0,2 |
| P3 | 2,0,1,2,0,1 |
| P4 | 1,2,0,1,2,0 |
| P5 | 2,1,0,2,1,0 |

Peak index `j=0` has intended departure 120 s and rational headway `8/9` s.
Global vehicle index is zero-based with low-demand indices 0–29 followed by
peak index `30+j`. Freeze:

| Decision | Peak block | Global IDs | Intended departure interval |
|---:|---:|---:|---:|
| 220 s | j=16–21 | 46–51 | 134.222222222222–138.666666666667 s |
| 240 s | j=38–43 | 68–73 | 153.777777777778–158.222222222222 s |
| 260 s | j=61–66 | 91–96 | 174.222222222222–178.666666666667 s |

Preparation IDs are `T220_P0` through `T220_P5`, then corresponding `T240_*`
and `T260_*`: 18 prefixes. Generate timestamps from exact rational/index rules,
not recursively rounded decimals. Hash the realized arrays before execution.

## 2. Prefix and observation boundary

Replay each prefix from time zero through its decision timestamp. The canonical
channel remains the approved one: every reference step, immutable 16×200 m bins
plus verified connectors, vehicle count, density, mean speed, empty mask,
cumulative intended/actual entry and exit counts, total source waiting, complete
advice, geometry, demand, response/type and structural metadata. Past lane-entry
labels, realized lane IDs, gaps, leaders and lane-change state are hidden from the
comparison channel but retained in a separate audit.

Serialize float64 physical arrays, integer arrays and Boolean masks with declared
shape/unit/dtype/order. Exact equality means elementwise equality of canonical
arrays and metadata after deterministic serialization; checksums verify bytes but
do not substitute for array comparison. NaN is forbidden. Empty-bin speed is zero
with its explicit mask. A replay mismatch for identical inputs is invalidity, not
near matching.

At decision, separately audit lane counts in the final 400 m. A qualifying pair
must have an exactly equal declared channel and a different three-lane occupancy
vector. There is no minimum positive L1 difference. Finer 100 m and coarser 400 m
projections remain diagnostic qualifications, not alternate matching channels.

## 3. Pair registry and selection

Compare pairs only within one decision time. List all 15 unordered pattern pairs
per time with exact-match status, first differing channel/index if any, final-400 m
lane vectors and L1 difference. Never inspect an action outcome.

From pairs satisfying exact history and nonzero contrast at every required step,
select at most two by descending L1 lane-count difference and then lexical
preparation IDs. Raw arrays, checksums and the complete pair table remain durable.
If no qualifying pair exists, stop without action runs or scenario changes.

## 4. Time-step execution candidates

The primary step is 0.5 s; 0.25 s is the approved numerical robustness step.

**Full dual-step bank:** run all 18 prefixes at both steps (36 prefix
invocations), intersect qualifying preparation pairs across the two steps, then
select. This prevents primary-step selection from hiding another pair that is
stable across both steps. **Selected at DG-R5.**

**Staged selected-pair check:** run all 18 at 0.5 s, select at most two pairs,
then rerun only their distinct states at 0.25 s (maximum 22 prefix invocations).
If a selected pair fails at 0.25 s, stop; do not search the unrun 0.25 s bank.
This uses fewer bounded instances but makes the 0.5 s bank the discovery step.
The instance-count difference is constant-factor operational cost, not an
algorithmic-complexity difference. Methodological soundness and feasibility take
priority over that count when DG-R5 is decided.
This candidate was not selected.

## 5. Readiness, budget and failure labels

After separate execution authorization, first perform read-only provider/version
discovery. Absence or incompatibility is reported; installation or configuration
requires separate permission. Record version/build and pin every native/default
parameter before scientific runs.

Retain up to 24 readiness/development invocations from the earlier contract for:
network connections, lane permissions, entry semantics, advice timing/response,
source-delay retention, native merging, deterministic replay, observation-bin
coverage, output precision, invalidity reporting and a zero-response sanity case.
Readiness fixes may correct harness conformance only.

Hard caps:

| Candidate | Readiness maximum | Prefix maximum | Total maximum |
|---|---:|---:|---:|
| Full dual-step | 24 | 36 | 60 |
| Staged selected-pair | 24 | 22 | 46 |

Labels are: qualifying dual-step exact pair; primary-step pair not robust to
0.25 s; no exact-history pair; exact pair but zero lane contrast; invalid
provider/harness/reference outcome; or incomplete execution. None is an action,
minimum-state, aggregate-sufficiency or gradient result.

## 6. Durable outputs and next stop

A future repository-owned runner must use immutable configuration, unique
non-overwriting output paths and separate `readiness`, `prefix`, and `summarize`
commands; `summarize` cannot launch traffic. Persist configuration/source hashes,
version, command, timestamps, raw observations, hidden-state audit, pair registry,
failure ledger and machine/human summaries.

After prefix completion, stop for user review. A qualifying pair may motivate a
separate action-evaluation plan; it does not authorize actions. Failure does not
activate the S07 broader bank, approximate matching, provider tuning or an
upstream preparation.
