# Checkpoint

Task: Persist RemoteCluster status and last heartbeat through tunnel connection changes.

Completed: Added Presence.UpdateRemoteCluster and backend storage; auth status refresh persists changes and retains the greatest heartbeat in UTC. Added regression coverage for tunnel removal and expiry preservation.

Verification: `go test ./lib/auth ./lib/services/local` passed. `git diff --check` passed.
