# Checkpoint

Task: Render notification HTML safely, secure links, and deduplicate non-success notifications by stable key.

Approach: Inspect local code and tests; follow red-green-refactor; run relevant and full existing test commands.

Tooling note: `rg --files -g '!*node_modules*'` failed because `rg` is unavailable (`/bin/bash: rg: command not found`). Using `find` and `grep` locally.

## Resolution

- Sanitized string notification HTML with the existing DOMPurify dependency; kept React element content intact.
- Secured anchors in rendered notification content with `rel="noopener noreferrer"` and `target="_blank"`.
- Resolved notification keys from explicit key, string text, or identifier; deduplicated only non-success notifications by key. Success notifications use their identifiers as React list keys so repeated messages render without duplicate-key warnings.
- Added regression tests in `packages/components/containers/notifications/notifications.test.tsx`; observed expected failures before implementation and green runs afterward.

## Verification

- `./node_modules/.bin/jest --config packages/components/jest.config.js --runInBand --ci`: 33 suites passed; 127 tests passed, 1 skipped.
- `./node_modules/.bin/tsc --project packages/components/tsconfig.json --noEmit`: passed.
- `./node_modules/.bin/eslint packages/components/containers/notifications/Container.tsx packages/components/containers/notifications/Notification.tsx packages/components/containers/notifications/manager.tsx packages/components/containers/notifications/interfaces.ts packages/components/containers/notifications/notifications.test.tsx --quiet`: passed.
- `./node_modules/.bin/prettier --check packages/components/containers/notifications/{Container.tsx,Notification.tsx,manager.tsx,interfaces.ts,notifications.test.tsx}`: passed.
- `git diff --check`: passed.

Jest emitted an existing Browserslist outdated-data notice; no dependencies were downloaded.
