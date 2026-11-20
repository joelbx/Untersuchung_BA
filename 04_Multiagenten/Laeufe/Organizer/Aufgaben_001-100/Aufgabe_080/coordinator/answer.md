The AlbumGrid now requests square cover art. The backend centers non-square images on a square PNG, keeps the existing image behavior for other requests, and uses separate cache keys for the two variants.

The focused artwork and endpoint tests pass, as do the broader core and server suites. The touched frontend files pass Prettier. I solved this without delegation.

I did not add the requested OCI `Source` interface: this Navidrome checkout has no `internal/storage/fs` package or OCI store types to implement it against.