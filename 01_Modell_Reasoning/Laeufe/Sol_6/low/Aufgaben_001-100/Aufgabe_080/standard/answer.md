Fixed the AlbumGrid shaking issue. Square requests now center non-square cover art on a square canvas and return PNG; the cache key includes the square setting. The grid requests square covers, while other artwork requests keep their existing shape and format.

The relevant Go tests pass: `go test ./core/artwork ./server/subsonic ./server/public`.

I did not create the requested OCI `Source` interface: this checkout has no `internal/storage/fs/oci` package or related types, so that separate interface request cannot be implemented here as specified.