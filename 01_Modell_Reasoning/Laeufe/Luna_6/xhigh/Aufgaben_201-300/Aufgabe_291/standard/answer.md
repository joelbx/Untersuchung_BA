Implemented CVSS v4.0 ingestion and aggregation. NVD metrics now populate score, vector, and severity on the content entry matching their source; aggregation returns MITRE then NVD. The existing `CveContent` fields were already present.

Updated `go-cve-dictionary` to a compatible version available in the local cache, and extended the aggregation test to cover both sources.

Verification: `GOPROXY=off GOSUMDB=off go test ./models` and `git diff --check` passed.