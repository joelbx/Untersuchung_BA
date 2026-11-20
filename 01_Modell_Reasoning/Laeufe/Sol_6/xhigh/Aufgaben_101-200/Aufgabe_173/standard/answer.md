Implemented database service failover. The proxy now keeps all matching servers, shuffles them using the configured clock, retries tunnel connection failures, and reports when none can be reached. Tests can supply a deterministic `Shuffle` hook and simulate outages with `OfflineTunnels` in [FakeRemoteSite](/app/lib/reversetunnel/fake.go:50).

[tsh db ls](/app/tool/tsh/db.go:58) now removes same-name duplicates. Database server logs include `HostID`, and sorting uses name then `HostID`.

Verification passed: API type tests, targeted Postgres and MySQL access and proxy tests, the new failover test, and the relevant `tsh` test.