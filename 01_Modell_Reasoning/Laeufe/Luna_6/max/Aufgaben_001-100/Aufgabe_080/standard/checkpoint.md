# Checkpoint

Issue: prevent album grid shaking with non-square artwork by adding square-aware image processing, cache keys, API plumbing, and frontend usage.

Completed:
- Added `square` to the artwork interface and implementation. Square variants are centered on a transparent square canvas and encoded as PNG; non-square variants retain the existing resizing/encoding behavior.
- Added the flag to resized-artwork cache keys and threaded it through internal readers, the Subsonic and public endpoints, the cache warmer, and frontend cover URLs. AlbumGridView requests square covers.
- Updated existing call sites and the endpoint test for the new parameter.

Verification:
- `go test ./core/artwork ./server/subsonic ./server/public` passed.
- `CI=true npm test -- --watchAll=false --runInBand` passed (12 suites, 45 tests).
- `npm run lint` passed; it printed only the existing outdated Browserslist data warning.
- `git diff --check` passed.

Repository note: `internal/storage/fs/oci/source.go` and its referenced OCI/container snapshot types do not exist in this checkout. That requested source is unrelated to the artwork issue and cannot be implemented using the repository's existing abstractions.
