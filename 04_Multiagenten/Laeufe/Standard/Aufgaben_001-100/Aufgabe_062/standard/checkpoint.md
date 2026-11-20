# Checkpoint

Implemented terminal restoration for canceled and closed password reads, the global `NotifyExit` hook, and its `tsh` exit call. Regression tests cover cancellation, deadline expiry, reclaiming reads, exit cleanup, and restore guards/errors. `go test ./lib/utils/prompt` and `git diff --check` pass. A `tsh` compile-only test was stopped after extended dependency compilation; it produced no diagnostic.
