Task: Add configurable tracing sampling ratio and propagators.
Status: Implemented in config and runtime. Added schema and regression tests. Relevant package tests pass offline.
Delegation: None.
Validation: GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/tracing ./internal/cmd; git diff --check.
