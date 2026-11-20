# Checkpoint

Task: Resolve AlbumGrid shaking with non-square covers.

Implemented: square flag through Artwork API, Subsonic endpoint, frontend URL helper and grid; square PNG processing with transparent centered padding; separate cache keys; updated callers and tests.

Verification:
- `GOTOOLCHAIN=local GOPROXY=off go test ./core/artwork ./server/subsonic ./server/public` — exit 0.
- `GOTOOLCHAIN=local GOPROXY=off go test ./core/... ./server/...` — exit 0.
- `./node_modules/.bin/eslint --max-warnings 0 src/subsonic/index.js src/album/AlbumGridView.js` — exit 0.
- `./node_modules/.bin/prettier -c src/subsonic/index.js src/album/AlbumGridView.js` — exit 0.
- `git diff --check` — exit 0.

Repository note: The supplied OCI Source interface list references `internal/storage/fs/oci/source.go`, but this Navidrome checkout has no `internal/storage` tree or OCI snapshot types. No unrelated OCI implementation was added.
Tooling note: `rg` is unavailable (`/bin/bash: rg: command not found`); local `find` and `grep` were used.
