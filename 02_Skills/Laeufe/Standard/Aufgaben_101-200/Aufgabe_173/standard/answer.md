Implemented database service failover. The proxy now collects all matching servers, shuffles them by default, and tries the next server when a tunnel has a connection problem. Tests can inject a deterministic `Shuffle` function and simulate individual offline tunnels.

`tsh db ls` now shows one entry per service name. Server sorting uses name then `HostID`, and `DatabaseServerV3.String()` includes `HostID`.

The existing database proxy, reverse tunnel, and `tsh` test suites passed. New tests passed for failover, the all-offline error, deduplication, and sorting.