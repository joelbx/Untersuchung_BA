# Checkpoint

Task: Add CVSS v4.0 NVD ingestion and deterministic aggregation alongside MITRE values.

Changes made:
- Confirmed `CveContent` already stores the three CVSS v4.0 fields.
- Updated the `go-cve-dictionary` dependency to a locally cached revision that exposes NVD CVSS v4.0 metrics.
- Added NVD v4.0 metric conversion into `CveContent`, keyed by the metric source like v2/v3.
- Extended `Cvss40Scores()` ordering to MITRE, then NVD, and updated its existing test to cover both.

Validation: `GOPROXY=off GOSUMDB=off go test -mod=mod ./models ./detector` passed, and `git diff --check` passed. Tests ran offline against the locally cached dependency.
