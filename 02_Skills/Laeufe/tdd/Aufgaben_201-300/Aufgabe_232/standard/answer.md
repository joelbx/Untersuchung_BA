Implemented the OS EOL lookup, per-target scan warnings, and ordered `Warning: ` lines in the scan summary. OS family constants and major-version parsing are centralized, with tests for the required dates, boundaries, and messages.

`GOPROXY=off go test ./...` passed. The run emitted an existing `go-sqlite3` C compiler warning.