# Checkpoint

Implemented the configuration loader result API: `Load` returns `*Result` with separate `Config` and `Warnings` fields, and `Config` no longer contains warnings. The CLI stores and logs returned warnings independently.

Deprecation checks now run before defaults and use Viper's input-file presence checks. Explicit deprecated cache keys and migration paths produce warnings; `ui.enabled` now produces a deprecation warning. Tests cover warnings on file keys and confirm environment values/defaults do not produce file deprecation warnings.

Verification passed: `go test ./internal/config ./cmd/flipt`; `git diff --check`.
