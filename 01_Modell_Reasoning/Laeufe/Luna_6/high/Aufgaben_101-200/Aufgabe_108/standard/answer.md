Implemented the typed cache abstraction in [simple_cache.go](/app/utils/cache/simple_cache.go), including TTL expiration, loader support, and active key listing. Migrated the HTTP client, genre repository, and now playing tracker away from direct `ttlcache` use and type assertions.

Verification passed: `go test ./utils/cache ./scanner ./core/scrobbler` and `git diff --check`.