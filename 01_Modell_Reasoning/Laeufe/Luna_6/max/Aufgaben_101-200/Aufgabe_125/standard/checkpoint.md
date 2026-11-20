# Checkpoint: topic backlinks

- Objective: implement topic backlinks, gated by the `topicBacklinks` setting, integrated with post creation/edit and timeline rendering.
- Findings: topic events already support localized text, icons, and `href`; post creation routes through `Topics.onNewPostMade`, and edits persist the post in `src/posts/edit.js`.
- Implementation: add `Topics.syncBacklinks`, associate referenced tids under each pid, append/remove backlink events, hide them from timelines unless `topicBacklinks` is enabled, and add the admin toggle and English strings.
- Verification: ESLint, JavaScript syntax checks, and JSON parsing pass. The existing topic event, topic, and post suites pass (292 tests); the temporary local Redis service used by the suites has been stopped.
