# Checkpoint

Task: persist RemoteCluster status and last heartbeat across tunnel changes.

Implemented:
- Added Presence.UpdateRemoteCluster and backend persistence with the resource expiry.
- Updated auth RemoteCluster reads to retain the greatest observed heartbeat in UTC and persist status changes. With no tunnels, status becomes Offline while the heartbeat remains.
- Implemented the interface on the HTTP client and role checked auth wrapper, with an update endpoint.
- Added regression coverage for tunnel creation, heartbeat update, deletion of the newest tunnel, deletion of the final tunnel, expiry preservation, and the HTTP update path.

Verification:
- `GOPROXY=off GOSUMDB=off go test ./lib/services/local -check.f 'TestUpdateRemoteCluster' -count=1` passed.
- `GOPROXY=off GOSUMDB=off go test ./lib/auth -check.f 'TestRemoteClusterHeartbeatAfterTunnelDeletion|TestRemoteClustersCRUD|TestUpdateRemoteCluster' -count=1` passed.
- `GOPROXY=off GOSUMDB=off go test ./lib/cache ./lib/services/suite -run '^$'` passed compilation; no tests were run by design.
- `git diff --check` passed.
- `GOPROXY=off GOSUMDB=off go test ./lib/services/local -count=1` passed (full local service package).
