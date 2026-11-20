# Backlink feature checkpoint

Started repository investigation. Need implement topic backlink synchronization, timeline visibility/rendering, admin config/UI/localization, and run relevant existing tests. Repository initially clean; no AGENTS.md found. `rg` is unavailable, so use grep/find.

Found integration points: `Topics.onNewPostMade` covers initial posts and replies; `Posts.edit` has the updated raw content; `Topics.events` stores timeline events with href support. Plan: track topic ids in `pid:{pid}:backlinks`, add/remove corresponding events on sync, filter backlink events in `Events.get` using `topicBacklinks`, and add the admin toggle and English locale keys.

Implemented sync, event visibility/removal, admin toggle, and English locale keys. Focused backlink and topic event tests pass (9 tests); ESLint and syntax checks pass. Local Redis was started because the configured test database port initially refused connections. Next: run existing topic and post suites, review edge cases, stop the temporary Redis process.

Completed. Added focused tests for initial posts, replies, URL forms, invalid input, event visibility, edit removal, and change counts. Combined relevant suites passed (298 tests); focused suites passed again after final review (10 tests). ESLint and `git diff --check` pass. Temporary Redis server was shut down.
