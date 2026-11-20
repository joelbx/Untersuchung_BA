Implemented square-aware artwork retrieval. Square requests produce a centered PNG on a square canvas, and the resize cache key includes the square flag. Both image endpoints parse and forward the flag; the album grid now requests square covers. See [artwork.go](/app/core/artwork/artwork.go:22), [reader_resized.go](/app/core/artwork/reader_resized.go:44), and [AlbumGridView.js](/app/ui/src/album/AlbumGridView.js:121).

Validation passed: the three targeted Go packages, Prettier, ESLint, and `git diff --check`.

The requested OCI `Source` interfaces remain unimplemented because this checkout has no `internal/storage/fs` package or definitions for `containers.Option`, `oci.Store`, or `StoreSnapshot`. Creating that API here would require inventing missing repository abstractions.