# Checkpoint

- Task: Reuse known `useLink` fetch failures for the same share and link for a bounded period.
- Implemented a module-scoped, per-share-and-link cache for `NOT_FOUND`, `NOT_ALLOWED`, and `INVALID_ID` API errors. Entries expire after 5 seconds; a successful response clears a stale error for the same key.
- Added focused tests for error reuse across hook instances, key isolation, expiry, successful fetches, and uncached errors.
- Verification: 19 targeted Jest tests passed; Drive TypeScript check, ESLint, and Prettier passed.
