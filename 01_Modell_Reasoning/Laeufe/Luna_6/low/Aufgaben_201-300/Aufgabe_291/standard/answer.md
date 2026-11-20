Implemented NVD CVSS v4.0 conversion and added NVD to `Cvss40Scores()` after MITRE. The `CveContent` fields were already present. Updated `go-cve-dictionary` to a revision that includes NVD v4.0 metrics.

Verification: `go test ./models` and `git diff --check` passed.