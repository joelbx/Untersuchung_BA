Task: Add short-lived reuse of known API fetch errors in useLink, scoped by shareId and linkId.
Status: Complete. Added 30-second per-hook error cache for NOT_FOUND, NOT_ALLOWED, and INVALID_ID; cached errors are rethrown until expiry. Other responses remain retryable and successful fetches continue normally.
Verification: useLink.test.ts passed (18 tests); Drive TypeScript check passed; targeted ESLint passed; Prettier formatting applied.
