Fixed the auth service crash when multiple audit event backends are configured. `MultiLog` now validates and fans out through emitters, and `stdout://` uses the new `WriterEmitter` to write newline-delimited JSON events.

Added coverage for event fanout, invalid backends, and file plus stdout configuration. `go test ./lib/events ./lib/service` and `git diff --check` passed.