# Checkpoint
Task: persist RemoteCluster status and last heartbeat across tunnel connection updates and deletes.
State: complete. Presence.UpdateRemoteCluster writes JSON, resource ID and expiry to remoteClusters/<name>. Auth reads persist computed status and monotonic UTC heartbeat; no tunnels set Offline while keeping heartbeat. Auth API/client/role wrapper support the new interface method.
Tests: GOPROXY=off GOSUMDB=off go test ./lib/services/local ./lib/auth -check.f 'TestUpdateRemoteCluster|TestRemoteClusterStatusSurvivesTunnelRemoval|TestRemoteClustersCRUD' -count=1 passed. git diff --check passed.
Delegation: none.
