# Checkpoint

Task: replace inline `height` values containing `vh` with `auto` in mail HTML, after `transformStylesheet` and before `transformRemote`.

Root cause: `prepareHtml` invoked `transformStylesheet` and then `transformRemote` without a pass over inline height styles. `transformStylesheet` only adjusts absolute positioning on the first child. Existing transforms use DOM selectors and mutate the supplied root in place.

Regression: `transformStyleAttributes.test.ts` initially failed with `Expected: "auto"; Received: "100vh"` using an empty transform. It now passes for root and nested styles, `calc(...)`, `!important`, and preservation of unrelated properties. The new pass is invoked at the required pipeline location.

Checks:
- `node_modules/.bin/jest --config applications/mail/jest.config.js --runInBand --coverage=false applications/mail/src/app/helpers/transforms/tests`: passed, 6 suites and 90 tests.
- `node_modules/.bin/eslint applications/mail/src/app/helpers/transforms/transformStyleAttributes.ts applications/mail/src/app/helpers/transforms/transforms.ts applications/mail/src/app/helpers/transforms/tests/transformStyleAttributes.test.ts --no-cache`: passed.
- `git diff --check`: passed.
- `node_modules/.bin/tsc --project applications/mail/tsconfig.json --noEmit --pretty false`: failed with exit 134, `FATAL ERROR: Reached heap limit Allocation failed - JavaScript heap out of memory` near 2 GB. Full type-check status remains unverified.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); local `grep`/`find` used. No dependencies downloaded.
