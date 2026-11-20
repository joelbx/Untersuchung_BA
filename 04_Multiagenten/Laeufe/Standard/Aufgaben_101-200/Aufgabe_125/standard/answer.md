Implemented topic backlinks. Posts now sync references when created or edited, adding and removing per-post associations and linked timeline events. Backlink events are shown only when the new admin setting is enabled, with localized “Referenced by” text.

Verification passed: 9 topic event tests, ESLint on changed JavaScript, and `git diff --check`.