Extracted tracing setup into [internal/tracing/tracing.go](/app/internal/tracing/tracing.go). It now builds the resource and always-on provider, creates Jaeger, Zipkin, and OTLP exporters, validates OTLP endpoints, and shares one shutdown operation between the provider and server lifecycle.

Updated [grpc.go](/app/internal/cmd/grpc.go) to use the new functions and register their shutdown callbacks. Added isolated tracing tests and enabled tracing in the gRPC server lifecycle test.

Verification passed: `go test ./internal/tracing ./internal/cmd` and `git diff --check`.