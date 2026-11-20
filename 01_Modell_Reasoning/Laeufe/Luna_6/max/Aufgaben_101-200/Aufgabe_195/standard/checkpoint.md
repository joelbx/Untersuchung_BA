# Checkpoint

Task: Refactor configuration loading so `Load(path)` returns `(*Result, error)`, with `Config` and `Warnings` separately exposed; emit deprecation warnings only for explicitly supplied deprecated keys, including `ui.enabled`.

Completed: Added `Result`, removed warnings from `Config`, collect deprecations via config-file presence before defaults, added the UI warning, updated the CLI to retain/log returned warnings, and updated config loader assertions.

Verification: `go test ./internal/config` passed. `go test ./cmd/flipt` passed (no test files; package compiled). `git diff --check` passed.
