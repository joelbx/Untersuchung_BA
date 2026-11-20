Implemented topic backlinks for new posts and edits. `Topics.syncBacklinks(postData)` adds and removes per-post associations and timeline events; the admin setting controls whether those events appear. The timeline text and setting are localized in English.

Verification: the topic and topic-event suites passed (**197 tests**). ESLint, JSON parsing, and `git diff --check` also passed.