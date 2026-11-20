# Fortinet CVE enrichment checkpoint

- Updated to the cached Fortinet-capable `go-cve-dictionary` version and aligned its indirect dependencies using only the local module cache.
- Added Fortinet CPE matching, confidence ranking, advisory IDs, enrichment, content conversion, source URLs, report ordering, and timestamp diff handling.
- Added focused model and HTTP-backed detector tests for Fortinet-only matching, all-source enrichment, advisory metadata, and report selection.
- Preserved the existing exported enrichment name as a wrapper for downstream callers.
- Verified with `GOPROXY=off GOSUMDB=off go test -mod=readonly ./...` and a final uncached `./models ./detector` run; both passed. `git diff --check` passed.
