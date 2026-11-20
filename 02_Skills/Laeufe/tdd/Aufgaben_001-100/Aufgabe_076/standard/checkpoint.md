# Checkpoint

Task: normalize address separator splitting and recipient conversion using test-driven development.

Status: added regression tests and implemented the shared address helpers. `rg` is unavailable (`/bin/bash: rg: command not found`); using local git grep/find.

RED: `yarn workspace @proton/shared test -- --grep 'address input'` could not launch Chrome: `Can not find the binary /root/.cache/ms-playwright/chromium-1041/chrome-linux/chrome`. Re-ran with the installed `/usr/bin/chromium` linked under `/tmp/codex-playwright` and `PLAYWRIGHT_BROWSERS_PATH=/tmp/codex-playwright`. The new tests failed as expected: `splitBySeparator is not a function` and bracketed email `Name` was `''` instead of the address. That command ran all 838 specs despite `--grep`; two unrelated baseline failures were `cookie helper > should expire cookies` and `toBase64 > should be an empty base64 on undefined file`.

GREEN: `PLAYWRIGHT_BROWSERS_PATH=/tmp/codex-playwright yarn workspace @proton/shared test` ran 838 specs. All three new address specs passed; 836 passed total and the same two baseline specs failed. `yarn workspace @proton/shared check-types` passed. Both autocomplete paste handlers now use `splitBySeparator` for completed addresses. `yarn workspace @proton/components test` passed (62 suites passed, 2 skipped; 304 tests passed, 10 skipped). `yarn workspace @proton/components check-types` passed. `yarn prettier --check` passed for the four changed source/test files.
