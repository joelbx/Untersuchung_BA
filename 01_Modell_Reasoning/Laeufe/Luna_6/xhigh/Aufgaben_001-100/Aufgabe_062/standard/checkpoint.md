# Checkpoint

Task: fix `ContextReader` terminal restoration around canceled/closed password reads and expose `NotifyExit` for the global stdin reader.

Implemented:
- Added `maybeRestoreTerm`, which restores only while in password mode with a saved terminal state and returns restoration errors.
- Restore terminal state and transition out of password mode when a read is abandoned; context expiration returns no value and preserves the context error.
- `Close` attempts restoration before marking the reader closed and returns restoration errors.
- Added `NotifyExit` to close the global stdin reader when it supports `Close()`.

Verification: `go test ./lib/utils/prompt` passes.

Repository tooling: `rg` is unavailable; used `find`, `grep`, and direct file reads.
