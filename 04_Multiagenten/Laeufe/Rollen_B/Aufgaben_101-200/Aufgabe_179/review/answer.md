VERDICT: FIX

**Code defect:** Tunnel creation and deletion do not update the stored cluster state in [presence.go](/app/lib/services/local/presence.go:480). [trustedcluster.go](/app/lib/auth/trustedcluster.go:357) updates it only during auth reads, so stored status can remain stale. Concurrent reads can also overwrite a newer heartbeat with an older snapshot because the backend update is unconditional. Update state on tunnel changes and protect the stored heartbeat from stale writes.

**Tests:** Both relevant existing tests passed (`OK: 1 passed` each):

- `go test -mod=vendor ./lib/services/local -run Test -check.f RemoteClustersCRUD -count=1 -v`
- `go test -mod=vendor ./lib/auth -run TestAPI -check.f TestRemoteClusterStatusKeepsLastHeartbeat -count=1 -v`

TEST_ENVIRONMENT_PROBLEM: None.