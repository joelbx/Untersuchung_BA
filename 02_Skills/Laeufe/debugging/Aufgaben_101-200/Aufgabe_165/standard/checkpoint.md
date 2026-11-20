# Checkpoint

Task: add `.well-known` `force_disable` policy to new room encryption and UI.

Root cause: the dialog checked only server force-enable, initialized the toggle as changeable, and substituted `true` when submitting a disabled toggle. The room default helper read only `.well-known` `default`.

Implemented: added the well-known field, a strict synchronous policy reader, a shared async server/well-known decision helper with server precedence and conflict warning, policy-driven dialog state and submission, and regression tests. The dialog waits for the policy before submitting private rooms.

Verification: the pre-fix regression run failed as expected for missing helpers and incorrect toggle behavior. A separate pre-fix immediate-submit test showed submission with encryption true before force-disable was resolved. Final targeted test, ESLint and Prettier runs are in progress.

Type-check limitation: `./node_modules/.bin/tsc --noEmit --jsx react` exited 2 with `src/Unread.ts(167,46): error TS2339: Property 'getLastUnthreadedReceiptFor' does not exist on type 'Thread | Room'. Property 'getLastUnthreadedReceiptFor' does not exist on type 'Thread'.` This is in an untouched file, so the full type check cannot currently certify the change.

Final verification: `./node_modules/.bin/jest --runInBand --silent test/components/views/dialogs/CreateRoomDialog-test.tsx test/createRoom-test.ts test/utils/rooms-test.ts` exited 0 (3 suites, 32 tests). ESLint on changed TypeScript files exited 0. Prettier check on changed source and test files exited 0. `git diff --check` exited 0.
