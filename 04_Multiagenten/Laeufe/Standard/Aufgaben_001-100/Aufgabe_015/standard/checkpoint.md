Issue: Gate QR sign-in by feature_qr_signin_reciprocate_show.
Status: Complete. Added experimental setting (default false, MSC3882/MSC3886 compatibility description), gated LoginWithQRSection and both tab entry points, and updated enabled/disabled tests.
Verification: 3 relevant Jest suites passed (60 tests, 8 snapshots); edited files passed ESLint and Prettier; git diff --check passed. Full TypeScript check remains blocked by an existing error in untouched test/components/structures/RoomView-test.tsx:178 (missing eventId).
