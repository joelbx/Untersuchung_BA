VERDICT: FIX

**Code review:** I found no defect in the applied patch. [controller.go](/app/lib/inventory/controller.go:261) rewrites wildcard heartbeat addresses before `UpsertNode`; [addr.go](/app/lib/utils/addr.go:252) preserves the heartbeat’s original port. No project code was changed during this review.

**Tests:** From `/app`, the focused API client test and both the focused and full `lib/inventory` tests passed:

- `GOTOOLCHAIN=local GOPROXY=off go test github.com/gravitational/teleport/api/client -run '^TestInventoryControlStreamPipe' -count=1`
- `GOTOOLCHAIN=local GOPROXY=off go test ./lib/inventory -run '^TestSSHServerHeartbeatAddress$' -count=1`
- `GOTOOLCHAIN=local GOPROXY=off go test ./lib/inventory -count=1`

**TEST_ENVIRONMENT_PROBLEM:** From `/app/api`, `GOTOOLCHAIN=local GOPROXY=off go test ./client -run '^TestInventoryControlStreamPipe' -count=1` could not start because `github.com/gogo/protobuf@v1.3.2` was absent from that module’s local cache. The full API client command, `GOTOOLCHAIN=local GOPROXY=off go test github.com/gravitational/teleport/api/client -count=1`, reported four mock-server connection failures to `[::]` addresses after 30-second deadlines; I interrupted it after about 100 seconds. The mock listener in [client_test.go](/app/api/client/client_test.go:95) binds with `net.Listen("tcp", "")`. Bind those fixtures to a reachable loopback address, or rerun the full suite in an environment that can connect to their wildcard addresses.

The required progress note is in [checkpoint.md](/app/.codex-role-output/checkpoint.md).