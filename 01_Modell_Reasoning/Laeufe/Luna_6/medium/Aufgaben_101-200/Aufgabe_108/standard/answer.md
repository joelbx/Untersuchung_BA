Implemented `SimpleCache[V]` in [simple_cache.go](/app/utils/cache/simple_cache.go), with typed values, TTL expiration, loader support, and active key listing. Migrated the HTTP client, genre repository, and scrobbler to use it, removing their direct `ttlcache` usage.

Verification passed: `go test ./utils/cache ./scanner ./core/scrobbler` and `git diff --check`.