# Checkpoint

Investigating namespace authorization and listing. Will add failing tests before production changes, then run relevant and full test suites. `rg` is unavailable; using local `find` and `grep`.

`go test ./...` encountered `internal/cache/redis.TestSet`: `panic: rootless Docker not found` while testcontainers tried to start Redis. This environment cannot run that integration test. Awaiting full suite output for any other failures. Focused authorization/server suite passed before final duplicate-count change; `go test ./internal/server -run 'TestListNamespaces_' -count=1` passed after it.
`go test ./...` also failed `internal/gitfs.Test_FS_Submodule`: `Get "https://github.com/flipt-io/flipt-gitops-test.git/info/refs?service=git-upload-pack": Forbidden`. External research/network access is blocked, so this integration test cannot complete here. Awaiting remaining suite output.
Full `go test ./...` completed with exit code 1. Only failing packages observed: `internal/cache/redis` (rootless Docker absent) and `internal/gitfs` (external Git request Forbidden). All other reported packages passed, including changed authz and server packages. Final focused command `go test ./internal/server/authz/... ./internal/server -count=1` passed.
