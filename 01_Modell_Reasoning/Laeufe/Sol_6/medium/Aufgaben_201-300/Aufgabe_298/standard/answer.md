Updated [simple_cache.go](/app/utils/cache/simple_cache.go) to evict expired entries during normal operations and added `Values()` so keys and values expose only active entries. Added tests for short TTLs, loader values, and capacity eviction.

Validation passed: cache tests, race enabled cache tests, and scrobbler tests.