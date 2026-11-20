# Checkpoint

Resolved Fortinet advisory coverage for FortiOS CPE detection and CVE enrichment. Updated go-cve-dictionary to a release with Fortinet models; mapped advisory metadata; added Fortinet confidence methods, advisory IDs, source ordering, and report links. Added regression tests for Fortinet-only CPEs, advisory IDs, HTTP enrichment, content conversion, confidence ranking, and selection order.

Verification: `GOPROXY=off GOSUMDB=off go test ./detector ./models ./server` passed. `git diff --check` passed. A go.mod replacement pins one unrelated transitive module to its cached version for offline builds.
