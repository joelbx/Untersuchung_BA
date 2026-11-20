# Checkpoint

Task: add `.well-known` `io.element.e2ee.force_disable` policy for new room encryption.
Status: implementation complete in checked-out files; no delegation used.
Changes: typed well-known field, synchronous force-disable helper, policy resolution with server precedence and conflict warning, private-room default override, dialog value/interactivity and submission alignment, focused tests.
Validation: Jest 3 suites / 31 tests passed; ESLint and Prettier passed on changed files. Full `tsc --noEmit --jsx react` fails at untouched `src/Unread.ts:167` because `Thread | Room` lacks `getLastUnthreadedReceiptFor` on `Thread`.
