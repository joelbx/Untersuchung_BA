VERDICT: FIX
Code defect: internal/tracing/tracing.go:25-29 merges OTEL_RESOURCE_ATTRIBUTES after service.version; OTEL_RESOURCE_ATTRIBUTES=service.version=other overrides fliptVersion, contrary to required service.version=<fliptVersion>. Move the version attribute after WithFromEnv while retaining environment precedence for service.name, and cover this case in the existing resource test.
Tests: GOPROXY=off GOSUMDB=off go test ./internal/tracing ./internal/cmd — PASS (both packages).
TEST_ENVIRONMENT_PROBLEM: none.
