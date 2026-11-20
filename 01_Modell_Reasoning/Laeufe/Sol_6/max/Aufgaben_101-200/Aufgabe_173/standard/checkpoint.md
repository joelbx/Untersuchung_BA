# HA database access checkpoint

- Task: update database proxy candidate selection, retry behavior, display deduplication, and test tunnel outage support.
- Initial inspection: relevant code is in `api/types/databaseserver.go`, `lib/srv/db/proxyserver.go`, `lib/reversetunnel/fake.go`, and `tool/tsh/db.go`.
- Implemented candidate collection, clock-seeded shuffle with test hook, tunnel failover, display deduplication, stable name/host sorting, HostID logging, and fake tunnel outages.
- Tests passed: `GOPROXY=off GOSUMDB=off go test ./types -run TestDatabaseServerOrderingAndDeduplication -count=1` (from `/app/api`); `GOPROXY=off GOSUMDB=off go test ./lib/srv/db -run 'TestDatabaseProxyFailover|TestAccessPostgres|TestAccessMySQL' -count=1`.
- Tests also passed: `GOPROXY=off GOSUMDB=off go test ./tool/tsh -run TestFetchDatabaseCreds -count=1`.
- Final review: `git diff --check` passed; only the intended repository files were changed, and the index baseline was untouched.
