Fixed the auth service crash for multiple audit backends. `MultiLog` now validates and fans out audit events, and `stdout://` uses the new `WriterEmitter` to write newline-delimited JSON.

Added tests for emission, close behavior, and mixed URI initialization. `go test ./lib/events ./lib/service` and `git diff --check` pass.