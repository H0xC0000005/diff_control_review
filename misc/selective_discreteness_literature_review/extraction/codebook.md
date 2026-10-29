# R6 evidence-extraction codebook — pilot version

Date: 2026-09-07  
Status: frozen after the 10-paper calibration on 2026-09-07

This codebook translates the protocol's extraction schema into compact, auditable fields. It codes implemented behavior rather than relying on authors' macro/meso/micro labels.

## Core fields

- `record_id`: stable ID from `master_records.csv`.
- `study_role`: `nearest`, `direct`, `contextual`, or `contextual_secondary`, as approved at R5.
- `document_status`: `peer_reviewed`, `thesis`, `preprint`, or `review`.
- `backbone`: principal dynamic model, such as `LTM`, `CTM`, `link_queue`, `packet_event`, `car_following`, `hybrid`, or `other`.
- `traffic_quantity`: `continuous_mass`, `integer_vehicle`, `packet_or_cohort`, `mixed`, or `not_applicable`.
- `identity_state`: `persistent_route_or_commodity`, `persistent_individual`, `movement_only`, `none`, or `unclear`.
- `order_state`: `exact_realized`, `aggregate_FIFO`, `partial_FIFO_parameter`, `probabilistic_or_relaxed`, `none`, or `unclear`.
- `spatial_state`: `link`, `movement`, `lane_group`, `lane`, `individual`, `hybrid`, or `other`.
- `storage_spillback`: `physical_explicit`, `aggregate_supply`, `point_queue`, `none`, or `unclear`.
- `signal_model`: `on_off`, `cycle_averaged`, `capacity_multiplier`, `actuated_logic`, `external_evaluator`, `none`, or `other`.
- `derivative_method`: `reverse_AD`, `forward_AD`, `analytic`, `finite_difference`, `smoothed_or_surrogate`, `black_box`, `none`, or `unclear`. Multiple mechanisms are separated with `+`.
- `derivative_validation`: `finite_difference`, `analytic_reference`, `optimization_only`, `none`, or `unclear`.
- `external_validation`: `micro_simulator`, `field_data`, `analytic_or_LWR`, `cross_fidelity_control`, `none`, or combinations thereof.
- `task`: short controlled description of calibration, signal optimization, route/toll control, trajectory optimization, or forward simulation.
- `component_relation`: one or more of `I_ledger`, `II_local_zone`, `III_service`, `differentiability`, `validation`, or `task_context`.
- `baseline_role`: proposed role such as executable baseline, equation/reference comparator, conceptual comparator, or richer evaluator.
- `method_credibility`: `strong`, `adequate`, or `weak_unclear`, always accompanied by `credibility_reason`.
- `key_author_claim`: concise paraphrase of the study's own principal result.
- `reviewer_inference`: audit interpretation, explicitly separate from the author claim.
- `uncertainty`: missing or ambiguous evidence requiring later resolution.

The pilot required no categorical change. It confirmed that identity, realized order, traffic quantity, storage representation, derivative construction, and external validation must remain separate fields. Bibliographic maturity corrections do not alter the behavioral codebook.

## Coding safeguards

1. `exact_realized` requires a persistent sequence or individual/event ordering that can distinguish equal aggregate compositions with different realized order; an assumed aggregate FIFO rule is not enough.
2. Commodity labels alone establish semantic identity, not realized queue order.
3. `reverse_AD` or another exact program derivative describes the implemented fixed execution path; it does not establish usefulness or unbiased derivatives at event boundaries.
4. A microscopic comparison establishes forward cross-fidelity evidence, not gradient transfer, unless control perturbations or gradients themselves are evaluated externally.
5. Review articles inform discovery and taxonomy but are excluded from primary-method counts.
6. Missing reporting is coded `unclear`, never inferred as absence.
