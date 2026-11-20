# Checkpoint

Task: Add a feature-gated Polls history entry point to RoomSummaryCard and a public PollHistoryDialog receiving roomId.

Implemented:
- Registered `feature_poll_history` as an off-by-default Messaging labs feature.
- Added the gated room summary button and poll icon; it opens `PollHistoryDialog` with `room.roomId`.
- Added the named-export dialog component with the requested props and BaseDialog title.
- Added a RightPanel integration test for the disabled button and enabled click behavior.

Checks:
- `node_modules/.bin/jest test/components/structures/RightPanel-test.tsx --runInBand --silent`: passed (3 tests).
- `node_modules/.bin/eslint src/components/views/right_panel/RoomSummaryCard.tsx src/components/views/dialogs/polls/PollHistoryDialog.tsx src/settings/Settings.tsx test/components/structures/RightPanel-test.tsx`: passed.
- `node_modules/.bin/prettier --check src/components/views/right_panel/RoomSummaryCard.tsx src/components/views/dialogs/polls/PollHistoryDialog.tsx src/settings/Settings.tsx test/components/structures/RightPanel-test.tsx`: passed.
- `node_modules/.bin/stylelint res/css/views/right_panel/_RoomSummaryCard.pcss`: passed.
- `node_modules/.bin/tsc --noEmit --jsx react`: failed on pre-existing SDK type mismatch: `src/components/views/messages/RoomCreate.tsx(50,38): error TS2339: Property 'findPredecessor' does not exist on type 'RoomState'.` No errors reported in changed files.

`rg` is unavailable (`/bin/bash: rg: command not found`); repository inspection used `find` and `grep`.
