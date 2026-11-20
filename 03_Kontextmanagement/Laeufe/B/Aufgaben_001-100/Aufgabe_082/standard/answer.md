Resolved the auth service crash: `MultiLog` now exposes a validated `MultiEmitter`, and the `stdout://` backend uses the new `WriterEmitter`. Added tests for event output, fanout, close errors, and multiple backend initialization.

`go test ./lib/events ./lib/service` and `git diff --check` passed.