Fixed the eviction race in [simple_cache.go](/app/utils/cache/simple_cache.go). Expiration sweeps and insertions, including loader insertions, now share a lock, so an expired entry cannot occupy capacity while a concurrent add evicts an active entry.

All three tests flagged by the reviewer passed: the cache tests, cache race tests, and scrobbler tests.