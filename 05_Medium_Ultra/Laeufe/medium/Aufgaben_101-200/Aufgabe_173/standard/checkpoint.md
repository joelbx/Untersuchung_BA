# Checkpoint

Task: HA database access and tsh database listing deduplication.

Implemented:
- Database server strings include HostID; sorting uses name and HostID; display deduplication preserves first occurrence.
- Fake tunnel supports OfflineTunnels keyed by ServerID.
- Proxy authorization retains all matching servers; configurable shuffle defaults to clock-seeded random order; connection problems retry remaining servers and report when none are reachable.
- tsh db ls sorts and deduplicates same-name services.
- Added API unit coverage and proxy failover integration coverage.

Verification:
- `go test ./lib/srv/db -run 'TestProxyRetriesOfflineDatabaseTunnel|TestProxyProtocolPostgres' -count=1` passed.
- `go test ./tool/tsh -run TestFetchDatabaseCreds -count=1` passed after final sort edit.
- API module test blocked by unavailable local testify module and GOPROXY=off; new test itself uses only standard library.
- `git diff --check` passed.
