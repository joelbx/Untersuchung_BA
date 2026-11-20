# Checkpoint

Task: render notification string HTML safely with secure links, and deduplicate non-success notifications using explicit or fallback keys.

Changed:
- `packages/components/containers/notifications/Container.tsx`: sanitize string HTML with DOMPurify, add `rel="noopener noreferrer"` and `target="_blank"` to every anchor; preserve React element content and distinct React keys for repeated success notifications.
- `packages/components/containers/notifications/manager.tsx`: derive notification key from explicit key, string text, or ID; deduplicate only non-success notifications by that key.
- `packages/components/containers/notifications/interfaces.ts`: allow an optional key when creating notifications.
- `packages/components/containers/notifications/notifications.test.tsx`: cover HTML/link handling, React elements, key fallback, and repeated success notifications.

Verification:
- `yarn workspace @proton/components jest containers/notifications/notifications.test.tsx --runInBand --coverage=false`: passed, 2 tests.
- `yarn workspace @proton/components check-types`: passed (exit 0).
- `yarn workspace @proton/components eslint containers/notifications/Container.tsx containers/notifications/manager.tsx containers/notifications/interfaces.ts containers/notifications/notifications.test.tsx --quiet`: passed (exit 0).
- `yarn workspace @proton/components test --coverage=false`: passed, 33 suites; 121 tests passed, 1 skipped.
- `git diff --check`: passed.

`rg` was unavailable, so local `find` and `grep` were used for investigation.
