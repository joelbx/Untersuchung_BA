# Checkpoint

Implemented terminal restoration on canceled password reads and reader close, added `NotifyExit` for the stdin singleton, and called it after `tsh` finishes. Added tests for cancellation, deadline, close, restore errors, and exit cleanup. Validation passed: `go test ./lib/utils/prompt -count=1`, `go test -race ./lib/utils/prompt -count=1`, and offline `go test ./tool/tsh -run '^$' -count=1`.
