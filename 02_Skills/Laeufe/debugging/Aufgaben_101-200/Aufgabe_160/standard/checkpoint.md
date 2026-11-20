# Debugging checkpoint

Task: Fix Direct Dial node heartbeats advertising wildcard addresses.

Status: Patch implemented and relevant tests passed. `rg` is unavailable, so local searches used `grep`/`find`.

Root cause: SSH heartbeat sends the server's listener address unchanged; `Controller.handleSSHServerHB` upserts it unchanged. The gRPC upstream wrapper discards the transport peer address, and the local in-memory pipe has no peer address field. Thus a listener on `[::]:3022` is advertised as `[::]:3022`.

Pattern: `lib/utils.NetAddr.IsHostUnspecified` recognizes empty, IPv4 wildcard, and IPv6 wildcard hosts; `net.SplitHostPort` and `net.JoinHostPort` preserve the heartbeat port while substituting the host. Existing gRPC code uses `peer.FromContext`.

Hypothesis confirmed: Carrying the TCP peer address in both upstream stream implementations and replacing a wildcard or localhost heartbeat host before `UpsertNode` makes the stored address use the peer host while leaving explicit host addresses intact.

Pre-fix reproduction: `GOPROXY=off GOSUMDB=off go test ./lib/inventory -run TestSSHServerHeartbeatPeerAddress -count=1` failed to compile because `ICSPipePeerAddr` and the pipe option parameter did not exist. The independent API module command `GOPROXY=off GOSUMDB=off go test ./client -run TestInventoryControlStreamPipePeerAddr -count=1` was blocked by `go: github.com/gogo/protobuf@v1.3.2: module lookup disabled by GOPROXY=off`; the same tests later passed when invoked through the root module's cached dependencies.

Implementation: Both upstream stream variants now expose their peer address; the gRPC wrapper reads it from its context. The controller substitutes the peer host for wildcard and localhost heartbeat hosts before upsert, retaining the heartbeat port. The root module can run API tests using its local module cache.

Checks passed: `GOPROXY=off GOSUMDB=off go test github.com/gravitational/teleport/api/client -run 'TestInventoryControlStreamPipe|TestUpstreamInventoryControlStreamPeerAddr' -count=1`; `GOPROXY=off GOSUMDB=off go test ./lib/inventory -count=1`; `git diff --check`.

Additional auth package compile check `GOPROXY=off GOSUMDB=off go test ./lib/auth -run '^$'` encountered local C build errors: `linux/hidraw.h: No such file or directory` from `github.com/flynn/hid`, and missing `pread64`, `pwrite64`, `off64_t` in `github.com/mattn/go-sqlite3`. This check cannot establish auth package success in this environment.
