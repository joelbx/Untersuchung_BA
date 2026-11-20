Fixed the AlbumGrid shaking issue. The grid now requests square artwork; the backend centers non-square covers on a transparent square PNG and uses a distinct cache key for that version.

The artwork, Subsonic, and public image paths were updated. Relevant Go tests, the Prettier check, and `git diff --check` pass.

I did not add the requested OCI `Source` interface: this checkout has no OCI storage package or supporting types, and that interface is unrelated to the album artwork issue.