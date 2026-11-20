# Checkpoint

Task: handle multiple database servers for the same service, including shuffled retries, display deduplication, and testable tunnel outages.

Status: implemented candidate collection, clock-seeded shuffle, tunnel retry, display deduplication, host ID logging and ordering, and offline fake tunnels. Added API type tests and a database failover test.

Verification: `go test ./types -count=1` passed in `/app/api`. Targeted database proxy tests covering Postgres, MySQL, and failover passed in `/app`. The `tool/tsh` FetchDatabaseCreds test passed. All tests ran with `GOPROXY=off GOSUMDB=off`. `git diff --check` passed.
