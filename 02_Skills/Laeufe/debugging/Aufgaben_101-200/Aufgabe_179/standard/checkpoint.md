# Debugging checkpoint

Issue: RemoteCluster status and last heartbeat regress when tunnel connections change.

Phase 1 underway: inspecting local implementation and tests. `rg` is unavailable (`/bin/bash: rg: command not found`); using grep/find.

Root cause: `AuthServer.updateRemoteClusterStatus` derives status from tunnels on reads and overwrites the heartbeat with the newest *remaining* tunnel, but never persists the heartbeat to the RemoteCluster backend item. When tunnels disappear, the only durable record still has a zero heartbeat. The local Presence service has `CreateRemoteCluster` but no update method. Existing `LatestTunnelConnection` and `TunnelConnectionStatus` provide the established selection/status pattern; retain the age threshold and persist a monotonic heartbeat.

Hypothesis: persisting the status and only increasing the heartbeat during AuthServer status updates will keep the last heartbeat after deletions. A regression test will exercise one and two connections, deletion order, and backend persistence.

Implementation: added Presence.UpdateRemoteCluster and backend Put with JSON and expiry; AuthServer now persists status changes and only increases last heartbeat. Client and role wrappers implement the expanded Presence interface, with a PUT API endpoint. Regression tests cover newest/last tunnel deletion, persisted status/heartbeat, and expiry.

Verification:
- Pre-fix: `GOPROXY=off go test -mod=vendor ./lib/auth -check.f=TestRemoteClusterHeartbeatAfterTunnelRemoval -count=1` failed at the expected heartbeat regression (`auth_test.go:151`).
- Post-fix: focused AuthServer regression passed.
- `GOPROXY=off go test -mod=vendor ./lib/services/local -check.f='TestUpdateRemoteCluster|TestRemoteClustersCRUD|TestTunnelConnectionsCRUD' -count=1` passed.
- `GOPROXY=off go test -mod=vendor ./lib/services/local ./lib/services ./lib/auth -count=1`: local and services passed; auth failed only at `PasswordSuite.TestTiming` (`password_test.go:171`, elapsed difference 27.89243445794465% greater than 10%). This timing assertion is unrelated to RemoteCluster; the full auth suite cannot be claimed green from this run.
- Final relevant checks after the last test edit: `GOPROXY=off go test -mod=vendor ./lib/auth -check.f=AuthSuite -count=1` passed; `GOPROXY=off go test -mod=vendor ./lib/services/local ./lib/services -count=1` passed; `git diff --check` passed. The AuthSuite regression also covers updating an existing tunnel's heartbeat.
