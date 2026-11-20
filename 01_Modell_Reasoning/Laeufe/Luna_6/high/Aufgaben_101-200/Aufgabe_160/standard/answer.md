Implemented peer address propagation and wildcard address correction.

- Added `PeerAddr()` and configurable `ICSPipePeerAddr` support in [inventory.go](/app/api/client/inventory.go).
- SSH heartbeats now use the stream peer host for local or wildcard addresses while preserving the heartbeat port, before `UpsertNode`, in [controller.go](/app/lib/inventory/controller.go).
- Added coverage for peer reporting and converting `[::]:3022` to the peer host with port `3022`.

`go test ./lib/inventory` passed, and `git diff --check` passed. The API client tests could not run because `github.com/gogo/protobuf@v1.3.2` is missing from the local cache and module lookup is disabled.