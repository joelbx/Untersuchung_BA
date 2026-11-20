Implemented the notification changes:

- String content is sanitized with DOMPurify and rendered as HTML. Links receive `target="_blank"` and `rel="noopener noreferrer"`.
- Non-success notifications deduplicate by explicit `key`, then string `text`, then notification ID. Success notifications can repeat.
- React element content remains supported.

The component type check completed without reported errors, and `git diff --check` passed. I found no existing tests specific to notification rendering or deduplication.