VERDICT: FIX

The applied address parsing changes match the stated requirements on review; I found no code defect. The relevant shared test suite did not pass:

- `yarn workspace @proton/shared test --grep recipient` exited 1 because Karma could not find its configured Playwright Chromium binary.
- A rerun using the installed `/usr/bin/chromium` executed 837 tests: 835 passed and 2 failed in unrelated `toBase64` and cookie tests.

**TEST_ENVIRONMENT_PROBLEM:** Configure Karma to use the available browser, resolve the two browser dependent failures, and rerun the shared suite. Details are in [checkpoint.md](/app/.codex-role-output/checkpoint.md).