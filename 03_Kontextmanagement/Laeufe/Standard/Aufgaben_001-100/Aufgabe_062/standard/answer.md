Updated `ContextReader` to restore terminal state when a password read is canceled or the reader closes, and to leave an abandoned read in a clean state. Added `NotifyExit` and called it when `tsh` exits.

Verified with `go test ./lib/utils/prompt`, a `tsh` test build, and `git diff --check`.