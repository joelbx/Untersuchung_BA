# Checkpoint

Implemented the terminal cleanup changes in `lib/utils/prompt`:

- Added `maybeRestoreTerm`, guarded by password mode and a saved terminal state, with restoration errors returned to callers.
- Restored terminal state when password reads are canceled and moved the reader to clean mode after successful restoration.
- Made `Close` attempt restoration before marking the reader closed.
- Added `NotifyExit` to close the global stdin reader.
- Password read cancellation/expiration returns an empty result and preserves the context error, including `context.DeadlineExceeded`.

Validation: `go test ./lib/utils/prompt` passed.
