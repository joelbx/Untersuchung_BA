The cache abstraction is missing, and direct `ttlcache` use is confined to three files:

- [play_tracker.go](/app/core/scrobbler/play_tracker.go:42) stores `NowPlayingInfo`, sets a 60-minute default and a per-track TTL, and casts values after retrieval.
- [cached_genre_repository.go](/app/scanner/cached_genre_repository.go:14) preloads genre IDs and uses a loader with a 24-hour TTL; it also casts the returned ID.
- [cached_http_client.go](/app/utils/cache/cached_http_client.go:18) caches serialized responses with a caller-provided TTL and a 100-entry limit, then casts on retrieval.

The likely fix is a typed `SimpleCache[V]` in `utils/cache`, followed by migration of those three callers. It needs to cover missing and expired keys, loader errors without insertion, and active keys only. Existing tests cover basic caller behavior and HTTP expiry, but do not cover the new interface’s edge cases. Preservation of the HTTP client’s size limit and logging callback needs an explicit decision because neither appears in the requested interface.

I recorded the findings in `.codex-role-output/checkpoint.md`. **No source files were edited**: this run’s specialist instruction limits me to diagnosis, despite the request to implement the fix.