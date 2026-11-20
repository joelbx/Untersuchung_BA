# Issue checkpoint

Task: preserve Trivy CVE content by source, including severity, CVSS, references, and dates, across conversion, library detection, aggregation, and TUI display.

Status: implementation and focused tests complete. `go test ./models ./contrib/trivy/pkg ./detector ./tui` passed with `GOTOOLCHAIN=local GOPROXY=off`; `git diff --check` passed. No delegation used.
