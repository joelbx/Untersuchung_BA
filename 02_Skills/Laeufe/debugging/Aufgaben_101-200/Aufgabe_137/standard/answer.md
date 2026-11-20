Tracing configuration now supports a sampling ratio from 0 to 1 and the eight supported propagators. Defaults and exact validation errors are in place, and the tracing provider and gRPC setup use the configured values. The CUE and JSON schemas were updated too.

All relevant tests passed: `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/tracing ./internal/cmd ./config -count=1`.