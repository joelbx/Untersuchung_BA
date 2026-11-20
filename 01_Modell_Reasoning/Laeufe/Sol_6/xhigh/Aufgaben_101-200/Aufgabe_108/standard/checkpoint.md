# Cache abstraction work

- Started: inspect repository cache usage, add `utils/cache` generic interface, migrate callers, and run relevant existing tests.
- Initial working tree: clean.
- External research is unavailable; using repository code and tests only.
- Added `SimpleCache[V]` in `utils/cache` with TTL handling centralized in the adapter.
- Migrated the now-playing cache, cached genre repository, and HTTP client. Preserved the HTTP cache size limit.
- Added focused cache behavior tests for retrieval, expiration, active keys, loading, and loader errors.
- Final verification: `GOPROXY=off GOSUMDB=off go test ./utils/cache ./core/scrobbler ./scanner` passes; `git diff --check` passes.
