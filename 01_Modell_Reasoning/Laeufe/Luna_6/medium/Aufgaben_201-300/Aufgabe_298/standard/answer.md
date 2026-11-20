Implemented opportunistic expiration eviction in [simple_cache.go](/app/utils/cache/simple_cache.go), added `Values()`, and filtered both enumeration methods so expired items are excluded even during the eviction throttle window. The existing cache continues to handle loader TTLs and capacity limits.

Verification: `go test ./utils/cache` passed.