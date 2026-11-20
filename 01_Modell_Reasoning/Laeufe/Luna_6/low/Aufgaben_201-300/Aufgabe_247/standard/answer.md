Implemented the upvoter access and response changes in [votes.js](/app/src/socket.io/posts/votes.js) and [votes.js](/app/public/src/client/topic/votes.js).

Non-admin requests now require `topics:read` for every category associated with the supplied post IDs; admins bypass the check. The server deduplicates UIDs before resolving usernames, preserves their order, and returns `cutoff: 6` with up to five usernames and an `otherCount`. The frontend uses the response cutoff and enables HTML tooltips.

The targeted test could not run because Redis is unavailable (`ECONNREFUSED 127.0.0.1:6379`); Mocha reported 0 passing. `git diff --check` passed.