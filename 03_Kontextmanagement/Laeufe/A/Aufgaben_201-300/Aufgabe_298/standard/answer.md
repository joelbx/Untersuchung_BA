Implemented opportunistic TTL eviction in [simple_cache.go](/app/utils/cache/simple_cache.go). Cache operations now trigger cleanup, and `Keys()` and the new `Values()` method expose only active entries. Added tests for 10 ms expiration and delayed loader insertion.

`go test ./utils/cache` and `go test -race ./utils/cache` both pass.