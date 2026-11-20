# Checkpoint

Task: improve HA database service selection, retries, display deduplication, and test controls.

Status: code and tests edited; verification in progress. `rg` is unavailable; using `find` and `grep` locally.

Initial test command `GOPROXY=off go test ./api/types ./lib/srv/db ./tool/tsh ./lib/reversetunnel` from `/app` failed: `main module (github.com/gravitational/teleport) does not contain package github.com/gravitational/teleport/api/types`. The API is a separate module.

Initial `GOPROXY=off go test ./types` from `/app/api` failed because the new test imported uncached `github.com/stretchr/testify`: `module lookup disabled by GOPROXY=off`. The new test now uses the standard library.

Final verification:
- `GOPROXY=off go test -count=1 ./types` from `/app/api`: passed.
- `GOPROXY=off go test -count=1 ./lib/srv/db ./tool/tsh ./lib/reversetunnel` from `/app`: passed.
- `git diff --check` from `/app`: passed.

Verification pending.
