Fixed the resource attribute order so the supplied Flipt version wins over `OTEL_RESOURCE_ATTRIBUTES`, while `OTEL_SERVICE_NAME` can still override the default service name. The resource test now covers the version override.

The reviewer’s exact command passed: `GOPROXY=off GOSUMDB=off go test ./internal/tracing ./internal/cmd`.