# Checkpoint

Implemented square artwork support through the artwork interface, resize/cache path, Subsonic and public image handlers, and frontend album grid URL construction. Square cache keys include the flag; square results use a centered transparent RGBA square and PNG encoding. Non-square requests keep the existing resized dimensions and format handling.

Verification: `go test ./core/artwork ./server/subsonic ./server/public` passed. `npm run lint -- --no-cache` passed (with the repository's outdated Browserslist database advisory). `git diff --check` passed.

Repository constraint: `internal/storage/fs/oci/source.go` and all referenced OCI/storage types (`oci.Store`, `containers.Option`, `storagefs.StoreSnapshot`, `SnapshotSource`) are absent from this checkout. No OCI source file was added because it cannot be implemented or compiled against the repository's existing code.
