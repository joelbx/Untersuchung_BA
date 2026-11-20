# Checkpoint

Task: prevent concurrent topic creation by the same actor on `POST /api/v3/topics`, preserving the API response and derived state.

Initial findings: `src/controllers/write/topics.js` called `api.topics.create` directly, with no per-actor guard. Repository started clean.

Implemented: exported `Topics.lockPosting(req, error)` returns `posting<uid or sessionID>` and rejects another in-progress post for that actor. Create and reply share the lock and release it in `finally`. Added an English error message and a concurrent HTTP test checking one success, four HTTP 400 responses, and increments of exactly one in global, category, and user topic counts.

Validation: focused Mocha tests passed (3 passing), ESLint passed, locale JSON parsed, and `git diff --check` passed. The test runtime uses an existing generated language bundle and warns that the new source translation is missing from that bundle until languages are rebuilt.
