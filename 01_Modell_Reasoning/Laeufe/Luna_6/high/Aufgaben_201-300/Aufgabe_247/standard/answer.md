Updated `getUpvoters` to check `topics:read` across every associated category for non-admins, deduplicate voter IDs before username lookup, and return ordered usernames with `cutoff: 6`. Updated the tooltip to use the server cutoff and allow HTML.

ESLint and `git diff --check` passed. `npx mocha test/posts.js` could not start because Redis was unavailable at `127.0.0.1:6379`.

Changed [votes.js](/app/src/socket.io/posts/votes.js) and [votes.js](/app/public/src/client/topic/votes.js).