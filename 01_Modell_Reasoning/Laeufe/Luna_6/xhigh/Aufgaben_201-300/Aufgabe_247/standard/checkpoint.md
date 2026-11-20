# Checkpoint

Issue: restrict `SocketPosts.getUpvoters` to callers with `topics:read` across every category associated with the supplied post IDs, preserve administrator access, deduplicate user IDs before username lookup, honor the server-provided cutoff in the frontend, and enable HTML tooltips.

Changes made:
- Added a bulk category read check using `posts.getCidsByPids` and `privileges.categories.filterCids`; administrators bypass it, and any missing or unreadable category rejects with `[[error:no-privileges]]` before vote data is fetched.
- Deduplicated visible voter UIDs across the response before one username lookup, retaining each PID's UID ordering.
- Added `cutoff: 6` to each response item, capped explicit usernames at five, and counted all remaining voters in `otherCount`.
- Updated the tooltip to use the returned cutoff and enabled Bootstrap tooltip HTML.

Verification:
- ESLint passed for both edited JavaScript files.
- The first focused test attempt lacked the configured local Redis service. After starting local Redis, `mocha test/posts.js --grep voting` passed (10 tests). The narrow grep on the individual test skipped its setup vote, so its empty-name assertion was not a meaningful test failure.
