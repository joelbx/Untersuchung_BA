# Checkpoint

Task: Fix Direct Dial node address reporting by carrying the inventory control stream peer address into SSH heartbeat handling.

Completed:
- Added `PeerAddr()` to `UpstreamInventoryControlStream` and populated it from the gRPC stream peer.
- Added `ICSPipeOption` and `ICSPipePeerAddr` for in-memory streams.
- Rewrote wildcard/local heartbeat addresses using the peer host while preserving their SSH port.
- Formatted the changed Go files.

Verification:
- `go test ./lib/inventory` passed.
- `cd api && go test ./client` could not run because `GOPROXY=off` and `github.com/gogo/protobuf@v1.3.2` is unavailable locally.
