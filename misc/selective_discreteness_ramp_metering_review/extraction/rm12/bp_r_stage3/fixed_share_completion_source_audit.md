# P.A continuation source audit: interval amounts, priority and sender caps

Date: 2026-10-08. Primary-source review and exact analytical work. Current
interactive P.A approval controls; feedback26 remains answered and unchanged.
No implementation anchoring, production edits or traffic experiments.

## A01 — supplied final Laval–Daganzo journal

[Supplied original](../../../archive/user_supplied/rm12_bp_r_stage3/Lane-changing%20in%20traffic%20streams.pdf)

[DOI](https://doi.org/10.1016/j.trb.2005.04.003)

Re-read original PDF pp4–6, equations7–13 and Edie footnote. Sending is a
desired advancing amount; lane-changing/through choices partition it.
The sampled actual rate is bounded by its corresponding desired amount
divided by the interval. Source-native instantaneous oriented forms support
D1's lineage, but do not establish a physical fractional sending ceiling
inside the new nonuniform amount-allowance lift. D2 is an explicit temporal
adaptation, not a theorem of exact source equivalence. Preserve source
orientation, clock, upstream-port geometry and actual accepted counters.

## W16N — fixed priorities and partial-FIFO node framework

[Primary manuscript arXiv:1601.01054](https://arxiv.org/pdf/1601.01054)

Read requirement7/Remark3.1 and section3.3/Theorem3.3. Fixed priorities must
be separated from live queue demand; a queue can increase sending to
capacity without earning a new priority. The paper supplies an explicit
multi-port algorithm, including configurable FIFO restrictions and stated
optimization requirements. That theorem is not transplanted: our static
capped-priority construction has original sampled weights, physical sender
constraints and optional directional caps under T.A/P.A. We neither add
mutual-restriction intervals nor claim global throughput optimality.

## W16D — node allocation execution is not physical time

[Primary manuscript arXiv:1608.07623](https://arxiv.org/pdf/1608.07623)

Re-read merge definition/afterward and diverge discussion. Fixed priorities,
completed requests and unused-share redistribution have a dynamic-node
precedent. Its internal allocation clock is not our causal traffic clock.
The present weighted-increment calculation is a static rate allocation;
actual traffic then integrates those rates until a wave or amount event.
No input deadline, held nominal rate or binary meter is imported.

## J12 — admissible junction waves and interior states

[Primary manuscript arXiv:1204.6727](https://arxiv.org/pdf/1204.6727)

Re-read section3.1. Incoming accepted totals cannot exceed primitive demand;
strictly restricted incoming roads develop congested sending states.
Outgoing fluxes obey receiving; zero-spatial-measure interior states may
support a consistent solver. This guides the exact donor/recipient wave
checks, not a published proof of our all-mode multilane/record scheme.
Its general fair-merge/FIFO-diverge theorem has different scope.

## Original contribution and limitations of this pass

The capped weighted port algorithms and bounded priority-property arguments
are reviewer derivations. The common six-section local field certificate
composes actual receiving, quota stop, two wave contacts, actual record edge
crossing and E1. Early/late donor cases prove D1/D2 temporal non-equivalence.
They do not establish reached controls, a whole event-solver theorem, or
necessity/useful gradients. Search results outside primary manuscripts were
not relied upon.

[Mathematical companion](../../../synthesis/rm12/bp_r_stage3/fixed_share_completion_math.pdf)

[Query/read log](../../../search/rm12_bp_r_stage3_fixed_share_completion_queries.csv)

[Scoped source table](../../../screening/rm12_bp_r_stage3_fixed_share_completion_sources.csv)
