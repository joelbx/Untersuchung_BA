# Checkpoint

Task: HA database service selection, tunnel retry, display deduplication.
Status: Investigating root cause before edits. `rg` unavailable; using grep/find.

Root cause: `pickDatabaseServer` returns on the first same-name server and `proxyContext` stores only it; `Connect` therefore makes one tunnel dial. `FakeRemoteSite.Dial` ignores ServerID, so outage tests cannot target one service. `tsh db ls` renders the full server list.
Pattern: Existing sort is name-only; existing test tunnel uses `ServerID` generated from host ID and cluster name. Similar code seeds RNG from `Clock.Now().UnixNano()` in lib/auth/auth.go.
Hypothesis: Retaining all matches and iterating a shuffled copy will reach a healthy service after a connection-problem dial error. The API reproduction test fails before the fix with `undefined: DeduplicateDatabaseServers` as expected.

Implementation: Added name/host sorting, display deduplication, HostID in String, optional offline fake tunnels, injectable shuffle with clock-seeded default, and retry across all matching services. Added API helper test and end-to-end tunnel failover test.
Checks passed: `go test ./types -run TestDatabaseServerHAHelpers -count=1` from /app/api; `go test ./lib/srv/db -run TestDatabaseTunnelFailover -count=1`; `go test ./lib/srv/db -run 'TestAccessPostgres|TestDatabaseTunnelFailover' -count=1`; `go test ./lib/reversetunnel ./tool/tsh -run '^$'`; `go test ./tool/tsh -run TestFetchDatabaseCreds -count=1`; `git diff --check`.
Initial command `go test ./api/types -run TestDatabaseServerHAHelpers -count=1` from /app failed because api is a separate Go module. Retried from /app/api successfully.
