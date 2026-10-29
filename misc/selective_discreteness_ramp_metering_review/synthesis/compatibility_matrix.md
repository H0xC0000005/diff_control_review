# Component compatibility audit

Date: 2026-09-14. Read-only audit; no implementation approval.

Inspected `src/diff_minimal_meso/nodes.py` (ordinary ORCA and restricted continuum service, structural input capacity and service inputs), the closed M0 plan, active M2 Phase-B G1–G6, and the established project context/roadmap. Function signatures are not proof of full task compatibility.

| Requirement | Existing/planned basis | Classification |
|---|---|---|
| Aggregate freeway propagation | Accepted first-order LTM | Reuse candidate; CTM papers support the model class, not equation identity with project LTM |
| Ramp storage and conservation | Source waiting and link storage; M2 physical ownership | Plausible with explicit finite-ramp versus external-source ownership; no overflow deletion |
| Metering control | Existing continuum-service inputs | Candidate bounded control adapter; metering rate versus exposure mapping and step units must be declared |
| Merge allocation | Existing ordinary and restricted node solvers | Compare actual priority/receiving semantics before proposing a new solver; no automatic need to replace Component 0.4 |
| Dynamic lane access/finite acceleration zone | M3 access/service ownership | Unresolved planned/new interface detail; cannot claim supported by the closed M2 neutral lane domain |
| Lateral lane-changing along freeway | Not part of current mainline | Essential lateral dynamics would trigger compatibility review; not hidden in a node wrapper |
| Independent speed state | Not part of current first-order backbone | Not necessary for every aggregate ramp task; essential second-order effects would require separate approval |
| Capacity-drop hysteresis | Not supplied by ordinary triangular FD/spillback alone | New scientific behavior if adopted; RM0003's binary dynamic state is not fixed structural metadata |
| Order/route contrast | Exact ledger infrastructure; M3 selects resolution | Available information need not affect a single common-destination merge; diagnostic mechanism must be shown |
| Gradient/evaluator evidence | Existing AD/signature discipline; later cross-fidelity task | Preserve this discipline; no external ramp mapping or correctness result established yet |

There is no demonstrated need to discard closed components. There is also no demonstrated complete ramp implementation ready to reuse. Both limits matter for the feasibility verdict.
