Updated `ContextReader` to restore terminal state when a password read is canceled or the reader closes, and to leave canceled reads ready for a subsequent clean read. Added `NotifyExit()` and called it from `tsh` after `Run` returns.

The prompt tests, race tests, `tsh` compile check, and `git diff --check` pass.