# Checkpoint

Task: implement configurable deletion of uploaded files exclusively referenced by purged posts, with path validation and individual/list deletion support.

Implemented:
- Added `Posts.uploads.deleteFromDisk` with string/array inputs, rejection of unsupported top-level types, path containment and symlink checks, and missing/invalid path handling.
- Post purge now dissociates uploads, checks remaining post references, then removes orphaned originals and resized variants unless `preserveOrphanedUploads` is enabled.
- Added the default-off setting and ACP checkbox/help text in English locales.

Validation:
- ESLint passes for the changed JavaScript files.
- JavaScript syntax checks, JSON parsing, and `git diff --check` pass.
- Existing `test/posts/uploads.js` was attempted but cannot initialize: its Redis dependency at `127.0.0.1:6379` refuses connections.
