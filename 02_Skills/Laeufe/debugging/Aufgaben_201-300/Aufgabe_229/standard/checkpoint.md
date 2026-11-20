# Checkpoint

## Root cause
- Group and user cover removal cleared database fields without deleting local files.
- Avatar socket removal built a path from `base_dir/public` and did not await deletion; that path does not match `upload_path/profile` in the configured upload layout.
- Account deletion targeted only legacy `{uid}-profile{type}.{ext}` names, while uploads use timestamped `{uid}-profile{type}-{timestamp}.{ext}` names.

## Changes
- Centralized user avatar and cover cleanup in `src/user/picture.js`, with strict local URL and user filename validation, all supported extensions, and ENOENT handling.
- Socket handlers call the centralized functions and retain their action hooks.
- Account deletion calls both cleanup functions before removing the user object.
- Group cover removal deletes locally referenced cover and thumbnail files, including older extension variants of those filenames, and clears all three fields.
- Added `test/manual/image-cleanup.js` as an isolated filesystem reproduction and regression check.

## Verification
- Before patch: `node test/manual/image-cleanup.js` failed because `User.getLocalAvatarPath` did not exist; after implementing user cleanup, it failed because group cover files remained.
- After patch: `node test/manual/image-cleanup.js` passed.
- `node_modules/.bin/eslint src/groups/cover.js src/user/picture.js src/user/delete.js src/socket.io/user/picture.js src/socket.io/user/profile.js test/manual/image-cleanup.js` passed.
- `git diff --check` passed.
- Existing test command `node_modules/.bin/mocha test/coverPhoto.js --reporter dot` failed before tests: `Error: connect ECONNREFUSED 127.0.0.1:6379`. The configured local Redis test service is unavailable, so integration behavior under the full test harness remains unverified.
- `rg` is unavailable; repository search used `grep` and `find`.
