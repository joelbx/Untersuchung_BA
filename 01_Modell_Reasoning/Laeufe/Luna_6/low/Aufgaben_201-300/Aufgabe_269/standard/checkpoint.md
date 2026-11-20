# Checkpoint: Trivy CVE source separation

- Added source-specific Trivy CveContent types and metadata ordering.
- Converter and library DB conversion now retain per-source vendor severity, CVSS metrics, references, and available timestamps.
- TUI collects references across Trivy content types.
- Verified with `go test ./contrib/trivy/pkg ./models ./detector ./tui` and `git diff --check`.
