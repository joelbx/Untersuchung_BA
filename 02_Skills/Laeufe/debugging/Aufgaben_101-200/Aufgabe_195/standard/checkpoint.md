# Checkpoint

Task: separate configuration warnings from Config through Load Result; warn on explicit deprecated keys including ui.enabled.

Status: investigating repository loader, callers, and tests. Initial search tool `rg` unavailable (`/bin/bash: rg: command not found`); using find/grep.

Root cause: `Config.prepare` sets defaults before evaluating deprecators; deprecators use `GetBool`/`IsSet`, so they cannot distinguish file presence reliably. `ui.enabled` has no deprecator. `Load` returns `*Config`, so warnings live in configuration and the CLI reads them there. Working pattern: cache/database implement `deprecations(v)` and `deprecation.String()` supplies the established message format. Hypothesis: evaluate deprecations against `v.InConfig` before defaults, collect them on a new `Result`, then prepare/unmarshal configuration. Added focused failing reproduction for explicit `ui.enabled: false` and `cache.memory.enabled: false`.

Implemented: `Load(path) (*Result, error)` with `Result.Config` and `Result.Warnings`; warnings collected from file keys before defaults; cache/database detection uses `InConfig`; UI deprecation added; CLI logs result warnings after configuring logger. `Config.Warnings` removed.

Verification: focused reproduction failed before patch for explicit `ui.enabled: false` and `cache.memory.enabled: false` as expected. Initial combined test run failed because an existing fixture explicitly has `cache.memory.enabled: false`; updated its warning expectation. Final `GOPROXY=off go test ./internal/config ./cmd/flipt -count=1` passed (cmd package has no tests). `git diff --check` passed. No downloads used.
