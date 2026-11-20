# Checkpoint

Task: implement topic backlinks in `/app`.

Completed:
- Implemented `Topics.syncBacklinks(postData)` with required field validation, site URL and bare `/topic/{tid}` detection (including slugs), filtering of self and missing topics, sorted-set reconciliation, backlink event creation, and cleanup of removed backlinks.
- Wired synchronization into new topic/reply creation and post edits.
- Added the default-off `topicBacklinks` admin setting and timeline visibility gate.
- Added a localized `backlink` timeline event with a link icon and corrected the shared event anchor markup.

Verification:
- ESLint passed for all modified JavaScript files.
- Modified JSON files parse successfully.
- `git diff --check` passed.
- Existing `test/topicEvents.js` and `test/topics.js` could not run because Redis at `127.0.0.1:6379` refused the connection.
