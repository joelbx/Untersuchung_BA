# Checkpoint

Investigating database server selection, tunnel dialing, and CLI listing. Local `rg` is unavailable, so repository searches use `grep` and `find`.

Implemented candidate collection, clock-seeded random ordering with an injectable Shuffle hook, retry on tunnel connection problems, and a specific error when all candidates are unreachable. Added fake per-server offline tunnels, stable name/host sorting, display deduplication, and HostID in server logging.

Verification:
- `go test ./lib/srv/db ./lib/reversetunnel ./tool/tsh` (from `/app`): passed.
- `go test ./lib/srv/db -run TestProxyDatabaseFailover -count=1` (from `/app`): passed, including first-tunnel outage and all-tunnels-offline cases.
- `go test ./types -run 'TestDeduplicateDatabaseServers|TestSortedDatabaseServersByNameAndHostID' -count=1` (from `/app/api`): passed after removing an unavailable test dependency.
- `git diff --check`: passed.

Offline tooling interruptions resolved locally:
- `go test ./api/types ./lib/srv/db ./lib/reversetunnel ./tool/tsh` (from `/app`) failed with `main module (github.com/gravitational/teleport) does not contain package github.com/gravitational/teleport/api/types`; the API is a separate module, and its tests were run from `/app/api`.
- First run of `go test ./types -run 'TestDeduplicateDatabaseServers|TestSortedDatabaseServersByNameAndHostID' -count=1` (from `/app/api`) failed with `module lookup disabled by GOPROXY=off` for `github.com/stretchr/testify v1.2.2`; the added test now uses the standard library and passed.
