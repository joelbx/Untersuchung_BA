# Checkpoint

Task: add tracing sampling ratio and propagator configuration, then apply it at tracing startup.

Implemented fields, defaults, exact validation errors, JSON/CUE schema entries, a ratio-based parent-aware sampler, and the selected OpenTelemetry propagators. Added test-first coverage for config defaults/loading/validation, schema acceptance, sampling at 0 and 1, and propagator selection. Updated the advanced-config expectation.

Verification:
- Config tests initially failed because fields/types were absent; schema test initially failed because new keys were rejected; runtime tests initially failed because provider did not accept a ratio and propagator constructor was absent.
- `GOPROXY=off go test ./internal/config -count=1` passed.
- `GOPROXY=off go test ./config -run 'Test_CUE|Test_JSONSchema' -count=1` passed.
- `GOPROXY=off go test ./internal/cmd ./internal/tracing ./internal/config ./config` passed.
- Final `GOPROXY=off go test ./...` failed only in `internal/cache/redis` (TestSet, TestGet, TestDelete: no Docker daemon) and `internal/gitfs` (Test_FS_Submodule: external Git URL returned Forbidden). All other packages passed; exact output is in `/tmp/flipt-go-test-final.log`.
- `GOWORK=off GOPROXY=off go test -mod=mod ./internal/tracing ./internal/cmd` failed because dependencies including `golang.org/x/sync@v0.6.0`, `golang.org/x/net@v0.23.0`, `golang.org/x/crypto@v0.21.0`, and `golang.org/x/sys@v0.18.0` are unavailable in the local cache (`module lookup disabled by GOPROXY=off`). Standalone non-workspace build remains unverified. Workspace build and tests passed.

Environment: `rg` unavailable (`/bin/bash: line 1: rg: command not found`); used `grep` and `find`.
- `git diff --check` passed.
