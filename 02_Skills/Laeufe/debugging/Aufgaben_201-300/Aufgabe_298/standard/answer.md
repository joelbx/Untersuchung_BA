Fixed `SimpleCache` so normal cache operations opportunistically evict expired entries. Added `Values()` to the interface; both `Keys()` and `Values()` return only active entries. Loader insertion, TTL expiration, and capacity behavior are covered by new tests.

Verified with `go test -race ./utils/cache ./core/scrobbler -count=1` and `git diff --check`.