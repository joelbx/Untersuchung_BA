Trivy CVE contents now use `trivy:<source>` keys and preserve each source’s severity, CVSS scores and vectors, references, and dates. I updated metadata aggregation and TUI references, and added regression tests for conflicting source data and severity attribution.

Verification: `GOTOOLCHAIN=local GOPROXY=off go test ./...` passed.