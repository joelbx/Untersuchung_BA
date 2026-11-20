# Checkpoint

Task: add a poll history entry point to RoomSummaryCard, gated by `feature_poll_history`, and create PollHistoryDialog with the specified public interface.

Status: implementation and regression tests added. Targeted RightPanel Jest suite passes (4 tests). ESLint and `git diff --check` pass.

Verification issues:
- `rg` is unavailable (`/bin/bash: rg: command not found`); used `find` and `grep`.
- `./node_modules/.bin/tsc --noEmit --jsx react` fails in unchanged `src/components/views/messages/RoomCreate.tsx:50:38`: TS2339, `findPredecessor` does not exist on type `RoomState`.
- Full `./node_modules/.bin/jest --runInBand --silent` completed: 376 suites passed, 7 failed; 3566 tests passed, 12 failed, 27 skipped, 2 todo. Failed suites: `MessagePanel-test.tsx` (creation event ID null), `MLocationBody-test.tsx` (map snapshot `Symbol(shapeMode)`), `RoomCreate-test.tsx` (`state.findPredecessor is not a function`), `StopGapWidget-test.ts` (widget API failure), `SmartMarker-test.tsx` (two map snapshot mismatches), `LocationViewDialog-test.tsx` (map snapshot mismatch), and `ZoomButtons-test.tsx` (map snapshot mismatch). The isolated command `./node_modules/.bin/jest test/components/structures/MessagePanel-test.tsx --runInBand --silent` fails identically (1 failed, 15 passed), so this failure is independent of suite order. No snapshots were updated.
- `./node_modules/.bin/jest test/stores/widgets/StopGapWidget-test.ts --runInBand --silent` fails in `feeds incoming to-device messages to the widget` and `when there is a voice broadcast recording › and receiving a action:io.element.join message › should pause the current voice broadcast recording`: `No iframe supplied` from `ClientWidgetApi`.
- `./node_modules/.bin/stylelint res/css/views/right_panel/_RoomSummaryCard.pcss` passed.
