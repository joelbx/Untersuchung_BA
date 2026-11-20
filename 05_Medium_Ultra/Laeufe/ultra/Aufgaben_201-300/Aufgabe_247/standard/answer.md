Resolved the upvoter access leak. [getUpvoters](/app/src/socket.io/posts/votes.js:38) now checks `topics:read` on every supplied post category before fetching votes, denies unresolved categories, and permits administrators. It also looks up deduplicated user IDs once, preserves username order, and returns a cutoff of 6 with at most five names shown.

The [tooltip](/app/public/src/client/topic/votes.js:48) now uses the server cutoff and supports HTML. [Tests](/app/test/posts.js:220) cover access, ordering, deduplication, and truncation.

I delegated the backend and frontend edits and an independent review, then verified the combined patch. The focused voting suite passed **12 tests**; targeted ESLint, syntax checks, and `git diff --check` passed.