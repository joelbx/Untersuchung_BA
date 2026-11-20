Implemented the chat privacy settings, server-side permission checks, batched legacy migration, OpenAPI updates, and allow/deny coverage. Explicit blocks take precedence; admins and global moderators bypass the privacy lists.

Lint and `git diff --check` pass. The relevant Mocha tests could not run because Redis was unavailable (`ECONNREFUSED 127.0.0.1:6379`).

The account settings page is supplied by the installed theme outside the checked-out repository. The account settings API accepts and stores the three new fields, but the theme UI still needs updating to expose them. Legacy `restrictChat` remains only in the migration so it can identify accounts to convert.

Progress is recorded in [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).