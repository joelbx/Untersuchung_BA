Moved tracing setup into [internal/tracing/tracing.go](/app/internal/tracing/tracing.go). It now builds the environment-aware resource and always-sampling provider, and creates Jaeger, Zipkin, or OTLP exporters with endpoint validation, headers, and idempotent shutdown.

Updated [internal/cmd/grpc.go](/app/internal/cmd/grpc.go) to use those constructors and register their shutdown functions. Added isolated tracing tests and a gRPC shutdown test with tracing enabled.

Verification passed: `GOPROXY=off go test ./internal/tracing ./internal/cmd` and `git diff --check`.