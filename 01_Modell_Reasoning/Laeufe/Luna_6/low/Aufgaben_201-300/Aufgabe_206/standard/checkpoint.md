# Checkpoint

Issue: concurrent topic creation by one actor can create duplicates.

Implementation: added `Topics.lockPosting(req, error)` using the database's atomic `locks` hash increments, keyed by `posting<uid>` for authenticated users or `posting<sessionID>` for guests. Topic creation and replies hold the lock across their API operation and release it in `finally`; overlapping attempts throw and the API route wrapper returns HTTP 400 with `status.code: "bad-request"`.

Verification: `npx eslint src/controllers/write/topics.js` passed. `npx mocha test/topics.js` could not run because Redis was unavailable (`ECONNREFUSED 127.0.0.1:6379`).
