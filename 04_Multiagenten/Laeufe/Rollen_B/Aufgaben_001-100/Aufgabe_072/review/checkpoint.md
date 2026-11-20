VERDICT: ACCEPT
Reviewed the applied diff in packages/components/helpers/url.ts, hooks/useLinkHandler.tsx, components/notifications/LinkConfirmationModal.tsx, and their existing tests. No correctness or regression issue found for the stated requirements. The hostname is encoded while protocol, path, query, and fragment text remain intact; the hook updates external link hrefs and reports missing href values.
Tests executed:
- `yarn workspace @proton/components test --runTestsByPath helpers/url.test.ts hooks/useLinkHandler.test.tsx --coverage=false` — PASS, 2 suites and 17 tests.
- `yarn workspace @proton/components check-types` — PASS, exit 0.
- `git diff --check` — PASS, exit 0.
TEST_ENVIRONMENT_PROBLEM: none.
