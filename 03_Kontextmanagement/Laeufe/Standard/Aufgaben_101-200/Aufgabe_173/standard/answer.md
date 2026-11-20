The proxy now collects all matching database services, shuffles them, and tries the next candidate when a tunnel dial has a connection problem. If none can be reached, it returns a specific connection error. Tests can set a deterministic `Shuffle` hook and mark individual fake tunnels offline.

`tsh db ls` now shows one entry per service name. Server sorting uses name and `HostID`, and server log strings include `HostID`.

The API, reverse tunnel, database proxy, and `tsh` tests passed. The new ordering and failover tests passed, and `git diff --check` found no issues.