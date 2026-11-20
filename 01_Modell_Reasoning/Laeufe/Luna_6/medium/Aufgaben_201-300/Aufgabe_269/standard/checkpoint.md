# Checkpoint

Task: separate Trivy CVE metadata by source throughout conversion, models, detector, and TUI.

Completed:
- Added Trivy source content types and made them available through model aggregation and source enumeration.
- Updated scan conversion and library detection to preserve per-source severity, CVSS scores/vectors, references, and publication dates while retaining multiple source entries for a CVE.
- Updated TUI reference collection to include every Trivy source type.

Verification: `go test ./contrib/trivy/pkg ./models ./detector ./tui` passed. `git diff --check` passed.
