VERDICT: FIX

[internal/tracing/tracing.go](/app/internal/tracing/tracing.go:25) applies environment attributes after `service.version`. Setting `OTEL_RESOURCE_ATTRIBUTES=service.version=other` can therefore replace the required `fliptVersion`. Apply the version attribute after the environment attributes, while preserving environment overrides for `service.name`, and cover this case in the existing resource test.

Tests: `GOPROXY=off GOSUMDB=off go test ./internal/tracing ./internal/cmd` — both packages passed. No test environment problem. This was an independent review; I did not change project code.