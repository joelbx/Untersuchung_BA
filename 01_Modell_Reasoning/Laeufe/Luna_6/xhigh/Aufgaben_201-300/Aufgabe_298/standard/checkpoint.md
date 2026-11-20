# Checkpoint

Task complete: expired-item eviction is scheduled through an `atomic.Pointer[time.Time]`; public cache operations trigger eviction checks; `Keys` and the new `Values` method expose only active items; loader insertion performs an eviction check and schedules the loaded item's TTL.

Verification: `go test ./utils/cache` passed, and `git diff --check` passed. The size limit continues to use ttlcache's existing capacity eviction behavior.
