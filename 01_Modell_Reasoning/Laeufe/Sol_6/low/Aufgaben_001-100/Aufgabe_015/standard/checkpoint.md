# Checkpoint

Implemented `feature_qr_signin_reciprocate_show` as a disabled-by-default experimental setting with a homeserver compatibility description. Both settings tabs and the shared QR section check the flag; existing MSC3882 and MSC3886 checks remain. Updated QR tests for enabled and disabled behavior.

Verification: 3 relevant Jest suites passed (59 tests). `yarn lint:types` reports an unrelated existing error in `test/components/structures/RoomView-test.tsx:178` (missing eventId). `git diff --check` passed.
