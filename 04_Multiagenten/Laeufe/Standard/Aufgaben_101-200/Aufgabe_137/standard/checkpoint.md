Task: Add trace sampling ratio and propagator configuration.
Status: Complete. Added config defaults and validation, schema, runtime sampler and propagator selection, and tests.
Verification: GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/tracing ./internal/cmd passed; git diff --check passed.
Constraints: Local repository and existing tests only; no downloads or git history/index/harness changes.
