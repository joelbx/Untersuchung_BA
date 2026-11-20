# Debugging checkpoint

Task: repair HTML rendering, safe links, and stable deduplication for notifications.

Phase 1 in progress. Repository is clean at start. `rg` is unavailable (`/bin/bash: rg: command not found`); using `grep`/`find` locally.

Phase 1: Reproduced both failures with `../../node_modules/.bin/jest --runInBand --coverage=false containers/notifications/notifications.test.tsx` (exit 1). React renders HTML string literally, and manager assigns `key: id` then compares `text` only. A React anchor has no enforced navigation attributes.

Phase 2: Existing `dompurify` dependency is used for untrusted markup elsewhere. Notifications render through `Container` and `Notification`; manager owns deduplication and key assignment. Existing interface excludes caller-provided `key`.

Phase 3 hypothesis: Rendering strings through DOMPurify, enforcing anchor attributes at the rendered notification, and deriving/comparing manager keys will resolve the failures. The minimal regression test above confirms the current behavior before implementation.

Phase 4: Added and executed regression tests before the fix (failed as expected), then implemented string sanitization with DOMPurify, enforced safe attributes on rendered anchors, and changed manager deduplication to compare derived/explicit keys for non-success notifications. Success notifications retain unique React rendering keys and are not deduplicated.

Verification after fix:
- `../../node_modules/.bin/jest --runInBand --coverage=false` from `packages/components`: exit 0, 33 suites passed, 121 tests passed, 1 skipped.
- `../../node_modules/.bin/tsc --noEmit --pretty false` from `packages/components`: exit 0.
- `../../node_modules/.bin/eslint containers/notifications/Notification.tsx containers/notifications/Container.tsx containers/notifications/manager.tsx containers/notifications/interfaces.ts containers/notifications/notifications.test.tsx --quiet`: exit 0.
- `git diff --check`: exit 0.
