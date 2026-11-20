Implemented square album covers in the grid. The `square` option now flows through the URL helper, Subsonic and public endpoints, artwork methods, and cache key. Square requests center the image on a square PNG canvas, including when the source is smaller than the requested size; regular requests retain the existing behavior. Added tests for image shape, cache keys, placeholders, and API forwarding.

The focused Go tests and UI formatting check pass. The full Go suite fails two unrelated TagLib m4a gain tag assertions.

I did not add the separately listed OCI `Source`: this Navidrome checkout has no `internal/storage/fs/oci` path or the referenced storage types.