# Checkpoint

Implemented QR sign-in feature flag control.

- Registered `feature_qr_signin_reciprocate_show` as an Experimental Labs feature, defaulting to disabled, with a homeserver MSC3882/MSC3886 compatibility description.
- Gated QR section rendering in `LoginWithQRSection` and both settings tabs.
- Updated existing QR tests to enable the flag when testing enabled behavior.

Verification:
- Focused Jest suites: 3 suites, 57 tests passed.
- Prettier and ESLint on changed source and test files passed.
- `yarn lint:types` is blocked by an existing unrelated TypeScript error in `test/components/structures/RoomView-test.tsx:178` (missing required `eventId`).
