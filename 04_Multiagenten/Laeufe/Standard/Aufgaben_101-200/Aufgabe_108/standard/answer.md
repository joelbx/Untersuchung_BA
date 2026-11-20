Added `SimpleCache[V]` in [utils/cache/simple_cache.go](/app/utils/cache/simple_cache.go) and migrated the play tracker, genre repository, and HTTP client to typed cache values. Expiration deadlines stay fixed on reads, and the HTTP cache retains its 100-entry limit.

Verified with `go test ./utils/cache ./core/scrobbler ./scanner` and `git diff --check`.