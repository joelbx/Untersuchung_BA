# Checkpoint

Task: Fix Direct Dial node address reporting by carrying the control stream's TCP peer address into SSH heartbeat processing and substituting the peer host for wildcard addresses while preserving the heartbeat port.

Completed:
- Added `PeerAddr() string` to `UpstreamInventoryControlStream`.
- Added `ICSPipeOption`, `ICSPipePeerAddr`, and variadic pipe options.
- Captured the gRPC stream peer address in `NewUpstreamInventoryControlStream`.
- Rewrote local/wildcard SSH heartbeat addresses using the peer address before `UpsertNode`.
- Added assertions for pipe peer reporting and conversion of `[::]:3022` to the peer host while retaining port `3022`.

Verification:
- `go test ./lib/inventory` passed.
- `go test ./client` from `api/` could not run because `github.com/gogo/protobuf@v1.3.2` is not cached and `GOPROXY=off` disables module lookup.
- `git diff --check` passed.
