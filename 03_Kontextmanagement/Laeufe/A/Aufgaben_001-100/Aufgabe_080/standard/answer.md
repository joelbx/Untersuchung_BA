Fixed the album grid artwork path. The grid now requests square covers; the backend centers non-square art on a square canvas, returns PNG for square requests, and uses separate cache keys for square and regular images.

The artwork, Subsonic, and public server tests pass. The changed UI files pass Prettier.

I did not add the requested OCI `Source` interface: this Navidrome checkout has none of the OCI storage package or types it depends on.