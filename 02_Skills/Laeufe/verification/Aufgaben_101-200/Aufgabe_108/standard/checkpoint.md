# Cache abstraction checkpoint

- Added `utils/cache.SimpleCache[V]` with typed values, TTL expiration without extending on reads, loader support, active keys, and optional internal entry limit.
- Migrated scrobbler, scanner, and HTTP client; removed the unused `ttlcache` module requirement and sums.
- Added tests for typed add/get, missing and expired keys, loader reuse and error propagation, and bounded eviction.
- Final verification: `GOPROXY=off go test -count=1 ./utils/cache ./scanner ./core/scrobbler` passed (all three packages); `git diff --check` passed.
- `rg` unavailable (`/bin/bash: rg: command not found`); used `grep`/`find` for local inspection.
