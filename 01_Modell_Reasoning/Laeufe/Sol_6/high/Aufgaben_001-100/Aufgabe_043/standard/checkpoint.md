# Checkpoint

Extracted resource, provider, and exporter construction into `internal/tracing`. The gRPC server now uses `tracing.NewProvider` and `tracing.GetExporter`, with both shutdown functions registered in its lifecycle. Added isolated tests for environment attributes, sampling, exporters, repeated calls, endpoint errors, and OTLP HTTP headers/path. `go test ./internal/tracing ./internal/cmd` and `git diff --check` pass.
