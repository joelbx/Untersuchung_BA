# Checkpoint

Task: Introduce `utils/cache.SimpleCache[V]`, migrate direct `ttlcache` consumers, and verify with existing tests.

Completed:
- Added a typed in-memory cache with `Add`, `AddWithTTL`, `Get`, `GetWithLoader`, and active `Keys` operations.
- Preserved HTTP response TTL behavior and the 100-entry capacity; migrated the play tracker and cached genre repository.
- Removed direct `ttlcache` imports and its module/checksum entries.
- Existing tests passed: `GOPROXY=off GOSUMDB=off go test ./utils/cache ./scanner ./core/scrobbler`.
