# Checkpoint

Implemented configurable topic backlinks. `Topics.syncBacklinks(postData)` scans local topic URLs, maintains `pid:{pid}:backlinks`, logs new backlink events, and purges events for removed references. Post creation and editing call it. Timeline events use `[[topic:backlink]]`, `/post/{pid}`, and the referencing author; the `topicBacklinks` setting controls visibility. Added admin control and English localization.

Checks:
- `./node_modules/.bin/mocha test/topicEvents.js`: 8 passing.
- `./node_modules/.bin/mocha test/topics.js test/posts.js`: 288 passing.
- `./node_modules/.bin/eslint src/topics/posts.js src/topics/events.js src/posts/edit.js test/topicEvents.js`: passed.
- `git diff --check`: passed.

Initial test attempt failed with `connect ECONNREFUSED 127.0.0.1:6379`; started local `redis-server --port 6379 --save '' --appendonly no` and reran successfully. Initial `rg` search failed because `rg` is unavailable; used `find` and `grep`.
