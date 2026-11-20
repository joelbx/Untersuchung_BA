# Fault localization progress

Inspected `RoomSummaryCard`, settings, Labs rendering, dialog contracts, styles, and existing tests. No project source or tests changed.

- `src/components/views/right_panel/RoomSummaryCard.tsx` renders About actions and already uses `useFeatureEnabled` and `Modal.createDialog`; add the guarded Polls history action here, passing `room.roomId`.
- `src/settings/Settings.tsx` has no `feature_poll_history`. Add an experimental Labs feature definition (boolean, default false, supported levels matching other Labs flags). `SettingsStore.getValue` throws for an unregistered setting; the hook cannot safely use the flag until registered.
- `src/components/views/dialogs/polls/PollHistoryDialog.tsx` does not exist. Its named component should accept the requested `onFinished` and `roomId` props and render `BaseDialog` with the translated title. The requested interface does not prescribe body content or use of roomId beyond passing it to the component.
- `LabsUserSettingsTab` lists registered feature settings automatically; no separate hardcoded tab entry appears needed.
- Existing RightPanel test covers a summary navigation action, but no poll history entry or dialog test exists. Relevant behavior to verify: hidden by default, visible when flag enabled, click opens named dialog with current `roomId`, and dialog closes through `onFinished`.
- Optional visual detail: `_RoomSummaryCard.pcss` has icons for existing actions but no polls icon.
