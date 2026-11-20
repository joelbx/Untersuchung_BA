# Checkpoint

Implemented configurable `meta.config.systemTags` as an array, privileged-only tag validation across topic posting, editing, queued posts, and the tag write API. Reserved tags are excluded by `isTagAllowed`. Comparison follows stored tag normalization.

Verification: `mocha test/topics.js test/posts.js` passed (264 tests); ESLint and `git diff --check` passed.
