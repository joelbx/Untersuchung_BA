Task complete: extracted tracing resource/provider/exporter construction to internal/tracing/tracing.go and wired gRPC startup/shutdown to the new package. Added isolated tracing tests for resource env attributes, sampling, exporter variants/repeated calls, endpoint errors, and OTLP HTTP headers/path. Removed obsolete cmd exporter test.
Verification: GOTOOLCHAIN=local GOPROXY=off GOMAXPROCS=2 go test -p 1 ./internal/tracing ./internal/cmd (pass); git diff --check (pass).
Delegation: none.
