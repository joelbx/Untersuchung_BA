Implemented square artwork rendering, added the `square` flag to artwork cache keys and backend calls, and updated the album grid to request square covers.

**Verification:** Go artwork and server tests passed; all 45 UI tests passed; frontend lint and `git diff --check` passed. Lint reported only an outdated Browserslist data warning.

The requested OCI `Source` file remains unimplemented: this checkout has no `internal/storage/fs/oci` package or the referenced OCI, container, and snapshot types.