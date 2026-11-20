Implemented NVD CVSS v4.0 ingestion and aggregation. NVD metrics are stored in `CveContent` under their source, and `Cvss40Scores()` returns MITRE then NVD. The model already had the required v4.0 fields; I updated `go-cve-dictionary` to a locally cached version that exposes NVD v4.0 data.

Added coverage for both sources and their order. `go test ./models -count=1` and `git diff --check` pass.