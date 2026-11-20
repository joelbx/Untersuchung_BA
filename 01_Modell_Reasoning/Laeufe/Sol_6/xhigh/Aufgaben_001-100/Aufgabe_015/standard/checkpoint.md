# Checkpoint

Task: Add application feature flag control for reciprocal QR sign in.

Plan: inspect existing settings and QR sign in components, implement the flag and visibility checks, update relevant tests, run existing tests.

Implemented: registered `feature_qr_signin_reciprocate_show` as an experimental setting with a disabled default and homeserver compatibility description. Gated the QR section and both settings tabs, including their active QR views. Added enabled, disabled, and close flow coverage in the existing component tests.

Verification: 3 relevant Jest suites passed (60 tests, 8 snapshots); `git diff --check`, Prettier, and ESLint passed. Full `tsc --noEmit --jsx react` reports an existing error in untouched `test/components/structures/RoomView-test.tsx:178` (missing `eventId`).
