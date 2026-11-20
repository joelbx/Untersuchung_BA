Implemented HA database service selection. The proxy now keeps all matching services, shuffles them through an injectable ordering hook, retries the next candidate when a tunnel has a connectivity failure, and returns a connection problem if none can be reached.

`DatabaseServerV3.String()` now includes `HostID`; server sorting uses name then `HostID`. `tsh db ls` deduplicates same-name services, and `FakeRemoteSite` can simulate outages by `ServerID`.

The API, reverse tunnel, database proxy, and `tsh` tests pass, including a new test for an offline first tunnel and for all tunnels being offline.