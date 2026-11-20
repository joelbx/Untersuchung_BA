Added the generic [SimpleCache[V]](/app/utils/cache/simple_cache.go) with typed values, TTL expiration, loader support, and active key listing. Migrated the scrobbler, scanner, and HTTP client to use it, and removed the unused `ttlcache` dependency.

Verification passed: `GOPROXY=off go test -count=1 ./utils/cache ./scanner ./core/scrobbler` and `git diff --check`.