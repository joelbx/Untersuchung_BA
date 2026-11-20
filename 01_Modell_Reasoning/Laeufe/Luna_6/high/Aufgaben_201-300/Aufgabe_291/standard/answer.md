Implemented CVSS v4.0 ingestion and aggregation.

- NVD conversion now stores each v4.0 metric’s score, vector, and severity under its source in [models/utils.go](/app/models/utils.go:122).
- Aggregation now returns MITRE entries followed by NVD entries in [models/vulninfos.go](/app/models/vulninfos.go:612).
- Updated `go-cve-dictionary` to a locally cached revision that includes `Nvd.Cvss40`; the existing `CveContent` fields were already present.

Verification passed: `GOPROXY=off go test ./models`. Checkpoint: `/app/.codex-role-output/checkpoint.md`.