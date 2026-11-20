Added `lockPosting` to [topics.js](/app/src/controllers/write/topics.js:16). Topic creation and replies now reject overlapping requests from the same user or guest session with HTTP 400 and `status.code: "bad-request"`; the accepted create returns `status.code: "ok"`. The lock is released after the operation finishes.

A delegated agent added the concurrent request regression in [test/topics.js](/app/test/topics.js:173); other agents reviewed the flow and patch. I integrated the changes and verified **230 passing topic tests**, plus ESLint and syntax checks. The test confirms one new topic and matching counter changes.

The lightweight lock is process local. A deployment with multiple Node workers needs a shared lock for the same guarantee across workers.