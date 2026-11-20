# Reverse links to topics

Status: implemented and verified.

- Added Topics.syncBacklinks in src/topics/posts.js. It validates post data, detects site and bare topic URLs, maintains pid:{pid}:backlinks, logs new backlink events, and removes stale backlink events. Synchronization drops associations for topics that were purged.
- Wired synchronization into post creation (including initial topic posts and replies) and edits.
- Added the topicBacklinks setting, admin toggle, localized labels, and timeline event visibility filter.
- Added focused integration tests in test/topicEvents.js.

Verification: topicEvents.js 10 passing; topics.js and posts.js 288 passing; ESLint on changed JS passed; git diff --check passed.
