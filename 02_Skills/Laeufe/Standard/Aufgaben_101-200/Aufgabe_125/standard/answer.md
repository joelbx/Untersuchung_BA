Implemented configurable topic backlinks. Posts now add backlinks when created, and edits add or remove them as references change. The timeline shows a localized “Referenced by” link to the referencing post when admins enable `topicBacklinks`.

Verification passed: 8 focused topic event tests, 288 topic and post tests, ESLint, and `git diff --check`.