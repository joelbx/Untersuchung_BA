# Checkpoint

Task: restore terminal state after abandoned password reads and at `tsh` exit.
Status: complete.
Changes: `ContextReader` restores terminal state on password cancellation and close, transitions canceled reads to clean state, and exposes restoration errors. Added `prompt.NotifyExit` and called it after `Run` in `tsh` main. Added tests for cancellation, deadline, close, restoration error, and global stdin shutdown.
Verification: `go test ./lib/utils/prompt`, `go test -race ./lib/utils/prompt`, `go test ./tool/tsh -run '^$'` with GOPROXY=off/GOSUMDB=off; `git diff --check` passed.
