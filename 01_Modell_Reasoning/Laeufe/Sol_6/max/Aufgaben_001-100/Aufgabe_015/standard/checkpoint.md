# Checkpoint

- Task: Gate QR sign-in UI behind `feature_qr_signin_reciprocate_show` and add the disabled-by-default experimental setting.
- Status: Complete. Added the disabled-by-default experimental setting, gated all three QR sign-in render paths, and tested opening and closing the QR view.
- Verification: 4 focused Jest suites passed (65 tests, 9 snapshots); targeted ESLint and Prettier passed.
- TypeScript check: One pre-existing error remains in untouched `test/components/structures/RoomView-test.tsx:178` (missing `eventId` in a `roomId` argument).
