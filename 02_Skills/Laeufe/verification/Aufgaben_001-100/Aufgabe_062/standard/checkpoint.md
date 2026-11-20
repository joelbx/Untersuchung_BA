# Checkpoint

Resolved terminal restoration for canceled password reads and reader shutdown. `ContextReader.ReadPassword` restores the saved terminal state on context cancellation or deadline, clears the pending password mode, and returns an empty result with the context error. `ContextReader.Close` attempts restoration before closing and returns restoration errors. `NotifyExit` closes the global stdin reader; `tsh` calls it after `Run` and before exit handling.

Verification completed:
- `GOPROXY=off GOSUMDB=off go test ./lib/utils/prompt` — passed.
- `GOPROXY=off GOSUMDB=off go test ./tool/tsh -run '^$'` — passed (compile check; no tests selected).
- `git diff --check` — passed.

Focused tests cover cancellation, deadline expiry, a subsequent clean read, close, restoration errors, and `NotifyExit`. `rg` was unavailable (`/bin/bash: rg: command not found`); local `find` and `grep` were used.
