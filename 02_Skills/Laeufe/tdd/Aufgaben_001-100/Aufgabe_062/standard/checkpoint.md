# Checkpoint

Task: restore terminal state on canceled or exiting password reads in `lib/utils/prompt`.

Implemented: `maybeRestoreTerm` restores only for active password state with saved terminal state and propagates errors. Context cancellation restores and leaves an ongoing password read reclaimable as a clean read. `Close` restores before closing. `NotifyExit` closes the global stdin reader, and `tsh` invokes it after `Run` returns.

TDD: added regression tests first. Initial run failed for missing restoration on cancellation, deadline, and close; the `NotifyExit` test initially failed to compile because the function was absent. After implementation, `GOPROXY=off GOSUMDB=off go test ./lib/utils/prompt -count=1 -timeout=30s` passed. `GOPROXY=off GOSUMDB=off timeout 120s go test ./tool/tsh -run '^$' -count=1` passed (build check; no tests selected). `git diff --check` passed.

Incomplete checks:
- `GOPROXY=off GOSUMDB=off go test ./...` ran for about six minutes and was manually interrupted while compiling and running unrelated packages. Exact observed errors were `go build github.com/gravitational/teleport/lib/srv/db.test: /usr/local/go/pkg/tool/linux_amd64/compile: signal: interrupt` and `go build github.com/gravitational/teleport/lib/service: /usr/local/go/pkg/tool/linux_amd64/compile: signal: interrupt`; several links and vet also reported `signal: interrupt`. The full suite result is unknown.
- `GOPROXY=off GOSUMDB=off go test -race ./lib/utils/prompt -count=1 -timeout=30s` was manually interrupted during dependency compilation (exit 130); race result is unknown.
