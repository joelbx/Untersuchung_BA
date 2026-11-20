Implemented square artwork rendering. Square requests now use a centered transparent canvas, return PNG, and have distinct cache keys. The Subsonic and public image handlers accept the `square` parameter, and the album grid requests square covers.

Verification passed: `go test ./core/artwork ./server/subsonic ./server/public`, frontend lint, and `git diff --check`.

The requested OCI `Source` could not be implemented: this checkout has no `internal/storage/fs/oci` package or the referenced OCI and snapshot types. I recorded that limitation in the checkpoint.

Changed: [reader_resized.go](/app/core/artwork/reader_resized.go), [artwork.go](/app/core/artwork/artwork.go), [AlbumGridView.js](/app/ui/src/album/AlbumGridView.js), and the image handlers.