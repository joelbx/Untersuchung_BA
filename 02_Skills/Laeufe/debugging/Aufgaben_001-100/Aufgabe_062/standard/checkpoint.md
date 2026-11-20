# Debugging checkpoint

Task: restore terminal state when `ContextReader` leaves password mode, and close the global reader on `NotifyExit`.

Status: investigating local implementation and tests. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep`.

Root cause: `firePasswordRead` saves the terminal state and starts `term.ReadPassword`, but `waitForRead` returns on context cancellation without restoring it. `Close` marks the reader closed without restoring. `fireCleanRead` only restores on a later clean read. Thus Ctrl-C or exit during a password prompt leaves echo and line mode disabled. A completed password read clears the saved state; an exit hook is needed for any still active global reader.

Pattern: the existing clean-read path calls `term.Restore` under `cr.mu`; the saved state is cleared when the background password read completes. A canceled password read remains blocked in the background, and subsequent reads reclaim that result.

Hypothesis: restore on canceled waits and on close, transition canceled password reads to clean state, and close global stdin on program exit. A blocked read can then finish and be reclaimed without keeping the terminal in password mode.

Reproduction: added regression tests for cancellation, deadline, and close. Before the patch, `GOTOOLCHAIN=local GOPROXY=off go test ./lib/utils/prompt -run 'TestContextReader_(CanceledPasswordRestoresTerminal|PasswordDeadlineRestoresTerminal|CloseRestoresPasswordTerminal)' -count=1` failed because `restoreCalled` was false in all three cases. A `NotifyExit` test failed to compile (`undefined: NotifyExit`) before its implementation.

Fix: `maybeRestoreTerm` now restores only a password state with a saved terminal state and moves the reader to clean state. Canceled waits and `Close` call it; `Close` returns restoration errors. `NotifyExit` closes the global stdin reader and `tsh` calls it after `Run`, before its exit handling.

Verification: `GOTOOLCHAIN=local GOPROXY=off go test ./lib/utils/prompt -count=1` passed after the fix and after adding an error propagation test. `git diff --check` passed. Race and `tsh` build checks are in progress.

The prompt race check `GOTOOLCHAIN=local GOPROXY=off go test ./lib/utils/prompt -race -count=1` passed (exit 0). The `tsh` build check is still compiling.

Final verification: reran the prompt race check after adding the restoration error test; it passed. `GOTOOLCHAIN=local GOPROXY=off go test ./tool/tsh -run '^$' -count=1` passed (build check; no tests selected). Final `git diff --check` passed. No downloads were used.
