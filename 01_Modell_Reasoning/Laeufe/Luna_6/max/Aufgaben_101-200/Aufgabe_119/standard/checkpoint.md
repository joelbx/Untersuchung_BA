# Checkpoint

Task: Refactor the Pill component into a functional component, extract permalink resolution into `usePermalink`, publish named exports, and update consumers.

Completed:
- Replaced the class component with a functional component and named exports: `Pill`, `PillType`, `pillRoomNotifPos`, and `pillRoomNotifLen`.
- Added `src/hooks/usePermalink.tsx` to resolve Matrix targets, names, avatars, profile lookups, space types, and user-view actions.
- Updated `ReplyChain`, `BridgeTile`, and `pillifyLinks` to consume the named API.

Verification:
- `yarn test --runInBand test/utils/pillify-test.tsx`: passed (3 tests).
- Focused ESLint: passed.
- Focused Prettier check: passed.
- `git diff --check`: passed.
- `yarn tsc --noEmit --jsx react`: blocked by existing Matrix SDK API mismatches in `LoginWithQR.tsx`, `Notifications.tsx`, and `VectorPushRulesDefinitions.ts`; no diagnostics reference the changed files.
