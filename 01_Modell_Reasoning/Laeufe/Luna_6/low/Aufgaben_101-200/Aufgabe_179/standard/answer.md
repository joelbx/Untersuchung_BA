Implemented persistent RemoteCluster status and heartbeat updates.

- Added `UpdateRemoteCluster(ctx, rc)` to `Presence`, with backend JSON persistence that preserves expiry and resource ID.
- Updated status refresh to persist `Offline` when no tunnels remain while retaining the last heartbeat. Active tunnels set status to `Online`; the heartbeat advances only when the latest tunnel heartbeat is newer and is stored in UTC.
- Added the required auth wrappers so the interface remains implemented.

Verified with `go test ./lib/services/local ./lib/auth`; both packages passed.