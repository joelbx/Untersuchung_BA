# Checkpoint

Task: fix AlbumGrid shaking for non-square covers in /app.

Completed:
- Added `square` to artwork Get/GetOrPlaceholder, propagated it through backend callers, and parsed the Subsonic request flag.
- Square requests resize within the requested bounds, center on a transparent RGBA square, and encode PNG. Non-square requests retain existing behavior. Resized cache keys include the square flag.
- AlbumGrid requests square covers; its URL helper accepts the flag. Cache warming prepares square 300px artwork.
- Added focused Go and frontend tests.

Verification:
- `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./core/artwork ./server/subsonic ./server/public` passed.
- `CI=true ./node_modules/.bin/react-scripts test --watch=false --runInBand src/subsonic/index.test.js` passed.
- Targeted ESLint and Prettier checks passed; `git diff --check` passed.

Repository mismatch: The supplied OCI Source interface belongs to a storage subsystem absent from this Navidrome checkout (`internal/storage/fs/oci`, `oci.Store`, `storagefs.StoreSnapshot`, and `containers.Option` do not exist). It was not added as unrelated, unbuildable code.
