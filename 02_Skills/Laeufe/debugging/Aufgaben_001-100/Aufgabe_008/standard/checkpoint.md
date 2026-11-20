# Checkpoint

Task: Add bounded reuse of known failed link fetches in `useLink`.

Investigation underway. Initial source shows `fetchLink` directly awaits `debouncedRequest` and has no failed-result cache. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep`/`find` instead.

Root cause: `useLink`'s `fetchLink` calls `debouncedRequest` on every invocation; the debounce only shares concurrent work. Rejected results are not retained, and `loadFreshLink` reaches this path repeatedly. Similar working behavior for successful links is `linksState` caching in `getEncryptedLink`, but failures cannot enter that link cache. Hypothesis: a per-hook, per-(shareId, linkId) timed error cache around the API request suppresses repeat known failures while preserving success and unrelated keys.

Regression: The new `useLink failed fetch backoff` tests initially failed with two API calls for the same known failure. A test-mock reset initially caused an unrelated `getLink` TypeError; corrected the fixture and confirmed the expected repeat-request failure before editing production code.

Fix: `useLink` holds a per-instance `linkFetchErrors` map keyed by the serialized `(shareId, linkId)` pair. Known API errors are rethrown from the cache for 10 seconds, after which the entry is removed. Other failures and successful results follow the original path.

Verification so far: `useLink.test.ts` passes (16 tests); ESLint and Prettier pass for both edited files; `git diff --check` passed. An initial `tsc --noEmit --pretty false` failed because caught errors are `unknown`; narrowed the API error shape and reran type checking (pending).

Final verification: `../../node_modules/.bin/jest --runInBand --coverage=false --watch=false --runTestsByPath src/app/store/_links/useLink.test.ts` passed (16/16); `../../node_modules/.bin/tsc --noEmit --pretty false` passed; `../../node_modules/.bin/eslint src/app/store/_links/useLink.ts src/app/store/_links/useLink.test.ts` passed; `../../node_modules/.bin/prettier --check src/app/store/_links/useLink.ts src/app/store/_links/useLink.test.ts` passed.
