# Tracing extraction checkpoint

- Task: move tracing provider and exporter initialization from the gRPC server into `internal/tracing` and retain orderly shutdown.
- Current state: provider and exporter construction moved to `internal/tracing`; gRPC now calls the new package and registers exporter and provider shutdown. Exporter tests run in isolation and cover supported schemes, environment attributes, repeated calls, invalid endpoints, and HTTP headers.
- Verification: `GOPROXY=off go test ./internal/tracing ./internal/cmd` passed; `git diff --check` passed.
