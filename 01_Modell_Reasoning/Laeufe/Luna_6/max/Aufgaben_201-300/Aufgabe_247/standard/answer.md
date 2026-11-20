Implemented the `getUpvoters` access check: non-admins must have `topics:read` access to every category associated with the supplied post IDs. The check happens before vote data is fetched, and inaccessible requests reject with `[[error:no-privileges]]`. Admins bypass the check.

The backend now returns a cutoff of 6, shows up to five usernames, counts the rest, and resolves each displayed UID once while preserving list order. The frontend reads the cutoff from the response and enables HTML tooltips.

Changed [votes.js](/app/src/socket.io/posts/votes.js:38) and [the topic votes client](/app/public/src/client/topic/votes.js:50).

ESLint and `git diff --check` passed. The targeted test could not complete because its setup could not connect to Redis at `127.0.0.1:6379`.