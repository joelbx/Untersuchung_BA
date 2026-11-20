# Checkpoint

Task: gate QR sign-in with `feature_qr_signin_reciprocate_show`.
Status: implementation and relevant tests complete.
Changes: disabled-by-default experimental setting with MSC3882/MSC3886 description; shared section and both settings tabs check the flag; enabled/disabled tests updated.
Verification: 3 Jest suites passed (60 tests), Prettier and git diff checks passed. Full TypeScript check reports an existing unrelated error in `test/components/structures/RoomView-test.tsx:178` (missing `eventId`).
