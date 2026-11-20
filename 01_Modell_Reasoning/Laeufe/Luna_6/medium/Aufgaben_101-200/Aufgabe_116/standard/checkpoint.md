# Checkpoint

Implemented `chat:privileged` as a global posting privilege and added its English admin UI label. `privileges.global.can` now accepts either one privilege (boolean result) or an array (boolean array result).

Chat middleware and messaging checks now use `['chat', 'chat:privileged']` and `.includes(true)`. `messaging.canMessageUser` rejects privileged targets unless the caller has `chat:privileged`, so create and invite flows share the same `[[error:no-privileges]]` behavior. Profile API responses include `canChat` computed with `messaging.canMessageUser`, and UserObject OpenAPI documents it.

Verification: `npx eslint` passed for all modified JavaScript files; `git diff --check` passed. `npx mocha test/messaging.js` could not run because Redis at `127.0.0.1:6379` was unavailable (before hook failed with ECONNREFUSED).
