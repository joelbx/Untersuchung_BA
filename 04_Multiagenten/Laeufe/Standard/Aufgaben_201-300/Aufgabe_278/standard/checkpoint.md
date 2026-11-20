Task: Fix mailbox element reload timing, retry handling, and stale response handling.
Status: Implemented and verified.
Changes: Added pending backend-action tracking and guarded mailbox cache reset/fetch; wired common item mutation hooks to action lifecycle; added contextual loading, failure retry, stale-response retry, and Stale propagation.
Verification: Mailbox.elements.test.tsx (12 passed); TypeScript check for applications/mail passed; git diff --check passed.
Constraints: Local repository and existing tests only; no git history/index/harness changes.
