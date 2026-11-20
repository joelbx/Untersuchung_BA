Implemented opportunistic expiration cleanup in [simple_cache.go](/app/utils/cache/simple_cache.go:12). Cache operations now evict expired entries using the next TTL deadline, and `Keys()` and the new `Values()` return only active entries. Loader results retain their TTL, and loader errors are returned.

Verification passed: `go test ./utils/cache ./core/scrobbler`; `git diff --check` is clean.