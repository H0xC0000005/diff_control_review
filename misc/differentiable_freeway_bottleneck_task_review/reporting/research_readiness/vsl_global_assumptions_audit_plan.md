# A bounded assumption audit before the compact VSL report

Date: 2026-10-19. **User-approved plan; audit executed and delivered at GA-G1.**
The user approved this plan and instructed execution as preliminary work for
the compact report. The bounded audit is now complete; no new scientific
choice was identified. Full report writing is not started.

[Audit findings and checkpoint](vsl_global_assumptions_findings_and_checkpoint.md)

This responds to the user's question whether the global assumptions need
separate examination before a mainly documentary consolidation. It does not
open full report writing or change a traffic-model decision.

The model was not developed without assumptions. Homogeneous preparation,
independent initial lane loads, terminal boundaries, service sharing and
recovery memory were selected explicitly; forward and sensitivity arguments
already have conditional domains. However, the five global groups recently
added to the report outline summarize those commitments without completing
an independent inventory and compatibility check. We should not present
those groups as a finished, verified global assumption set.

The remaining question is concrete: **can we state the whole task's root
assumptions clearly, recover them from accepted decisions, and show which
conclusions depend on which conditions without adding a hidden premise?**
A brief separate audit is appropriate before writing the compact report.

## What the audit should establish

The target is an explicit conditional modeling world. A reader should be
able to see what traffic is represented, what causal interactions are
retained, why those simplifications suit an elementary information/gradient
task, and where its conclusions stop. Source support and scientific role
are separate: a literature-motivated closure still has assumptions, while
a clearly declared study-defined closure can be legitimate for this
standalone task without claiming calibrated real-traffic validity.

The audit reuses the accepted equations, source reviews and proofs. It
does not assume that every simplification must be removed or every closure
must already be a published complete model. It checks whether the declared
world and claims are coherent and appropriately bounded.

## Three bounded passes

1. **Recover and classify the actual assumptions.** Read the current
   asymmetric forward, history, action and sensitivity contracts against
   their accepted component decisions. Extract every premise needed by the
   represented dynamics and the stated results. Separate task/observer/
   objective definitions, global representation and causal hypotheses,
   local constitutive closures, sufficient operating bounds and additional
   result-specific conditions. MA1–MA5 are an organizing starting point;
   their wording or grouping may change without changing an accepted law.
2. **Check compatibility, support and sufficiency.** Trace component inputs,
   retained state/history, fixed parameters, boundary conditions and event
   rules to the recovered assumptions. Check that the existing common
   forward domain applies across the advice interval and is nonempty, using
   accepted symbolic arguments and witnesses. Check whether assumptions
   from different source models remain compatible after adaptation, and
   label what is literature-supported, an explicit study choice, derived,
   or still unsupported for a stronger claim. Explain why consequential
   simplifications preserve the mechanisms needed for the elementary task.
   An unexamined physical claim is not repaired by attaching a reference.
3. **Map assumptions to conclusions and stop at a checkpoint.** Attach the
   necessary global and extra conditions to forward/clearance claims,
   information and compact-peer results, conditional action value and
   regular derivatives. Separate what is proved, hypothesized and left for
   later empirical/numerical evidence. Produce the concise assumption
   statement for the report and a traceable supporting matrix, then report
   either a coherent set or the smallest genuinely unresolved choice.

The audit must not require all special results to share one parameter
setting. The matched-history construction, positive-action existence proof
and active-delay witness have distinct additional conditions. In particular,
there is still no joint strong-delay/action/physical witness. Their boundaries
must be explicit rather than combined into an unsupported universal result.

## Minimal coverage and ownership

| Review item | Direct question | Ownership and dependency |
|---|---|---|
| **GA-Q1: representation and causal world** | Are the geometry, initial/boundary data, homogeneous/aggregate representation, advice response, lane coupling, service and recovery-memory assumptions explicit and mutually compatible? | Type 2 global check against accepted G1/G3/G4 traffic/task contracts. Component wording is evidence, not authority to change them. |
| **GA-Q2: operating domain and justification** | Does the declared domain support the joined model, and is each assumption's rationale and evidence limit stated accurately? | Type 2 global check after GA-Q1, reusing AS1/forward qualification and component/source audits. No new applied physical admission is presumed. |
| **GA-Q3: claim dependencies** | Do the information, action and derivative conclusions use only declared conditions, with no assumed positive outcome? | Type 2 global check after GA-Q1–Q2 against G2/G4 and the Step 3 contract. Regular-gradient conditions do not exclude forward-admitted nonregular cases. |
| **GA-L1: traceable transcription** | Are accepted decision/source locations and condition IDs correctly copied and linked? | Type 1 editorial work in support of GA-Q1–Q3; it cannot introduce a new physical, information or derivative assumption. |

No new model alternatives are selected by these questions. If the audit
finds a missing assumption that changes scientific meaning, it must expose
that choice and reopen its smallest affected global contract, with the
smallest viable alternatives, before dependent drafting proceeds.

## Deliverable and completion gate

Produce one short reader-facing assumption statement, organized for the
report's Part 2, plus a supporting table:

**statement and category → accepted decision/equation → rationale and
source status → affected components/claims → extra conditions and limits.**

The checkpoint passes when each essential premise is accounted for, no
unresolved contradiction or circular assumption is found, and the joined
domain and result-specific domains are accurately distinguished. Completeness
is relative to the declared task and model, not a claim to cover all freeway
behavior. Conservation, clearance, different useful actions and useful
gradients must not be inserted as unproved root assumptions.

If the gate passes, the next allowed action is the compact methods-writing
pass using the audited set. If it exposes a genuinely new assumption or
conflict, stop with the specific gap and methodological consequences. An
open empirical limitation can remain explicitly scoped; it does not by
itself require replacing the accepted standalone model.

No general re-review of the model, simulator code, dependency installation,
traffic experiment, calibration, AD or numerical-gradient run is included.
Execution stops at the completed GA-G1 checkpoint. It does not alter Step 3's
recorded formal closure status or open full report writing.

## Execution outcome

GA-Q1, GA-Q2, GA-Q3 and GA-L1 are complete at methodological review scope.
The recovered assumptions form a coherent conditional set, with a nonempty
retained forward domain and separate conditions for stronger results. The
audit corrected one stale symmetry statement in the future physical-admission
document to match accepted AS1; no traffic law or bound changed. The new
short statement and dependency audit supply the completed deliverable.

[Short report assumption statement](../../synthesis/research_readiness/vsl_global_assumptions_statement.md)

[Source, compatibility and claim-dependency audit](../../extraction/research_readiness/vsl_global_assumptions_dependency_audit.md)

[Execution work and checks](vsl_global_assumptions_audit_work_report.md)

## Existing material to reuse

[Current report outline and audited MA overview](vsl_feedback9_report_structure_discussion.md#global-modeling-assumptions-an-explicit-part-2-subsection)

[AS1 initialization and forward-assumption dependency map](../../extraction/research_readiness/vsl_as1_initialization_proof_map.md)

[W-F conditional whole-advice-range qualification](vsl_wf_forward_qualification_and_checkpoint.md)

[Current asymmetric standalone contract](../../synthesis/research_readiness/vsl_asymmetric_standalone_verification_protocol.md)

[Step 3 consistency audit](vsl_as3_step3_consistency_audit.md)

[Asymmetric derivation and claim boundaries](../../extraction/research_readiness/vsl_as3_derivation_and_claim_audit.md)

[Existing component/source map](../../extraction/research_readiness/vsl_feedback8_model_stack_source_map.md)

[Applied physical-support limits](../../extraction/research_readiness/vsl_mp6_physical_source_audit.md)

[Planning work and document checks](vsl_global_assumptions_audit_planning_work_report.md)
