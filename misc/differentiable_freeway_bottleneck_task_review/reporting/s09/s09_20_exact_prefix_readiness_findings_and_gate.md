# S09.20 — Exact-prefix readiness findings and provider gate

Date: 2026-09-29. Status: **Superseded as an active gate; DG-R6 provider
provisioning is withdrawn by the methodology-only scope correction.** Parent:
[S08 closure](../s08/s08_99_exact_prefix_planning_sprint_closure.md). Current authority:
[S09.35](s09_35_scope_correction_and_methodology_alternatives.md).

> **Scope notice:** This document preserves the short-lived empirical-readiness
> interpretation for audit history. No candidate below is pending. Provider
> availability is not a blocker for the methodology review.

## Main finding

The approved exact-prefix method is ready, but its required independent reference
provider is unavailable in the inspected local environment. Read-only discovery
found no `sumo`, `sumo-gui` or `netconvert` executable on `PATH` or in the
inspected standard/system and Conda locations. None of the base, project,
`differential_sim`, or `llmfe` Python environments exposes `traci`, `sumolib`, or
`libsumo`. The durable [provider inventory](../../extraction/s09_provider_inventory.json)
records the inspected scope.

This is an engineering readiness stop, not evidence about exact matching or the
traffic hypothesis. Without a provider/version, native defaults cannot be pinned,
the network and lane connections cannot be generated and inspected, deterministic
replay cannot be checked, and no prefix observation is valid. No harness or
scientific run was attempted.

## S09-UG1 / DG-R6 — How should the required reference provider be supplied?

### Problem statement

How should S09 obtain a reproducible SUMO executable and matching Python API so
the approved readiness and full dual-step prefix screen can proceed without
changing the scientific reference contract?

### Assumed model-chain function

SUMO supplies the independent native car-following and lane-changing reference.
The review harness supplies fixed preparations and common advice semantics,
records the strong lane-blind history and hidden-state audit, and performs exact
pair comparison. The provider is therefore an execution dependency; it is not a
candidate differentiable simulator or a source of invented traffic equations.

### Core gap

No usable local provider or API was found, and installation/configuration was
outside the authority that opened S09. The approved screen cannot distinguish a
scientific absence of exact pairs from absence of the engine needed to generate
the evidence.

### Candidate A — provision a dedicated pinned SUMO environment (provisional recommendation)

Authorize installation of an official SUMO distribution and matching Python API
in a dedicated environment, record source/channel/version/build, and resume S09
at readiness. Keep the main project environment and frozen scientific contract
unchanged. Installation success does not waive any readiness check.

**Pros:** Preserves the reviewed reference method; gives a locally reproducible,
version-pinned execution basis; permits direct inspection of generated network
connections and installed API behavior.

**Cons:** Requires an external dependency download and environment setup; the
available package channel/version must be checked before commands are frozen;
provider installation may still reveal API or native-default incompatibilities.

**Dependencies and consequences:** Requires explicit installation/network
authorization. Resume the same S09 readiness stage after provisioning. Do not
use installation effort as permission to tune native behavior or weaken the
contract.

### Candidate B — supply an existing managed provider or execution environment

Provide a known executable/API path, module environment, container, or managed
host where the same provider can be inspected and pinned. Resume only after the
review can record the actual version/build and preserve immutable inputs and
durable outputs.

**Pros:** Avoids adding a local installation; may reuse an institutionally
managed or already validated engine; preserves the SUMO reference contract.

**Cons:** No such provider was found in the inspected local scope; remote or
managed access may complicate reproducibility, file transfer, command audit and
result retention.

**Dependencies and consequences:** The user must identify or authorize access to
the environment. Readiness remains mandatory there; undocumented results or an
uninspectable service are insufficient.

### Candidate C — defer the empirical screen

Close or pause S09 with provider unavailable and retain the complete approved
contract for later execution.

**Pros:** Avoids environment changes while preserving all methodological work and
the precise failure classification.

**Cons:** Leaves exact native collision feasibility, decision relevance, minimum
state and gradient usefulness unresolved.

**Dependencies and consequences:** No scientific negative conclusion follows.
The broader S07 preparation, approximate matching and analytical merge model do
not activate automatically.

An alternative reference engine is not a drop-in provisioning option: it would
change native traffic semantics and require reopening the reference contract
before implementation.

### Provisional recommendation

**Candidate A.** It is the smallest path that preserves the approved method and
makes the evidence locally reproducible. The immediate continuation would be
provider provisioning followed by readiness, not the 36-prefix bank directly.

**Superseded gate:** do not choose DG-R6 under the current scope. No installation,
harness or traffic execution belongs to this review. See [S09.35](s09_35_scope_correction_and_methodology_alternatives.md)
for the static and analytical alternatives.
