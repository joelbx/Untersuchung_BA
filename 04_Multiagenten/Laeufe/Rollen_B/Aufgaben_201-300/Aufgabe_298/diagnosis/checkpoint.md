# Fault localization checkpoint

Inspected `utils/cache/simple_cache.go`, its existing tests, and `core/scrobbler/play_tracker.go`/tests. The wrapper has no eviction sweep or deadline; `Keys` delegates directly to ttlcache and `Values` is absent from the interface and implementation. Add/AddWithTTL/Get/GetWithLoader do not trigger a sweep. The loader callback inserts with `t.Set`, bypassing `AddWithTTL`. `GetNowPlaying` enumerates Keys then calls Get for each player.

Existing tests check Get expiration at 10 ms plus a 50 ms wait, basic Keys, loader, capacity, and default TTL. They do not check expired Keys/Values, eviction upon later operations, or loaded key/value patterns. `GOPROXY=off GOSUMDB=off go test ./utils/cache` passes. No project source or tests were changed.
