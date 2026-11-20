Updated `ContextReader` to restore terminal state when a password read is canceled or times out, and before closing during password mode. Added `NotifyExit` and called it from `tsh` after `Run` returns.

The prompt package tests and race check pass. The `tsh` compile check remains unverified: it was interrupted after more than three minutes in a C compiler step.