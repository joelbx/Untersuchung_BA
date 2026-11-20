Task: Separate config loader warnings from Config via Result, add explicit-file-key deprecations including ui.enabled, update callers and tests.
Status: implementation complete; relevant tests passed.
Changes: Result{Config, Warnings}; deprecation checks before defaults with Viper InConfig; CLI logs Result.Warnings; config tests cover cache, database, UI, defaults, and env-only behavior.
Tests: go test ./internal/config ./cmd/flipt; git diff --check.
Delegation: none.
