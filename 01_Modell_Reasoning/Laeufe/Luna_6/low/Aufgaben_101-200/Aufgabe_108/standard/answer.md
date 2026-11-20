Implemented the typed `SimpleCache[V]` in [simple_cache.go](/app/utils/cache/simple_cache.go) and migrated the scrobbler, genre repository, and HTTP client to use it. The wrapper centralizes `ttlcache` usage and removes callers’ value assertions.

Existing tests passed: `go test ./utils/cache ./core/scrobbler ./scanner`.