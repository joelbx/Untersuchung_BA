# Checkpoint

Resolved notification HTML rendering and deduplication in `packages/components/containers/notifications`.

- String content is sanitized with the existing DOMPurify dependency before rendering as HTML. React element content remains supported.
- Links in both HTML strings and React element content receive `rel="noopener noreferrer"` and `target="_blank"`.
- Non-success notifications deduplicate by explicit key, string text, or notification id, in that order. Success notifications remain repeatable. React list keys use notification ids.
- Added `notifications.spec.tsx` for HTML safety, link attributes, React content, deduplication, and repeatable success messages.

Checks:
- `yarn workspace @proton/components jest notifications.spec.tsx --runInBand --coverage=false`: passed (2 tests).
- `yarn workspace @proton/components check-types`: passed.
- `yarn workspace @proton/components test --coverage=false`: passed (33 suites, 121 tests passed, 1 skipped).
- `yarn workspace @proton/components eslint containers/notifications/Container.tsx containers/notifications/Notification.tsx containers/notifications/interfaces.ts containers/notifications/manager.tsx containers/notifications/notifications.spec.tsx --quiet`: passed.
- `yarn workspace @proton/components prettier --check containers/notifications/Container.tsx containers/notifications/Notification.tsx containers/notifications/interfaces.ts containers/notifications/manager.tsx containers/notifications/notifications.spec.tsx`: passed after formatting.
- `git diff --check`: passed.

Initial test discovery command `yarn workspace @proton/components jest containers/notifications --runInBand --coverage=false` exited 1 because no existing tests matched that path at the time. The new focused test and full component suite subsequently passed.
