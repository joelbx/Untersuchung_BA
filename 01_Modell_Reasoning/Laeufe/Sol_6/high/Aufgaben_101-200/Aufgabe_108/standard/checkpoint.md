# Checkpoint

Task: introduce utils/cache.SimpleCache[V], migrate direct ttlcache users, and run relevant existing tests.
Status: complete.
Changes: typed ttlcache adapter with non-extending TTL and active Keys; migrated play tracker, genre repository, and HTTP client; retained the HTTP cache size limit.
Verification: GOPROXY=off GOSUMDB=off go test ./utils/cache ./scanner ./core/scrobbler (passed); git diff --check (passed).
