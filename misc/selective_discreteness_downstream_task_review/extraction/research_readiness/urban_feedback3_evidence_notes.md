# Feedback 3: what the existing records actually establish

22 October 2026. Supporting evidence for the [plain-language response](../../reporting/research_readiness/urban_feedback3_response.md). This is a bounded source check and conceptual audit, not a new traffic model or numerical validation.

## Lane allocation was a research direction, not a selected zone-entry law

[PROJECT_CONTEXT §5.5](../../../../context_snapshots/diff_minimal_meso/PROJECT_CONTEXT.md#L178) already separates perceived resistance, desired allocation and physically realized occupancy. It explicitly leaves the exact lane-choice/equilibrium rule unselected. [The accepted urban P4 handoff](../../synthesis/project_impact_matrix.md#L19) likewise leaves lane intent, access, storage, ordered service and their update order for later definition.

The [adoption matrix](../../synthesis/literature_adoption_matrix.md#L35) identifies T0030 as the lane-allocation anchor for the aggregate lane/storage rival B2. It describes B3 as a project-owned composition, rather than selecting the same complete lane operator for B3. Thus the earlier review supports investigating responsive allocation without establishing its exact zone-entry formulation.

## Primary-source check: the scope of the equilibrium anchor

Gong, Bliemer and Raadsen, *Extended macroscopic node model for multilane traffic*, Transportation Research Part B 195 (2025), 103208, [publisher/DOI page, §5](https://doi.org/10.1016/j.trb.2025.103208).

Its equilibrium balances exit resistance across used lanes available to a movement; unused alternatives cannot offer less resistance. This is not equality of occupancy across all lanes. The authors explicitly distinguish allocating sending flow at the link exit from choosing a lane when entering a link queue. These qualifications support the equilibrium idea while preventing direct identification with the proposed finite-zone entry rule.

Checked on 2026-10-22 using indexed text from the primary publisher page, including §5 and its equilibrium conditions. Direct page opening returned HTTP 403; no full-PDF inspection, complete algorithm qualification or new equation adoption is claimed. No statement about the paper's existence/uniqueness results is transferred to the urban model.

## Fixed lane assignment does not imply threshold-only sensitivities

The [accepted service definition](../../synthesis/experiment_formulation_formal.tex#L40) makes effective movement service vary with the allocated fractions. The [objective](../../synthesis/experiment_formulation_formal.tex#L60) counts time accumulated by traffic through completion.

A queue in one fixed lane can drain faster when its effective service rate increases, even with unchanged lane assignment and the same binding service limit. Its waiting-time area then changes without any blockage threshold switching. Likewise, with fixed geometry, the time at which a blocking queue clears can move continuously. These are logical counterexamples to the threshold-only claim, not executed scenarios or claims that all gradients are nonzero.

Responsive allocation may add genuine sensitivity through state-dependent preferences and admitted lane shares. A deterministic least-cost winner can nevertheless jump at a tie. Neither responsiveness nor determinism establishes differentiability or useful gradients. Stable-branch conditions and later validation remain necessary.

## Assignment does not erase order within a shared lane

[PROJECT_CONTEXT §5.4](../../../../context_snapshots/diff_minimal_meso/PROJECT_CONTEXT.md#L162) gives the decisive example: the same lane composition can place through traffic before a left-turn block or the left-turn block before through traffic. With no bypass and a blocked left-turn exit, the former can discharge through traffic while the latter cannot. A deterministic lane allocation need not make these sequences identical.

Order across physically independent lanes can cease to be one global service order. The ordered traffic within each realized shared lane can still matter. Movement-exclusive neutral lanes are a special case, not a basis for deleting within-lane order throughout V1/V3.

## Responsive entry allocation is not existing M2 load balancing

[M2's closed G2](../../../../context_snapshots/diff_minimal_meso/temp_content/milestone_2_per_lane_interaction_zone/phase_B_revision.md#L16) admits entries to their single precommitted lane and explicitly excludes searching alternatives or balancing load. Its conservative partition, eligibility and causal spillback remain useful infrastructure.

The present review must state where responsive intent becomes commitment. A proposed allocation step before realized entry may be compatible with a fixed-lane ingress interface, but that compatibility must be established. If the new rule moves the commitment point, revises committed entries or changes the ingress meaning, explicitly reopen the smallest affected G2 contract and dependents. This audit neither changes that archive nor approves an adapter.

## Lane redistribution and lossless merging have different meanings

[M1's exact-merge semantics](../../../../context_snapshots/diff_minimal_meso/docs/milestones/milestone_1_ordered_route_mass_ledger.md#L123) combine adjacent entries only when route and timing structure agree exactly. Traffic behavior is preserved. Lane redistribution changes where mass is allocated and may split one block into several fragments; it is not intrinsically a compression operation.

A mixing operation can be continuous—for example, a fixed weighted average of continuous masses—even though it may erase an order effect. Exact ordered models can also change active branches. The present evidence therefore supports deferring optional mixing, but proves neither its implementation impossibility nor the superiority of exact-order gradients.
