# Checkpoint

Task: Resolve nullable database values in `/app`, add public generic helpers `gg.P` and `gg.V`, and run relevant existing tests.

Implemented:
- Added `gg.P[T]` and `gg.V[T]` with zero-value and nil handling.
- Changed nullable album/artist metadata timestamps, share expiration/last-visited timestamps, and album `image_files` to pointer fields.
- Updated timestamp reads/writes and image-file consumers to unwrap pointers safely; absent expiration stays nil and artist refresh clears its timestamp explicitly.
- Updated artwork test fixtures to use `gg.P` for image file values.

Validation:
- `go test ./utils/gg ./model ./persistence ./core ./core/artwork ./scanner ./server/subsonic ./server/public` passed.
- `go test ./...` compiled the repository and passed all packages except `scanner/metadata/taglib`, where 4 tests failed due to metadata parsing expectations and permission behavior in the TagLib test environment. No changed files are in that package.
- `git diff --check` passed.

Initial state: `rg` is not installed; no `AGENTS.md` files were found. Changes remain in the checked-out worktree for coordinator export.
