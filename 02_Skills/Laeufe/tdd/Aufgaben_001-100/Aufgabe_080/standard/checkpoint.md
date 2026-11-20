# Work checkpoint

Repository: /app (Navidrome). Implemented square artwork output for cover art: centered image on square transparent PNG canvas, square-aware cache key, API and public route parameter propagation, album grid URL flag. Added Go image behavior and endpoint tests plus a UI URL test.

TDD red checks observed:
- `GOTOOLCHAIN=local GOPROXY=off go test ./core/artwork -run TestArtwork -count=1`: rectangular JPEG returned `jpeg` instead of requested square `png`.
- Same command: zero-size square request produced `png: invalid format: invalid image size: 0x0`.
- Same command: non-square GIF resize returned `jpeg` instead of `gif`.
- `CI=true npm test -- --watch=false --runInBand src/subsonic/index.test.js`: square query option was absent.

Green checks:
- `GOTOOLCHAIN=local GOPROXY=off go test ./core/artwork ./server/subsonic ./server/public -count=1`: passed after final Go edits.
- `CI=true npm test -- --watch=false --runInBand`: 13 suites, 46 tests passed.
- `git diff --check`: passed.

Full Go suite: `GOTOOLCHAIN=local GOPROXY=off go test ./...` exited 1. All packages except `scanner/metadata/taglib` passed. Its two failures were `Correctly parses m4a (aac) gain tags` and `Correctly parses m4a (aac) gain tags (uppercase)` at `taglib_test.go:98`: expected one `replaygain_album_gain` value `0.37`, received duplicate `0.37` values. This is unrelated to artwork edits. The full run began before the final GIF preservation edit; the changed packages passed again afterward.

Requested OCI `internal/storage/fs/oci/source.go` interface could not be added coherently: this Navidrome checkout has no `internal/storage/fs/oci`, `containers.Option`, `oci.Store`, or `storagefs.StoreSnapshot` definitions. No OCI files changed.
