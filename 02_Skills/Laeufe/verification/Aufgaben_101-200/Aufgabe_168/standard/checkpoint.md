# Checkpoint

Task: prevent duplicate Kick, Ban, and Mute actions in the user info panel.

Implemented a synchronous ref guard and shared pending state for the selected room member. The lock starts before confirmation and clears after cancellation, success, or failure. All three buttons receive `disabled`; AccessibleButton supplies `aria-disabled="true"`. Errors are reported once by the shared action runner.

Verification:
- `./node_modules/.bin/jest test/components/views/right_panel/UserInfo-test.tsx --runInBand --silent`: 70 tests passed (final run after formatting).
- `./node_modules/.bin/prettier --check src/components/views/right_panel/UserInfo.tsx test/components/views/right_panel/UserInfo-test.tsx`: passed after formatting.
- `./node_modules/.bin/eslint src/components/views/right_panel/UserInfo.tsx test/components/views/right_panel/UserInfo-test.tsx`: passed.
- `git diff --check`: passed.
- `./node_modules/.bin/tsc --noEmit --jsx react --pretty false`: exit 2 due existing errors outside changed files, including missing declarations for uuid, content-type, and sdp-transform in matrix-js-sdk, and unrelated OIDC/verification type errors. No errors were reported for the changed files. Full typecheck remains uncertain because of these repository dependency and baseline errors.
