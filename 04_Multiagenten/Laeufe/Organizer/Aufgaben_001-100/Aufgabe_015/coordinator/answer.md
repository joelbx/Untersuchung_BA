Added the disabled-by-default `feature_qr_signin_reciprocate_show` Labs setting with a description of the MSC3882 and MSC3886 homeserver requirements. Both settings tabs and `LoginWithQRSection` now require the flag; the section also requires both server capabilities. When enabled, the existing “Show QR code” action opens the QR login view.

All 60 tests in the three relevant suites passed, along with targeted ESLint and Prettier checks. The full TypeScript check remains blocked by an unrelated existing error in `RoomView-test.tsx:178`.

No delegation was used.