# Checkpoint

Implemented local image cleanup for group covers and thumbnails, user covers and avatars, and account deletion. User cleanup covers legacy and timestamped `.png`, `.jpeg`, `.jpg`, `.bmp` filenames under `upload_path/profile`; it validates configured local upload URLs before deleting a referenced image during replacement. Explicit removal clears the related database fields and retains the socket action hooks. Missing files are tolerated.

Verification run:
- `./node_modules/.bin/eslint src/groups/cover.js src/socket.io/user/picture.js src/socket.io/user/profile.js src/user/delete.js src/user/picture.js` — exit 0.
- `node .codex-role-output/verify-images.js` — exit 0, `isolated image cleanup checks passed`. This checks all four extensions, timestamped variants, preserved unrelated files, missing files, group cover and thumbnail cleanup, and unsafe group URLs.
- `git diff --check` — exit 0.

Integration test attempted:
- `./node_modules/.bin/mocha test/user.js --grep 'cover image|remove uploaded picture' --reporter dot` — exit 1 during root `before all`: `Error: connect ECONNREFUSED 127.0.0.1:6379`. 0 tests passed, 1 setup failure. End-to-end database and socket behavior therefore remains unverified in this environment.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); local `grep`/`find` were used.
