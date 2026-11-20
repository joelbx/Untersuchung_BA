Added an opt-in **Polls history** setting and button to `RoomSummaryCard`. When enabled, the button opens the new named-export `PollHistoryDialog` with the current room’s `roomId`.

The relevant right-panel tests pass (11 tests), and formatting and lint checks pass. Full type checking still reports an error in the untouched [RoomCreate.tsx](/app/src/components/views/messages/RoomCreate.tsx:50).