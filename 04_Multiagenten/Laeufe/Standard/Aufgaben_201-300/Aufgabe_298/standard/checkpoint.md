# Cache expiration issue

Completed: added atomic eviction deadline and opportunistic expired-item cleanup for cache operations; scheduled sweeps at inserted items' TTL; added active-only Keys and Values without changing LRU order. Added tests for 10 ms expiration, loader reload, and size-limit order.

Verified: `go test ./utils/cache`, `go test ./core/scrobbler`, and `git diff --check` passed.
