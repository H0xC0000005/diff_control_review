# Search queries — version 0.1

Date: 2026-09-07

## Pilot interpretation

The protocol's four concept families are retained. General scholarly web search is effective for primary publisher records and exact-title verification. Direct arXiv queries require tighter traffic phrases because generic uses of “signal,” “network,” and “traffic” retrieve communications, physics, and computing papers.

## A1 — arXiv differentiable traffic simulation

- `site:arxiv.org traffic "differentiable simulation" signal control`
- `site:arxiv.org traffic "automatic differentiation" "network loading"`
- `site:arxiv.org "differentiable traffic simulation"`
- `site:arxiv.org (traffic OR transportation) differentiable (LTM OR CTM OR "network loading" OR signal)`

Retain papers whose simulator dynamics—not only a learned controller—are differentiated. False positives from particle/communication “traffic” and generic “signal” require road-traffic terms in the title or abstract.

## A2 — arXiv order, FIFO, lane, and spillback

- `site:arxiv.org traffic "partial FIFO" lane queue spillback`
- `site:arxiv.org traffic "queue transmission" turn-level`
- `site:arxiv.org mesoscopic traffic (LTM OR "link transmission") spillback`
- `site:arxiv.org traffic ("route identity" OR "vehicle tracking" OR packet OR cohort) FIFO`

## W1 — differentiable model family

- `"differentiable traffic simulation" traffic signal optimization`
- `"automatic differentiation" traffic "dynamic network loading"`
- `traffic simulator exact gradient discrete vehicle lane`
- `differentiable hybrid traffic simulation signal control`

## W2 — structured macro/meso family

- `traffic dynamic network loading partial FIFO lane queue spillback`
- `turn-level queue transmission traffic link model signal`
- `lane-group queue blockage turn pocket signal optimization`
- `mesoscopic LTM individual vehicle tracking FIFO`
- `queue-based mesoscopic traffic simulator signal optimization`

## W3 — exact-title sentinel verification

Use quoted titles for each sentinel paper. Prefer DOI publisher pages, proceedings records, institutional repositories, or arXiv records over secondary summaries.

## Citation expansion rules

For every nearest-predecessor candidate, inspect:

1. papers it identifies as its closest prior art;
2. later papers that cite or extend its specific state representation;
3. method papers sharing named terms such as mutual restriction intervals, movement-based FIFO, turn-level queue transmission, lane-group blockage, individual-tracking LTM, differentiable hybrid conversion, or differentiable LTM.

