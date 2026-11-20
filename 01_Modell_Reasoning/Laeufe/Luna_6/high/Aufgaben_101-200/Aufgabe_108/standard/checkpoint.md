# Checkpoint

Task completed: Added the generic `utils/cache.SimpleCache[V]` API with typed values, optional TTL expiration, loader support, and active key listing. Migrated HTTP response caching, genre caching, and now playing tracking away from direct `ttlcache` use.

Verification: `go test ./utils/cache ./scanner ./core/scrobbler` passed. `git diff --check` passed. No direct Go `ttlcache` references remain in the application packages inspected.
