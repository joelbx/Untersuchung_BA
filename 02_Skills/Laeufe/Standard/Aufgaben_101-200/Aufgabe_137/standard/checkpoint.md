# Checkpoint

Implemented trace sampling ratio and propagator configuration in `internal/config/tracing.go`, `internal/config/config.go`, and the JSON schema. The gRPC tracing setup now applies the configured ratio and propagators. Added configuration and tracing tests.

Verification:
- `gofmt -w internal/config/tracing.go internal/config/config.go internal/config/tracing_test.go internal/tracing/tracing.go internal/cmd/grpc.go` — passed.
- `gofmt -w internal/tracing/tracing.go internal/tracing/tracing_test.go && git diff --check && python3 -m json.tool config/flipt.schema.json >/dev/null && test -z "$(gofmt -l internal/config/tracing.go internal/config/config.go internal/config/tracing_test.go internal/tracing/tracing.go internal/tracing/tracing_test.go internal/cmd/grpc.go)"` — passed before the final import alias fix; final formatting and diff check still pending.
- `GOPROXY=off GOSUMDB=off go test -mod=mod ./internal/config ./internal/tracing ./internal/cmd` — failed before compilation: `go: -mod may only be set to readonly or vendor when in workspace mode, but it is set to "mod"`.
- `GOWORK=off GOPROXY=off GOSUMDB=off go test -mod=mod ./internal/config ./internal/tracing ./internal/cmd` — failed before compilation because required modules are absent from the local cache; for example `/go/pkg/mod/github.com/segmentio/asm@v1.2.0/cpu/arm/arm.go:5:2: module lookup disabled by GOPROXY=off`. The command also reported missing `golang.org/x/sync`, `golang.org/x/net`, `golang.org/x/crypto`, and `golang.org/x/sys`. Tests remain unverified. No dependencies were downloaded.

`rg` is unavailable (`/bin/bash: rg: command not found`); fallback local search was used.
- Final `gofmt`, `git diff --check`, JSON syntax, and `gofmt -l` checks — passed after the import alias fix.
