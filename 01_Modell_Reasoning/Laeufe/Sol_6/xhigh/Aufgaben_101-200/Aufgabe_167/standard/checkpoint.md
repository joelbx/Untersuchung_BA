# OCI snapshot source work

Status: complete. Added the OCI snapshot source and server wiring, updated context-aware source calls, reopened local OCI targets on each fetch, and handled layer namespaces and gzip content.

Verification: `go test ./internal/oci ./internal/storage/fs/... ./internal/config ./internal/cmd` and `git diff --check` passed. Added tests cover local external updates, subscriptions, gzip layers, and an HTTP registry.
