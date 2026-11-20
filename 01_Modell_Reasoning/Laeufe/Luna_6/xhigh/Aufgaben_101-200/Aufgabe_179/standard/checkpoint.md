# Checkpoint

Task: Fix RemoteCluster status and heartbeat persistence when tunnel connections change.

Changes made:
- Added `Presence.UpdateRemoteCluster(ctx, rc)` and a local backend implementation that stores serialized RemoteCluster data under `remoteClusters/<name>`, retaining expiry and resource ID.
- Persisted status and the UTC heartbeat high water mark after tunnel upserts and deletes, including bulk deletion paths.
- Refreshed and persisted status on RemoteCluster reads: no connections means Offline with the heartbeat retained; existing connections mean Online and the heartbeat never decreases.
- Updated AuthServer status handling and added the matching auth client/API implementation required by the expanded Presence interface.

Verification:
- `go test ./lib/services/local ./lib/auth` passed.
- `go test ./lib/services/...` passed.
- `go test ./lib/cache` failed in existing watcher startup/recovery cases (`TestOnlyRecentDisconnect` and `TestRecovery`) due timeouts; rerunning those cases reproduced the failures.

Constraints respected: No network research, downloads, delegated work, history/index changes, or harness changes.
