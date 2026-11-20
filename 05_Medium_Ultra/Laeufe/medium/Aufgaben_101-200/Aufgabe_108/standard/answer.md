Added `SimpleCache[V]` in [simple_cache.go](/app/utils/cache/simple_cache.go) and migrated the play tracker, genre repository, and HTTP client to typed cache operations. Entries expire at fixed times, and the HTTP client retains its 100-entry limit.

Added cache behavior tests. `GOPROXY=off go test ./utils/cache ./scanner ./core/scrobbler` and `git diff --check` pass.