# Checkpoint

Completed `utils/cache.SimpleCache[V]` as a typed adapter around ttlcache. Migrated HTTP response cache, cached genre repository, and play tracker. The adapter centralizes no-extension TTL behavior and filters expired entries from Keys; HTTP retains its 100 entry limit. Added tests for add/get, TTL expiration, loader reuse and direct error propagation, active keys, and nil interface values.

Validation: `go test ./utils/cache ./scanner ./core/scrobbler` passed. `git diff --check` passed. No delegation used.
