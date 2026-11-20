# Checkpoint

Task: fix SimpleCache expiration so normal operations opportunistically evict expired entries, provide Values(), and preserve TTL, loader, and size-limit behavior.

Implemented in `utils/cache/simple_cache.go`:
- Added `evictExpired` with an atomic eviction deadline and a 10 ms scan interval.
- Triggered eviction before add, get, loader-backed get, and enumeration.
- Added `Values()` and filtered both `Keys()` and `Values()` against each item's expiration time, including during the eviction throttle window.
- Existing ttlcache behavior remains responsible for TTL loading and capacity eviction.

Verification: `go test ./utils/cache` passed.
