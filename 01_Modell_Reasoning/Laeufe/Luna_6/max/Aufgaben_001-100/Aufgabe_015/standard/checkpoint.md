# Checkpoint

Task: add application-level control for QR sign-in visibility using `feature_qr_signin_reciprocate_show`, default disabled, and verify the QR flow in the relevant existing tests.

Completed: added the disabled-by-default experimental setting and compatibility description; gated the QR section and both settings tabs on the setting plus required MSC support; updated coverage for disabled/enabled visibility, opening the QR view, and the disabled default.

Validation: 4 focused Jest suites passed (62 tests); ESLint and Prettier passed. `yarn lint:types` reported one unrelated existing error at `test/components/structures/RoomView-test.tsx:178` (missing `eventId`).
