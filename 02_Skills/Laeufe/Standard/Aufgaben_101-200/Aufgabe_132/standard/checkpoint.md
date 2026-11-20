# Checkpoint

Implemented reserved system tags through the `meta.config.systemTags` array (default `[]`). Topic creation, editing, queued posting, and the add-tags API pass the acting uid into tag validation; nonprivileged use raises `You can not use this system tag.` The socket `isTagAllowed` check returns false for reserved tags.

Verification:
- `./node_modules/.bin/mocha test/topics.js --exit`: 168 passing.
- `./node_modules/.bin/mocha test/categories.js --grep 'tag whitelist' --exit`: 6 passing.
- `./node_modules/.bin/eslint src/topics/tags.js src/topics/create.js src/posts/edit.js src/posts/queue.js src/socket.io/topics/tags.js src/controllers/write/topics.js test/topics.js`: passed.

Initial check `./node_modules/.bin/mocha test/topics.js --grep 'system tags' --exit` failed with `connect ECONNREFUSED 127.0.0.1:6379`; a local Redis server was started, then tests passed. A partial suite run, `./node_modules/.bin/mocha test/topics.js test/categories.js --grep 'tags|tag whitelist|tag privilege' --exit`, failed in an existing topic tag score assertion because the grep filter skipped its earlier fixture topics; the full topic suite passed.
