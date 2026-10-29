# Feedback 17: repository migration and VSL bootstrap

2026-10-29. The user authorizes migration of all original misc reviews,
creation of the standalone VSL handoff/project, retention of established
implementation customs, and online Git hosting. Both repositories are private.

The review archive imports 1,413 source files plus referenced context. PDFs,
TeX and non-Markdown evidence retain their bytes. Markdown navigation-only
changes make links portable and repair 82 pre-existing backup-relative links
using uniquely matching existing targets. Source/export hashes are recorded.
Original source folders and the urban AGENTS.md, PROJECT_CONTEXT.md and
PLANS.md remain unchanged. Continue independent reviews in diff_control_review.

The VSL repository contains 20 selected source snapshots and new purpose,
agent, roadmap, model/evidence and start-here documents. Its generic A–F
implementation workflow is retained; urban-specific scientific invariants
are replaced by the already reviewed VSL contract. No implementation plan is
approved and no simulator or numerical traffic evidence is created. The
development agent starts with Phase A planning in that repository.

Preparation used standard-library Python copying/hash/link checks and installed
pypdf. Git initialization, local author identity inherited from the existing
project, repository-local line-ending settings and byte-preserving attributes
support tracked snapshots. The initial documentation commits are unsigned.
Prepared archive files are force-added where historical .gitignore snapshots
would otherwise exclude referenced context; no force push is used.
GitHub CLI creates private repositories under the existing project owner's
account; Git pushes use the existing gh credential helper without changing
global Git authentication. No dependency installation or experiment is run.

Commands are the staged build/validation and publication helpers in
/tmp/vsl_feedback17_20261029, followed by git init/add/commit/push and remote
ref/privacy verification. The manifest and publication receipt make the
delivered contents independently inspectable after those temporary helpers expire.

[Source manifest](source_manifest.json)

[Link repair record](preexisting_missing_links.json)

[Document validation](document_validation.json)

[Publication receipt](publication_receipt.json)

Remaining scientific questions are the prior empirical information/advice,
gradient-usefulness and physical-fidelity outcomes; they do not block this
documentation handoff. Colleague discussion retains its earlier status.
The next allowed actions are topic-based review in this repository and a
separately assigned implementation proposal in diff_freeway_vsl.
