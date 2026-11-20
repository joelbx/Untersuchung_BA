# Checkpoint

Task: support separate database credential keys with URL precedence, protocol validation, safe errors, and consistent migration/runtime behavior.

Initial state: repository status clean. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep`.

Investigation in progress. No fix attempted yet.

Root cause (phase 1): `config.Load` reads only `db.url`; `db.Open` and `NewMigrator` pass `cfg.Database.URL` directly to `db.parse`. `parse` includes raw URL in errors. Default URL would mask field input unless explicitly cleared. Recent commit is unrelated UI dependency change.

Pattern analysis (phase 2): existing URL parsing in `storage/db/db.go` supplies engine-specific parameters; existing `Scheme` enum in config shows map-based parsing but silently coerces unknown values. Database fields need strict parsing and common target resolution before the existing driver parser.

Hypothesis (phase 3): a single config-side target resolver with URL precedence, strict protocol parsing, and one shared open path will fix load/open/migration divergence; errors must avoid raw DSNs.

Implementation and verification (phase 4): Added a failing focused config test before implementation; initial run failed because `ConnectionURL` was absent. Added strict `DatabaseProtocol`, field loading/validation, URL precedence, target derivation, redacted parsing errors, common open path for runtime and migration, and by-value migrator API. Added migration field-mode and redaction tests. A later failing test showed invalid `db.port: banana` was silently converted to zero; strict integer parsing fixed it.

Verification: `GOPROXY=off go test ./...` passed (exit 0) after final edits. `git diff --check` passed (exit 0). The C compiler emits an existing SQLite warning during tests, but tests complete successfully. No downloads were used.
