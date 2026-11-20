# Cache abstraction checkpoint

Implemented `utils/cache.SimpleCache[V]` and `NewSimpleCache[V]` over ttlcache. The wrapper disables TTL extension on reads, returns typed values, propagates loader errors, and filters expired keys. Updated play tracking, genre caching, and cached HTTP responses to use it. The HTTP cache keeps its 100-entry limit and new-item logging.

Verification:
- `go test ./utils/cache ./core/scrobbler ./scanner` passed after all edits.
- `git diff --check` passed.
- `rg` was unavailable (`/bin/bash: rg: command not found`); local `find` and `grep` were used for inspection.
