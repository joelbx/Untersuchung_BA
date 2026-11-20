# Checkpoint

Task: Extract tracing resource, provider, and exporter setup from gRPC startup into `internal/tracing`, preserve shutdown sequencing, and run relevant local tests.

Status: complete. Added `internal/tracing/tracing.go` and isolated tests; gRPC startup now calls `tracing.NewProvider` and `tracing.GetExporter`, and retains provider/exporter shutdown registration. Removed the shared exporter `sync.Once` state and moved exporter tests out of `internal/cmd`.

Verification: `GOPROXY=off GOSUMDB=off go test ./internal/tracing ./internal/cmd` passed. `git diff --check` passed. Tests cover resource defaults and environment overrides, version, root span sampling, all exporter schemes, invalid endpoints, repeated initialization, and HTTP headers/path.
