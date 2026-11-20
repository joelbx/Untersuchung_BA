Implemented reserved system tag enforcement.

- `meta.config.systemTags` tags now require an admin or global moderator during topic creation, editing, and queued topic validation. Other users receive `You can not use this system tag.`
- `isTagAllowed` returns `false` for configured system tags.
- Updated [checkpoint.md](/app/.codex-role-output/checkpoint.md).

ESLint and `git diff --check` pass. The category tests could not start because Redis was unavailable at `127.0.0.1:6379`.