Added an OCI snapshot source and wired it into storage startup. Local OCI directories are reopened on each fetch so external updates are detected; the source caches snapshots by digest and publishes only changed snapshots. Existing sources now use the context-aware `Get` interface.

Tests pass: `go test ./internal/oci ./internal/storage/fs/... ./internal/config ./internal/cmd`.