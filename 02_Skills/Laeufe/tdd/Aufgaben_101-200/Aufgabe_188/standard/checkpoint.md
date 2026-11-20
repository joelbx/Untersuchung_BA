# Checkpoint

Task: centralize storage size units in `/app`.
Status: implementation complete.

TDD: `yarn workspace @proton/components test --runInBand --watch=false containers/members/MemberStorageSelector.test.ts` failed as expected before implementation: Drive Pro and Drive Business returned 1,073,741,824,000 bytes rather than 1,099,511,627,776 bytes. After implementation, the selector and CSV test files passed (66 tests, 5 snapshots).

Verification:
- `yarn workspace @proton/components test --runInBand --watch=false`: passed, 152 suites / 1,193 tests; 2 suites and 28 tests skipped.
- `node_modules/.bin/prettier --check` on all changed TypeScript files: passed.
- `git diff --check`: passed.
- `yarn workspace @proton/shared check-types` and `yarn workspace @proton/components check-types` both failed in existing `packages/crypto/lib/worker/api.ts:579`: incompatible `openpgp` and nested `pmcrypto/node_modules/openpgp` `PartialConfig` types. The storage changes do not touch that file; type checking remains unconfirmed.
- `yarn workspace @proton/shared test` compiled successfully but Karma could not start ChromeHeadless: `Can not find the binary /root/.cache/ms-playwright/chromium-1124/chrome-linux/chrome`. Local `/usr/bin/chromium-browser --version` also fails because the chromium snap is not installed. Shared tests remain unexecuted.
- `rg` unavailable (`/bin/bash: rg: command not found`); used `git grep`.
