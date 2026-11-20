Task: implement .well-known force_disable for new room encryption.
Status: complete. Added typed policy field, synchronous force-disable utility, private default precedence, shared server/.well-known permission helper, and dialog effective-state handling. Added policy and dialog tests.
Verification: focused Jest suites passed (28 tests); ESLint, Prettier, and git diff --check passed. Full TypeScript check is blocked by an existing unrelated src/Unread.ts:167 error (Thread lacks getLastUnthreadedReceiptFor).
Constraints observed: local code/tests only; no history/index/harness changes.
