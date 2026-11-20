# Checkpoint

Task: Add `.well-known` `force_disable` encryption policy for new rooms.

Plan: inspect existing policy and dialog behavior, write failing tests, implement minimal changes, run focused and full test suites.

Status: implementation and regression tests complete. Watched dialog tests fail for unlocked pending state, forced-off state, and submission before policy resolution; watched policy tests fail before the new helpers existed. Focused and full verification completed.

Verification:
- `node_modules/.bin/jest --runInBand --silent test/utils/room/shouldForceDisableEncryption-test.ts test/components/views/dialogs/CreateRoomDialog-test.tsx test/createRoom-test.ts`: 3 suites, 33 tests passed.
- `node_modules/.bin/jest --runInBand --silent`: 470 suites passed, 1 failed; 4,459 tests passed, 3 failed, 29 skipped, 2 todo. The only failing suite was `test/stores/widgets/StopGapWidget-test.ts`, with three tests failing `No iframe supplied` from `ClientWidgetApi`. Running that suite alone with `node_modules/.bin/jest --runInBand --silent test/stores/widgets/StopGapWidget-test.ts` reproduced all three failures. This suite is unrelated to the encryption policy changes.
- `node_modules/.bin/eslint` on all changed source and test files: passed.
- `node_modules/.bin/prettier --check` on all changed source and test files: passed.

Type check: `node_modules/.bin/tsc --noEmit --jsx react` exited 2 and reported `src/Unread.ts(167,46): error TS2339: Property 'getLastUnthreadedReceiptFor' does not exist on type 'Thread | Room'`. This is outside the changed paths.
