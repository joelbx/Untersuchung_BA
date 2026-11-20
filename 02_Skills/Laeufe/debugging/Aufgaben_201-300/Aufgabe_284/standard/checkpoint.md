# Checkpoint

Task: replace the reverse tunnel server's local site slice with one instance and reuse the proxy access point/cache.

Investigation in progress. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep` and `find`.

## Investigation
- `NewServer` creates one local site, then appends it to `localSites`; no other constructor call exists in production.
- `newlocalSite` calls `srv.newAccessPoint`, creating the redundant cache. `Config.LocalAccessPoint` already provides the proxy cache.
- `findLocalCluster` searches the slice during service registration; no local site is ever added after initialization. `onSiteTunnelClose` can remove it from the slice, leaving no local site.
- `auth.ProxyAccessPoint` contains the methods of `auth.RemoteProxyAccessPoint`, so the existing proxy access point can serve local-site reads.

## Hypothesis
A single `server.localSite` wired to `server.LocalAccessPoint`, with certificate cluster validation at service registration, removes the redundant cache while keeping local routing behavior.

## Resolution
- Replaced the local-site slice with one `localSite` and routed service registration, site lookup, reconnect notices, closure handling, and proxy fan-out through it.
- `newlocalSite` now uses `server.localAuthClient`, `server.LocalAccessPoint`, and `server.PeerClient`; it does not create a secondary resource cache. The separate host-certificate cache remains for forwarding certificates.
- Added certificate cluster-name validation for local service connections.

## Verification
- Before patch: `GOPROXY=off GOSUMDB=off go test ./lib/reversetunnel -run 'TestLocalSiteOverlap|TestRequireLocalAgentForConn' -count=1` failed to compile as expected: old `newlocalSite` signature, missing `localSite` field, missing `requireLocalAgentForConn` method.
- After patch: `GOPROXY=off GOSUMDB=off go test ./lib/reversetunnel -count=1` passed.
- `git diff --check` passed.
