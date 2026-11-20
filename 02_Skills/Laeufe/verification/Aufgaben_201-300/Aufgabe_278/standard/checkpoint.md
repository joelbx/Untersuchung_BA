# Checkpoint

Issue: mailbox list reload, retry, stale response, and pending backend action handling.

Changes: loading selector uses current page and parameters; list requests wait for pending backend operations; relevant mutation hooks track operation lifecycles; failure and stale responses have separate timed retries; stale responses are rejected before data is stored; reducer and selector state updated; focused tests added.

Tooling: `rg` was unavailable (`/bin/bash: rg: command not found`), so local searches used `find` and `grep`.

Verification completed before final edits:
- `./node_modules/.bin/tsc --noEmit -p applications/mail/tsconfig.json`: exit 0.
- `./node_modules/.bin/jest --config applications/mail/jest.config.js --runInBand --coverage=false applications/mail/src/app/logic/elements/elementsSlice.test.ts applications/mail/src/app/containers/mailbox/tests/Mailbox.elements.test.tsx`: 2 suites, 17 tests passed; Jest reported an open-handle notice after completion.

Final focused test and type check reruns: pending.

Final verification:
- `./node_modules/.bin/jest --config applications/mail/jest.config.js --runInBand --coverage=false applications/mail/src/app/logic/elements/elementsSlice.test.ts`: 1 suite, 5 tests passed, exit 0.
- `./node_modules/.bin/tsc --noEmit -p applications/mail/tsconfig.json`: exit 0 after final edits.
- `git diff --check`: exit 0.
