# Checkpoint

Refactored `src/components/views/elements/Pill.tsx` into a functional component with named exports. Added `src/hooks/usePermalink.tsx`, updated all Pill imports and `@room` helper uses, and added focused Pill tests.

Verification:
- `node_modules/.bin/jest --runInBand test/components/views/elements/Pill-test.tsx test/utils/pillify-test.tsx`: exit 0, 2 suites and 7 tests passed. Existing pillify fixture emits warnings about a room with no m.room.create event.
- `node_modules/.bin/eslint src/hooks/usePermalink.tsx src/components/views/elements/Pill.tsx src/components/views/elements/ReplyChain.tsx src/components/views/settings/BridgeTile.tsx src/utils/pillify.tsx test/components/views/elements/Pill-test.tsx`: exit 0.
- `node_modules/.bin/prettier --check` on those same six files: exit 0.
- `git diff --check`: exit 0.
- `node_modules/.bin/tsc --noEmit --jsx react`: exit 2. Errors: TS2724 in unchanged `src/components/views/auth/LoginWithQR.tsx` (missing `MSC3903ECDHv2RendezvousChannel`); TS2339/TS2551 in unchanged `src/components/views/settings/Notifications.tsx` (missing `getPushRuleAndKindById`); TS2339 in unchanged `src/notifications/VectorPushRulesDefinitions.ts` (missing `RuleId` poll constants). These local matrix-js-sdk type mismatches prevent a passing whole-project type check. No errors were reported in edited files, but whole-project type correctness remains unverified.

Final pass after moving `PillType` into the hook and re-exporting it from Pill (removing the component/hook import cycle):
- Focused Jest command above: exit 0, 2 suites / 7 tests passed.
- ESLint, Prettier, and `git diff --check` command above: exit 0.
- Full TypeScript command above: exit 2 with the same errors in the same three unchanged files; no diagnostics in edited files.
