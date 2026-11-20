Task: Fix PosthogAnalytics initialization, privacy modes, tracking guards, hashing, and location redaction.

Starting state: working tree clean. Relevant source: `src/PosthogAnalytics.ts`; existing tests: `test/PosthogAnalytics-test.ts`.

Completed: `PosthogAnalytics` now stores `Anonymity`, `enabled`, and `initialised` independently; validates both PostHog config fields; forces anonymous mode under DNT; guards all capture paths; awaits PostHog capture; hashes user and room IDs; redacts URLs according to the current mode; and provides the requested state and logout methods. Added privacy, initialization, and async capture coverage to `test/PosthogAnalytics-test.ts`.

Verification: focused Jest suite passed (28 tests); ESLint passed for both changed files; focused TypeScript check passed; `git diff --check` passed. Repository-wide TypeScript check reports existing errors outside `PosthogAnalytics.ts`, including unresolved dependency typings and unrelated source type errors.
