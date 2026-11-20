# Checkpoint

Implemented calendar URL validation in SubscribeCalendarModal with MAX_LENGTHS_API.CALENDAR_URL = 10000, one ordered warning function, disabled submit state, and removal of the URL counter and input maxLength. Input trimming is retained. ResizeObserver Jest mocks are in shared setup files for components, calendar, and mail; inline test assignments were removed.

TDD: the new modal regression test first failed because overlength URLs showed no warning. After setup changes it failed for that expected behavior. A second malformed-overlength test failed because the Invalid URL error hid the length warning; this was fixed. Focused modal suite passes (5 tests).

Checks passed:
- Components Jest suite: 35 suites passed, 135 tests passed, 1 skipped.
- Calendar Jest suite: 16 suites passed, 126 tests passed.
- Mail Jest suite: 76 suites passed, 696 tests passed, 1 skipped, 32 snapshots passed. Jest emitted existing OpenPGP asm.js warnings and an open-handle notice after completion; exit code 0.
- Components TypeScript: `./node_modules/.bin/tsc --noEmit -p packages/components/tsconfig.json`.
- `git diff --check` and Prettier check on modified implementation/setup files.
- Focused modal test rerun after test cleanup: 5 passed.
