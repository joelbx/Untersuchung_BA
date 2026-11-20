# Checkpoint

Implemented `feature_qr_signin_reciprocate_show` as an experimental setting, default `false`, with a homeserver compatibility description. `LoginWithQRSection` now requires the setting plus MSC3882 and MSC3886. Both settings tabs gate the section. Updated focused tests for enabled and disabled behavior.

Verification:
- `yarn jest --runInBand test/components/views/settings/devices/LoginWithQRSection-test.tsx test/components/views/settings/tabs/user/SecurityUserSettingsTab-test.tsx test/components/views/settings/tabs/user/SessionManagerTab-test.tsx`: exit 0, 3 suites/60 tests/8 snapshots passed (console warnings from existing test fixtures).
- `./node_modules/.bin/eslint ...` on the seven edited source/test files: exit 0.
- `./node_modules/.bin/prettier --check ...` on the seven edited source/test files: exit 0.
- `git diff --check`: exit 0.
- `yarn lint:types`: exit 2. Error: `test/components/structures/RoomView-test.tsx(178,65): error TS2345: Argument of type '{ roomId: string; }' is not assignable to parameter of type '{ roomId: string; eventId: string; }'. Property 'eventId' is missing in type '{ roomId: string; }' but required in type '{ roomId: string; eventId: string; }'.` This file was not edited in this task; full type check remains unverified.
- `rg` unavailable: `/bin/bash: rg: command not found`; used local grep/find.

Final focused test rerun after formatting: `yarn jest --runInBand --silent test/components/views/settings/devices/LoginWithQRSection-test.tsx test/components/views/settings/tabs/user/SecurityUserSettingsTab-test.tsx test/components/views/settings/tabs/user/SessionManagerTab-test.tsx`: exit 0, 3 suites/60 tests/8 snapshots passed.
