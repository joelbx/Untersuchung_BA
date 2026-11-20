# Checkpoint

Added `utils/cache.SimpleCache[V]` around ttlcache with a shared no-extension TTL policy, typed values, active-key filtering, and a private size-limited constructor for HTTP caching. Migrated the three direct ttlcache callers and added cache contract tests. `go test ./utils/cache ./core/scrobbler ./scanner` passed; `git diff --check` passed; only the adapter imports ttlcache.
