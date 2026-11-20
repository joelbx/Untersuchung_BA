Task: extract tracing provider and exporter setup from internal/cmd/grpc.go into internal/tracing.
Status: complete.
Changes: provider/resource and exporter helpers in internal/tracing; gRPC lifecycle calls helpers and shuts down provider before exporters; isolated tests cover resource attributes, sampling, exporter types, repeat calls, malformed endpoints, and OTLP HTTP headers.
Verification: GOPROXY=off go test ./internal/tracing ./internal/cmd -run 'Test(Resource|NewProvider|GetExporter|OTLPHTTPHeaders|NewGRPCServer)$' -count=1 (pass); git diff --check (pass).
Constraints: local code/tests only; git history and index baseline untouched.
