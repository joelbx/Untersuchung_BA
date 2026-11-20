VERDICT: ACCEPT

The checked-out patch meets the stated tracing requirements. Defaults and validation are in [tracing.go](/app/internal/config/tracing.go) and [config.go](/app/internal/config/config.go); runtime sampling and propagator selection are wired through [tracing.go](/app/internal/tracing/tracing.go) and [grpc.go](/app/internal/cmd/grpc.go). I found no code defect requiring correction.

`GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/tracing ./internal/cmd` passed for all three packages. `git diff --check` passed. No `TEST_ENVIRONMENT_PROBLEM`.