Task: unify device verification status rendering.
Status: implemented and verified.
Changes: added DeviceVerificationStatusCard; CurrentDeviceSection and DeviceDetails use it; DeviceDetails accepts DeviceWithVerification; updated tests and snapshots.
Validation: 3 focused Jest suites passed (12 tests, 6 snapshots); ESLint on changed source/tests passed; git diff --check passed. Full TypeScript check reports existing matrix-js-sdk and unrelated widget/receipt errors, with no errors in changed device files.
