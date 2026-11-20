Task: extract tracing resource, provider, and exporter construction from internal/cmd/grpc.go into internal/tracing.
Status: complete. Server uses tracing.NewProvider and tracing.GetExporter; provider and exporter shutdowns are registered. Exporter creation is independent per call. Added focused tracing tests and updated existing gRPC exporter tests.
Verification: go test ./internal/tracing ./internal/cmd (passed).
