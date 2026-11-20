# Checkpoint

Task: restrict configured system tags to privileged users in topic creation, editing, queued posting, and the topic tagging API; exclude reserved tags from `isTagAllowed`.

Implementation: `meta.config.systemTags` defaults to an empty comma-separated string and is editable in admin tag settings. Tag validation receives the acting UID and uses `user.isPrivileged`; unauthorized use throws `You can not use this system tag.` The tagging API validates before writing.

TDD: `./node_modules/.bin/mocha test/topics.js --grep 'system tags' --timeout 25000` first failed with `Missing expected rejection` for creation; after that fix, the API regression first failed with the same expected assertion. Both passed after implementation (5 passing).

Verification:
- `./node_modules/.bin/mocha test/topics.js --timeout 25000`: 169 passing.
- `./node_modules/.bin/mocha test/categories.js --timeout 25000`: 54 passing.
- `./node_modules/.bin/eslint src/topics/tags.js src/topics/create.js src/posts/edit.js src/posts/queue.js src/socket.io/topics/tags.js src/controllers/write/topics.js test/topics.js`: passed.
- `git diff --check`: passed.
- `npm test`: failed, 177 passing and 1 failing. The failing test is `response status code should match one of the schema defined responses` in `test/api.js`: `GET /api/admin/extend/plugins` returned 500 because the app could not fetch `https://packages.nodebb.org/api/v1/plugins` (tunneling socket 403). This is an offline external-service failure; full-suite status remains uncertain beyond the tests run before its bail.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used grep/find. Initial focused test could not connect to Redis (`ECONNREFUSED 127.0.0.1:6379`); started the locally installed Redis server and reran it.
