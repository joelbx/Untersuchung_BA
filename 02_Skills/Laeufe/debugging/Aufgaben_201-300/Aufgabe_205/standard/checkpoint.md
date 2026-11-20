# Token utility checkpoint

Investigating existing API utility and database conventions. Initial `src/api/utils.js` exposes only `log` and `getLastSeen` at the module root; no `utils.tokens` interface is present. No edits to implementation yet.

## Investigation

Root cause: `src/api/utils.js` only implements top-level `log` and `getLastSeen`. Existing token creation in `src/api/users.js` stores an array in `core.api` settings, so there are no `token:{token}` records or lifecycle indexes. The requested internal API is therefore absent. Working patterns: `src/utils.js` provides UUID generation; `user.exists` checks users; database adapters implement `setObject`, `setObjectField`, `getObjects`, `getSortedSetRange`, `sortedSetScores`, and `sortedSetRemove` with empty-array support. Hypothesis: adding a `utils.tokens` facade backed by these operations will provide the lifecycle and preserve existing top-level aliases.

## Verification so far

Focused regression: `./node_modules/.bin/mocha --reporter dot test/api-utils-tokens.js` passed after implementing the utility. Existing authentication test command `./node_modules/.bin/mocha --reporter dot test/authentication.js` failed in the before-all hook: `connect ECONNREFUSED 127.0.0.1:6379`. Its result remains unverified because local Redis is unavailable. Initial eslint command `./node_modules/.bin/eslint src/api/utils.js test/api-utils-tokens.js` failed on line length and unsupported nullish-coalescing syntax; edits made and rerun pending.

## Final patch and checks

Implemented `utils.tokens` lifecycle in `src/api/utils.js`, keeping top-level usage aliases for existing callers. Added indexed-token fallback in bearer verification so newly generated tokens authenticate while legacy settings tokens remain accepted. Regression test `test/api-utils-tokens.js` covers empty inputs, generation and user validation, creation and ownership indexes, hydration, usage, update, deletion, and bearer verification. It failed before the implementation (missing `utils.tokens`; bearer fallback also failed before its change) and now passes.

Final executed checks:
- `./node_modules/.bin/mocha --reporter dot test/api-utils-tokens.js` — 2 passing.
- `./node_modules/.bin/eslint src/api/utils.js src/routes/authentication.js test/api-utils-tokens.js` — passed.
- `git diff --check` — passed.
- `./node_modules/.bin/mocha --reporter dot test/authentication.js` — blocked by `connect ECONNREFUSED 127.0.0.1:6379` in before-all hook, so existing integration suite remains unverified locally.
