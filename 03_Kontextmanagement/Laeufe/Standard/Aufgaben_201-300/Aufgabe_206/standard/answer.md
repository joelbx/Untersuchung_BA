Added a per-user or guest-session posting lock around topic creation and replies. Overlapping requests now receive HTTP 400 with `bad-request`; the lock is released on success or error.

The new concurrent request test confirms one `ok` response, seven rejected requests, and exactly one new topic and post. Lint passed, and all 230 tests in `test/topics.js` passed.