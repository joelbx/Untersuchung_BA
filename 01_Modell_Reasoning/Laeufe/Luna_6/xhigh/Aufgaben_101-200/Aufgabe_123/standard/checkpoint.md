# Checkpoint

Task: fix notification HTML rendering, safe link attributes, and duplicate suppression per the issue requirements.

Implemented in `packages/components/containers/notifications`:
- String HTML is sanitized with DOMPurify before rendering.
- Anchors in sanitized HTML and React element content receive `rel="noopener noreferrer"` and `target="_blank"`.
- Notification creation accepts an optional stable `key`; non-success notifications deduplicate by that key, defaulting to string text or the notification ID as required.
- Success notifications bypass deduplication, while list rendering uses unique notification IDs.

Validation: components TypeScript check passed; existing components suite passed (32 suites, 119 passed, 1 skipped); components lint passed; `git diff --check` passed.
