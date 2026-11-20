Added `SimpleCache[V]` in [utils/cache/simple_cache.go](/app/utils/cache/simple_cache.go) and migrated the three direct `ttlcache` callers to typed cache operations. The wrapper keeps TTL behavior consistent and excludes expired entries from `Keys`.

Added tests for expiration and loader behavior. `go test ./utils/cache ./scanner ./core/scrobbler` passes.