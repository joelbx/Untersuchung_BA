Fixed the album grid shaking caused by non-square covers. The grid now requests square artwork; the backend centers each cover on a square PNG canvas and uses a separate cache key for that version. Regular artwork requests retain their existing shape and format.

The artwork, Subsonic, and public server tests pass. UI lint and formatting checks pass.

I did not add the requested OCI `Source` interface: this checkout has no `internal/storage/fs/oci` package or the related OCI types, and that interface is unrelated to the album issue.