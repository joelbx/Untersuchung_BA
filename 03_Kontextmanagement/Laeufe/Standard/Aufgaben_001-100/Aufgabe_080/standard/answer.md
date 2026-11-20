Fixed the AlbumGrid cover issue. The grid now requests square artwork; the backend centers non-square covers on a square PNG canvas and uses separate cache keys for square and regular versions.

The affected Go tests and all 45 UI tests pass. The full Go suite still has two failures in unchanged TagLib AAC replaygain tests.

I did not add the listed OCI `Source` interfaces: this Navidrome checkout has no `internal/storage/fs/oci` package or supporting types.