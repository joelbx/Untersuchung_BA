Task: Introduce utils/cache SimpleCache[V], migrate direct ttlcache callers, and run relevant existing tests.
Status: Complete.
Changes: Added typed ttlcache wrapper and tests; migrated play tracker, cached genre repository, and HTTP client. TTLs do not extend on hits; HTTP cache retains its 100-entry limit.
Validation: GOPROXY=off go test ./utils/cache ./core/scrobbler ./scanner; git diff --check.
