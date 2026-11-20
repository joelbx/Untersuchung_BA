Correction round (2026-10-22)
- Inspected the working-tree Pill refactor and independent review. Review identified no concrete defect in changed code.
- Reran exact reviewer Jest command: `./node_modules/.bin/jest --runInBand test/utils/pillify-test.tsx test/components/views/messages/TextualBody-test.tsx` — 2 suites, 18 tests, 5 snapshots passed.
- Reran exact reviewer TypeScript command: `./node_modules/.bin/tsc --noEmit --jsx react` — fails only in unchanged LoginWithQR.tsx, Notifications.tsx, and VectorPushRulesDefinitions.ts due to APIs absent from the prepared matrix-js-sdk. TEST_ENVIRONMENT_PROBLEM; dependency alignment would require changing the prepared environment and is unavailable under no-download instructions.
- `git diff --check` passes. No source changes in this correction round; original patch remains coherent.
