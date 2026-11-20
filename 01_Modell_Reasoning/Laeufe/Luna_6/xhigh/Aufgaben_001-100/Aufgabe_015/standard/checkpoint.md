# Checkpoint

Task: Add application feature-flag control for QR sign-in (`feature_qr_signin_reciprocate_show`), default disabled, and ensure QR UI and flow require the flag plus MSC3882/MSC3886 support.

Implemented:
- Registered the feature in Experimental Labs, defaulting to disabled, with a homeserver MSC compatibility description.
- Gated `LoginWithQRSection` and both settings tabs on the flag, including the QR flow view.
- Updated existing QR component/tab tests to cover disabled and enabled states; added the new description to English strings.

Verification: The three focused Jest suites passed (60 tests, 8 snapshots). The broad session manager suite logs pre-existing React/test fixture warnings.

Final checks:
- Focused Jest suites: pass (60 tests, 8 snapshots).
- ESLint on changed TS/TSX files: pass.
- Prettier on changed source, tests, and English strings: pass.
- `tsc --noEmit --jsx react`: reports an unrelated existing error in `test/components/structures/RoomView-test.tsx:178` (missing required `eventId`).
