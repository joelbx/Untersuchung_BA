# Checkpoint

Implemented opportunistic expiration cleanup in `utils/cache/simple_cache.go`:

- Added `Values()` to `SimpleCache`; `Keys()` and `Values()` expose only active entries.
- Added `evictExpired()` backed by an atomic pointer to the next expiration deadline, with serialized deadline refresh.
- Wired eviction into add/get/enumeration operations and immediately before a loader inserts its result.
- Preserved loader errors and loaded TTLs. Enumeration uses read-only range iteration so it does not change LRU order; ttlcache continues enforcing the size limit.

Verification: `go test ./utils/cache ./core/scrobbler` passed after the final code change; `git diff --check` is clean. `gofmt` applied.
