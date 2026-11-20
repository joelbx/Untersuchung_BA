# Checkpoint

Task: add disabled-by-default `feature_qr_signin_reciprocate_show` control to QR sign-in surfaces.

Status: implemented in `Settings.tsx`, `LoginWithQRSection`, `SecurityUserSettingsTab`, and `SessionManagerTab`. Existing QR tests updated for enabled and disabled states.

Verification: 3 targeted Jest suites passed (60 tests, 8 snapshots); targeted ESLint and Prettier passed; `git diff --check` passed. Full TypeScript check fails at existing unrelated `test/components/structures/RoomView-test.tsx:178` due to missing `eventId`.

Delegation: none.
