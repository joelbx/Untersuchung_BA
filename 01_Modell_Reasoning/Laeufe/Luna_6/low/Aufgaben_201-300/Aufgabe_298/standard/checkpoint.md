# Checkpoint

Issue: opportunistically evict expired entries in `utils/cache` and expose active values.

Initial inspection: implementation is in `utils/cache/simple_cache.go`; tests are in `utils/cache/simple_cache_test.go`.

Implementation: `simpleCache` now uses an atomic deadline to rate limit opportunistic scans, triggered by add/get/loader/keys/values operations. Expired entries are explicitly deleted; `Values()` returns active cache values.

Verification: `go test ./utils/cache` passed.
