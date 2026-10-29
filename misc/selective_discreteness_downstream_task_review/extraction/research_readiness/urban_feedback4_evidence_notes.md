# Feedback 4: partial transfers, waiting ownership and signal sensitivity

23 October 2026. Supporting notes for the [response](../../reporting/research_readiness/urban_feedback4_response.md). No new equations are adopted and no numerical traffic experiment is performed.

## Partial entry is already part of the continuous-mass basis

[PROJECT_CONTEXT §5.2](../../../../context_snapshots/diff_minimal_meso/PROJECT_CONTEXT.md#L126) permits continuous splitting without mass loss. [M1's approved scope](../../../../context_snapshots/diff_minimal_meso/docs/milestones/milestone_1_ordered_route_mass_ledger.md#L40) includes partial splitting, and its [timing contract](../../../../context_snapshots/diff_minimal_meso/docs/milestones/milestone_1_ordered_route_mass_ledger.md#L78) derives resident eligibility from actual entry. Thus packet size alone is not an all-or-nothing admission condition. A waiting label does not advance physical entry or readiness.

[M2 G2](../../../../context_snapshots/diff_minimal_meso/temp_content/milestone_2_per_lane_interaction_zone/phase_B_revision.md#L16) already retains rejected mass upstream, uses the assigned lane's receiving bound and conserves the U/Z transaction. It forbids same-step admission/discharge. The present proposal does not amend those timing or conservation rules.

## Space, rate and access are different constraints

[PROJECT_CONTEXT §5.5](../../../../context_snapshots/diff_minimal_meso/PROJECT_CONTEXT.md#L178) separates desired allocation from realized accessibility. [The accepted bay handoff](../../synthesis/project_impact_matrix.md#L19) leaves the actual access/storage/service law to be supplied. Spare storage cannot establish that a blocked turner reaches the opening. A positive service rate also cannot establish that a not-yet-arrived packet is eligible.

No positive admission deadband is selected. The repository disallows silently adding clipping, smoothing or other behavior-changing numerical conventions. A tolerance in an assertion is not an authorization to withhold physically feasible positive mass. Any future threshold would need its units, traffic meaning and effects justified under the normal methodology workflow.

## Upstream queue records must not become duplicate physical mass

[The accepted physical partition](../../../../context_snapshots/diff_minimal_meso/temp_content/milestone_2_per_lane_interaction_zone/phase_B_revision.md#L12) separates aggregate upstream traffic from the physical local zone. The [complete objective](../../synthesis/experiment_formulation_formal.tex#L60) counts every released unit through completion, including moving and waiting mass.

Pending lane queues can be logical partitions or views of upstream ledger mass, with lane-target metadata, while actual ownership remains upstream. A proposed implementation must choose one authoritative account and reconcile its views. Calling a pending queue a lane does not grant extra physical storage or prove that its path is independently accessible. Modeling it as an actual additional upstream lane would require a separately specified physical domain.

## Early commitment and provisional intent make different predictions

If mass assigned to lane A keeps that target while waiting, a later improvement in lane B changes only uncommitted traffic. If the target is provisional, the already waiting mass may change desired shares. These are different behavioral responses to control, even before considering solver details. The inherited M2 seam commits entries to one lane; compatibility of responsive allocation before that seam must be established rather than assumed. No retargeting of committed or resident traffic is approved here.

The reuse-existing-target shortcut is not a new lane-choice law when its input was already selected by that law. Without a valid existing target it would change the model. The allocation cost, feasible choices and physical access remain unspecified, so this note does not claim a complete equilibrium.

## Primary-source check for the phase-gradient correction

Geng and Cassandras, [*Multi-intersection Traffic Light Control Using Infinitesimal Perturbation Analysis*, arXiv:1204.1910v3](https://arxiv.org/abs/1204.1910v3), 2012. The official abstract describes event-based congestion gradient estimates with respect to green/red durations. This supports the limited claim that phase-based traffic models need not have universally zero duration sensitivities. It does not establish a derivative for the urban model or justify importing the paper's stochastic/hybrid controller.

The local logical counterexample is extending a green interval while traffic is waiting: the switching time moves and service duration changes even though the instantaneous signal state is unchanged at most times. Differentiating a fixed sampled on/off mask can miss this path. Conversely, average service does not ensure a nonzero realized-flow or objective derivative when another constraint binds.

Checked the official abstract and metadata on 2026-10-23. No full-paper method qualification, implementation adoption or numerical result is claimed. The selected urban action remains the [average phase-fraction service definition](../../synthesis/experiment_formulation_formal.tex#L40).
