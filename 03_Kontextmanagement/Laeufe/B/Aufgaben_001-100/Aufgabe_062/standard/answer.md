Updated `ContextReader` to restore terminal settings when a password read is canceled or closed, and to leave canceled reads in a clean state. Added `NotifyExit` and called it from `tsh` before exit.

The prompt package tests pass under the race detector, and `git diff --check` is clean. The broader `tsh` compile check was stopped after a prolonged build without output.