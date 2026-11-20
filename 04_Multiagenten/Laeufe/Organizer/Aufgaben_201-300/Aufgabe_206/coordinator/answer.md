Added `lockPosting` in [topics.js](/app/src/controllers/write/topics.js) to reject overlapping create or reply requests from the same user or guest session. The lock is released after response handling, including when an error occurs. A concurrent request receives HTTP 400 with `status.code: "bad-request"`; the accepted create request returns `status.code: "ok"`.

The new HTTP regression test confirms that one of eight concurrent create requests succeeds and that the global, category, and user topic counts each increase by one. The full topic suite passed (**230 tests**), as did ESLint and `git diff --check`.

The lock is local to one application process, so it does not coordinate requests handled by different processes. No delegation was used.