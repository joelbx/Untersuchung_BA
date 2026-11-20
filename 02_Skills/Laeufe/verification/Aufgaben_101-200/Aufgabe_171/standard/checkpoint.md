# Checkpoint

Task: add gRPC middleware handling for `x-flipt-accept-server-version`.

Implemented: context helpers, unary metadata interceptor with a 1.0.0 fallback, server chain registration, and focused tests for present, missing, and invalid versions.

Verification: `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./internal/server/middleware/grpc ./internal/cmd` passed (both packages, exit 0). `git diff --check` passed. The test command modified `go.work.sum`; its generated change was removed.

Tooling note: `rg` is unavailable (`/bin/bash: rg: command not found`); used local grep/find fallback.
