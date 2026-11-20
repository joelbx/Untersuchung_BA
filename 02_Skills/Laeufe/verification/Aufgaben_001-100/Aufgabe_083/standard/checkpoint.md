# Checkpoint

Task: refactor extended-attribute creation and parsing in the Drive application.

Status: implementation and focused regression tests updated in `store/_links`, the upload worker call site, and `utils/type/DeepPartial.ts`. The issue's `services/extendedAttributes.ts` path does not exist in this checkout; the implementation is in `store/_links/extendedAttributes.ts`.

Verification: `/app/node_modules/.bin/jest --runInBand --ci --coverage=false src/app/store/_links/extendedAttributes.test.ts` passed (5 tests) on final files. `/app/node_modules/.bin/tsc --noEmit --incremental false --pretty false` passed on final files. ESLint on the four changed source/test files passed. `git diff --check` passed.

Tooling: `./node_modules/.bin/jest --runInBand --ci --coverage=false src/app/store/_links/extendedAttributes.test.ts` and `./node_modules/.bin/tsc --noEmit --incremental false --pretty false` failed from the Drive directory with `/bin/bash: ... No such file or directory`; repository root binaries were used instead.
