# Checkpoint

Implemented `.well-known` `io.element.e2ee.force_disable` support for new-room encryption decisions. Added `shouldForceDisableEncryption`, `checkUserIsAllowedToChangeEncryption`, policy-aware private defaults, and dialog state/submit handling. Added focused tests for forced values, policy conflicts, and non-boolean settings.

Checks:
- `./node_modules/.bin/jest --runInBand --silent test/createRoom-test.ts test/components/views/dialogs/CreateRoomDialog-test.tsx` — passed: 2 suites, 29 tests.
- `./node_modules/.bin/eslint src/createRoom.ts src/utils/WellKnownUtils.ts src/utils/room/shouldForceDisableEncryption.ts src/utils/rooms.ts src/components/views/dialogs/CreateRoomDialog.tsx test/createRoom-test.ts test/components/views/dialogs/CreateRoomDialog-test.tsx` — passed.
- `./node_modules/.bin/prettier --check src/createRoom.ts src/utils/WellKnownUtils.ts src/utils/room/shouldForceDisableEncryption.ts src/utils/rooms.ts src/components/views/dialogs/CreateRoomDialog.tsx test/createRoom-test.ts test/components/views/dialogs/CreateRoomDialog-test.tsx` — passed.
- `git diff --check` — passed.
- `./node_modules/.bin/tsc --noEmit --jsx react` — failed on unrelated existing error: `src/Unread.ts(167,46): error TS2339: Property 'getLastUnthreadedReceiptFor' does not exist on type 'Thread | Room'. Property 'getLastUnthreadedReceiptFor' does not exist on type 'Thread'.` TypeScript verification of the full repository remains uncertain until that error is resolved.

Tooling: `rg` was unavailable (`/bin/bash: rg: command not found`); used local `find` and `grep` for discovery.
