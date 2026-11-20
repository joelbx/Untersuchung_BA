# Checkpoint

Implemented peer address propagation on upstream inventory streams, configurable in-memory pipe peer addresses, and SSH heartbeat host rewriting before `UpsertNode`. The heartbeat's original port is preserved. Added focused tests for pipe options and wildcard/local/routable heartbeat addresses.

## Checks

- `gofmt -w api/client/inventory.go api/client/inventory_test.go lib/inventory/controller.go lib/inventory/controller_test.go` — passed.
- `git diff --check` — passed.
- `GOPROXY=off GOSUMDB=off go test ./lib/inventory` (from `/app`) — passed.
- `GOPROXY=off GOSUMDB=off go test github.com/gravitational/teleport/api/client -run '^TestInventoryControlStreamPipe' -count=1` (from `/app`) — passed.
- `go test ./lib/inventory ./api/client` (from `/app`) — failed: `main module (github.com/gravitational/teleport) does not contain package github.com/gravitational/teleport/api/client`; the API is a separate module.
- `GOPROXY=off GOSUMDB=off go test ./client` (from `/app/api`) — failed: `go: github.com/gogo/protobuf@v1.3.2: module lookup disabled by GOPROXY=off`. API client focused tests were instead run via the main module.
- `GOPROXY=off GOSUMDB=off go test github.com/gravitational/teleport/api/client` (from `/app`) — failed in `TestSetOIDCRedirectURLBackwardsCompatibility` after a 30.03s timeout: `all connection methods failed`, `failed to connect to addr [::]:41771 as an auth server`, `context deadline exceeded`. The command was interrupted after this failure. The rest of the full API client suite is unverified.
