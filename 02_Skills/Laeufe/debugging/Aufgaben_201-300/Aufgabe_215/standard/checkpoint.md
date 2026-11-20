# Checkpoint

Investigating HTTPS configuration and serving behavior in `/app`. `rg` is unavailable, so repository inspection will use `find` and `grep`. No source changes yet.

Root cause: `configure` reads only HTTP and gRPC ports from a global Viper instance, has no scheme/certificate keys or validation, and `execute` always uses `httpServer.ListenAndServe` plus plaintext gRPC. Existing `config/default.yml` documents only HTTP settings. The existing config/info handlers already write JSON bodies and yield 200.

Implemented: per-call `configure(path)` with FLIPT environment overrides, server scheme/ports/certificate fields, exact HTTPS validation errors, and JSON scheme output. HTTPS mode now serves REST/UI via `ListenAndServeTLS` and gRPC via server credentials; the gateway verifies the configured certificate. Added advanced HTTPS YAML and local TLS fixtures, tests, and configuration documentation. HTTP remains the default.

Verification: the new tests initially failed to compile for the expected missing interfaces. `GOPROXY=off go test ./...` passes. `GOPROXY=off go build -o /tmp/flipt-https-smoke ./cmd/flipt` passes. A local process smoke check with the fixture certificate returned HTTP 200 and `{}` from `https://localhost:18444/api/v1/flags` using certificate verification, exercising both HTTPS and the TLS gRPC gateway. The compiler emits only the existing sqlite3 C warning. `git diff --check` passes.

An initial shell-based smoke check returned 200 from `/meta/info` but its cleanup waited on a process that was signaled during initial migrations; it was terminated and replaced with a bounded Python subprocess smoke check. No source change was needed for that timing issue.
