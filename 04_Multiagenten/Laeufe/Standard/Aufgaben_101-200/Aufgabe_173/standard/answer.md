Updated the database proxy to shuffle all matching services, retry the next candidate when a tunnel has a connection problem, and return a specific error when none can be reached. Authorization now retains every candidate, and tests can set a deterministic order and simulate offline tunnels.

`tsh db ls` now shows one entry per database name. Server logs include `HostID`, and sorting uses name then `HostID`.

The existing database proxy, reverse tunnel, and `tsh` tests passed, along with new tests for ordering, deduplication, offline fallback, and the all offline error.