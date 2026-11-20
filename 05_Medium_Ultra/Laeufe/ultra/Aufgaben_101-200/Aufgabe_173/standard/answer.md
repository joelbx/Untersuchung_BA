Implemented HA database failover in [proxyserver.go](/app/lib/srv/db/proxyserver.go). The proxy keeps all matching services, shuffles them with a clock-seeded default or an injected `Shuffle` hook, and tries the next candidate when a tunnel reports a connection problem. It returns a clear error if none can be reached.

`FakeRemoteSite` can now simulate per-server tunnel outages. Database server logs include `HostID`, and `tsh db ls` sorts by name and host ID before removing same-name duplicates.

Native subagents handled the API type, tunnel fixture, and `tsh` changes; I integrated them and added a failover test covering both recovery and the all-offline case. The full database proxy, API types, and reverse tunnel test packages passed, as did the relevant `tsh` test.