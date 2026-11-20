# Checkpoint

Task: fix mailbox element list reload timing, pending backend action tracking, and stale/failure retry handling.

Completed:
- Added pending backend action state and lifecycle actions, preserving its count across list parameter resets.
- Guarded mailbox requests until pending actions finish and made loading account for request intent, page, and query params.
- Added distinct delayed retries for request failures (2s) and stale responses (1s); stale results are rejected before list state can commit them.
- Tracked label, move, star, read/unread, delete, and empty-label operations through their backend/event refresh work. Concurrent label and undo requests are awaited through settlement.

Verification:
- `yarn workspace proton-mail test --runTestsByPath src/app/containers/mailbox/tests/Mailbox.elements.test.tsx --watch=false --coverage=false` — passed (12 tests; Jest emitted its existing open-handle notice after completion).
- `yarn workspace proton-mail check-types --pretty false` — passed.
- ESLint on changed TypeScript files — passed.
- `git diff --check` — passed.
