# Checkpoint

Task: Fix repeated failed API requests in Drive's `useLink` hook by caching known client-visible fetch errors per `(shareId, linkId)` for a bounded backoff period.

Completed: Added a shared internal `(shareId, linkId)` error cache for `NOT_FOUND`, `NOT_ALLOWED`, and `INVALID_ID`. A cached original error is reused for one second, and its cache entry is removed automatically. Successful responses keep the existing conversion path.

Verification: `yarn workspace proton-drive test --runTestsByPath src/app/store/_links/useLink.test.ts` passed (12 tests); `yarn workspace proton-drive check-types --pretty false` passed; targeted ESLint and `git diff --check` passed.
