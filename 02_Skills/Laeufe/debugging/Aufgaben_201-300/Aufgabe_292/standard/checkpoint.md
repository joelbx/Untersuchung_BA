# Checkpoint

Investigating polling lifecycle in `internal/storage/fs` using the assigned systematic debugging process. Initial search found `rg` unavailable; using local `find` and `grep` instead. No repository files changed yet.

Root cause: five constructors start `go NewPoller(...).Poll(ctx, update)` and discard the poller. `Poller` accepts an external context and has no cancellation or completion tracking, so a store cannot stop or join its worker. Git with an immutable hash deliberately does not start polling. The existing `SnapshotStore` interface only exposes `View` and `String`; this change will add methods to concrete implementations without introducing an interface.

Hypothesis: keeping an owned poller on each store and having `Close` cancel and join its worker will prevent post-close updates. Added `TestPollerCloseWaitsForUpdate` as a pre-fix reproduction. `GOPROXY=off go test ./internal/storage/fs -run TestPollerCloseWaitsForUpdate -count=1` is in progress.

The pre-fix test failed to compile for the expected missing API (`NewPoller` parameters, parameterless `Poll`, and `Close`). Implemented an owned context, cancellation, completion channel, and idempotent `Poll`/`Close` in `Poller`. Each of the five concrete stores now retains its poller and exposes `Close`, with a nil-poller no-op for immutable Git hashes and unstarted stores. Running `GOPROXY=off go test ./internal/storage/fs/... -count=1`.

Verification complete: `GOPROXY=off go test ./internal/storage/fs/... -count=1` passed for all filesystem storage packages; `GOPROXY=off go test -race ./internal/storage/fs ./internal/storage/fs/local -run 'TestPollerCloseWaitsForUpdate|Test_Store_Close|Test_Store$' -count=1` passed. `git diff --check` passed. Backend tests that require external Git, S3, or Azure services retain their existing environment-based skip behavior; no external services were used. Backend test helpers now register `Close` cleanup so workers finish before test completion.
