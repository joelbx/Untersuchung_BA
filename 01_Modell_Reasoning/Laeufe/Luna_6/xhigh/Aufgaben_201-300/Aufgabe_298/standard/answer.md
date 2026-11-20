Implemented opportunistic expiration sweeps with an atomic deadline, and added `Values()` to return active entries. `Keys()` now uses the same active-item filtering; loader inserts schedule their TTL after an eviction check.

Verification passed: `go test ./utils/cache` and `git diff --check`.