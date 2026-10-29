"""Generate the 2026-09-04 weekly project update deck."""

from __future__ import annotations

from pathlib import Path
import subprocess

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt


ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = Path(__file__).resolve().parent
OUT = OUT_DIR / "weekly_update_20260904.pptx"
SPILL = ROOT / "reports/milestone_0_a1_headless_visualizer/integration_e_20260901/spillback_chain_candidate_b"
GRID = ROOT / "reports/milestone_0_a1_headless_visualizer/candidate_b_e3_20260901/grid_2x2_aggregate_shared_2_to_5"
SPILL_GIF = OUT_DIR / "spillback_chain_1fps.gif"
GRID_GIF = OUT_DIR / "grid_2x2_1fps.gif"
SPILL_MP4 = OUT_DIR / "spillback_chain_1fps.mp4"
GRID_MP4 = OUT_DIR / "grid_2x2_1fps.mp4"
FFMPEG = Path("/home/zpz/miniconda3/envs/differential_sim/bin/ffmpeg")

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


def make_gif(frame_dir: Path, output: Path) -> None:
    paths = sorted((frame_dir / "frames").glob("frame_*.png"))
    if not paths:
        raise FileNotFoundError(f"no frames in {frame_dir}")
    frames = [Image.open(path).convert("RGB") for path in paths]
    frames[0].save(
        output,
        save_all=True,
        append_images=frames[1:],
        duration=1000,
        loop=0,
        optimize=False,
    )
    for frame in frames:
        frame.close()


make_gif(SPILL, SPILL_GIF)
make_gif(GRID, GRID_GIF)


def make_mp4(frame_dir: Path, output: Path) -> None:
    if not FFMPEG.is_file():
        raise FileNotFoundError(f"ffmpeg not found at {FFMPEG}")
    subprocess.run(
        [
            str(FFMPEG), "-y", "-framerate", "1",
            "-pattern_type", "glob", "-i", str(frame_dir / "frames/frame_*.png"),
            "-c:v", "libopenh264", "-pix_fmt", "yuv420p",
            "-vf", "pad=ceil(iw/2)*2:ceil(ih/2)*2", "-movflags", "+faststart",
            str(output),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


make_mp4(SPILL, SPILL_MP4)
make_mp4(GRID, GRID_MP4)

prs = Presentation()
prs.slide_width = Inches(13.333333)
prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]


def set_text(shape, text, size=18, color=DARK, bold=False, align=PP_ALIGN.LEFT):
    frame = shape.text_frame
    frame.clear(); frame.word_wrap = True
    frame.margin_left = Inches(0.10); frame.margin_right = Inches(0.10)
    frame.margin_top = Inches(0.05); frame.margin_bottom = Inches(0.05)
    paragraph = frame.paragraphs[0]
    paragraph.text = text; paragraph.alignment = align
    for run in paragraph.runs:
        run.font.name = FONT; run.font.size = Pt(size)
        run.font.bold = bold; run.font.color.rgb = color
    return shape


def add_text(slide, x, y, w, h, text, size=18, color=DARK, bold=False, align=PP_ALIGN.LEFT):
    return set_text(slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)), text, size, color, bold, align)


def add_box(slide, x, y, w, h, text, fill=LIGHT, line=TEAL, size=18, bold=False):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid(); shape.fill.fore_color.rgb = fill
    shape.line.color.rgb = line; shape.line.width = Pt(1.25)
    shape.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    return set_text(shape, text, size, DARK, bold, PP_ALIGN.CENTER)


def add_title(slide, title, kicker=None):
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.13))
    bar.fill.solid(); bar.fill.fore_color.rgb = TEAL; bar.line.fill.background()
    add_text(slide, 0.55, 0.32, 12.2, 0.55, title, 32, NAVY, True)
    if kicker:
        add_text(slide, 0.58, 0.88, 12.0, 0.32, kicker, 14, MID)


def add_bullets(slide, x, y, w, h, items, size=18):
    shape = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    frame = shape.text_frame; frame.clear(); frame.word_wrap = True
    frame.margin_left = Inches(0.08); frame.margin_right = Inches(0.05)
    for index, item in enumerate(items):
        p = frame.paragraphs[0] if index == 0 else frame.add_paragraph()
        p.text = item; p.font.name = FONT; p.font.size = Pt(size)
        p.font.color.rgb = DARK; p.space_after = Pt(8); p.bullet = True
        for run in p.runs:
            run.font.name = FONT; run.font.size = Pt(size); run.font.color.rgb = DARK
    return shape


def connector(slide, x1, y1, x2, y2):
    line = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    line.line.color.rgb = MID; line.line.width = Pt(1.5); line.line.end_arrowhead = True


def image_contain(slide, path, x, y, w, h):
    with Image.open(path) as image:
        iw, ih = image.size
    scale = min(w / iw, h / ih)
    pw, ph = iw * scale, ih * scale
    return slide.shapes.add_picture(str(path), Inches(x + (w - pw) / 2), Inches(y + (h - ph) / 2), Inches(pw), Inches(ph))


def movie_contain(slide, movie, poster, x, y, w, h):
    with Image.open(poster) as image:
        iw, ih = image.size
    scale = min(w / iw, h / ih)
    pw, ph = iw * scale, ih * scale
    return slide.shapes.add_movie(
        str(movie), Inches(x + (w - pw) / 2), Inches(y + (h - ph) / 2),
        Inches(pw), Inches(ph), poster_frame_image=str(poster), mime_type="video/mp4",
    )


# 1 — title boilerplate
slide = prs.slides.add_slide(blank)
bg = slide.background.fill; bg.solid(); bg.fore_color.rgb = NAVY
accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.72), Inches(1.25), Inches(0.16), Inches(4.45))
accent.fill.solid(); accent.fill.fore_color.rgb = TEAL; accent.line.fill.background()
add_text(slide, 1.2, 1.55, 10.8, 1.0, "Differentiable Minimal Mesoscopic Traffic Simulation", 32, WHITE, True)
add_text(slide, 1.22, 2.85, 10.4, 0.8, "Weekly implementation update", 24, RGBColor(205, 220, 228))
add_text(slide, 1.22, 5.55, 10.4, 0.45, "M0 closure · visualizer · M1 · M2 planning | 4 September 2026", 18, WHITE)

# 2 — contents boilerplate
slide = prs.slides.add_slide(blank); add_title(slide, "Contents")
for i, (num, label) in enumerate([
    ("01", "Milestone 0 closure"), ("02", "Headless visualizer and two cases"),
    ("03", "Milestone 1 ordered route-mass ledger"), ("04", "Milestone 2 interaction-zone planning"),
]):
    y = 1.35 + i * 1.03
    add_box(slide, 0.85, y, 1.05, 0.67, num, TEAL, TEAL, 18, True)
    add_box(slide, 2.1, y, 10.15, 0.67, label, LIGHT, PALE, 18)

# 3
slide = prs.slides.add_slide(blank); add_title(slide, "Milestone 0 closed: trusted differentiable macro backbone")
add_box(slide, 0.7, 1.2, 2.65, 1.15, "Triangular FD\n+ LTM links", PALE, TEAL, 18, True)
add_box(slide, 3.65, 1.2, 2.65, 1.15, "Movement maps\n+ node solver", LIGHT, TEAL, 18, True)
add_box(slide, 6.6, 1.2, 2.65, 1.15, "Continuum signal\n+ rollout", PALE, TEAL, 18, True)
add_box(slide, 9.55, 1.2, 2.65, 1.15, "Objectives\n+ gradient checks", LIGHT, TEAL, 18, True)
add_bullets(slide, 0.9, 3.0, 11.5, 2.8, [
    "Component 0.5 completed signal service; Components 0.6–0.7 closed rollout and evidence.",
    "Continuous vehicle-equivalent mass; fixed topology and phase permissions remain structural.",
    "Hand references → conservation/admissibility → reverse/JVP/finite-difference agreement.",
    "Outcome: a reproducible aggregate baseline against which mesoscopic refinements can be isolated.",
])

# 4
slide = prs.slides.add_slide(blank); add_title(slide, "M0_a1 visualizer: make dynamics inspectable")
image_contain(slide, SPILL / "overview.png", 0.55, 1.15, 6.2, 5.65)
add_bullets(slide, 7.05, 1.45, 5.65, 4.8, [
    "Headless Matplotlib renderer over recorded simulator histories—not a second simulator.",
    "Shows topology, occupancy/storage, boundary flow, queues, signal service, and conservation.",
    "Deterministic frames and manifests support review, regression diagnosis, and presentations.",
    "Branch-isolated optional tool: no change to the accepted M0 numerical path.",
])

# 5
slide = prs.slides.add_slide(blank); add_title(slide, "Visualizer case 1: two-link spillback chain", "Embedded MP4 at ~1 frame/s; click to play in slide-show mode")
movie_contain(slide, SPILL_MP4, SPILL / "frames/frame_0000.png", 0.45, 1.15, 8.2, 5.9)
add_bullets(slide, 8.85, 1.45, 4.0, 4.8, [
    "Downstream storage fills first.",
    "Receiving falls and constrains upstream inflow.",
    "The queue propagates backward without losing mass.",
    "6 intervals; TST = 21 veh-eq·s; residual = 0.",
])

# 6
slide = prs.slides.add_slide(blank); add_title(slide, "Spillback case: what the accounting proves")
add_box(slide, 0.75, 1.25, 3.2, 1.25, "Arrivals\nenter source accounting", PALE, TEAL, 18, True)
add_box(slide, 5.05, 1.25, 3.2, 1.25, "Resident mass\nlinks + source queue", LIGHT, TEAL, 18, True)
add_box(slide, 9.35, 1.25, 3.2, 1.25, "Departures\nenter sink accounting", PALE, TEAL, 18, True)
connector(slide, 3.98, 1.88, 5.02, 1.88); connector(slide, 8.28, 1.88, 9.32, 1.88)
add_bullets(slide, 0.95, 3.25, 11.4, 2.5, [
    "Every internal boundary uses the same realized mass as upstream outflow and downstream inflow.",
    "Storage limits receiving; rejected inflow remains upstream rather than being clipped.",
    "Cumulative arrivals = resident mass + cumulative exits at every recorded boundary.",
    "The animation connects the causal queue pattern to an exact zero conservation residual.",
])

# 7
slide = prs.slides.add_slide(blank); add_title(slide, "Visualizer case 2: full 2×2 network", "Embedded MP4 at ~1 frame/s; click to play in slide-show mode")
movie_contain(slide, GRID_MP4, GRID / "frames/frame_0000.png", 0.35, 1.1, 8.5, 6.0)
add_bullets(slide, 9.0, 1.35, 3.95, 5.0, [
    "Four intersections share a network-wide flow history.",
    "Selected and background routes compete through common nodes.",
    "Signals regulate movement service and downstream occupancy.",
    "18 intervals; TST = 550.025 veh-eq·s.",
])

# 8
slide = prs.slides.add_slide(blank); add_title(slide, "2×2 grid: network-wide traffic accounting")
image_contain(slide, GRID / "overview.png", 0.45, 1.1, 6.25, 5.85)
add_bullets(slide, 6.95, 1.25, 5.9, 5.3, [
    "18 directed links are accounted consistently across sources, internal nodes, and sinks.",
    "Each node movement is simultaneously an input-link exit and output-link entry.",
    "Source queues retain demand rejected by entry capacity; sink totals retain completed mass.",
    "Network identity: generated mass = source queues + link occupancy + cumulative sink exits.",
    "Maximum recorded residual: 7.105×10⁻¹⁵ veh-eq (floating-point scale).",
])

# 9
slide = prs.slides.add_slide(blank); add_title(slide, "Milestone 1: why retain ordered route mass?")
add_box(slide, 0.7, 1.25, 3.6, 1.35, "Macro state\ncontinuous totals", LIGHT, TEAL, 18, True)
add_box(slide, 4.85, 1.25, 3.6, 1.35, "+ ordered route ledger\ncontinuous mass blocks", PALE, TEAL, 18, True)
add_box(slide, 9.0, 1.25, 3.6, 1.35, "Future meso behavior\nroute/order-aware service", LIGHT, TEAL, 18, True)
connector(slide, 4.33, 1.92, 4.82, 1.92); connector(slide, 8.48, 1.92, 8.97, 1.92)
add_bullets(slide, 0.95, 3.35, 11.4, 2.4, [
    "Question: retain semantic discreteness without integerizing physical vehicle flow.",
    "Routes remain structural table references; each local entry stores route position and divisible mass.",
    "Current movement is projected from route metadata rather than duplicated in persistent state.",
])

# 10
slide = prs.slides.add_slide(blank); add_title(slide, "M1 component chain and accepted interfaces")
labels = ["Route table", "Ordered ledger", "Movement\nprojection", "Split / forward /\nexact merge", "Route-aware\nrollout", "Evidence"]
for i, label in enumerate(labels):
    x = 0.35 + i * 2.15
    add_box(slide, x, 1.35, 1.85, 1.15, label, PALE if i % 2 == 0 else LIGHT, TEAL, 17, True)
    if i < len(labels) - 1: connector(slide, x + 1.85, 1.93, x + 2.08, 1.93)
add_bullets(slide, 0.9, 3.25, 11.6, 2.65, [
    "One exact ordered authority per location; aggregate LTM remains the physical backbone.",
    "Continuous partial transfers split mass and interpolate eligibility time affinely.",
    "Only adjacent entries with identical route state and continuous timing merge losslessly.",
    "Every component closed through implementation, validation, and user checkpoint.",
])

# 11
slide = prs.slides.add_slide(blank); add_title(slide, "M1 case: state, notation, and time boundary")
add_box(slide, 0.45, 1.10, 4.00, 1.45,
        "Network and routes\nsource 0 → link 0 ↘\n                         link 2 → link 3 (A) / link 4 (B)\nsource 1 → link 1 ↗",
        fill=PALE, line=TEAL, size=18)
add_box(slide, 4.70, 1.10, 4.00, 1.45,
        "Boundary b\ncomplete state after interval [b−1,b)\nBoundary 0 is empty; Δt = 1 s",
        fill=LIGHT, line=TEAL, size=18, bold=True)
add_box(slide, 8.95, 1.10, 3.95, 1.45,
        "Where mass can exist\nS0/S1 = source queues\nL0…L4 = link ledgers\nC = completed route mass",
        fill=PALE, line=TEAL, size=18)
add_box(slide, 0.55, 2.95, 7.65, 1.55,
        "One entry: A@p0 : 0.25 [−1.0,−0.5]\nroute A · position 0 · mass 0.25 veh-eq · front/tail eligibility times in seconds\nEntries inside [ … ] are ordered downstream-first; the order is exact FIFO metadata.",
        fill=LIGHT, line=TEAL, size=18)
add_box(slide, 8.45, 2.95, 4.35, 1.55,
        "Route table\nA: L0 → L2 → L3\nB: L1 → L2 → L4\np increments after each node crossing",
        fill=PALE, line=TEAL, size=18)
add_bullets(slide, 0.80, 4.85, 11.85, 1.30, [
    "Nodes are transactions, not storage: during an interval they transfer mass; at a boundary every pack is in S, L, or C.",
    "When a pack enters a link, its eligibility profile is shifted by that link's 1 s free-flow delay.",
])

# 12
slide = prs.slides.add_slide(blank); add_title(slide, "M1 case: complete quantitative state evolution")
add_box(slide, 0.40, 1.05, 6.15, 2.05,
        "INTERVAL [0,1) → B1\nBefore transfer at sources:\nS0=[A 0.25(−1,−0.5), A 0.25(−0.5,0)]\nS1=[B 0.50(−1,0)]\nAdmit all; shift +1 s; exact-merge A\nB1: L0=[A@p0 0.50(1,2)]\n       L1=[B@p0 0.50(1,2)]",
        fill=PALE, line=GREEN, size=18)
add_box(slide, 6.78, 1.05, 6.15, 2.05,
        "INTERVAL [1,2) → B2\nNew S0=[A@p0 0.125(0,1)]\nNew S1=[B@p0 0.125(0,1)]\nSource entry capacity is zero: retain both\nL0/L1 cross merge node; p0→p1\nB2: S0=A0.125; S1=B0.125\n       L2=[A 0.50(2,3), B 0.50(2,3)]",
        fill=LIGHT, line=AMBER, size=18)
add_box(slide, 0.40, 3.30, 6.15, 2.05,
        "INTERVALS [2,4) → B3/B4\nQueued 0.125 packs enter L0/L1\nL2 order [A,B] is preserved; no merge\nDiverge projects A→L3, B→L4\nB3: L0=A0.125(3,4); L1=B0.125(3,4)\n       L3=A0.50(3,3.5); L4=B0.50(3.5,4)\nB4: C=[0.50,0.50]; L2=[A0.125,B0.125]",
        fill=PALE, line=TEAL, size=18)
add_box(slide, 6.78, 3.30, 6.15, 2.05,
        "INTERVALS [4,6) → B5/B6\nRemaining [A0.125,B0.125] diverges\nB5: L3=A@p2 0.125(5,5.5)\n       L4=B@p2 0.125(5.5,6)\nB6: all S/L ledgers empty\n       C=[A 0.625, B 0.625]\nB7: unchanged terminal check",
        fill=LIGHT, line=TEAL, size=18)
add_box(slide, 0.55, 5.65, 12.20, 0.90,
        "Closure: generated 1.25 = completed A 0.625 + B 0.625; all queues/links empty; residual = 0.\nL2 keeps [A,B] and route positions: correct divergence, one exact merge, route mismatch safely not merged.",
        fill=PALE, line=TEAL, size=18, bold=True)

# 13
slide = prs.slides.add_slide(blank); add_title(slide, "M1 key choices and engineering difficulty")
add_box(slide, 0.65, 1.25, 3.75, 1.35, "Selective discreteness\nIDs/order fixed; mass continuous", PALE, TEAL, 18, True)
add_box(slide, 4.8, 1.25, 3.75, 1.35, "Two synchronized views\nledger authority; totals derived", LIGHT, TEAL, 18, True)
add_box(slide, 8.95, 1.25, 3.75, 1.35, "Piecewise AD\ncheck stable signatures", PALE, TEAL, 18, True)
add_bullets(slide, 0.9, 3.35, 11.6, 2.45, [
    "The hard boundary is semantic: exact lossless merge is allowed; behavioral compression is not.",
    "Immutable tuples and differentiable tensors must preserve graphs through split/forward operations.",
    "A corrective integration pass repaired coupling evidence without weakening scientific criteria.",
])

# 13
slide = prs.slides.add_slide(blank); add_title(slide, "Milestone 2: per-lane cumulative-mass interaction zone")
add_box(slide, 0.55, 1.25, 3.4, 1.4, "Uₐ\naggregate upstream LTM", LIGHT, TEAL, 18, True)
add_box(slide, 4.95, 1.25, 3.4, 1.4, "Zₐ\nper-lane rank grid + ledger", PALE, TEAL, 18, True)
add_box(slide, 9.35, 1.25, 3.4, 1.4, "Node\nneutral M2 service seam", LIGHT, TEAL, 18, True)
connector(slide, 3.98, 1.95, 4.92, 1.95); connector(slide, 8.38, 1.95, 9.32, 1.95)
add_bullets(slide, 0.9, 3.35, 11.6, 2.5, [
    "Physical link is partitioned once: upstream propagation plus downstream lane-local refinement.",
    "Equal-width bins index cumulative traffic mass, not physical distance; partial final bins preserve storage.",
    "M2 builds conservative representation/coupling; M3 owns lane allocation and FIFO/blockage behavior.",
])

# 14 — deliberately dense question map per amendment
slide = prs.slides.add_slide(blank); add_title(slide, "M2 planning: 6 global + 19 component questions")

def question_panel(slide, x, y, w, h, heading, lines, fill):
    panel = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    panel.fill.solid(); panel.fill.fore_color.rgb = fill
    panel.line.color.rgb = TEAL; panel.line.width = Pt(1.0)
    add_text(slide, x + 0.10, y + 0.06, w - 0.20, 0.30, heading, 13, NAVY, True)
    add_text(slide, x + 0.12, y + 0.39, w - 0.24, h - 0.44, "\n".join(lines), 10, DARK)

question_panel(slide, 0.35, 1.05, 3.05, 5.95, "GLOBAL BACKBONE — CLOSED", [
    "G1  Physical partition + storage/delay",
    "G2  U/Z transfer + time indexing",
    "G3  Equal-bin tensor/cache contract",
    "G4  Neutral node-service boundary",
    "G5  Matched equivalence evidence",
    "G6  Differentiability + signatures",
    "",
    "Closed first; these constrain every",
    "component-local decision below.",
], PALE)

question_panel(slide, 3.60, 1.05, 3.00, 1.82, "2.1  GEOMETRY / TOPOLOGY", [
    "Q1  Record + reconciliation owner",
    "Q2  Per-lane physical heterogeneity",
    "Q3  Lane order + permission coverage",
], LIGHT)
question_panel(slide, 6.75, 1.05, 3.00, 1.82, "2.2  ORDERED LANE STATE", [
    "Q1  Lane-ledger record boundary",
    "Q2  Commitment map + validation",
    "Q3  Exact merge + fragmentation",
], PALE)
question_panel(slide, 9.90, 1.05, 3.00, 1.82, "2.3  RANK GRID", [
    "Q1  Bin/partial-capacity schema",
    "Q2  Edge convention + signature",
    "Q3  Cached-grid ownership",
], LIGHT)
question_panel(slide, 3.60, 3.05, 3.00, 2.20, "2.4  INTERNAL PHYSICS", [
    "Q1  Lane capacity + delays",
    "Q2  Commitment-feasible receiving",
    "Q3  Zone eligibility representation",
    "Q4  Storage roundoff/failure policy",
], PALE)
question_panel(slide, 6.75, 3.05, 3.00, 2.20, "2.5  ROLLOUT", [
    "Q1  Scenario/state/result histories",
    "Q2  Refined/unrefined orchestration",
    "Q3  Boundary conservation context",
], LIGHT)
question_panel(slide, 9.90, 3.05, 3.00, 2.20, "2.6  EVIDENCE", [
    "Q1  Independent scalar-oracle floor",
    "Q2  FD/tolerance/signature schema",
    "Q3  Artifact + provenance contract",
], PALE)
add_box(slide, 3.60, 5.48, 9.30, 1.05,
        "Dependency order: 2.1 → 2.2 → 2.3 → 2.4 → 2.5 → 2.6\nPhase B is resolving the interfaces before implementation.",
        fill=LIGHT, line=TEAL, size=14, bold=True)

prs.save(OUT)
print(OUT)
print(SPILL_GIF)
print(GRID_GIF)
print(SPILL_MP4)
print(GRID_MP4)
