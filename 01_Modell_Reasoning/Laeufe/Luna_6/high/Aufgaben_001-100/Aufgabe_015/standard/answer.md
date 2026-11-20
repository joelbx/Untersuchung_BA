Added the `feature_qr_signin_reciprocate_show` Experimental setting, defaulting to disabled, and gated QR sign-in in both settings tabs and `LoginWithQRSection`. Updated existing QR tests to enable the flag when checking the flow.

The focused suites passed: **57 tests across 3 suites**. Prettier and ESLint passed. `yarn lint:types` encountered an unrelated existing error in `RoomView-test.tsx:178` because `eventId` is missing.

Key changes: [Settings.tsx](/app/src/settings/Settings.tsx:499), [LoginWithQRSection.tsx](/app/src/components/views/settings/devices/LoginWithQRSection.tsx:36), [SessionManagerTab.tsx](/app/src/components/views/settings/tabs/user/SessionManagerTab.tsx:283), [SecurityUserSettingsTab.tsx](/app/src/components/views/settings/tabs/user/SecurityUserSettingsTab.tsx:396).