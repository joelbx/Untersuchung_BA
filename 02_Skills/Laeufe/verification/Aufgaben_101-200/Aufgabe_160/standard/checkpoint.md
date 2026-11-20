# Checkpoint

Task: Fix Direct Dial node wildcard heartbeat address using inventory control stream peer address.

Implemented:
- Added `PeerAddr() string` to upstream inventory streams. The gRPC stream captures its peer from `stream.Context()`; the in-memory pipe accepts `ICSPipeOption` and `ICSPipePeerAddr`.
- The controller replaces a heartbeat's wildcard or loopback host with the peer host before `UpsertNode`, preserving the heartbeat port via `utils.ReplaceLocalhost`.
- Added pipe and controller address tests.

Verification:
- From `/app`, `GOPROXY=off GOSUMDB=off go test ./lib/inventory -run 'TestSSHServerHeartbeatPeerAddress|TestControllerBasics' -count=1` passed (`ok ... 1.141s`).
- From `/app`, `GOPROXY=off GOSUMDB=off go test github.com/gravitational/teleport/api/client -run 'TestInventoryControlStreamPipe' -count=1` passed (`ok ... 0.019s`).
- From `/app/api`, `GOPROXY=off GOSUMDB=off go test ./client -run 'TestInventoryControlStreamPipe' -count=1` could not start: `go: github.com/gogo/protobuf@v1.3.2: module lookup disabled by GOPROXY=off`. The root module command above successfully ran the same package tests against the local API module.
- Initial combined command run from `/app/api` had `gofmt` path errors (`stat api/client/inventory.go: no such file or directory`); `gofmt` was rerun from `/app` successfully.

Remaining: final diff/format check.
- From `/app`, `GOPROXY=off GOSUMDB=off go test ./lib/inventory github.com/gravitational/teleport/api/client -count=1`: inventory package passed (`ok ... 1.177s`); the full API client package continued without output for roughly 40 seconds and was interrupted (exit 1). It is not claimed as passing. Focused API client tests above passed.
- From `/app`, `gofmt -l api/client/inventory.go api/client/inventory_test.go lib/inventory/controller.go lib/inventory/controller_test.go` produced no output; `git diff --check` produced no output.

Final state: implementation and focused verification complete. Full API client suite status is unknown due to interruption; standalone API module cannot resolve an uncached dependency offline.
