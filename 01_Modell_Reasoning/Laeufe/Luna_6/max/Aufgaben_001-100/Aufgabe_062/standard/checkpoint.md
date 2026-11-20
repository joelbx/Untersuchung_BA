# Checkpoint

Task: Fix terminal restoration for password-mode `ContextReader`, add the public `prompt.NotifyExit`, and invoke it when the `tsh` CLI run ends.

Implemented:
- Added `maybeRestoreTerm`, guarded by password state and a saved terminal state; used it for abandoned reads, interrupted password reads, clean-read transitions, and reader close.
- Reset an abandoned password read to clean state and preserve context cancellation/deadline errors.
- Added `NotifyExit` to close the global stdin reader and log close failures.
- Call `NotifyExit` after `tsh` command execution and before exit handling.

Validation:
- `go test ./lib/utils/prompt` passes.
- `go test ./tool/tsh` fails in unrelated `TestExportingTraces`: its test exporter connection to `grpc://0.0.0.0:33177` times out, then tracing scope assertions fail.
- `git diff --check` passes.
