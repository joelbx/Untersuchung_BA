Task complete: useLink caches NOT_FOUND, NOT_ALLOWED, and INVALID_ID fetch errors per shareId:linkId for 30 seconds, then evicts them. Cached errors reject without another API call; successful requests retain existing processing.
Verification: git diff --check passed; Drive useLink.test.ts passed (12 tests).
