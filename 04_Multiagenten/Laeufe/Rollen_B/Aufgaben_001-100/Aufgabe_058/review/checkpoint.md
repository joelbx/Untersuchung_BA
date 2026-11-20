VERDICT: FIX
Independent review complete. Code defect: src/PosthogAnalytics.ts:159-160 switches to Anonymous without resetting PostHog's identified distinct ID. After identifyUser in Pseudonymous mode, subsequent anonymous captures can remain tied to that identity. Correction: reset PostHog when an enabled identified client transitions to Anonymous, and keep logout semantics consistent.
Relevant existing test: ./node_modules/.bin/jest test/PosthogAnalytics-test.ts --runInBand --silent => PASS, 21/21 tests.
Changed-file lint: ./node_modules/.bin/eslint --max-warnings 0 src/PosthogAnalytics.ts test/PosthogAnalytics-test.ts => PASS.
TEST_ENVIRONMENT_PROBLEM: ./node_modules/.bin/tsc --noEmit --jsx react => exit 2; repository-wide dependency/type errors, including missing @sentry/types and rrweb-snapshot in posthog-js and mismatched matrix-js-sdk types. No diagnostics identified in changed files. Resolve installed dependency/type compatibility before relying on this check.
No project code or tests changed during review.
