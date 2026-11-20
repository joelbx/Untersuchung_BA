# Checkpoint

Issue: duplicate Kick, Ban, and Mute activations in the user info panel.

Implemented a member-scoped synchronous action guard shared by all three controls. It starts before confirmation, sets `disabled` and `aria-disabled`, awaits confirmation and the operation, then releases on success, cancel, or failure. Errors open one dialog. The guard remounts when the selected room/member changes.

Tests: added regression coverage in `test/components/views/right_panel/UserInfo-test.tsx` for rapid click and keyboard activation during confirmation, cancellation without requests, and pending mute/failure recovery. The first test was observed failing before production changes because controls were not disabled. The focused suite passes (70/70). Scoped ESLint, Prettier, and `git diff --check` pass.

Environment: `rg` unavailable (`/bin/bash: rg: command not found`); used local `find` and `grep`. `./node_modules/.bin/tsc --noEmit --jsx react` fails on existing errors outside the changed files, including missing dependency declarations for uuid/content-type/sdp-transform and SDK API mismatches in OIDC and VerificationPanel. No type error in changed files was reported. No downloads attempted.

Full suite command: `./node_modules/.bin/jest --runInBand --silent` is running. It has reported `test/components/structures/TimelinePanel-test.tsx` failure (`updates thread previews`: unable to find `ReplyEvent1`); final totals pending.

Final verification: full Jest run completed with 475 passing suites and 3 failing suites (4596 passing tests, 5 failing tests, 29 skipped, 2 todo). Failing suites/tests:
- `test/components/structures/TimelinePanel-test.tsx`: `updates thread previews` cannot find `ReplyEvent1`.
- `test/utils/oidc/authorize-test.ts`: `startOidcLogin() navigates to authorization endpoint with correct parameters` fails because `generateOidcAuthorizationUrl` is not a function.
- `test/stores/widgets/StopGapWidget-test.ts`: `should replace parameters in widget url template`, `feeds incoming to-device messages to the widget`, and `should pause the current voice broadcast recording` all fail with `No iframe supplied`.
The changed UserInfo suite passed in the full run and separately (70/70). Final scoped ESLint, Prettier check, and `git diff --check` passed.
