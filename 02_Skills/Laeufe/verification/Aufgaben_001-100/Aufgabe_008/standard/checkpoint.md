# Checkpoint

Task: Add a bounded per-link cache for recognized fetch errors in Drive `useLink`.

Initial inspection: `fetchLink` currently calls `debouncedRequest` directly and does not reuse failures. `rg` is unavailable (`/bin/bash: rg: command not found`); use `grep`/`find` for local search.

Implementation: `useLink.ts` now caches `NOT_FOUND`, `NOT_ALLOWED`, and `INVALID_ID` API errors per share/link for 5000 ms, returning the same error during that interval. Added `useLink.fetch.test.ts` for reuse, expiry, key isolation, uncached errors, and successful fetches.

Verification: `../../node_modules/.bin/jest --runInBand --ci --coverage=false --runTestsByPath src/app/store/_links/useLink.fetch.test.ts src/app/store/_links/useLink.test.ts` from `applications/drive` passed (2 suites, 17 tests). `../../node_modules/.bin/prettier --check src/app/store/_links/useLink.ts src/app/store/_links/useLink.fetch.test.ts` passed. `git diff --check` passed. TypeScript and ESLint checks are running.

The first Jest attempt from `/app` was interrupted after about a minute with no output (exit 130); the workspace-scoped rerun above completed successfully.

Final verification: `../../node_modules/.bin/tsc --noEmit --project tsconfig.json` from `applications/drive` exited 0 with no diagnostics. `../../node_modules/.bin/eslint src/app/store/_links/useLink.ts src/app/store/_links/useLink.fetch.test.ts` exited 0 with no diagnostics. No dependencies downloaded.
