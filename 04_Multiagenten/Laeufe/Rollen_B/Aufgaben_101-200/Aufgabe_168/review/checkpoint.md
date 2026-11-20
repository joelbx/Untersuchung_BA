VERDICT: FIX
Independent review complete. No code defect found in the applied UserInfo admin-action lock. The ref guards repeat activation before React renders disabled and aria-disabled; the provider shares pending state across Kick, Ban, and Mute; cancellation and failure release it.

Tests/checks:
- `./node_modules/.bin/jest --runInBand test/components/views/right_panel/UserInfo-test.tsx`: PASS, 70 tests, 6 snapshots. Output included React act warnings.
- `./node_modules/.bin/eslint --max-warnings 0 src/components/views/right_panel/UserInfo.tsx test/components/views/right_panel/UserInfo-test.tsx`: PASS.
- `./node_modules/.bin/prettier --check src/components/views/right_panel/UserInfo.tsx test/components/views/right_panel/UserInfo-test.tsx`: PASS.
- `./node_modules/.bin/tsc --noEmit --jsx react`: FAIL, exit 2. TEST_ENVIRONMENT_PROBLEM: missing declarations for uuid/content-type/sdp-transform and matrix-js-sdk API mismatches in files outside this patch (e.g. VerificationPanel.tsx, oidc/authorize.ts); no diagnostics in either changed file. Align installed SDK/declarations with the repository lockfile, then rerun the TypeScript check.

No project code or tests were edited during review.
