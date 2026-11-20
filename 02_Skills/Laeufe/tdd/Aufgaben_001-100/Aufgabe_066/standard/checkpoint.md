# Checkpoint

Task: replace inline `height` values using `vh` with `auto` in mail HTML preparation, between stylesheet and remote transforms.

Status: added an integration regression test before production changes. It failed as expected (`height` was `100vh` instead of `auto`), then passed after adding `transformStyleAttributes` and wiring it between stylesheet and remote transforms.

Environment: `rg` is unavailable (`/bin/bash: rg: command not found`); using `find` and `grep` for repository inspection.

Checks: focused Jest test passed; all six transform suites passed (90 tests). Full direct Jest run passed: 117 suites, 994 tests passed, 2 skipped, 32 snapshots passed. The initial command `./node_modules/.bin/jest src/app/helpers/transforms/tests/transforms.test.ts --runInBand --coverage=false --silent` from `applications/mail` failed because that workspace has no local Jest binary; `/app/node_modules/.bin/jest` worked. `npm test -- --coverage=false` failed before running Jest with `TypeError: Cannot read properties of undefined (reading 'stdin')`; direct `/app/node_modules/.bin/jest --runInBand --logHeapUsage --forceExit --coverage=false --silent` passed. `/app/node_modules/.bin/tsc --noEmit --pretty false` exited 134 after V8 `Allocation failed - JavaScript heap out of memory` near the default 2 GB heap; retry with `NODE_OPTIONS=--max-old-space-size=4096` passed. Targeted ESLint, Prettier, and `git diff --check` passed. Full Jest emitted OpenPGP asm.js warnings and a force-exit notice.

Result: the new transform walks the root and descendants with inline styles, replaces viewport based `height` with `auto`, preserves other style properties and the height priority, and runs after `transformStylesheet` and before `transformRemote`.
