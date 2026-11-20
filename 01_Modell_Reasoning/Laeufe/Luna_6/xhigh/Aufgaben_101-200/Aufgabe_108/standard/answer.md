Implemented the typed `SimpleCache[V]` API with TTL expiration, loader support, and active key listing in [simple_cache.go](/app/utils/cache/simple_cache.go).

Migrated the HTTP client, cached genre repository, and play tracker to the abstraction, removing their type assertions and the `ttlcache` dependency. The HTTP client retains its 100 entry limit.

Verified with `go test ./utils/cache ./scanner ./core/scrobbler`; all passed.