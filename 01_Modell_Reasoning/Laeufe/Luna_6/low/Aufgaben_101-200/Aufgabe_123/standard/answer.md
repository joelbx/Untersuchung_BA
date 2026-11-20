Implemented safe HTML rendering and notification deduplication.

- String content is sanitized before rendering; links receive `rel="noopener noreferrer"` and `target="_blank"`. React element content remains supported.
- Non-success notifications deduplicate using an explicit key, the string text, or the notification ID, in that order. Success notifications can repeat.
- Replacing a duplicate resets its timeout.

Verification: component type check passed; all 32 component test suites passed (119 tests passed, 1 skipped); `git diff --check` passed. There are no existing tests specifically for notifications.