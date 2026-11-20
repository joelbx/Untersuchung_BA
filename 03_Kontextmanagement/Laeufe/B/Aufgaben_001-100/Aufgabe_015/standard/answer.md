Implemented the disabled-by-default `feature_qr_signin_reciprocate_show` setting with a homeserver compatibility description. QR sign-in now appears in both settings tabs only when the flag is enabled and the server supports MSC3882 and MSC3886.

All 60 targeted tests pass; ESLint and the diff check pass. The full TypeScript check still reports an error in the untouched `RoomView-test.tsx`.