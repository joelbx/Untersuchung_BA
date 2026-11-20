# Checkpoint

Issue: cloned entities retain technical fields.

Implemented `removeTechnicalFields<E extends SomeEntity>(entity: E): void` in `src/api/common/utils/EntityUtils.ts`. It mutates the entity recursively, deleting own enumerable keys starting with `_finalEncrypted`, `_defaultEncrypted`, or `_errors` while preserving other properties. A WeakSet handles shared references and cycles. Added tests in `test/tests/api/common/utils/EntityUtilsTest.ts` for root fields, nested objects and arrays, and an entity without technical fields.

Verification:
- Red test: `npm run fasttest` exited 1 before implementation with `No matching export ... removeTechnicalFields`.
- Green test: `npm run fasttest` exited 0; `All 8683 assertions passed (old style total: 9821)`.
- `./node_modules/.bin/tsc --noEmit --incremental false` exited 0.
- `./node_modules/.bin/prettier --check src/api/common/utils/EntityUtils.ts test/tests/api/common/utils/EntityUtilsTest.ts` exited 0.
- `./node_modules/.bin/eslint src/api/common/utils/EntityUtils.ts test/tests/api/common/utils/EntityUtilsTest.ts` exited 0.
- `git diff --check` exited 0.

Local discovery: `rg` unavailable (`/bin/bash: rg: command not found`); used `find` and `grep`.
