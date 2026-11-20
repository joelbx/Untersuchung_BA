# Checkpoint

Task: Resolve AlbumGrid shaking with non-square album covers in /app.

## Investigation
- The grid uses `getCoverArtUrl(record, 300)` and measures its cover container width for image height.
- `resizeImage` used `imaging.Fit`, which keeps a non-square image non-square; it also returned the original for small images. The cache key had no square variant.
- Added a regression test for square/non-square output before the fix. Initial check: `GOTOOLCHAIN=local GOPROXY=off go test ./core/artwork -run TestArtwork -count=1` failed as expected with `too many arguments in call to resizeImage` at artwork_internal_test.go:219.
- Compared existing image path and callers before patching; root cause was the absence of a square image variant in the artwork pipeline and request URL.

## Changes
- Added `square` through Artwork, resize reader, cache key, Subsonic/public endpoints, cache warmer, and frontend URL/grid.
- Square output uses a centered image over `image.NewRGBA` and PNG encoding; regular output preserves previous shape and format.
- Added Go regression tests for dimensions, output format, small covers, key separation, and request propagation; added a frontend URL test.

## Verification
- `GOTOOLCHAIN=local GOPROXY=off go test ./core/artwork ./server/subsonic ./server/public ./core -count=1`: passed.
- `CI=true npm test -- --watch=false --runInBand`: 13 suites, 46 tests passed (after adding focused URL test).
- `./node_modules/.bin/prettier -c src/album/AlbumGridView.js src/subsonic/index.js src/subsonic/index.test.js`: passed.
- `./node_modules/.bin/eslint --max-warnings 0 src/album/AlbumGridView.js src/subsonic/index.js src/subsonic/index.test.js`: passed (Browserslist data warning only).
- `GOTOOLCHAIN=local GOPROXY=off go test ./... -run '^$'`: passed; compiles all Go packages without running their tests.
- `git diff --check`: passed.

## Scope note
The requested OCI Source interface references `internal/storage/fs/oci`, `oci.Store`, `storagefs.StoreSnapshot`, and `containers.Option[Source]`, none of which exist in this repository. It is unrelated to the AlbumGrid issue, so no speculative OCI subsystem was added.
