Implemented the notification fixes.

- HTML strings are sanitized with DOMPurify before rendering, and all notification links receive `target="_blank"` and `rel="noopener noreferrer"` in [Notification.tsx](/app/packages/components/containers/notifications/Notification.tsx:24).
- Notifications accept an optional key and deduplicate non-success messages by that key, using the specified fallbacks in [manager.tsx](/app/packages/components/containers/notifications/manager.tsx:64).
- Success notifications remain distinct, with unique list keys in [Container.tsx](/app/packages/components/containers/notifications/Container.tsx:10).

Verification passed: component type check, targeted ESLint, and the existing test suite (32 suites; 119 passed, 1 skipped). `git diff --check` also passed.