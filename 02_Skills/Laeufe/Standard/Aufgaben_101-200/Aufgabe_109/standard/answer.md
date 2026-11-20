Added an off-by-default `feature_poll_history` labs setting and a “Polls history” button to the room summary. When enabled, the button opens the new `PollHistoryDialog` with the current room’s `roomId`.

The RightPanel tests pass, as do ESLint, Prettier, and Stylelint. Type checking remains blocked by an existing `RoomCreate.tsx` SDK type error; it reported no errors in the changed files.