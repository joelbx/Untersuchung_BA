# Checkpoint

Task: Fix RemoteCluster persistence and status/heartbeat behavior when tunnel connections are created, updated, or deleted.

Changes made:
- Added `Presence.UpdateRemoteCluster(ctx, rc)` and a local backend implementation that writes JSON to `remoteClusters/<name>` while preserving resource expiry and ID.
- Auth status refresh now persists status. It marks clusters offline when no connections remain, retains their previous heartbeat, marks clusters online when connections exist, and advances heartbeat only to a newer UTC timestamp.
- Tunnel upserts and individual, cluster-wide, and global deletes refresh persisted RemoteCluster status. Added an authenticated API update route and client implementation for the new Presence method.

Verification:
- `go test ./lib/services/local ./lib/cache ./lib/services/...` passed.
- Filtered auth tunnel and RemoteCluster CRUD tests passed.
- Full auth tests twice hit the existing `PasswordSuite.TestTiming` threshold (10.79% and 12.05% over its 10% limit); all other checks in the combined run passed.
