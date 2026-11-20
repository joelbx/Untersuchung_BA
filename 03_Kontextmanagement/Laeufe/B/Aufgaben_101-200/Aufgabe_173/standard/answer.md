Implemented HA database failover in `/app`. The proxy now shuffles all matching services and tries the next one when a tunnel has a connection problem. `tsh db ls` deduplicates same-name services, and tests can control ordering and simulate offline tunnels.

The API ordering test, proxy failover and access tests, and `tsh` test passed. `git diff --check` passed.