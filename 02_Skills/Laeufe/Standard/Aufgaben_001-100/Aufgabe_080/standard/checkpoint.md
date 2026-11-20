# Checkpoint

Task: fix AlbumGrid shaking for non-square artwork.

Implemented square-aware artwork retrieval, cache keys, PNG output with centered artwork on a square background, Subsonic parameter forwarding, and square AlbumGrid URLs. Other artwork callers retain the original shape. Added tests for image dimensions, format, cache key separation, and API parameter forwarding.

Validation:
- `GOPROXY=off GOSUMDB=off go test ./core/artwork ./server/subsonic ./server/public` passed.
- `./node_modules/.bin/prettier -c src/subsonic/index.js src/album/AlbumGridView.js && ./node_modules/.bin/eslint --max-warnings 0 src/subsonic/index.js src/album/AlbumGridView.js` passed from ui/.
- `git diff --check` passed.

Initial test run failed to compile because `core/artwork/sources.go` still called `a.Get` with three arguments. Updated that call and reran the tests successfully.

The issue's OCI `internal/storage/fs/oci/source.go` interface belongs to a different repository layout. This checkout is Navidrome and contains no `internal/` tree, OCI store, `storagefs.StoreSnapshot`, or `containers.Option` definitions. No OCI source was created because its required types and intended behavior cannot be established from this repository.
