VERDICT: FIX

The Pill refactor passed the targeted existing tests: `./node_modules/.bin/jest --runInBand test/utils/pillify-test.tsx test/components/views/messages/TextualBody-test.tsx` — 2 suites, 18 tests, and 5 snapshots passed. I found no concrete defect in the changed code.

**TEST_ENVIRONMENT_PROBLEM:** `./node_modules/.bin/tsc --noEmit --jsx react` failed with SDK API errors in [LoginWithQR.tsx](/app/src/components/views/auth/LoginWithQR.tsx:20), [Notifications.tsx](/app/src/components/views/settings/Notifications.tsx:489), and [VectorPushRulesDefinitions.ts](/app/src/notifications/VectorPushRulesDefinitions.ts:136). Those files are outside the patch. Align the installed `matrix-js-sdk` with this checkout, then rerun the type check. The failed check requires a FIX verdict under the review criteria.

Review notes are in [checkpoint.md](/app/.codex-role-output/checkpoint.md).