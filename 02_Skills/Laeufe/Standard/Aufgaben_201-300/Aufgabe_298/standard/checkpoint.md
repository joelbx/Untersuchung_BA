# Cache eviction checkpoint

- Implemented opportunistic expiration cleanup in `utils/cache/simple_cache.go` with an atomic eviction deadline and a mutex for deadline updates.
- `Add`, `AddWithTTL`, `Get`, `GetWithLoader`, `Keys`, and `Values` now trigger cleanup. Loader inserts trigger cleanup again after the loader returns.
- Added `Values()` to `SimpleCache`; `Keys()` and `Values()` enumerate active items.
- Added tests for 10 ms expiry, loader values and TTL, physical eviction, and capacity behavior after expiry.
- Verification passed: `GOPROXY=off GOTOOLCHAIN=local go test -race -count=1 ./utils/cache`; `git diff --check`.
