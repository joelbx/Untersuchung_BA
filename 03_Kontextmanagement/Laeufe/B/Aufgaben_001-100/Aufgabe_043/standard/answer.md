Resolved the tracing coupling. Provider and exporter setup now live in [internal/tracing/tracing.go](/app/internal/tracing/tracing.go), and [gRPC startup](/app/internal/cmd/grpc.go) uses them and registers their shutdown functions.

The tracing and gRPC package tests passed with network access disabled; `git diff --check` also passed.