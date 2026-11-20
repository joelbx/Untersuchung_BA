# Trivy CVE source separation

Status: implementation complete. `go test ./contrib/trivy/... ./models ./detector ./reporter ./tui` and `git diff --check` pass with local dependencies only.

Finding: both Trivy paths currently emit one generic `trivy` entry. Scan conversion overwrites an earlier target's content for the same CVE. Trivy exposes `VendorSeverity` and `CVSS` maps keyed by source, plus a selected `SeveritySource`.

Changes: added source-specific conversion and merge logic, registered Trivy content types, updated metadata aggregation and TUI references, refreshed parser expectations, and added regression tests for source severity, CVSS, dates, and repeated targets.

Goal: preserve source-specific severity, CVSS, references, and dates in separate `trivy:<source>` contents; run relevant existing tests.
