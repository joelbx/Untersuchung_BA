# Checkpoint

Task: replace inline `height` values containing `vh` with `auto` in email HTML after `transformStylesheet` and before `transformRemote`.

Changes: added `transformStyleAttributes`, wired it into `prepareHtml`, and added a focused test for root and nested elements, calc values, `!important`, and unaffected declarations.

Checks:
- `../../node_modules/.bin/jest --runInBand --coverage=false --watch=false src/app/helpers/transforms/tests` from `/app/applications/mail`: exit 0; 6 suites, 90 tests passed.
- `../../node_modules/.bin/eslint src/app/helpers/transforms/transformStyleAttributes.ts src/app/helpers/transforms/transforms.ts src/app/helpers/transforms/tests/transformStyleAttributes.test.ts --quiet` from `/app/applications/mail`: exit 0.
- `../../node_modules/.bin/prettier --check src/app/helpers/transforms/transformStyleAttributes.ts src/app/helpers/transforms/transforms.ts src/app/helpers/transforms/tests/transformStyleAttributes.test.ts` from `/app/applications/mail`: exit 0.
- `git diff --check` from `/app`: exit 0.
- `../../node_modules/.bin/tsc --noEmit --pretty false` from `/app/applications/mail`: exit 134, `FATAL ERROR: Reached heap limit Allocation failed - JavaScript heap out of memory` at about 2 GB. Type checking remains uncertain pending retry with a larger heap.
- `NODE_OPTIONS=--max-old-space-size=6144 ../../node_modules/.bin/tsc --noEmit --pretty false` from `/app/applications/mail`: exit 0, no diagnostics. The initial heap-limit uncertainty is resolved.
