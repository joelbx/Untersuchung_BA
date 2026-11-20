# Checkpoint

Implemented RemoteCluster persistence and status handling.

- Added `Presence.UpdateRemoteCluster(ctx, rc)` and local backend upsert that JSON-serializes the resource, stores it at `remoteClusters/<name>`, and carries forward expiry/resource ID.
- Auth status refresh now writes the status back. It reports offline with no connections while retaining heartbeat; with connections it reports online and only advances the heartbeat to the greatest stored/observed timestamp (normalized to UTC).
- Added the authenticated HTTP client/server update path needed to keep the extended Presence interface implemented end to end.

Verification: `go test ./lib/services/local` passed. `go test ./lib/auth` compiled but failed `PasswordSuite.TestTiming` (measured difference 13.26%, threshold 10%); remaining 81 auth tests passed. `git diff --check` passed.
