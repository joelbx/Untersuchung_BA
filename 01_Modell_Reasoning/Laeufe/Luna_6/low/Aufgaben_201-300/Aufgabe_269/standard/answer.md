Implemented source-specific Trivy CVE content across conversion, library detection, model aggregation, and TUI references. Each source record preserves its vendor severity and CVSS metrics; the converter also keeps publication and modification dates when Trivy provides them.

Verified with `go test ./contrib/trivy/pkg ./models ./detector ./tui` and `git diff --check`.

The Trivy library database vulnerability record used by `detector/library.go` does not contain publication or modification dates, so that path cannot populate those fields.