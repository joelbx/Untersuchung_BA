Implemented source-specific Trivy CVE records. The converter and library detector now preserve per-source severity, CVSS, references, and publication dates, and merge repeated findings without replacing other sources.

Added Trivy source types and included them in metadata aggregation and TUI reference display. Updated parser snapshots to reflect the new output.

Relevant changes: [converter.go](/app/contrib/trivy/pkg/converter.go:170), [library.go](/app/detector/library.go:229), [cvecontents.go](/app/models/cvecontents.go:342), [vulninfos.go](/app/models/vulninfos.go:391), [tui.go](/app/tui/tui.go:948).

Verification passed: `go test ./models ./contrib/trivy/... ./detector ./tui` and `git diff --check`.