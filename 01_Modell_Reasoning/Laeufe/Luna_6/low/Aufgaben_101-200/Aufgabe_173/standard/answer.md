Implemented the HA database access changes.

- Proxy authorization now retains all same-name database servers. `Connect` shuffles candidates and tries each one, continuing on connection problems and returning a specific error if none can be reached.
- Added the configurable `Shuffle` hook and `FakeRemoteSite.OfflineTunnels`.
- Added database server name deduplication for `tsh db ls`, included `HostID` in server strings, and sorted by name then host ID.

Verification: `go test ./types` from `/app/api` and `git diff --check` passed. The root checkout has no `go.mod`, and the other package tests could not run because dependencies were unavailable in GOPATH mode. Checkpoint: [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).