# Checkpoint

Task: Refactor Drive extended-attribute helpers and types, update call site, and make parsing resilient.

Implemented:
- Added `DeepPartial` at `applications/drive/src/app/utils/type/DeepPartial.ts`.
- Exported strict XAttr types and changed file creation/encryption to accept an options object.
- Corrected exact chunk boundaries, omitted absent digests, froze created file attributes, and handled malformed/partial JSON safely.
- Updated upload call site and focused tests.

Checks:
- `../../node_modules/.bin/jest src/app/store/_links/extendedAttributes.test.ts --runInBand --ci --coverage=false` (from `applications/drive`): passed, 5 tests.
- `../../node_modules/.bin/tsc --noEmit --incremental false` (from `applications/drive`): passed.
- `../../node_modules/.bin/eslint src/app/store/_links/extendedAttributes.ts src/app/store/_links/extendedAttributes.test.ts src/app/store/_uploads/worker/worker.ts src/app/utils/type/DeepPartial.ts` (from `applications/drive`): passed.
- `git diff --check`: passed.
- Repeated `../../node_modules/.bin/tsc --noEmit --incremental false` after the final `DeepPartial` change: passed.
- `../../node_modules/.bin/prettier --check src/app/utils/type/DeepPartial.ts src/app/store/_links/extendedAttributes.ts src/app/store/_links/extendedAttributes.test.ts src/app/store/_uploads/worker/worker.ts` (from `applications/drive`): passed.
