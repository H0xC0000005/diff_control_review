"""Generate the Milestone 0 implementation-progress presentation."""

from __future__ import annotations

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt


OUT = Path(__file__).with_name("milestone_0_implementation_progress.pptx")
FONT = "Calibri"
NAVY = RGBColor(24, 42, 64)
TEAL = RGBColor(32, 137, 145)
PALE = RGBColor(235, 243, 245)
LIGHT = RGBColor(246, 248, 250)
MID = RGBColor(97, 112, 128)
DARK = RGBColor(32, 40, 48)
WHITE = RGBColor(255, 255, 255)
GREEN = RGBColor(52, 145, 91)
AMBER = RGBColor(212, 145, 39)


prs = Presentation()
prs.slide_width = Inches(13.333333)
prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]


def set_text(shape, text, size=18, color=DARK, bold=False, align=PP_ALIGN.LEFT):
    frame = shape.text_frame
    frame.clear()
    frame.word_wrap = True
    frame.margin_left = Inches(0.10)
    frame.margin_right = Inches(0.10)
    frame.margin_top = Inches(0.05)
    frame.margin_bottom = Inches(0.05)
    paragraph = frame.paragraphs[0]
    paragraph.text = text
    paragraph.alignment = align
    for run in paragraph.runs:
        run.font.name = FONT
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.color.rgb = color
    return shape


def add_text(slide, x, y, w, h, text, size=18, color=DARK, bold=False, align=PP_ALIGN.LEFT):
    return set_text(
        slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)),
        text, size, color, bold, align,
    )


def add_box(slide, x, y, w, h, text, fill=LIGHT, line=TEAL, size=18, bold=False):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.color.rgb = line
    shape.line.width = Pt(1.25)
    shape.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    set_text(shape, text, size=size, bold=bold, align=PP_ALIGN.CENTER)
    return shape


def add_title(slide, title, kicker=None):
    bar = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.13)
    )
    bar.fill.solid(); bar.fill.fore_color.rgb = TEAL; bar.line.fill.background()
    add_text(slide, 0.55, 0.32, 12.2, 0.55, title, size=32, color=NAVY, bold=True)
    if kicker:
        add_text(slide, 0.58, 0.88, 12.0, 0.32, kicker, size=14, color=MID)


def add_bullets(slide, x, y, w, h, items, size=18, color=DARK):
    shape = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    frame = shape.text_frame
    frame.clear(); frame.word_wrap = True
    frame.margin_left = Inches(0.08); frame.margin_right = Inches(0.05)
    frame.margin_top = Inches(0.04); frame.margin_bottom = Inches(0.04)
    for idx, item in enumerate(items):
        p = frame.paragraphs[0] if idx == 0 else frame.add_paragraph()
        p.text = item; p.level = 0; p.font.name = FONT; p.font.size = Pt(size)
        p.font.color.rgb = color; p.space_after = Pt(9); p.bullet = True
        for run in p.runs:
            run.font.name = FONT; run.font.size = Pt(size); run.font.color.rgb = color
    return shape


def connector(slide, x1, y1, x2, y2):
    line = slide.shapes.add_connector(
        MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2)
    )
    line.line.color.rgb = MID; line.line.width = Pt(1.5)
    line.line.end_arrowhead = True
    return line


# 1 — title boilerplate
slide = prs.slides.add_slide(blank)
bg = slide.background.fill; bg.solid(); bg.fore_color.rgb = NAVY
accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.72), Inches(1.25), Inches(0.16), Inches(4.45))
accent.fill.solid(); accent.fill.fore_color.rgb = TEAL; accent.line.fill.background()
add_text(slide, 1.2, 1.55, 10.8, 1.35, "Differentiable Minimal Mesoscopic Traffic Simulation", 32, WHITE, True)
add_text(slide, 1.22, 3.05, 10.4, 0.7, "Implementation progress through Milestone 0 · Component 0.5", 20, RGBColor(205, 220, 228))
add_text(slide, 1.22, 5.55, 10.4, 0.45, "Project implementation overview · 28 August 2026", 18, WHITE)

# 2 — contents boilerplate
slide = prs.slides.add_slide(blank); add_title(slide, "Contents")
items = [
    ("01", "Scientific target and engineering strategy"),
    ("02", "Milestone/phase architecture and implementation principles"),
    ("03", "Implemented components 0.1–0.5"),
    ("04", "Major design questions considered and resolved"),
]
for idx, (number, label) in enumerate(items):
    y = 1.35 + idx * 1.03
    add_box(slide, 0.85, y, 1.05, 0.67, number, fill=TEAL, line=TEAL, size=18, bold=True)
    add_box(slide, 2.1, y, 10.15, 0.67, label, fill=LIGHT, line=PALE, size=18)

# 3
slide = prs.slides.add_slide(blank); add_title(slide, "Scientific target → implementation strategy")
add_box(slide, 0.75, 1.35, 5.75, 2.0,
        "Research question\nHow much traffic discreteness is needed\nfor useful signal-control gradients?",
        fill=PALE, line=TEAL, size=18, bold=True)
add_box(slide, 6.85, 1.35, 5.75, 2.0,
        "Working hypothesis\nContinuous mass + selected discrete\nroute/order/lane semantics",
        fill=LIGHT, line=NAVY, size=18, bold=True)
connector(slide, 6.45, 2.35, 6.82, 2.35)
add_bullets(slide, 1.05, 4.05, 11.35, 2.25, [
    "Start from a transparent, differentiable aggregate LTM baseline.",
    "Keep structural identities fixed; differentiate only continuous traffic and control paths.",
    "Add mesoscopic order/lane detail later and test forward fidelity, gradient fidelity, and usefulness separately.",
])

# 4
slide = prs.slides.add_slide(blank); add_title(slide, "Gated workflow and component architecture")
labels = ["0.1\nFD + units", "0.2\nLTM link", "0.3\nMovement map", "0.4\nNode solver", "0.5\nSignal service", "0.6\nRollout", "0.7\nGradients"]
for i, label in enumerate(labels):
    x = 0.45 + i * 1.82
    fill = PALE if i < 5 else LIGHT
    line = GREEN if i < 5 else AMBER
    add_box(slide, x, 1.45, 1.52, 1.02, label, fill=fill, line=line, size=18, bold=True)
    if i < 6: connector(slide, x + 1.52, 1.96, x + 1.78, 1.96)
add_bullets(slide, 0.9, 3.25, 11.7, 2.55, [
    "Phases A–C froze the complete system before component implementation.",
    "Each component follows Dᵢ implementation → Eᵢ evidence → user checkpoint.",
    "Components 0.1–0.5 are accepted by the latest feedback and validated independently.",
    "Components 0.6–0.7 and milestone integration remain gated future work.",
])

# 5
slide = prs.slides.add_slide(blank); add_title(slide, "Milestones, phases, and component gates")
add_box(slide, 0.65, 1.15, 3.85, 1.15,
        "Milestone\nOne scientifically distinct outcome", fill=PALE, line=TEAL, size=18, bold=True)
add_box(slide, 4.75, 1.15, 3.85, 1.15,
        "Phase\nOne approval or execution stage", fill=LIGHT, line=TEAL, size=18, bold=True)
add_box(slide, 8.85, 1.15, 3.85, 1.15,
        "Component\nOne dependency-ordered subsystem", fill=PALE, line=TEAL, size=18, bold=True)
phase_labels = ["A\nPropose", "B\nDiscuss", "C\nFreeze", "Dᵢ/Eᵢ\nBuild + check", "Integration\nCompose + check", "F\nClose"]
phase_widths = [1.55, 1.55, 1.55, 2.15, 2.45, 1.55]
x = 0.75
for index, (label, width) in enumerate(zip(phase_labels, phase_widths, strict=True)):
    add_box(slide, x, 2.85, width, 1.0, label, fill=LIGHT, line=NAVY, size=18, bold=True)
    if index < len(phase_labels) - 1:
        connector(slide, x + width, 3.35, x + width + 0.25, 3.35)
    x += width + 0.3
add_bullets(slide, 0.95, 4.45, 11.5, 1.75, [
    "A component checkpoint establishes a trusted dependency; it is not a new scientific milestone.",
    "Scientific ambiguities stop the gate; implementation-conformance errors may be fixed within scope.",
    "Integration begins only after every component checkpoint is explicitly accepted.",
])

# 6
slide = prs.slides.add_slide(blank); add_title(slide, "Project milestone design and rationale")
milestones = [
    ("M0", "Differentiable aggregate LTM baseline"),
    ("M1", "Ordered continuous route-mass ledger"),
    ("M2", "Per-lane cumulative-mass interaction zone"),
    ("M3", "Lane allocation, finite storage, exact FIFO"),
    ("M4", "Matched macro–meso sensitivity study"),
    ("M5", "Fixed-time signal optimization"),
    ("M6", "Cross-fidelity transfer to a richer simulator"),
]
for index, (identifier, purpose) in enumerate(milestones):
    y = 1.05 + index * 0.78
    add_box(slide, 0.65, y, 1.0, 0.58, identifier,
            fill=TEAL if index == 0 else LIGHT,
            line=TEAL if index == 0 else MID, size=18, bold=True)
    add_box(slide, 1.8, y, 6.3, 0.58, purpose,
            fill=PALE if index == 0 else LIGHT,
            line=TEAL if index == 0 else PALE, size=18)
add_box(slide, 8.55, 1.05, 4.15, 5.25,
        "Why this separation?\n\n"
        "• Establish aggregate physics before metadata.\n"
        "• Add local behavior only after conservative coupling.\n"
        "• Isolate representation effects from optimization effects.\n"
        "• Test numerical gradients before claiming usefulness.\n"
        "• Reserve cross-fidelity claims for the final evidence layer.",
        fill=PALE, line=TEAL, size=18, bold=False)

# 7
slide = prs.slides.add_slide(blank); add_title(slide, "Implementation principles")
add_box(slide, 0.75, 1.25, 3.75, 1.25, "Small semantic modules\nOne scientific responsibility each", fill=PALE, line=TEAL, size=18, bold=True)
add_box(slide, 4.8, 1.25, 3.75, 1.25, "Typed explicit interfaces\nShapes · units · dtype · device", fill=LIGHT, line=TEAL, size=18, bold=True)
add_box(slide, 8.85, 1.25, 3.75, 1.25, "Pure tensor operations\nOut-of-place state updates", fill=PALE, line=TEAL, size=18, bold=True)
add_bullets(slide, 0.95, 3.25, 11.5, 2.55, [
    "Keep topology, movement identity, routes, and phase permissions structural.",
    "Keep continuous mass, cumulative counts, flows, and green exposure on the AD path.",
    "Prefer established traffic equations and independently readable reference implementations.",
    "Implement the smallest transparent baseline before optimizing storage or batching.",
])

# 7
slide = prs.slides.add_slide(blank); add_title(slide, "Important implementation considerations")
add_box(slide, 0.75, 1.25, 3.75, 1.25, "Conservation first\nNo silent mass loss or repair", fill=PALE, line=TEAL, size=18, bold=True)
add_box(slide, 4.8, 1.25, 3.75, 1.25, "Piecewise gradients\nStable regimes ≠ event ties", fill=LIGHT, line=TEAL, size=18, bold=True)
add_box(slide, 8.85, 1.25, 3.75, 1.25, "Model boundaries\nDo not overclaim fidelity", fill=PALE, line=TEAL, size=18, bold=True)
add_bullets(slide, 0.95, 3.25, 11.5, 2.55, [
    "Reject invalid scientific inputs; do not clip, normalize, smooth, or add epsilon fallbacks.",
    "Validate hand equations and forward invariants before testing gradients.",
    "Compare reverse AD, JVP, and central differences only away from active-set boundaries.",
    "Separate continuum-signal arithmetic correctness from finite-cycle behavioral fidelity.",
])

# 7
slide = prs.slides.add_slide(blank); add_title(slide, "Component 0.1 — traffic units and triangular FD")
add_box(slide, 0.75, 1.35, 4.0, 1.4, "Inputs\nv, w, jam density, link length, Δt", fill=LIGHT, line=TEAL, size=18)
add_box(slide, 4.95, 1.35, 3.4, 1.4, "Derived\ncapacity, storage, τf, τb", fill=PALE, line=TEAL, size=18)
add_box(slide, 8.55, 1.35, 4.0, 1.4, "Guard\nΔt ≤ min(τf, τb)", fill=LIGHT, line=TEAL, size=18)
connector(slide, 4.76, 2.05, 4.92, 2.05); connector(slide, 8.36, 2.05, 8.52, 2.05)
add_bullets(slide, 0.95, 3.45, 11.5, 2.35, [
    "Continuous vehicle-equivalent mass; SI units are explicit and immutable.",
    "Hand anchor: C=0.5625 veh/s, K=45 veh, τf=20 s, τb=60 s.",
    "Strict structural validation rejects invalid speeds, densities, geometry, and time steps.",
])

# 8
slide = prs.slides.add_slide(blank); add_title(slide, "Component 0.2 — cumulative-count LTM link")
add_box(slide, 0.7, 1.25, 3.2, 1.15, "History query\nlinear at shifted time", fill=LIGHT, line=TEAL, size=18)
add_box(slide, 5.05, 1.25, 3.2, 1.15, "Sending\nmin(CΔt, Nᵢₙ(qf)−Nₒᵤₜ)", fill=PALE, line=TEAL, size=18)
add_box(slide, 9.4, 1.25, 3.2, 1.15, "Receiving\nmin(CΔt, Nₒᵤₜ(qb)+K−Nᵢₙ)", fill=LIGHT, line=TEAL, size=18)
connector(slide, 3.92, 1.82, 5.02, 1.82); connector(slide, 8.27, 1.82, 9.37, 1.82)
add_bullets(slide, 0.9, 3.25, 11.6, 2.65, [
    "Boundary histories are updated out of place; empty prehistory is exactly zero.",
    "Fractional delays preserve continuous mass and retain the PyTorch graph.",
    "Independent scalar oracle covers capacity, storage, congestion, and interpolation.",
    "Stable reverse derivative matches central finite difference; GPU execution is verified.",
])

# 8
slide = prs.slides.add_slide(blank); add_title(slide, "Component 0.3 — fixed movement projection")
add_box(slide, 0.8, 1.25, 3.25, 1.35, "Input sending S[i]", fill=LIGHT, line=TEAL, size=18, bold=True)
add_box(slide, 5.0, 1.25, 3.25, 1.35, "D[m] = β[m] · S[i(m)]", fill=PALE, line=TEAL, size=18, bold=True)
add_box(slide, 9.2, 1.25, 3.25, 1.35, "Aggregate by input/output", fill=LIGHT, line=TEAL, size=18, bold=True)
connector(slide, 4.08, 1.93, 4.97, 1.93); connector(slide, 8.28, 1.93, 9.17, 1.93)
add_bullets(slide, 0.95, 3.35, 11.5, 2.55, [
    "Explicit local link order + canonical lexicographic sparse movement order.",
    "Turning rows use float64, atol=10⁻⁹, and no clipping or renormalization.",
    "Gather/project and grouped reductions preserve conservation and gradients.",
    "Exact Jacobian and mapped-permutation tests protect the cross-component identity contract.",
])

# 9
slide = prs.slides.add_slide(blank); add_title(slide, "Component 0.4 — two explicit node regimes")
add_box(slide, 0.75, 1.25, 5.8, 2.25,
        "ORDINARY_ORCA\nTampère capacity-oriented priorities\nFull input FIFO\nFinite active-set redistribution",
        fill=PALE, line=TEAL, size=18, bold=True)
add_box(slide, 6.8, 1.25, 5.8, 2.25,
        "RESTRICTED CONTINUUM SIGNAL\nmin(demand, green service, green supply share)\nNo cross-input share redistribution\nH1–H4 scope",
        fill=LIGHT, line=NAVY, size=18, bold=True)
add_bullets(slide, 0.95, 4.15, 11.5, 1.95, [
    "Exact ties remain visible; incumbent pivoting is current-solve state only.",
    "Independent scalar solver + rational 2×2 trace validate redistribution and FIFO.",
    "Stable merge derivative dx₀/dR=0.6 matches finite difference and CUDA.",
])

# 10
slide = prs.slides.add_slide(blank); add_title(slide, "Component 0.5 — continuum fixed-time signal service")
add_box(slide, 0.7, 1.25, 3.4, 1.2, "Physical green g\ng≥0, Σg=1", fill=LIGHT, line=TEAL, size=18, bold=True)
add_box(slide, 4.95, 1.25, 3.4, 1.2, "Exposure e=A g\nBoolean permissions", fill=PALE, line=TEAL, size=18, bold=True)
add_box(slide, 9.2, 1.25, 3.4, 1.2, "Service μ=gᵢ sᵢ Δt\nH1/H2 validated", fill=LIGHT, line=TEAL, size=18, bold=True)
connector(slide, 4.12, 1.85, 4.92, 1.85); connector(slide, 8.37, 1.85, 9.17, 1.85)
add_bullets(slide, 0.95, 3.25, 11.5, 2.6, [
    "Physical greens are rejected when invalid—never clipped, normalized, or softened.",
    "Analytical exposure Jacobian equals A; fixed-total torch.func.jvp matches exactly.",
    "Han coupling gives flow (1,6), leaves 3 units unused, and gradient (0,10).",
    "Claim is continuum arithmetic/AD correctness, not finite-cycle switching equivalence.",
])

# 11
slide = prs.slides.add_slide(blank); add_title(slide, "Design questions — propagation and representation")
add_box(slide, 0.75, 1.25, 5.75, 2.05,
        "G1 · Delay handling\nRoot: fixed steps do not align with physical travel times.\nChoice: query cumulative histories at exact shifted times\nwith structural linear interpolation.",
        fill=PALE, line=TEAL, size=18)
add_box(slide, 6.8, 1.25, 5.75, 2.05,
        "G2 · Movement representation\nRoot: readable local identity conflicts with global batching.\nChoice: canonical node-local sparse maps; any optimized\nlayout must remain a derived equivalent view.",
        fill=LIGHT, line=TEAL, size=18)
add_box(slide, 0.75, 3.75, 5.75, 2.05,
        "G4 · Traffic quantity and units\nRoot: rates, densities, and step masses are easy to mix.\nChoice: continuous vehicle-equivalent mass with explicit\nrate × time conversions at interfaces.",
        fill=LIGHT, line=TEAL, size=18)
add_box(slide, 6.8, 3.75, 5.75, 2.05,
        "Initial LTM state\nRoot: arbitrary occupancy needs causally consistent history.\nChoice: empty-start baseline now; synthetic prehistory only\nfor isolated references, richer initialization deferred.",
        fill=PALE, line=TEAL, size=18)

# 12
slide = prs.slides.add_slide(blank); add_title(slide, "Design questions — node and signal semantics")
add_box(slide, 0.75, 1.25, 5.75, 2.05,
        "G3 · Ordinary node allocation\nRoot: demand, supply, priority, and FIFO may compete.\nChoice: Tampère Branch-T/ORCA with full FIFO and\ncapacity-oriented finite active-set allocation.",
        fill=PALE, line=TEAL, size=18)
add_box(slide, 6.8, 1.25, 5.75, 2.05,
        "G3-S · Signal/node coupling\nRoot: unused phase share must not become free ORCA supply.\nChoice: separate restricted Han service under H1–H4;\nno cross-input or cross-phase redistribution.",
        fill=LIGHT, line=TEAL, size=18)
add_box(slide, 0.75, 3.75, 5.75, 2.05,
        "C0.4-Q5 · Constraint ties\nRoot: several constraints may bind while the derivative\nis not unique. Choice: expose all ties; retain a current-solve\nincumbent only when forward-equivalent.",
        fill=LIGHT, line=TEAL, size=18)
add_box(slide, 6.8, 3.75, 5.75, 2.05,
        "C0.5-Q1/Q2 · Green coordinates\nRoot: optimizer convenience can hide infeasible controls.\nChoice: accept physical unit-simplex greens directly; reject\ninvalid values without clipping or normalization.",
        fill=PALE, line=TEAL, size=18)

OUT.parent.mkdir(parents=True, exist_ok=True)
prs.save(OUT)
print(OUT)
