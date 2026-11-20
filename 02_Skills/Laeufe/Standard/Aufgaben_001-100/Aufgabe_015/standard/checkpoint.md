# Checkpoint

Task: gate QR sign-in behind `feature_qr_signin_reciprocate_show` with a disabled default.

Implemented: registered an experimental Labs flag with MSC3882/MSC3886 compatibility text; gated `LoginWithQRSection`, `SecurityUserSettingsTab`, and `SessionManagerTab`; updated English source strings and QR settings tests.

Validation: `./node_modules/.bin/jest --runInBand test/components/views/settings/devices/LoginWithQRSection-test.tsx test/components/views/settings/tabs/user/SecurityUserSettingsTab-test.tsx test/components/views/settings/tabs/user/SessionManagerTab-test.tsx` passed (3 suites, 60 tests, 8 snapshots). It emitted existing React act warnings and a mock crypto error during QR flow tests. `./node_modules/.bin/eslint` on changed TS/TSX files passed. `./node_modules/.bin/prettier --check` on changed TS/TSX files passed after formatting. `git diff --check` passed. Project-wide TypeScript check failed on an unrelated existing test type error detailed below.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used `grep`/`find` instead.

TypeScript check: `./node_modules/.bin/tsc --noEmit --jsx react` exited 2 on an unrelated existing type error: `test/components/structures/RoomView-test.tsx(178,65): error TS2345: Argument of type '{ roomId: string; }' is not assignable to parameter of type '{ roomId: string; eventId: string; }'. Property 'eventId' is missing in type '{ roomId: string; }' but required in type '{ roomId: string; eventId: string; }'.` This prevents a clean project-wide type-check result; changed files passed ESLint and targeted Jest suites.
