# Checkpoint

Task: Add a Polls history entry point to RoomSummaryCard behind `feature_poll_history`, opening a room-scoped PollHistoryDialog.

Systematic debugging:
- Root cause: RoomSummaryCard had no poll history action and the settings registry had no `feature_poll_history` Labs entry. Existing card actions use `useFeatureEnabled` and `Modal.createDialog`.
- Reproduction: Added a RightPanel integration test. Before the fix, `./node_modules/.bin/jest test/components/structures/RightPanel-test.tsx --runInBand --silent` failed because no “Polls history” control was rendered.
- Fix: Registered the disabled-by-default Labs setting, added the named PollHistoryDialog component, connected the room card button and icon, and added the English string.

Checks:
- `./node_modules/.bin/jest test/components/structures/RightPanel-test.tsx --runInBand --silent`: passed, 3 tests.
- `./node_modules/.bin/prettier --check src/components/views/right_panel/RoomSummaryCard.tsx src/components/views/dialogs/polls/PollHistoryDialog.tsx src/settings/Settings.tsx test/components/structures/RightPanel-test.tsx src/i18n/strings/en_EN.json`: passed.
- `./node_modules/.bin/eslint --max-warnings 0 src/components/views/right_panel/RoomSummaryCard.tsx src/components/views/dialogs/polls/PollHistoryDialog.tsx src/settings/Settings.tsx test/components/structures/RightPanel-test.tsx`: passed.
- `./node_modules/.bin/stylelint res/css/views/right_panel/_RoomSummaryCard.pcss`: passed.
- `./node_modules/.bin/tsc --noEmit --jsx react`: failed with `src/components/views/messages/RoomCreate.tsx(50,38): error TS2339: Property 'findPredecessor' does not exist on type 'RoomState'.` That file is unchanged by this patch, so the global type check remains uncertain due to an existing SDK type mismatch.
- `./node_modules/.bin/jest test/settings/SettingsStore-test.ts --runInBand --silent`: passed, 1 test.

Environment: `rg` unavailable; used `find` and `grep`. No downloads performed.
