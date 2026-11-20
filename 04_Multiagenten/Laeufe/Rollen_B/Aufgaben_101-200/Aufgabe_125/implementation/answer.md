Implemented topic backlinks. Posts now synchronize references on creation and edit, remove stale backlink events, and show localized “Referenced by” links in the timeline when the `topicBacklinks` admin setting is enabled.

Verification: 8 topic event tests passed; targeted ESLint and `git diff --check` passed.