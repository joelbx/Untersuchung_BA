Added the disabled-by-default `feature_qr_signin_reciprocate_show` setting to Experimental Labs, with a description requiring MSC3882 and MSC3886 support. The shared QR section and both settings tabs now gate the section and QR flow on that setting.

Updated the existing QR tests for enabled and disabled states. The flow continues to expose `data-testid="login-with-qr"` when opened.

**Verification:** All 3 focused Jest suites passed (60 tests, 8 snapshots); ESLint and Prettier passed. TypeScript checking is blocked by an unrelated existing error in `RoomView-test.tsx:178` (missing `eventId`).

Key changes: [Settings.tsx](/app/src/settings/Settings.tsx:499), [LoginWithQRSection.tsx](/app/src/components/views/settings/devices/LoginWithQRSection.tsx:35), [SessionManagerTab.tsx](/app/src/components/views/settings/tabs/user/SessionManagerTab.tsx:133).