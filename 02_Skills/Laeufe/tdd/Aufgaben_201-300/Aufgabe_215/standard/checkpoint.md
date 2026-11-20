# Checkpoint

Task: add HTTPS configuration and serving in /app using test-driven development.

Completed: added `Scheme`, configuration keys/defaults and validation; switched REST/UI and gRPC transports to TLS for HTTPS; preserved HTTP behavior; updated configuration examples and docs. Added tests and local TLS fixtures. A `.gitignore` exception makes new files under `cmd/flipt` visible to the coordinator.

Red checks observed: initial configuration test run failed to compile on absent `configure(path)`, Scheme and TLS fields; transport tests failed to compile on absent transport functions; independent CORS origins test failed with `[ * ]` default (actual output `[*]`) before the fix.

Green checks: `GOPROXY=off go test ./cmd/flipt -count=1`, `GOPROXY=off go test ./...`, and `git diff --check` all completed successfully. The Go build emits a warning from the existing sqlite3 C dependency (`sqlite3-binding.c:125322`, function may return address of local variable). No tests failed in the final suite.
