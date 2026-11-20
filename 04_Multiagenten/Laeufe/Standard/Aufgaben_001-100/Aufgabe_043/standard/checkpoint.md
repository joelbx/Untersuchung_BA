# Checkpoint

Task complete: tracing resource, provider, and exporter construction now live in `internal/tracing/tracing.go`; gRPC startup delegates to them and shuts down the provider before its exporter. Exporter construction is independent across invocations, with idempotent shutdown. Isolated tests cover resource attributes, sampling, supported and invalid endpoints, exporter selection, and repeated shutdown.

Verification: `go test ./internal/tracing ./internal/cmd -count=1` passed.
