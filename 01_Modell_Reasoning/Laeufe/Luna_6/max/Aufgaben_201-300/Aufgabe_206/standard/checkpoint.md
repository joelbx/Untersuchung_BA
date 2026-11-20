# Checkpoint

Issue: prevent duplicate topic creation from overlapping create-topic requests by the same actor.

Implemented in `src/controllers/write/topics.js`: an atomic shared lock keyed by authenticated uid or guest sessionID now wraps topic creation and replies. Concurrent attempts receive `[[error:already-posting]]`, mapped by the existing v3 error handler to HTTP 400 and `bad-request`. The acquired lock is released in `finally`. Added the English error text in `public/language/en-GB/error.json`.

Verification: `test/topics.js` passed (229 passing) with a temporary local Redis instance; ESLint on the changed controller passed; locale JSON parse and `git diff --check` passed. The temporary Redis instance was shut down.
