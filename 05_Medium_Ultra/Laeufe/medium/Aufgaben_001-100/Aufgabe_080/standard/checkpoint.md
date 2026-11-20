Issue: AlbumGrid shaking with non-square covers.
Completed: Artwork.Get/GetOrPlaceholder accept square; resized artwork uses centered square PNG canvas and square-aware cache keys; Subsonic/public endpoints pass square; UI grid requests square covers. Existing callers pass false. Added tests for rectangular JPEG conversion, no-upscale square output, cache key distinction, and endpoint forwarding.
Verification: GOPROXY=off GOSUMDB=off go test ./core/artwork ./server/subsonic ./server/public passed; UI npm test passed (12 suites, 45 tests); npm run check-formatting passed; git diff --check passed.
Scope note: OCI Source interface list is unrelated to this Navidrome repository; internal/storage/fs/oci does not exist.
