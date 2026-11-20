Implemented RemoteCluster status and heartbeat persistence.

- Added `Presence.UpdateRemoteCluster` and persisted serialized clusters under `remoteClusters/<name>`, retaining expiry in [presence.go](/app/lib/services/local/presence.go:632).
- Tunnel upserts and deletions now persist Online or Offline status and keep the heartbeat from moving backward. RemoteCluster reads also refresh and persist status in [presence.go](/app/lib/services/local/presence.go:721).
- Updated AuthServer status handling and added the matching auth client/API support required by the expanded interface.

**Verification:** `go test ./lib/services/local ./lib/auth` and `go test ./lib/services/...` passed. `go test ./lib/cache` failed on watcher startup/recovery timeouts in `TestOnlyRecentDisconnect` and `TestRecovery`; rerunning those cases reproduced the failures.