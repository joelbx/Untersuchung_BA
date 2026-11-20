Implemented peer address propagation and wildcard address rewriting.

- Added `PeerAddr()` to `UpstreamInventoryControlStream`; real streams read the gRPC peer address, and pipe streams accept `ICSPipePeerAddr(...)`.
- SSH heartbeats with wildcard hosts now use the peer host while preserving the heartbeat’s port.
- Added focused assertions for pipe peer reporting and the rewritten node address.

`go test ./lib/inventory` passes. The API client tests could not run because required modules are unavailable with `GOPROXY=off`. `git diff --check` passes.