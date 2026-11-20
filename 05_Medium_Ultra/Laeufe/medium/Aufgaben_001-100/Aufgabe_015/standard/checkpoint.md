Task: gate Sign in with QR behind feature_qr_signin_reciprocate_show.
Status: implementation and targeted tests complete.
Changes: registered experimental setting with disabled default and homeserver compatibility description; gated QR section and both settings tabs; added enabled/disabled tests.
Verification: 3 targeted Jest suites passed (60 tests, 8 snapshots); Prettier and git diff --check passed. Full TypeScript check found an unrelated existing error in test/components/structures/RoomView-test.tsx:178 (missing eventId). ESLint on edited files passed.
