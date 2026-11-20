# Checkpoint

Task: persist RemoteCluster status and last heartbeat across tunnel connection changes.

Implemented:
- Added Presence.UpdateRemoteCluster and local backend storage with expiry.
- Persisted status and monotonic UTC heartbeat during auth RemoteCluster reads.
- Added client/API and role checked support required by Presence interface.
- Added auth regression test for latest and final tunnel removal, including non-UTC input; local test for persistence and expiry.

Verified:
- `go test ./lib/services/local -count=1` passed.
- `go test ./lib/auth -run '^TestAPI$' -check.f 'TestRemoteClusterHeartbeatSurvivesTunnelRemoval|TestRemoteClustersCRUD' -count=1` passed.
- `git diff --check` passed.
