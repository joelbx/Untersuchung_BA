Implemented source-specific Trivy CVE content records keyed as `trivy:<source>`. The converter and library detector preserve each source’s severity, CVSS metrics, references, and dates, and merge records across repeated findings. Added Trivy content types to model aggregation and updated TUI reference collection.

Updated the existing parser expectations in [parser_test.go](/app/contrib/trivy/parser/v2/parser_test.go).

Verification passed: `go test ./models ./contrib/trivy/... ./detector ./tui` and `git diff --check`.