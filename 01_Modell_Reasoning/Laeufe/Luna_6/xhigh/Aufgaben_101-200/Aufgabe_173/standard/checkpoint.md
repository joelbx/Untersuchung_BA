# Checkpoint

Task: Resolve the HA database proxy selection issue in `/app`.

Implemented:
- Database server strings include `HostID`; stable sorting compares service name then host ID.
- Added ordered `DeduplicateDatabaseServers` and applied it to `tsh db ls`.
- Added `FakeRemoteSite.OfflineTunnels` for server-specific simulated connection failures.
- Added configurable proxy candidate shuffling, defaulting to a time-seeded RNG based on the configured clock.
- Authorization records all matching database services; proxy dialing retries connectivity failures across the shuffled candidates and reports a specific final connectivity error.

Validation:
- `cd api && go test ./types` passed.
- `go test ./lib/reversetunnel ./lib/srv/db ./tool/tsh` passed.
