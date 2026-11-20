Implemented opportunistic expiration cleanup in [simple_cache.go](/app/utils/cache/simple_cache.go). Cache operations now trigger rate limited eviction, and `Values()` returns the active values. The checkpoint is at `.codex-role-output/checkpoint.md`.

Verified with `go test ./utils/cache` (passed).