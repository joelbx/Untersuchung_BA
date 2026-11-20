# Checkpoint

Implemented database service candidate failover and display deduplication:

- Database server strings include `HostID`; stable sorting compares name then host ID; added `DeduplicateDatabaseServers` preserving first occurrences.
- `FakeRemoteSite.OfflineTunnels` simulates connection problem errors per tunnel server ID.
- `ProxyServerConfig.Shuffle` accepts deterministic ordering; its default uses a locally seeded RNG and configured clock.
- Authorization stores every same-name service; `Connect` tries shuffled candidates and continues after connection problem errors, returning a specific aggregate connection error if none can be reached.
- `tsh db ls` deduplicates before rendering.

Verification: `go test ./types` from `/app/api` passed. Root has no `go.mod`, so `go test ./api/types ...` from `/app` cannot resolve module packages; GOPATH mode attempts for root packages also fail because dependencies are unavailable. `git diff --check` passed.
