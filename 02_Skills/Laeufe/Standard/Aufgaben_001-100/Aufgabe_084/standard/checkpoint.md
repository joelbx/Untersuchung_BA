# Checkpoint

Implemented `removeTechnicalFields<E extends SomeEntity>(entity: E): void` in `src/api/common/utils/EntityUtils.ts`. It mutates the entity recursively, including nested objects and arrays, deleting keys prefixed `_finalEncrypted`, `_defaultEncrypted`, or `_errors`. A WeakSet prevents revisiting shared or cyclic objects. Added regression tests for unchanged entities and nested cleanup in `test/tests/api/common/utils/EntityUtilsTest.ts`.

Checks executed:
- `./node_modules/.bin/tsc --noEmit --incremental false` — passed.
- `npm run fasttest` — passed; all 8682 assertions passed (old style total: 9820).
- `./node_modules/.bin/prettier --check src/api/common/utils/EntityUtils.ts test/tests/api/common/utils/EntityUtilsTest.ts` — passed.
- `git diff --check` — passed.

Tooling note: `rg` was unavailable (`/bin/bash: rg: command not found`), so inspection used `find` and `grep`. No check remains blocked.
