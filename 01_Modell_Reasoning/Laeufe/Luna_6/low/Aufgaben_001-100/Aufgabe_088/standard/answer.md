Implemented optional field selection for `getObject` and `getObjects` across MongoDB, Postgres, and Redis. Empty fields return full objects; requested fields include `null` when absent, and multi-object results preserve input key order. Postgres helpers now follow the same empty-fields and missing-key behavior.

ESLint and `git diff --check` passed. The existing hash suite could not run because Redis was unavailable at `127.0.0.1:6379`.

Checkpoint: [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md)