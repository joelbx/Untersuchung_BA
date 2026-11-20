# Checkpoint

Task: Resolve Trivy CVE content source separation in `/app`.

Completed:
- Added source-specific Trivy content types and included them in model aggregation.
- Updated scan conversion and library detection to preserve per-source severity, CVSS, references, and publication/modification dates while merging repeated CVEs.
- Updated TUI reference collection and existing parser expectations for source-specific records.

Verification:
- `go test ./models ./contrib/trivy/... ./detector ./tui` — passed.
- `git diff --check` — passed.
