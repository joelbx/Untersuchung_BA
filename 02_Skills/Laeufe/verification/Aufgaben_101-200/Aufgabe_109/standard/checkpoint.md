# Checkpoint

Implemented the disabled-by-default `feature_poll_history` Messaging lab, its RoomSummaryCard button and icon, and a named `PollHistoryDialog` component. The button passes `room.roomId` through `Modal.createDialog`.

Verification run:
- `./node_modules/.bin/jest --runInBand --watch=false --silent test/components/views/right_panel/RoomSummaryCard-test.tsx`: exit 0, 2 tests passed.
- `./node_modules/.bin/jest --runInBand --watch=false test/components/views/right_panel/RoomHeaderButtons-test.tsx`: exit 0, 5 tests passed.
- `./node_modules/.bin/eslint --max-warnings 0 src/components/views/right_panel/RoomSummaryCard.tsx src/components/views/dialogs/polls/PollHistoryDialog.tsx src/settings/Settings.tsx test/components/views/right_panel/RoomSummaryCard-test.tsx && ./node_modules/.bin/prettier --check src/components/views/right_panel/RoomSummaryCard.tsx src/components/views/dialogs/polls/PollHistoryDialog.tsx src/settings/Settings.tsx test/components/views/right_panel/RoomSummaryCard-test.tsx res/css/views/right_panel/_RoomSummaryCard.pcss && git diff --check`: exit 0.
- `./node_modules/.bin/stylelint res/css/views/right_panel/_RoomSummaryCard.pcss`: exit 0.
- `./node_modules/.bin/tsc --noEmit --jsx react`: exit 2; `src/components/views/messages/RoomCreate.tsx(50,38): error TS2339: Property 'findPredecessor' does not exist on type 'RoomState'.` This is in an unchanged file; full type check status remains failing.

`rg` is unavailable (`/bin/bash: line 1: rg: command not found`); local `find` and `grep` were used.
