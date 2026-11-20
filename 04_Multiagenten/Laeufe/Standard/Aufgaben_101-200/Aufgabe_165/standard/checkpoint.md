# Checkpoint

Task: implement well-known E2EE force_disable for new rooms, UI, and shared policy helper.
Status: complete.
Changes: added typed well-known flag and synchronous reader; updated private-room default; added shared async server/well-known decision with server precedence and conflict warning; updated CreateRoomDialog to lock during policy resolution, display enforced value, and submit displayed value; added focused coverage.
Verification: 30 focused tests passed; ESLint and Prettier passed for touched files; git diff --check passed. Full TypeScript check reports a pre-existing error at src/Unread.ts:167 (getLastUnthreadedReceiptFor on Thread | Room).
