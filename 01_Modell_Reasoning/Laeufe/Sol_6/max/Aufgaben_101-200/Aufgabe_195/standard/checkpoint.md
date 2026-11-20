# Configuration refactor checkpoint

- Task: return configuration and load warnings separately through `Result`; warn for explicitly configured deprecated keys, including `ui.enabled`.
- Status: complete. Implemented `Result`, moved warnings out of `Config`, and made the CLI log `Result.Warnings`. Deprecations are checked against keys present in the file before defaults. Added `ui.enabled` to the deprecation notices and updated tests for explicit keys, including `false` values and environment-only values.
- Verification: `GOTOOLCHAIN=local GOPROXY=off go test ./internal/config ./internal/cmd ./cmd/flipt` passed; `git diff --check` passed.
