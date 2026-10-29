# RM9 dialogue and scientific change-control record

Date: 2026-10-01.

## Authorization and execution

The user approved RM8-UG1.A as the first method and instructed continuation.
Recorded RM8 closure, opened/transcribed RM9's bounded protocol and performed
source/analytic review to its first real methodological obstruction. No repeated
planning gate for that same family was imposed. No implementation or experiment.
Feedback inbox latest relevant entries were read and left intact; the interactive
instruction controls continuation.

## Findings that revise the formulation inventory

- An autonomous shoulder/rest group does not inherit exact dynamics for 3+
  lanes. Adjacent lane information may be reconstructed from other admitted
  observables; the counterexample is not a strong-history pair.
- Lane-specific FD speeds and the true speed-measurement map matter to exact
  identifiability. Equal-speed symmetry and redundant speed are not silently used.
- Common arrival/departure histories imply equal total system time. A queue-
  relocation distinction is insufficient for the approved objective.
- RM0018 is the existing Wright source; the published author-hosted version
  provides a priority/invariance caution. No new duplicate source ID.
- RM0004 ramp preference does not define arbitrary finite-access behavior;
  a unique source-backed shared-receiving contract is now required.

The [RM9-UG1 packet](../reporting/rm9_20_findings_and_gate.md) and
[contract inventory](../synthesis/rm9/rm9_formulation_contract_inventory.md) are
synchronized. Fixed priorities, bounded ramp preference and stylized proportional
cohorts are distinct choices, with the fixed-ratio B variant correctly recognized
as part of A. No choice is approved. The nodal invariance caution does not reopen
the separate closed VSL batch certificate.

## Mathematical artifact and build

Main mathematics is retained as
`synthesis/rm9/rm9_compact_state_and_observer_audit.tex` and `.pdf`.
Verified pdflatex/latexmk first. Initial build found missing optional lmodern;
removed that font dependency and used installed Computer Modern without package
installation or mathematical changes. Final build command:

```
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/rm9_latex misc/selective_discreteness_ramp_metering_review/synthesis/rm9/rm9_compact_state_and_observer_audit.tex
```

Auxiliary files stay in /tmp. The delivered PDF is copied beside the TeX source.
No numeric traffic examples, simulations or derivative experiments were executed.

## First-audit disposition before subsequent approval

Stopped under RM9's unapproved-allocation/source-adaptation condition at
RM9-UG1, with recommendation A. RM9-G3/G4 certificates remain unestablished;
no observer weakening, whole source-model repair, successor or experiment opened.

## Subsequent user decision and continuation — 2026-10-01

The user endorsed automatic allocation of unused capacity, explicitly adopted
Candidate A as a default and instructed continuation. RM9-UG1 is closed; the
family is Default, not Fixed. The user also requested explanation of service
rules' effects on control. See the [decision record](rm9_allocator_a_approval_and_continuation.md).

Continuation transcribed the two-input law and proved its bounds/work conservation;
derived branch sensitivities; provided hand-calculated service/eligibility
examples; and audited source transfer/receiving branches. Queue relocation alone
is not a total-time benefit under common full departures. Actual ramp propagation,
local receiver eligibility and later departure timing belong in the chain.

The source diagnostics expose an unclosed conservative joint update, without
claiming universal failure of the complete source algorithm. The 2014 optimized
lane-flow predecessor does not supply an autonomous meter-only law. The 2015
Part I lead remains primary metadata, not inspected methods. RM9-UG2 now compares
a concrete restricted conservative adaptation with retaining the fuller
cooperation family for further source-level resolution. Recommendations remain
provisional, and the inventory is synchronized. No new physical law adopted.

Mathematical artifacts: `synthesis/rm9/rm9_priority_allocator_and_control_effects.tex`
and `.pdf`. Build:

```
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/rm9_allocator_latex misc/selective_discreteness_ramp_metering_review/synthesis/rm9/rm9_priority_allocator_and_control_effects.tex
```

PDF copied beside TeX; auxiliaries stay in /tmp. No numerical traffic or gradient
experiments, environment modifications or production implementation. Current
status: RM9 open at RM9-UG2, UG1 closed/A Default, G3/G4 unestablished. See the
[continuation work report](../reporting/rm9_95_allocator_continuation_work_report.md).

Final global/local consistency check corrected the still-unapproved UG2.A
proposal: post-lateral sending/receiving are also bounded by residual original
shared budgets. Recomputing state limits alone could double-spend capacity.
No approved allocation or physical law was changed by this proposal correction.

## Semantic clarification of allocation and Section 4 — 2026-10-01

The user asked whether the mainline priority share a represents extra ramp
service cost due to slow entry/acceleration. Clarified that it allocates scarce
receiving: each accepted unit consumes one receiving unit in the node law.
An acceleration/capacity-loss mechanism is separate and has not been adopted.

The user then asked for the logic of Section 4 without approving it. Explained
a two-lane local mass-flow model: occupancy creates bounded discretionary
sideways offers; donor/receiver limits determine actual redistribution;
remaining shared budgets and updated state determine forward motion/ramp entry;
accepted transfers update queues and subsequent departures. Metering affects
release, then occupancy and autonomous response; it does not choose lateral
movement directly. Mainline redistribution and ramp entry are separate flows.

Made the lateral-first shared-capacity precedence explicit in Candidate A and
the inventory. Its resource interpretation may affect results; conservation
alone does not validate a physical merge/acceleration penalty. A candidate
conservative law is not proof of hidden-history necessity or useful gradients.
UG2 remains open, UG1.A remains Default. No equation or approval changed.

Files updated: this dialogue, RM9.30 candidate consequences and the contract
inventory. Commands: sed reads, standard-library Python edits/local-link checks.
An initial text-edit assertion caught a mismatched substring before any write;
corrected the edit target. Final checks: all local links in these three documents
resolve and decision statuses are retained. No numerical traffic/gradient tests,
new formulas, PDF rebuild, production change or successor. Next allowed action
remains discussion of UG2; semantic clarification is not approval.

## Spatial discretization clarification — 2026-10-02

The user asked whether "per cell" implies CTM in the merge region or a lane-aware
macroscopic model with no longitudinal cells. Checked the existing Section 4
TeX and UG2 candidate text. The length, timestep restriction, cell index and
next-cell receiving establish a CTM-style lane-resolved local cell model:
sideways exchange stays within a longitudinal cell, while forward flow passes
to the next cell in the same lane. Lane-aware macroscopic state and CTM spatial
propagation are compatible descriptions of the proposed model.

The exact local domain, number/length of cells, ramp-entry location and external
boundary coupling remain unspecified. Do not infer a whole-zone well-mixed
compartment, a chosen many-cell geometry, or lane expansion of the whole freeway.
A one-cell reduction requires explicit boundaries and a separate sufficiency/
physical justification within the existing G2/G1 contracts.

Updated RM9.30 and the active inventory to make that already-written spatial
meaning explicit. No equation/PDF, geometry choice, approval or decision status
changed. UG1.A remains Default, UG2 remains proposed/open. No additional gate,
implementation, simulation or successor was opened. Commands: sed inspection,
standard-library Python text edits and local-link/status checks; all passed.
Next allowed action remains discussion of the existing UG2 physical-law contract.

## User-proposed secondary extensions — 2026-10-02

The user proposed two mainline lanes with movement away from merging traffic,
short-lane position-dependent urgency and speed-dependent service consumption,
and explicitly considered them secondary/unnecessary for this stage. Confirmed
family-level methodological plausibility, distinguished already-proposed two
mainline lanes from new anticipatory rules, and treated the finite acceleration
lane as an explicit geometry/state extension if needed. Primary FB0030 and
RM8-P01 methods were rechecked; they support mechanism antecedents rather than
the user's exact coefficients or a universal slower-means-more-service law.

Recorded [RM9-X1–X3](../synthesis/rm9/rm9_deferred_lane_interaction_extensions.md)
as Deferred hypotheses, with state/observer/resource dependencies and admission
triggers. These variants may be examined separately later; they are not identical
to adopting the fuller UG2.B family. Documented separate physical traffic mass
and receiving-resource accounting, no forced merge at a finite lane end, and no
double counting of an acceleration effect through multiple penalties.

Synchronized candidate consequences, inventory and current handoff. UG1.A stays
Default, UG2 stays open; no approval inferred from "ok" or future-extension
interest. No mathematical formula/PDF change, production work, experiment or
successor. A minimal restricted result may be positive, sufficient/aggregate or
negative; deferred mechanisms should address identified evidence gaps or a
planned robustness study rather than guarantee positivity. Work/verification
record is retained in the extension register.

## Handout accepted; UG2.A closed; extensions deferred — 2026-10-02

The user fully viewed and accepted the PDF handout, confirmed stashing the
extension ideas, and instructed continuation to the next user gate. Recorded
[UG2.A adoption](rm9_handout_acceptance_and_ug2_closure.md) without another
confirmation. The acceptance concerns the explicit bounded two-lane CTM-style
adaptation for analytic review, not a literature/calibration or gradient pass.
UG1 allocation stays Default; X1–X3 remain deferred. No git stash, production
change, simulation or successor is authorized. Continue the existing RM9 protocol
and reopen only a genuinely affected scientific contract if new evidence requires.

## Accepted-kernel audit and smallest resource reopening — 2026-10-02

Continued after UG2.A acceptance. Proved conditional mass/storage bounds and
per-cell total-plus-one-lane state equivalence. On an uncapped, unimpeded ordinary
branch, proved that the accepted residual budgets reduce forward flow by the
lateral rate, including unequal lane speeds. The debit persists at fixed cell
state as timestep shrinks. This quantifies a service assumption not established
by the conservation proof; previous "no capacity-drop penalty" wording was
insufficiently explicit about the implicit debit. It is not a speed-based ramp
multiplier, a complete departure loss, or proof of real metering benefit.

A conditional independent-speed observer theorem also reconstructs lane state
and donor direction on a strict free-flow branch. It is not an adopted speed
map or a universal congested/history sufficiency result. No exact hidden-history/
useful-action certificate or verified/independently useful gradient was claimed.

[UG3](../reporting/rm9_40_accepted_kernel_findings_and_resource_gate.md) reopens only
G2's residual forward-rate resource clause. A retains the accepted resource
as a declared conditional debit hypothesis; B (recommended) proposes separate
transverse occupancy and longitudinal face resources with recomputation.
The original equations, UG2 acceptance, Default allocator and deferred X1–X3
remain intact; B is not adopted silently. This is a physical-law decision,
not a numerical-cost or repeated proposal approval.

Main mathematics is `synthesis/rm9/rm9_accepted_kernel_semantics_audit.tex`/`.pdf`.
Build command:

```
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/rm9_kernel_audit_latex misc/selective_discreteness_ramp_metering_review/synthesis/rm9/rm9_accepted_kernel_semantics_audit.tex
```

An initial build caught a missing TeX environment-closing backslash; corrected
that transcription and rebuilt without changing mathematics or installing any
package. Auxiliaries stay in /tmp; PDF copied beside its TeX. This was symbolic
review and hand arithmetic, not simulation or a numerical gradient experiment.
The [work report](../reporting/rm9_96_accepted_kernel_audit_work_report.md) records
verification, assumptions, files and remaining risks. Stop at UG3, no successor.

## Forward allowance and A's source support — 2026-10-02

The user first asks whether forward allowance means usable service capacity,
then questions the unchanged recipient allowance after lateral inflow and asks
whether A is literature-grounded. Clarify that sending is a traffic offer
bounded by capacity; the recipient's inflow can increase that offer on an
uncapped branch, while actual downstream receiving may still constrain flow.
Lateral inflow is external to one lane but internal to road conservation.

Rechecked existing FB0030 Eqs. 20–22: modified sending credits lateral inflow;
the extra old-sending cap comes from our conservative adaptation. RM0018
supports forward merge supply sharing, not that transverse resource clause.
RM8-P01 supports acceleration/void disruption, not the exact one-for-one debit.
Thus A has component-level antecedents, not literature validation of its exact
coupling. Its strongest conditional interpretation is restricted per-step
movement eligibility; no such eligibility mechanism is newly adopted. The
fixed-cell small-step debit means this cannot just be called a vanishing lag.

Recorded the [clarification and work report](../reporting/rm9_41_resource_literature_clarification.md)
and synchronized candidates, inventory, claims and handoff. Conservation was
the adaptation's motivation, not proof of physical necessity. B remains
recommended but unapproved. User objection is not an approval; UG3/G2 remain
open and UG2's historical acceptance is preserved. X1–X3 remain deferred.
No formula/PDF, production, experiment, CSV/source archive or feedback change.


## UG3.B approved; separate-resource audit continued to UG4 — 2026-10-02

The user selects B as more logical and requiring fewer assumptions, and asks
continuation to the next user gate. [Recorded UG3.B approval](rm9_resource_b_approval_and_continuation.md)
and the explicit smallest G2 amendment; did not ask repeated confirmation.
Other UG2 clauses and UG1 Default allocation stay. Gate-specific B does not
select the old fuller-physics UG2.B or any other task alternative.

Re-audited conditional storage/conservation and the corrected free-flow rate.
The old automatic unit debit is absent. Derived post-lateral reconstruction and
conditional reconstruction from completed previous-step fluxes. An exact
admissible rational example shows the lateral map need not be injective under
mass/storage CFL bounds; equal post-states cannot distinguish actions applied
only after that common map, with all remaining state/forcing common.
No extra timestep/propensity restriction was adopted to force reconstruction.

The first-order kernel does not settle independent detector speed in congestion
or its observation stage/support. [UG4](../reporting/rm9_50_separate_resource_findings_and_observer_gate.md)
asks for an explicit idealized first-order observation benchmark (A recommended)
or a bounded measurement/source-first review (B). Both preserve strong history;
neither is adopted. No future candidate-action flow is fed to initial decisions.
This is G1 specification, not renewed G2 approval, numerical cost or SUMO access.

Current mathematics is in
synthesis/rm9/rm9_separate_resource_and_observer_audit.tex and .pdf.
Build command:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/rm9_b_observer_latex misc/selective_discreteness_ramp_metering_review/synthesis/rm9/rm9_separate_resource_and_observer_audit.tex

Historical handouts/source archives and CSVs retained. Source speed section and
node priorities rechecked in existing primary PDFs. New reviewer claims C23–C28
remain separate from physical/gradient evidence. No traffic run or numerical
gradient check. The [work report](../reporting/rm9_97_separate_resource_work_report.md)
records commands, document/PDF checks and limits. Stop at UG4; RM9 is not closed.

Final document verification passed: 17 Markdown records, 114 local links, six
new scoped claims, unchanged 11-query/seven-source CSV inventories and both
historical PDF hashes, exact rational hand arithmetic and a clean five-page
LaTeX PDF. The revised PDF retains editable TeX and direct primary-source links.
No scientific numerical test ran. UG4 remains unapproved after verification.

## Weekly presentation request 6 — 2026-10-02

Read the PowerPoint default rules and request 6 in the global feedback inbox.
The user requested a colleague-facing deck from the VSL task definition to
current ramp-metering progress, emphasizing task semantics, hidden information,
control relevance, literature support and gradient paths rather than sprint
chronology. Generated two boilerplate slides and 12 substantive slides, with
white backgrounds, Calibri 32/18 pt, grouped geometric diagrams, scalable
typeset equations, one analytical illustration and source-backed speaker notes.

Deliverable: [weekly freeway-control deck](../../slides/weekly_freeway_control_review_20261002.pptx).
The [generator](../../slides/generate_weekly_freeway_control_review_20261002.py),
[work record and notes](../../slides/weekly_freeway_control_review_20261002_notes.md),
[layout preview](../../slides/weekly_freeway_control_review_20261002_preview.png)
and [validation record](../../slides/weekly_freeway_control_review_20261002_validation.json)
are retained beside the deck. Build command:

    /home/zpz/miniconda3/envs/differential_sim/bin/python misc/slides/generate_weekly_freeway_control_review_20261002.py

Format, line-count, shape bounds, text-fit, source-path, package/XML and SVG
relationship checks pass. Manual layout inspection prompted wider equation-row
spacing and concise label/title wrapping without reducing the specified fonts.
Preview rendering substitutes DejaVu Sans for unavailable local Calibri and is
not native Office rendering. Existing dependencies were used; no installation,
production change, traffic experiment or numerical gradient test was performed.

The deck preserves S13's conditional analytical closure and distinguishes it
from a calibrated or independently validated study. It reports approved UG3.B
and the pending UG4 observer choice without selecting an observer or claiming
a ramp equal-history/useful-action certificate. Request 6 is marked answered
only after artifact validation; no scientific review gate is advanced.

## Presentation objective notation clarified — 2026-10-02

The user's follow-up asks about the VSL mean-time objective and its derivative.
The [S13 explanation and work record](../../differentiable_freeway_bottleneck_task_review/reporting/s13/s13_80_m2_contract_dialogue.md)
document the three-page derivation and presentation correction. Weekly slide
13 now labels ramp J as total system time, distinguishing it from the VSL
per-mass mean on slide 8. No ramp objective, equation, resource rule or observer
contract changes; UG4 remains unapproved.

## Slide 11 mechanism clarified — 2026-10-02

The user found the slide implicit and requested a brief semantic explanation
and revision emphasizing its core idea. Re-read the approved UG3.B resource
amendment and current findings. The intended kernel is a minimal density-driven
conservative lane exchange followed by recomputation of each lane's ordinary
forward sending/receiving; it is not individual lane-change dynamics or a
direct lane-control actuator. Ramp releases can change occupancy and therefore
the later flow response, but useful hidden information remains unproved.

Renamed slide 11 to “Ramp: lane exchange reshapes forward flow” and made two
stages explicit. A geometric example shows masses 3/7 becoming 5/5, retaining
the transferred portion's color and total mass 10. These numbers are purely
illustrative, not an executed transfer-law calculation. The visible text
distinguishes occupancy changes from fixed physical lane capacity, defines
sending/receiving and retains common ramp/mainline receiving and literature
attribution. Speaker notes preserve bounded storage, stage semantics, the
approved adaptation and the absence of guaranteed throughput improvement.

Changed the existing slide generator and regenerated the weekly PPTX, its
notes, mathematical SVG/PNG assets, layout previews and validation JSON:

    /home/zpz/miniconda3/envs/differential_sim/bin/python misc/slides/generate_weekly_freeway_control_review_20261002.py

The original long diagram caption failed the conservative text-fit check and
was shortened without reducing fonts. Format/package/source/bounds/text-fit
checks pass; the revised full-size slide preview was inspected and the two
stage headings shortened further for clear separation. The deck still has
14 slides and slide 11 has six body lines plus one equation line. No
simulation, scientific numerical test, installation or production change.
This is a presentation correction under current assumptions; RM9/UG4 status
and all scientific choices remain unchanged. The next allowed review action
remains observer-gate discussion.

## Longitudinal CTM structure made explicit in the deck — 2026-10-02

The user pointed out that the revised lane-exchange slide still concealed
longitudinal cell transmission and could be read as one whole-lane aggregate
pool. Re-read the adopted RM9 separate-resource mathematical kernel. This is a
presentation omission: the accepted model already stores continuous mass by
longitudinal cell and physical lane and advances it in discrete time steps.
No methodological amendment or new decision is required.

Slide 10 now names the local lane-aware CTM structure. Slide 11 is renamed
“Ramp: lane-aware CTM across road cells” and replaces the single-cell
before/after example with two lanes spanning three schematic adjacent cells.
Cell faces and forward arrows distinguish longitudinal transfers from paired
lateral exchange within a cell. Its two typeset equations show the ordinary
upstream-sending/downstream-receiving minimum and the time-step lane-cell
mass balance. All symbols are defined in visible text; accepted inflow includes
ramp entry. The common receiving allocator at the merge is explicitly retained
and the ordinary interface minimum is not misapplied separately to competing
ramp/mainline inputs.

Three illustrated cells do not freeze cell count, geometry or ramp placement;
symbolic occupancy bars are not numerical results. Speaker notes retain this
boundary, finite storage, the approved lateral-first/forward-second ordering,
literature antecedents and the reviewer adaptation. Whole-ramp transcription
and observer support remain open as before.

Changed the weekly slide generator and regenerated its PPTX, SVG/PNG assets,
notes, previews and validation JSON using:

    /home/zpz/miniconda3/envs/differential_sim/bin/python misc/slides/generate_weekly_freeway_control_review_20261002.py

The existing package, source-path, font, line-count, text-fit and bounds checks
pass; inspected the full-size slide 11 preview and moved input arrows away
from lane labels. There remain 14 slides; slide 11 has six body lines plus
two equation lines. Preview is the documented font-substituted layout proof,
not native Office rendering. No production or scientific-model change,
dependency installation, traffic simulation or numerical gradient test was
performed. RM9 remains open at UG4; next review action is discussion of the
observer contract.

## Within-cell lateral CTM operator added to slide 11 — 2026-10-02

The user requested the lane-exchange mechanism itself, since the slide's
equations only displayed forward cell transmission. Rechecked the accepted
bounded propensity, lateral sending/receiving minimum and paired mass update
in the separate-resource audit. This fills a presentation omission without
changing the method or opening a new scientific choice.

Slide 11 now has four equations in two labeled stages. The lateral stage
first limits directed exchange by a density-preference fraction of donor
sending and the neighboring lane's receiving, both evaluated before exchange
in the same longitudinal cell. It then updates each lane by timestep times
incoming minus outgoing lateral rate; summing lanes cancels those terms.
The forward stage retains the upstream/downstream CTM minimum and final
lane-cell mass balance using the post-exchange state. The density preference
is bounded, is a model rule rather than a control action, and its exact
normalized density-contrast law remains in the existing mathematical audit
linked from the notes. No new propensity or parameter is adopted.

Retained the three-cell/two-lane geometric diagram and distinguished lateral
and forward equation groups with labels and colors. Defined every displayed
symbol in four concise body lines. Notes preserve finite storage/timestep
bounds, the approved separate resources, common ramp/mainline receiving,
unfrozen geometry, source/adaptation boundaries and lack of a usefulness
claim. Shortened the title after a text-fit failure, retaining the specified
font sizes. The final title is “Ramp CTM: lateral and forward flow”.

Changed the generator and regenerated the weekly deck, mathematical SVG/PNG
asset, notes, previews and validation JSON with:

    /home/zpz/miniconda3/envs/differential_sim/bin/python misc/slides/generate_weekly_freeway_control_review_20261002.py

Format, source paths, fonts, text-fit/bounds, ZIP/XML and SVG relationships
pass. The full-size slide preview was inspected. There are still 14 slides;
slide 11 now has four body lines plus four equation lines. Previews retain
the documented substitute font and are not native Office rendering. No
production code, dependency, traffic simulation, numerical gradient check
or scientific contract changes. RM9 remains open at UG4; the next review
action remains discussion of the observer contract.

## General ramp-metering derivative explained — 2026-10-02

The user requested a brief derivation of the general ramp objective derivative.
Re-read the current separate-resource audit's sensitivity/accounting section
and the RM8 gradient screen. The explanation separates two steps: conservation
gives the cost derivative as a time-weighted sensitivity of total final exits;
the model chain rule supplies that exit sensitivity from meter-rate changes.
Neither local ramp entry nor queue relocation alone certifies an improvement.

The [one-page explanation PDF](../synthesis/rm9/rm9_ramp_total_time_derivative_explained.pdf)
and [editable TeX](../synthesis/rm9/rm9_ramp_total_time_derivative_explained.tex)
define all affected population, fixed external arrivals, final exit rate,
common clearing horizon and total-time objective. They derive the slide's
continuous integral formula by differentiating conservation and reversing
integration order, give the exact left-endpoint CTM sum and show the general
state/exit sensitivity recursion. Fixed-branch limits, possible zero
sensitivity, fixed-mass mean normalization and lack of numerical/usefulness
validation remain explicit. No deck or scientific decision changes.

Verified installed latexmk/pdflatex; build command:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/rm9_general_derivative_latex misc/selective_discreteness_ramp_metering_review/synthesis/rm9/rm9_ramp_total_time_derivative_explained.tex

Copied the built PDF beside its source. Final compilation has no warnings
or overfull/underfull boxes; pypdf confirms one complete readable page.
Shortened the source footer after the initial text overflow. No visual PDF
renderer was available. No production edit, dependency installation,
simulation or numerical gradient test. RM9 remains open at UG4; the next
review action remains observer-contract discussion.

## Colleague concern: aggregate flow can reveal lane contrast — 2026-10-05

The user requested understanding before opening any new work direction:
definition, concrete example, why/when aggregate methods can distinguish
equal-mass states, how the concern arose, literature/current evidence and the
remaining gap. This authorizes explanatory document/source checks only, not
UG4 observer adoption, a new source-review track or a modified traffic model.

Re-read the current handoff, separate-resource mathematical audit, C23–C28
ledger, formulation inventory and historical source/resource records.
Rechecked the existing FB0030 and RM0018 primary PDFs by web open/find; also
read FB0030's local archived text. No new search/source archive or CSV entry.
FB0030 printed pp. 1768–1769 distinguish detector/model speed means and report
different lane-specific FD parameters. RM0018 Section 3.1 supports finite
demand/supply and priorities, not the observer reconstruction theorem.

Created the [four-page explanation PDF](../synthesis/rm9/rm9_lane_contrast_and_aggregate_flow_explained.pdf)
and [TeX](../synthesis/rm9/rm9_lane_contrast_and_aggregate_flow_explained.tex).
Clarified that the relevant factor is known free-flow mobility (speed/cell
length), not vehicle-mass inflation. Reproduced the normalized 2/8 versus 6/4
illustration: equal total 10, distinct flows 14 and 12. Explained exact
two-lane post-exchange reconstruction under unequal known mobilities and
aligned uncapped/unimpeded observations; this is stronger than merely partial
distinction in that branch. Separated failure of a mass-only dynamic closure
from information missing from the strong observer. Added a clearly labeled
capped-flow snapshot illustration and retained the existing stage-collapse
example without promoting either to an equal-history/useful-action witness.

The explanation emphasizes that an informative flow must already be available
at the allowed time/support; candidate future flow cannot be an initial input.
Unknown congested speed, complete history, initial conditions and ramp balances
remain the same G1/UG4 boundary. Sources motivate heterogeneity and clipping;
the inversion and stage results are reviewer derivations for the adapted kernel,
not published field observability or independent usefulness claims. No gate,
candidate, claim status, calibrated parameter or source algorithm is changed.
Added only an explanatory reading link to the current handoff.

Verified existing LaTeX; build command:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/rm9_aggregate_flow_explanation_latex misc/selective_discreteness_ramp_metering_review/synthesis/rm9/rm9_lane_contrast_and_aggregate_flow_explained.tex

Copied PDF beside source. Ragged-right table columns and a shorter source
footer fixed initial layout warnings. Final LaTeX log has no warnings or
overfull/underfull boxes. Pypdf confirms four pages with all expected sections.
Exact Fraction hand checks reproduce both free-flow totals and inverses,
both capped totals and the existing noninjective lateral-map example. These
are arithmetic checks of explanations, not traffic runs or gradient tests.
No visual PDF renderer is installed; no visual rendering claim. No slide,
production, dependency or empirical change. RM9 remains open at UG4; next
allowed main review action remains observer-contract discussion.

## Default information-gap plan for discussion — 2026-10-05

The user asks to establish a default plan before discussing concerns and
revisions. They explicitly reject more than two mainline lanes solely to
defeat mass/flow identification, and require method-first task admission
rather than restrictions inherited from current project progress. Those
guardrails are confirmed; observer/state/action amendments are not approved.

Created the [discussion proposal](../synthesis/rm9/rm9_information_gap_review_plan_proposal.md).
It distinguishes hidden decision-relevant state from observed mass/flow and
from a failure of a particular mass-only closure. Four candidates are recorded
with formulation, evidence, Pros/Cons and dependencies: the current constrained
two-lane task; physically justified acceleration-lane geometry; acceleration,
relaxation or composition; and a separately admitted gap-timing control task.
None is assumed to produce a positive result, and the latter three are not opened.

Provisional default: bounded source/measurement admission, then current-task
history/decision-relevance audit. This favors UG4.B over the earlier unapproved
UG4.A recommendation; A remains a viable faster conditional benchmark. Updated
the active findings, inventory and handoff to distinguish the dated
recommendation from approval. Approved G0/G2 and UG1–UG3 remain unchanged.
Extensions require a physical evidence gap and separate adoption, not merely
a negative current-task result. X1–X3 remain Deferred.

Re-read current and predecessor source/task records. Rechecked existing primary
lane-CTM, acceleration/void and gap-meter papers and aggregate-control abstracts
via web open. These are orientation checks, not a new completed admission
review. The isolated-merge PDF web open failed; used its existing local review
record without claiming a fresh full-text inspection. No broad search campaign,
new archive/CSV entry, simulation, numerical gradient check or production edit.

Changed only the proposal, active findings/inventory/handoff, deferred register
and this dialogue. Commands: rg/cat/sed, primary web open, apply_patch and Python
standard-library link/status validation. The proposal is formula-free; retained
the existing mathematical PDF. Local links and pending/deferral consistency
were checked; no scientific test was required for planning text. RM9 remains
open at UG4. Next allowed action: discuss the proposed default and user concerns,
then record any explicit observer/task choice. No execution step has started.

## Ordering interpretation and safeguards — 2026-10-05

The user proposes minimizing additional assumptions, trying genuine regimes
of the current task before compatible added assumptions, and ranking alternatives
by the parts of the task they change. They ask whether this matches the proposed
ordering and where misunderstandings could arise. This is planning discussion,
not execution or approval of an observer/physical amendment.

Clarified the proposal and synchronized the handoff/inventory: unchanged-law
regimes precede independently motivated within-family assumptions; assumptions
must not be selected solely to create hiddenness, and compatible assumptions
can still change scientific meaning. Lack of literature refutation permits a
labeled hypothesis, not an established positive claim. The expected negative
result remains a conjecture; the free-flow inverse does not settle all branches.
Hiddenness must survive full admitted history and affect common feasible actions.

D2–D4 are families to rank by actual changes to geometry, state, laws, observer,
actuator, objective and derivative contract, not a fixed numerical sequence.
Physical evidence takes priority over proximity to the current model; code reuse
does not count. Alternative scoping need not wait for exhaustive attempts to
rescue the current formulation. No candidate adoption, source-review execution,
simulator/gradient run or new review stage. RM9 remains open at UG4.

Commands: sed/tail reads, apply_patch and Python local-link/status checks. Changed
only the proposal, handoff, inventory and this dialogue; no scientific tests
required for the textual clarification. Next allowed action remains discussion
of the default plan and explicit observer/task choices.

## Consolidated agreed brief plan — 2026-10-05

The user states that the plan is agreed and asks for one brief explicit version
of next review sub-questions, steps and purposes. Created the
[brief next-step plan](../synthesis/rm9/rm9_next_review_brief_plan.md), now the
current ordering reference. It covers observation grounding; unchanged-task
hiddenness; conditional justified within-family assumptions; action relevance
and general gradient readiness; alternatives ranked by scientific changes;
and scoped disposition. Alternative source scoping can proceed in parallel,
but no extension or changed contract is automatically admitted.

Record the user's agreement as acceptance of source-first review ordering,
not adoption of a concrete speed map or authorization to run a simulator or
start a successor. Updated the detailed proposal, active handoff/inventory and
findings to distinguish agreed ordering from pending observer adoption and
preserve historical recommendations. RM9 remains open at UG4.

The next substantive output is an evidence/observer/task matrix with a concrete
observer proposal; pause before adopting a scientific amendment. This turn
only consolidates the plan. Commands: sed reads, apply_patch and Python
local-link/status checks; no scientific tests required, no model/experiment
change. Files changed: brief plan, detailed proposal, handoff, inventory,
findings and this dialogue.

## Explicit brief-flow acceptance and UG4 integration — 2026-10-05

The user explicitly accepts the brief flow and asks whether UG4 requires
separate consideration or can be combined with it. Clarified that UG4 is R1's
observation-grounding work, not a duplicate review or prerequisite route vote.
Split the recorded gate into UG4-R (route selection, closed by this acceptance:
source-first B) and UG4-O (concrete observer/support contract, still open).
The accepted flow authorizes bounded evidence review without repeated approval;
it does not adopt the speed map, weaken history or approve richer dynamics.

Synchronized the brief plan, detailed proposal, handoff, inventory and findings.
Historical A/B recommendation text is preserved with explicit supersession.
No substantive evidence review, traffic experiment, implementation or numerical
gradient check was performed in this clarification turn. Commands: sed/cat,
apply_patch and Python link/status checks; scientific tests not applicable.
Next allowed substantive action: R1 source/measurement audit and concrete
observer proposal, stopping before a changed scientific contract is adopted.

## Review-stage placement clarification — 2026-10-05

The user says the flow is ready and asks how it fits the current stage ordering.
Inspected the branch README, RM9 protocol, handoff and inherited design sequence.
Mapped the accepted R1–R6 work steps onto the existing RM9 contracts: R1/G1/UG4;
R2 identifiability and G3 preparation; R3 conditional G1/G2 amendments; R4/G3
then conceptual G4; R5 bounded alternative screening; R6/G5 disposition. These
are RM9 continuation steps, not six stages, a new RM10 or implementation phases.
RM7 planning and RM8 admission remain closed; UG1–UG3 retain adopted semantics.

Clarified the boundary between screening alternatives in RM9 and adopting or
fully formulating a materially different task. The latter requires explicit
current-task disposition and an amendment/successor plan. A small same-task
amendment can stay in RM9 if adopted; RM9 closure still requires user approval.
The accepted source-first R1 review needs no repeated route confirmation.

Updated the brief plan, protocol, README and handoff; archived the clarification
here. Commands: batched cat/sed/rg reads, apply_patch, Python link/status checks.
No scientific tests required; no substantive source audit, production edit,
simulation or numeric gradient check in this structural clarification turn.
Next substantive action remains the accepted R1 observation/source audit.

## R1 executed to concrete observer gate — 2026-10-05

The user authorizes R1 to the next gate. Executed the bounded source/measurement
pass: reused FB0030, performed five targeted searches, and inspected selected
primary sections in FHWA guidance and Jamshidnejad/De Schutter papers. Added
RM9-O01–O04 with exact access/version/assumption limits. The generalized metric
source's multilane extension excludes lane changes; it is not an observer
theorem for the adapted kernel. No new full-text binary or estimator run.

Produced the [source/task matrix](../extraction/rm9_r1_measurement_source_audit.md),
[mathematical PDF](../synthesis/rm9/rm9_r1_observation_contract_audit.pdf)
and [TeX](../synthesis/rm9/rm9_r1_observation_contract_audit.tex),
[C29–C32 ledger](../extraction/rm9_r1_observation_claims.md) and
[UG4-O findings](../reporting/rm9_60_r1_observation_findings_and_gate.md).
The current law provides mass and accepted face flow, not a source-validated
congested detector passage-speed function. True cell total is not the source's
detector-derived density. Initialization, completed-step indexing and actual
ramp release/entry balances are transcribed as proposed contract requirements.

Added materially distinct Candidate C: section-aligned mass-weighted speed
with an explicit representative equilibrium FD closure at the stored-state
epoch. It avoids the cell-to-face approximation while retaining exact section
and homogeneous/equilibrium idealizations. Preserved historical passage A's
strongest qualified form and P's physical-passage-first alternative. Recommend
C on support/assumption grounds, not because it hides information: exact section
mass/speed can identify the free-flow stored split with unequal known speeds.
No candidate is adopted. Source-first B was a review route and remains closed;
it is not a newly proposed speed map. G0/G2 and all UG1–UG3 laws remain intact.

Synchronized active handoff/inventory, brief/detailed plan, protocol and README;
marked earlier route findings historical. R1 evidence pass reaches UG4-O;
G1 itself remains open, R2 has not run, X1–X3 and multi-ramp/VSL remain deferred.
The next action is discussion/adoption of C/A/P, not automatic positive-case
construction. Actual geometry/initialization must be coherent before a full
feasible information/action certificate.

Built with:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/rm9_r1_observation_latex misc/selective_discreteness_ramp_metering_review/synthesis/rm9/rm9_r1_observation_contract_audit.tex

Used existing differential_sim Python/pypdf for extraction/copy/checks after
default Python lacked pypdf. Validation command:

    /home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/rm9_r1_validate.py

Corrected initial equation/table box warnings. Final five-page PDF has no
LaTeX warnings or overfull/underfull boxes. Local links, source/query CSV IDs,
PDF section text, pending statuses and explanatory Fraction arithmetic pass.
No PDF raster renderer is available; no rendered visual claim. No simulation,
numeric gradient test, production or dependency edit. Files/commands/risks and
results are consolidated in the [work report](../reporting/rm9_98_r1_work_report.md)
and [validation JSON](../reporting/rm9_r1_document_validation.json).

## Semantic observer comparison — 2026-10-05

The user understands the complete gate but asks for a brief semantic introduction
and fair comparison. Their impression of lane aggregation/FD discounting exposed
two ambiguities to clarify: which traffic the speed represents, and how physical
passage speeds are mapped from the modeled state. Created the
[semantic comparison](../synthesis/rm9/rm9_r1_observer_semantic_comparison.md)
and synchronized the active gate's interpretation and handoff navigation.

C describes the traffic present in a section at an instant (mass weights);
A describes actual crossings in a completed window (passage weights), with the
extra upstream-cell-to-face approximation. P asks for grounding of that same
passage target before adopting a map; it is not a third aggregation formula.
FD representative-speed assignment is separate from cross-lane averaging and
is not a mass/service discount. A conceptual queued-versus-passing illustration
explains the populations without claiming a verified case or model fidelity.
C and A have no universal information ranking; C remains provisionally
recommended on section support/fewer approximations, not positivity.

Rechecked FHWA primary definitions. Commands: sed/tail reads, web open,
apply_patch and local-link/status validation. Formula-free explanation; no PDF,
formula, model, dependency or traffic experiment change. Current UG4-O remains
open, C/A/P unapproved, R2 not started. Next action is user discussion/choice,
not implementation or an additional source-review stage.

## C approved; bounded audit to UG5 — 2026-10-05

The user selects C because its section population view fits their TST intuition
and instructs continuation. Recorded the
[approval](rm9_observer_c_approval_and_continuation.md), closing UG4-O. Clarified
that C does not calculate TST, replace all-stream accounting or validate blocked
physical motion. Actual completed faces, full causal history and public inputs
remain; no task geometry/initial knowledge is chosen for favorable hiddenness.

Executed a bounded R2 branch/history audit, R3 assumption screen and R5 primary
source/mechanism comparison. New C33–C39 distinguish local branch inverses from
cross-branch roots and prove conditional complete-state history sufficiency.
Queues do not undo earlier unique state knowledge. Snapshot ambiguity and a
coordinate lost before actions act are not full-history/useful-action evidence.
No supported positive pair is established; all uncertain congested initial
histories are not universally excluded. R2 is a bounded result, not exhaustive
classification. R4 has no new certificate to activate; gradient claims remain
conditional/unverified.

Four targeted searches, existing primary source rechecks and selected RM9-L02/L03
methods are logged. An inaccessible RM0014 web PDF did not become new method
evidence; existing extraction was reused. The L03 landing was blocked, but its
primary content PDF was accessible. Chapter 3.3.1 provides a changed aggregate
demand-law competitor; Chapter 4 lane-drop is not already a ramp adaptation.
This prevents equating physical acceleration effects with a need for extra
state. No law is copied or speed state added.

Produced the [four-page audit](../synthesis/rm9/rm9_observer_c_history_audit.pdf),
[TeX](../synthesis/rm9/rm9_observer_c_history_audit.tex),
[claims](../extraction/rm9_observer_c_history_claims.md),
[source access](../archive/metadata/rm9_observer_c_source_access_record.md) and
[expanded UG5](../reporting/rm9_70_observer_c_findings_and_disposition_gate.md).
UG5 candidates: A scoped result plus minimum recovery/acceleration proposal,
B genuine uncertain-start audit under current laws, C actual finite-lane
proposal, D scoped closure and parking. A is provisional; no task or RM9 closure
is approved. Historical PDFs retain creation-time pending text; active proposal,
comparison, claim statuses, navigation and inventory are explicitly synchronized.

Build command:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/rm9_observer_c_latex misc/selective_discreteness_ramp_metering_review/synthesis/rm9/rm9_observer_c_history_audit.tex

The initial 0.82pt overfull paragraph was reworded and rebuilt. Validation and
full changed-file/command/result limits are recorded in the
[work report](../reporting/rm9_99_observer_c_work_report.md). No simulator,
SUMO, numerical gradient check, dependency change or successor. Next allowed
action is UG5 user discussion/selection; RM9 remains open.

## UG5.B purpose, novelty and expected yield — 2026-10-05

The user asks whether B tries to overcome the current negative result through
initial aggregate ambiguity and why it would be new or productive work.
Clarified that complete-state sufficiency remains valid; B concerns a genuinely
incomplete initial-information domain, not overturning the theorem. Initial
aggregate knowledge includes approved C speed and all declared flow/ramp/history
channels. Existing cross-branch snapshot structure only motivates a possible
domain, not persistent historical or useful-action ambiguity.

New work would bind an independently supported site/initial-history domain,
then analyze complete coupled historical compatibility and useful common actions.
Updated B's living inventory with sequential evidence gates and stop criteria:
unsupported domain means stop with an evidence gap, unique historical state means
scoped negative, surviving but action-irrelevant state means partial/action-negative,
and useful-action distinction means a candidate task with gradients still unproved.
No positive yield or stronger negative theorem is promised. More general merge
literature alone would not close the missing analytic obligation.

The [clarification](../reporting/rm9_71_candidate_b_purpose_and_limits.md)
records rationale, boundaries and work report. B remains unapproved; A remains
provisionally recommended for physical-mechanism comparison. C observer/G2 and
RM9-UG5 status are unchanged. Reads, apply_patch and local-link/status checks only;
no new review execution, source campaign, traffic run or model change.

## UG5 A/C philosophy and mixed-search preference — 2026-10-05

The user views B as too deep a residual-domain search and prefers a mixed search
for feasible methods. They ask whether A/C differ philosophically or primarily
in the direction of physical/task changes. Recorded the preference without
approving a candidate or closing RM9. A/C share physical evidence first, strongest
aggregate competitor and minimum-required-state principles. A starts from
discharge/recovery dynamics; C from finite spatial merge opportunities. A need
not require a finite acceleration lane; C does. Neither is automatically smaller
or more likely positive. Recovery-law error and spatial-resolution error must
each be separated from irreducible information loss.

Clarified that complete-state determinism applies to amended models too: new
mechanisms alone cannot create hidden information. C must retain matched per-cell
observations, not use equal whole-lane totals as a full-observer collision. A
must revisit physical speed semantics and test whether its proposed extra state
is already inferred by the mean-speed/history channel.

Created the [comparison](../synthesis/rm9/rm9_ug5_a_c_semantic_comparison.md),
synchronized the living candidates and handoff. Proposed a brief A/C screen
before deep commitment as a planning stance; A's previous recommendation remains
provisional and nonexclusive. No dual-family pass or combined model is approved.
Directly rechecked existing primary Laval/Cassidy/Daganzo Section 2 and FB0030
route/cooperation passages; no new source/query IDs. Reads, primary open/find,
apply_patch and local-link/status checks only. No formulas, new task law,
simulation, successor or RM9 closure. Current gate remains UG5.

## Brief A/C screen authorized and completed — 2026-10-05

The user finds A more natural in the model chain but accepts a brief mixed
comparison rather than absolute ordering, and instructs execution. This approves
the procedural screen only; it does not select A/C, close RM9 or open a successor.
Conducted two targeted searches and selected primary rechecks, reusing existing
RM8-P01, RM9-L03, FB0030 and RM0004. Added one publisher-abstract lead RM9-L04
with an explicit combined-control/full-method evidence boundary. Q21/Q22 logged.

The [screen](../reporting/rm9_72_a_c_brief_feasibility_screen.md) and
[evidence C40–C42](../extraction/rm9_a_c_brief_screen_evidence.md) recommend A
as the better-supported next planning lead. C is not refuted: inspected geometry
antecedents exist, but RM0004's hypothetical acceleration lane has only one cell,
and its ramp-priority/no-mainline-spillback rule is not our finite-receiving law.
The final article was read after the alternative thesis link failed; no thesis
inspection is claimed. Neither direction establishes a genuine same-history/
useful-action or gradient chain. Modified aggregate discharge and resolved
spatial aggregate models remain strong competitors.

Updated live screen/gate status, comparison, handoff, inventory, README and brief
plan. Existing laws/observer, TST and deferred extensions remain. Proposed next
decision: scoped elementary-task disposition and A-led task planning, with C
reserved unless needed or independently preferred. No detailed law/geometry/state
is formulated and no successor opens before that choice. Work report is in the
screen: reads, two web queries, primary open/find, apply_patch and Python CSV/link/
status checks; no PDF/formula, simulation, gradient experiment or dependencies.
RM9 remains open at UG5; the brief screen requires no duplicate approval.

## UG5.A selection and A-only successor — 2026-10-05

The subsequent user instruction selects A and requests full review to a positive
or negative conclusion, with C held until A completes. Recorded scoped RM9
closure in `reporting/rm9_99_scoped_closure.md`, opened RM10 and executed its
source/analytic review. This supersedes the pending UG5 text above; the closed
RM9 laws/observer are historical contracts, not an adopted non-equilibrium model.
The [current RM10 handoff](../reporting/rm10/current_handoff.md) records the
completed scoped negative admission and pending user result acceptance. No C
task review, experiment or production change was authorized or performed.
