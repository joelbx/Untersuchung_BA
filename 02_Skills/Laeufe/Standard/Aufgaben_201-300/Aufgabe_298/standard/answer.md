Implemented opportunistic expiration cleanup in [simple_cache.go](/app/utils/cache/simple_cache.go). Cache operations now trigger cleanup, and the new `Values()` method returns active values alongside active `Keys()`.

Added tests for 10 ms expiration, loader TTLs, and capacity after expiry. `go test -race -count=1 ./utils/cache` passed.