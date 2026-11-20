Implemented database service failover. The proxy now keeps all matching services, shuffles them using the configured clock by default, and tries the next candidate when a tunnel dial reports a connection problem. If none can be reached, it returns a specific error. Tests can supply a deterministic `Shuffle` hook and simulate per-server outages through `FakeRemoteSite.OfflineTunnels`.

I also added `HostID` to server log output, sorted same-name servers by `HostID`, and deduplicated `tsh db ls` results.

Verification passed: the full `lib/srv/db` suite, the `lib/reversetunnel` suite, the focused `api/types` test, and the tsh compile check. TLS handshake failures remain outside the dial retry loop because the handshake occurs after `Connect` returns.