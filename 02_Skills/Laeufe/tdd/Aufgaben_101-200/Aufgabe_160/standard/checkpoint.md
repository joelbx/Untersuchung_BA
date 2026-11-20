# Checkpoint

Task: Fix Direct Dial SSH node heartbeats that advertise a wildcard address.

Plan: Add a failing stream peer-address test and a failing heartbeat rewrite test; implement the smallest changes; run focused and broader existing Go tests. External research and downloads are unavailable.

Initial state: working tree clean. `rg` is unavailable in this environment, so local searches use `grep` and `find`.

Red checks:
- `/app`: `GOPROXY=off GOSUMDB=off go test ./api/client -run '^TestInventoryControlStreamPipePeerAddr$' -count=1` failed because `api` is a nested module (`main module ... does not contain package .../api/client`).
- `/app/api`: `GOPROXY=off GOSUMDB=off go test ./client -run '^TestInventoryControlStreamPipePeerAddr$' -count=1` could not compile: `github.com/gogo/protobuf@v1.3.2: module lookup disabled by GOPROXY=off`. Its behavioral red result remains unobserved.
- `/app`: `GOPROXY=off GOSUMDB=off go test ./lib/inventory -run '^TestSSHHeartbeatUsesPeerHostForLocalAddress$' -count=1` fails to compile because `ICSPipePeerAddr` and the pipe option are missing; this is the expected missing-interface failure.

Green checks:
- `/app`: `GOPROXY=off GOSUMDB=off go test ./lib/inventory -run '^TestSSHHeartbeatUsesPeerHostForLocalAddress$' -count=1` passed.
- `/app`: `GOPROXY=off GOSUMDB=off go test ./lib/inventory -count=1` passed.
- `/app`: `GOPROXY=off GOSUMDB=off go test github.com/gravitational/teleport/api/client -run '^TestInventoryControlStreamPipePeerAddr$' -count=1` passed. Testing the nested API package via the root module uses its cached dependency graph.
- `git diff --check` passed.

Other checks:
- `/app/api`: `GOPROXY=off GOSUMDB=off go test ./client -count=1` blocked by `go: github.com/gogo/protobuf@v1.3.2: module lookup disabled by GOPROXY=off`. The API test and full client package suite remain unverified.
- `/app`: `GOPROXY=off GOSUMDB=off go test ./...` reported `github.com/flynn/hid ... fatal error: linux/hidraw.h: No such file or directory` and `github.com/mattn/go-sqlite3 ... pread64/pwrite64/off64_t` compilation errors. The run was interrupted after these unrelated native build failures, so the entire root suite did not complete.
- `/app`: `GOPROXY=off GOSUMDB=off go test github.com/gravitational/teleport/api/client -count=1` produced no result during the available run time and was interrupted; the full API client suite remains unverified.
