Implemented reserved system tag enforcement.

- `Topics.validateTags` now checks `meta.config.systemTags` and rejects unprivileged users with `You can not use this system tag.` Topic creation, editing, and queued topic validation pass the user ID.
- `isTagAllowed` returns `false` for reserved tags.
- Added tests for unprivileged and privileged topic creation and the socket tag check.

Targeted ESLint and `git diff --check` passed. The topic and category tests could not start because Redis at `127.0.0.1:6379` was unavailable.

Key changes: [tag validation](</app/src/topics/tags.js>), [socket tag check](</app/src/socket.io/topics/tags.js>).