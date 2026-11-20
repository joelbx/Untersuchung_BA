# Checkpoint

Implemented terminal restoration after abandoned password reads and during `ContextReader.Close`, added `prompt.NotifyExit`, and wired the `tsh` exit path. Added tests for cancellation, deadline expiration, subsequent clean reads, close, singleton exit, and restoration errors.

Checks:
- `GOPROXY=off GOSUMDB=off go test ./lib/utils/prompt` passed.
- `GOPROXY=off GOSUMDB=off go test -race ./lib/utils/prompt` passed.
- `git diff --check` passed.
- `GOPROXY=off GOSUMDB=off go test ./tool/tsh -run '^$'` was interrupted after more than three minutes in a C compiler step (exit code 130, no diagnostic output). The `tsh` package compile remains unverified.

`rg` is unavailable; local grep/find used instead. No external research or dependency download used.
