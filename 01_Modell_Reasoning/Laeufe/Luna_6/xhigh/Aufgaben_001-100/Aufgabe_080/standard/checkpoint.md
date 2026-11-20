# Checkpoint

Task: Fix album artwork shaking for non-square cover art.

Completed: Added a square option to artwork retrieval, included it in resized cache keys, generated centered square PNGs when requested, plumbed the option through the public and Subsonic endpoints, and enabled it for album grid covers. Existing callers explicitly request non-square output.

Validation passed:
- `go test ./core/artwork ./server/subsonic ./server/public`
- Prettier check for changed frontend files
- ESLint for changed frontend files
- `git diff --check`

Repository limitation: The requested OCI Source interfaces refer to `internal/storage/fs`, `containers.Option`, `oci.Store`, and `StoreSnapshot`, none of which exist in this checkout. No OCI source file was created without those local abstractions.
