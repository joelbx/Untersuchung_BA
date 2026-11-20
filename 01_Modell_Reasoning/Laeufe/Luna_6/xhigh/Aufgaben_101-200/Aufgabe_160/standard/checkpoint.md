# Checkpoint

Task: Resolve the Direct Dial wildcard node address issue in `/app`.

Requirements identified:
- Add `PeerAddr() string` to `UpstreamInventoryControlStream`.
- Add variadic `ICSPipeOption` configuration to `InventoryControlStreamPipe`, including `ICSPipePeerAddr`.
- In SSH heartbeat handling, replace a wildcard host with the control stream peer host while retaining the heartbeat port, and use the result for `UpsertNode`.

Initial state: repository is checked out at `/app`; `git status --short --branch` reports a clean worktree on detached `HEAD`. `rg` is unavailable in this environment, so repository searches will use `find` and standard shell tools.

Implementation completed:
- Added peer address storage to both gRPC-backed and in-memory upstream streams; the pipe accepts `ICSPipeOption` and `ICSPipePeerAddr`.
- SSH heartbeats now replace localhost/unspecified hosts with the control stream peer host through `utils.ReplaceLocalhost`, which retains the heartbeat port.
- Added tests for the pipe option and IPv6/IPv4 wildcard, routable, and empty-peer heartbeat addresses.

Verification:
- `GOPROXY=off go test ./lib/inventory` passed.
- `GOPROXY=off go test github.com/gravitational/teleport/api/client -run '^TestInventoryControlStreamPipe' -count=1` passed.
- `git diff --check` passed.
- The nested API module test command could not resolve uncached `github.com/gogo/protobuf@v1.3.2` with downloads disabled; the focused client tests passed through the root module.
