# Token utilities issue checkpoint

- Implemented the `utils.tokens` lifecycle API in `src/api/utils.js`: list, generate, get, update, delete, log usage, and get last-seen.
- Token records are stored under `token:{token}` and indexed by creation time, numeric UID, and last-seen time. Hydration preserves scalar/array shape, includes the token ID, normalizes numeric metadata, and handles empty inputs.
- Updated API usage logging and admin last-seen lookup to call the namespaced API. Authentication now checks internally stored tokens before falling back to legacy `core.api` settings.
- Final review complete; no unrelated source or harness changes.
- Verification: ESLint and `git diff --check` pass. The focused existing authentication test could not start because Redis was unavailable (`ECONNREFUSED`); no test cases ran.
