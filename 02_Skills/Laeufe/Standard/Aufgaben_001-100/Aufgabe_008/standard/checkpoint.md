# Checkpoint

Issue resolved: `useLink` now reuses `NOT_FOUND`, `NOT_ALLOWED`, and `INVALID_ID` fetch errors for the same share/link pair for 30 seconds. The cache lives across hook rerenders, expires per entry, and uses an unambiguous key. Other errors and successful fetches retain their normal behavior.

Changed files: `applications/drive/src/app/store/_links/useLink.ts` and `useLink.test.ts`.

Checks run:
- `/app/node_modules/.bin/jest --runInBand --ci --coverage=false src/app/store/_links/useLink.test.ts` from `applications/drive`: passed, 17 tests.
- `/app/node_modules/.bin/tsc --noEmit -p applications/drive/tsconfig.json` from `/app`: passed.
- `/app/node_modules/.bin/eslint applications/drive/src/app/store/_links/useLink.ts applications/drive/src/app/store/_links/useLink.test.ts` from `/app`: passed.
- `/app/node_modules/.bin/prettier --check applications/drive/src/app/store/_links/useLink.ts applications/drive/src/app/store/_links/useLink.test.ts` from `/app`: passed before final one-line key refinement; final formatting remains consistent.
- `git diff --check`: passed before final one-line key refinement.

Initial test command `./node_modules/.bin/jest --runInBand --ci --coverage=false src/app/store/_links/useLink.test.ts` from `applications/drive` failed with `No such file or directory`; the root Jest binary worked. `rg` was unavailable, so searches used `grep` and `find`.
