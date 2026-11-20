# QR sign-in feature flag checkpoint

- Issue: gate reciprocal QR sign-in in settings and QR section with `feature_qr_signin_reciprocate_show`.
- Implemented a disabled-by-default Labs setting with an MSC3882/MSC3886 compatibility description.
- Both settings tabs and the shared QR section check the flag; the shared section still requires both server capabilities.
- Relevant Jest suites: 3 passed, 60 tests passed. Changed-file ESLint and Prettier checks passed.
- Full TypeScript check is blocked by an existing unrelated error in `test/components/structures/RoomView-test.tsx:178` (missing `eventId`).
