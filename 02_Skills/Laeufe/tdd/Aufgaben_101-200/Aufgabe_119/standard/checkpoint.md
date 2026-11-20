# Checkpoint

Task: Refactor Pill to a functional component with usePermalink and named exports.
Status: inspecting repository and test setup; no implementation changes yet.
Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); use `find`/`grep`.

Verification so far:
- RED: `node_modules/.bin/jest test/components/views/elements/Pill-test.tsx --runInBand --silent` failed because named `Pill` and helper exports were missing.
- Focused Pill test passes after implementation. Existing `pillify` assertions for a fallback avatar character conflicted with the no-unresolved-avatar requirement; updated expected text to `@room`.
- `node_modules/.bin/tsc --noEmit --jsx react --pretty false` exits 2 with pre-existing SDK API mismatches in LoginWithQR.tsx, Notifications.tsx, and VectorPushRulesDefinitions.ts; no diagnostics in edited files.
- Full Jest suite in progress.
- `node_modules/.bin/eslint` on all edited TS/TSX files passed after adding the required copyright header.
- `node_modules/.bin/jest test/components/views/messages/TextualBody-test.tsx --runInBand --updateSnapshot --silent` passed; updated two snapshots for verbatim href and self-mention class.
- Full Jest suite observed failures in Notifications-test.tsx and LoginWithQR-test.tsx, consistent with SDK/API mismatch diagnostics; its final summary is pending.
- A proposed profile transition test passed without a code change, so it was removed under TDD rules.

Final verification:
- `node_modules/.bin/jest --runInBand --silent` exited 1: 4 suites failed, 402 passed; 15 tests failed, 3692 passed. Failures: Notifications-test.tsx, LoginWithQR-test.tsx, StopGapWidget-test.ts, and TextualBody-test.tsx. TextualBody had two obsolete snapshots during the full run; they were updated and its targeted rerun passed (15 tests, 5 snapshots). The other three suites are unrelated to Pill and were not changed.
- `node_modules/.bin/jest test/components/views/elements/Pill-test.tsx test/utils/pillify-test.tsx test/components/views/messages/TextualBody-test.tsx --runInBand --silent` exited 0: 3 suites, 21 tests, 5 snapshots passed.
- `git diff --check` passed.
