Implemented persistent RemoteCluster status and heartbeat handling.

- Added `Presence.UpdateRemoteCluster(ctx, rc)` and local backend storage at `remoteClusters/<name>`, preserving expiry.
- Status refresh now stores `offline` when no tunnels remain and retains the saved heartbeat. With tunnels, it stores `online` and advances the heartbeat only when a newer UTC timestamp is observed.
- Added the authenticated API client and server path for the new Presence method.

Verification: `go test ./lib/services/local` passed. `go test ./lib/auth` had 81 passing tests and one failure in `PasswordSuite.TestTiming` due to a 13.26% timing difference exceeding its 10% threshold. `git diff --check` passed.