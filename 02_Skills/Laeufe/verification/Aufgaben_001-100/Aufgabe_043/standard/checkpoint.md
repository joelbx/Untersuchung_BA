# Checkpoint

- Task: extract tracing resource, provider, and exporter setup from `internal/cmd/grpc.go` into `internal/tracing`, then verify with local Go tests.
- Initial inspection: `rg` is unavailable (`/bin/bash: rg: command not found`); using `grep` and `find`.
- Added `internal/tracing/tracing.go` with resource, provider, and per-call exporter construction. Updated `internal/cmd/grpc.go` to use it and moved exporter tests to `internal/tracing` with environment, sampling, endpoint, header, and repeat-call checks.
- Initial `GOPROXY=off GOSUMDB=off go test ./internal/tracing ./internal/cmd` failed: `go vet` rejected a `%v` format for a function value in `tracing_test.go:91`. Corrected the format; this was a test-only issue.
- Final `GOPROXY=off GOSUMDB=off go test ./internal/tracing ./internal/cmd`: exit 0 (`internal/tracing` and `internal/cmd` both `ok`). `git diff --check`: exit 0.
