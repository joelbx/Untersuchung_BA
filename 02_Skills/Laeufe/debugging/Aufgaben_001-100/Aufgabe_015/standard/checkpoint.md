# Checkpoint

Issue: QR sign in visibility lacks application feature flag.
Assigned process: systematic debugging.

Root cause: `LoginWithQRSection` required only MSC3882 and MSC3886. Both settings tabs rendered the section regardless of an application feature value. `feature_qr_signin_reciprocate_show` did not exist in `SETTINGS`. Existing feature definitions show the registry pattern for experimental, device/config controlled flags.

Reproduction: Added disabled flag regression tests for the shared section and both tabs. Before the fix, `./node_modules/.bin/jest --runInBand test/components/views/settings/devices/LoginWithQRSection-test.tsx test/components/views/settings/tabs/user/SecurityUserSettingsTab-test.tsx test/components/views/settings/tabs/user/SessionManagerTab-test.tsx --silent` failed in those three new cases because the QR heading appeared.

Fix: Register the experimental feature with default false and MSC compatibility description. Check the setting in the shared section and both tabs. Existing enabled feature tests confirm the QR action enters `LoginWithQR` via `data-testid="login-with-qr"`.

Verification: The same targeted Jest command passed (3 suites, 60 tests, 8 snapshots). Prettier check of changed files and `git diff --check` passed.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); used local `find`/`grep`.

Type check: `./node_modules/.bin/tsc --noEmit --jsx react` failed with an unrelated existing error: `test/components/structures/RoomView-test.tsx(178,65): error TS2345: Argument of type '{ roomId: string; }' is not assignable to parameter of type '{ roomId: string; eventId: string; }'. Property 'eventId' is missing in type '{ roomId: string; }' but required in type '{ roomId: string; eventId: string; }'.` Type check is therefore not fully green; this error is outside the edited paths.
Changed-file ESLint command passed: `./node_modules/.bin/eslint src/settings/Settings.tsx src/components/views/settings/devices/LoginWithQRSection.tsx src/components/views/settings/tabs/user/SecurityUserSettingsTab.tsx src/components/views/settings/tabs/user/SessionManagerTab.tsx test/components/views/settings/devices/LoginWithQRSection-test.tsx test/components/views/settings/tabs/user/SecurityUserSettingsTab-test.tsx test/components/views/settings/tabs/user/SessionManagerTab-test.tsx --max-warnings 0`.
