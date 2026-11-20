Task: introduce utils/cache SimpleCache[V], migrate direct ttlcache callers, run relevant existing tests.
Status: complete.
Changes: typed synchronized cache with fixed expiration and loader, migrated play tracker, cached genre repository, and HTTP client; preserved HTTP cache entry limit; added focused cache tests.
Verification: GOPROXY=off go test ./utils/cache ./scanner ./core/scrobbler passed; git diff --check passed.
Constraints honored: local code/tests only; no git history/index baseline/harness changes.
