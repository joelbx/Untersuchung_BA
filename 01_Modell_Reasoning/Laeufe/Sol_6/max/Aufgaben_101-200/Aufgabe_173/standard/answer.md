Implemented HA database failover in [proxyserver.go](/app/lib/srv/db/proxyserver.go:248). The proxy now considers all matching services, shuffles their order, retries tunnel connection problems, and returns a specific error when none can be reached. Tests can supply a deterministic shuffle and simulate offline tunnels.

[Database server types](/app/api/types/databaseserver.go:289) now include `HostID` in log strings, sort by name then host ID, and provide `DeduplicateDatabaseServers`; [tsh db ls](/app/tool/tsh/db.go:59) uses the helper before rendering.

Focused API, database access/failover, and `tsh` tests passed. `git diff --check` passed.