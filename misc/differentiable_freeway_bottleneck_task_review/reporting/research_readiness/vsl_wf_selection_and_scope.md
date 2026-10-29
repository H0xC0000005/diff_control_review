# W-F selected: advice acts through traffic, not directly on merging work

Date: 2026-10-16. **Approved by the user; J4-W1 closed.** The user states
that merging dynamics should depend on local traffic and geometry, with
speed advice acting through the traffic state. Proceed with the concrete
W-F expression presented at J4-W1. W-A is unselected.

The terminal's immediate E work now uses A's actual passing flow and the
positive difference between the modeled A and E speeds, with fixed common
coefficient units. It no longer divides by the currently chosen advice or
the capacity calculated from that advice. The coefficient can be recorded
directly in dimensional form. The previously proposed upper-advice anchor
only fixes those units once; changing the action or search interval must
not change the physical coefficient.

“Local traffic state” includes the already selected recovery account and its
sufficient recent history. This selection does not undo O-R, require a
memoryless queue-only model, or introduce a new observation. H1 uses the
actual common free-motion speed in its declared ideal response regime;
the longitudinal capacity constraints retain their physical role.

The choice changes one constitutive expression. H1/T1, S-E-P's current-state
allocation, R-E's E-only new profiles, O-R renewal, ordinary underload,
known empty histories, continuous mass and local choke-line completion
retain their selected meanings. Exact fairness/speed/parameter credibility
and empirical usefulness are not established by approving W-F.

## Executed continuation and checkpoint

The resumed J4 pass supplies a conditional forward qualification over the
entire original constant-advice interval under the retained primary-domain
bounds. It uses the monotone finite H1 arrival pulse, proves that E cannot
re-form a queue after clearance, bounds A's possible queue switches, and
joins the earlier causal-regime and positive-budget arguments to finite
clearance and complete accounting. No action subinterval is substituted.

Stop at **WF-Q1**, the completed forward-model evidence checkpoint inside
J4. It is not a new model-choice gate. Physical/applied MP6 and the dependent
information/action/gradient/SUMO qualification remain for the rest of Step 3.
No simulator code, installations, traffic experiments or Step 4 is opened.

[Traffic meaning, qualification and remaining review](vsl_wf_forward_qualification_and_checkpoint.md)

[Selected law and analytical argument](../../synthesis/research_readiness/vsl_wf_forward_qualification.pdf)

[Earlier alternatives and exact substitution](vsl_j4_speed_response_findings_and_gate.md)
