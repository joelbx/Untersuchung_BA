Implemented the typed expression AST, nested function parsing, matcher expressions, and namespace-aware interpolation. Updated trait allowlisting and PAM environment validation/logging.

`go test ./lib/utils/parse` and `go test ./lib/services` pass. `go test ./lib/srv` is blocked by missing/incompatible system C headers. `git diff --check` passes.

Checkpoint: [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md)