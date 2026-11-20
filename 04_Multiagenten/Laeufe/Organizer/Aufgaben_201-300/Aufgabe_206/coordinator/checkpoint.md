Issue: concurrent POST /api/v3/topics requests by one actor can create duplicate topics.
Implemented: per-actor in-process posting lock in src/controllers/write/topics.js, shared by create and reply, released in finally after response formatting. Added English error message and HTTP regression test for one success, seven 400 responses, and one increment in global/category/user topic counts.
Verification: ESLint and JSON parse passed; full test/topics.js suite passed (230 passing); git diff --check passed. Temporary local Redis instance stopped.
Delegation: none; solved directly.
