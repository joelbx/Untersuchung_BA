# Checkpoint

Task: Add `.well-known` `io.element.e2ee.force_disable` encryption policy for new rooms.

Implemented: well-known type, strict force-disable helper, private-room default precedence, shared server/well-known policy resolution, dialog enforced state and pending disabled control, focused tests.

Verification:
- `./node_modules/.bin/jest --runInBand --silent test/createRoom-test.ts test/components/views/dialogs/CreateRoomDialog-test.tsx` passed: 2 suites, 28 tests (after fixture fix; before final formatting).
- `./node_modules/.bin/eslint src/createRoom.ts src/utils/WellKnownUtils.ts src/utils/rooms.ts src/utils/room/shouldForceDisableEncryption.ts src/components/views/dialogs/CreateRoomDialog.tsx test/createRoom-test.ts test/components/views/dialogs/CreateRoomDialog-test.tsx` exited 0.
- `./node_modules/.bin/tsc --noEmit --jsx react` exited 2: `src/Unread.ts(167,46): error TS2339: Property 'getLastUnthreadedReceiptFor' does not exist on type 'Thread | Room'. Property 'getLastUnthreadedReceiptFor' does not exist on type 'Thread'.` This is outside the edited files; full type-check remains uncertain.
- `git diff --check` exited 0.

Final verification after all edits:
- `./node_modules/.bin/jest --runInBand --silent test/createRoom-test.ts test/components/views/dialogs/CreateRoomDialog-test.tsx` exited 0: 2 suites, 28 tests passed.
- `./node_modules/.bin/prettier --check src/createRoom.ts src/utils/WellKnownUtils.ts src/utils/rooms.ts src/utils/room/shouldForceDisableEncryption.ts src/components/views/dialogs/CreateRoomDialog.tsx src/i18n/strings/en_EN.json test/createRoom-test.ts test/components/views/dialogs/CreateRoomDialog-test.tsx` exited 0.
- `git diff --check` exited 0.
