# Checkpoint

Task: Clean up local user and group uploaded images when removed or when an account is deleted.

Implemented: Centralized user avatar and cover cleanup in `src/user/picture.js`, including legacy and timestamped png/jpeg/jpg/bmp files; account deletion calls the same file cleanup. Group cover removal deletes validated local cover and thumbnail files and extension variants. Socket handlers delegate to user image removal and retain action hooks. Missing files (ENOENT) are tolerated.

Passed checks:
- `./node_modules/.bin/eslint src/user/picture.js src/user/delete.js src/groups/cover.js src/socket.io/user/picture.js src/socket.io/user/profile.js`
- `git diff --check`
- Focused local Node filesystem assertions for all user extensions, timestamped names, another user's file preservation, group cover/thumbnail extension variants, and repeated removal with missing files (exit code 0).

Blocked integration check: `./node_modules/.bin/mocha test/user.js test/groups.js --grep 'cover image|remove uploaded picture|profile picture' --exit` failed in root before hook with `connect ECONNREFUSED 127.0.0.1:6379`; 0 tests ran. Redis is unavailable, so integration behavior remains unverified by that suite.
