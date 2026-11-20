Fixed the auth service crash when multiple audit backends are configured. `MultiLog` now validates and fans out events through `MultiEmitter`, and `stdout://` uses the new `WriterEmitter` for newline-delimited JSON events.

Added focused tests for fan out, invalid loggers, and close errors. `GOPROXY=off GOSUMDB=off go test ./lib/events ./lib/service` and `git diff --check` passed.