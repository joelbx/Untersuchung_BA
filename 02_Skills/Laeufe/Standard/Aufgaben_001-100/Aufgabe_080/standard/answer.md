Fixed the AlbumGrid shaking issue. The grid now requests square covers; the backend centers non-square artwork on a square background, returns it as PNG, and keeps square and regular images in separate cache entries. Other artwork requests retain their existing behavior.

The artwork, Subsonic, and public server tests pass. Prettier, ESLint, and `git diff --check` also pass. Details are in [checkpoint.md](/app/.codex-role-output/checkpoint.md).

I did not create the requested OCI `Source`: this Navidrome checkout has no OCI package or the types that interface requires.