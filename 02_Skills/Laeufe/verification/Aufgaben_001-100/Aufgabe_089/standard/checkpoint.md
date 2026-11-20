# Checkpoint

Resolved referential validation in `internal/cue`, added exported filesystem snapshot constructors that validate files, and added import preflight checks before writes. Updated legacy test fixtures so they meet the schema and corrected valid CUE fixtures with real variant keys.

Verification (2026-10-27):
- `go test ./internal/cue ./internal/ext ./internal/storage/fs ./cmd/flipt -count=1 -timeout=60s` — exit 0; all tested packages passed (`cmd/flipt` has no test files).
- `git diff --check` — exit 0.

Tooling note: `rg` is unavailable (`/bin/bash: rg: command not found`); local `grep`/`find` were used. No downloads were requested.
