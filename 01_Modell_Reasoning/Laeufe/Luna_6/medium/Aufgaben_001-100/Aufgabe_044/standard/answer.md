Implemented accessible namespace evaluation in both authorization engines, added middleware context propagation for `ListNamespaces`, and filtered namespace results with an accessible-only total count.

Verification passed: `go test ./internal/server/authz/... ./internal/server`.

The checkpoint is recorded in `.codex-role-output/checkpoint.md`.