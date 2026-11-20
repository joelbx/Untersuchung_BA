Added [SimpleCache[V]](/app/utils/cache/simple_cache.go) and migrated the play tracker, genre repository, and HTTP client to use it. Cached values are now typed at the call sites, TTLs do not extend on reads, and the HTTP client retains its 100-entry limit.

The cache, scanner, and scrobbler tests pass: `go test ./utils/cache ./scanner ./core/scrobbler`.