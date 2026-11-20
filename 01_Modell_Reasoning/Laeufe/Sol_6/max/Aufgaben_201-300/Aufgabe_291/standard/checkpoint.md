# CVSS v4 NVD issue checkpoint

- Started from a clean checked-out repository at `/app`.
- `CveContent` already contains CVSS v4 score, vector, and severity fields.
- The pinned `go-cve-dictionary` NVD model lacks `Cvss40`; a newer revision already cached locally adds it. Updated `go.mod` and `go.sum` to that revision.
- Added NVD v4 conversion by metric source and [Mitre, Nvd] score aggregation, with conversion and aggregation tests.
- Focused model tests and full `models`, `detector`, and `reporter/...` tests passed offline with `GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local`.
- `git diff --check` passed. No git history or index changes were made.
