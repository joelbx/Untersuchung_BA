# Checkpoint

Task complete: `config.Load` returns `*Result` with `Config` and `Warnings`; warnings are collected from explicitly present file keys before defaults. Added `ui.enabled` deprecation, updated CLI logging and tests.

Checks: `go test ./internal/config ./cmd/flipt` passed; `git diff --check` passed.

Tooling note: `rg` was unavailable (`/bin/bash: rg: command not found`); used local `grep` and `find` instead.
