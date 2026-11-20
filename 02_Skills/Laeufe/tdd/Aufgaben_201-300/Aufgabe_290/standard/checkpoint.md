# Checkpoint

Task: Make call sounds audible when a muted media element is asked to play; preserve public media event handling and stable sound identifiers.

Status: Implemented muted-element recovery before queued `play()`, exported `AudioID`, and added the public `handleEvent` listener plus its disabled debug setting. Targeted Jest tests, changed-file ESLint, and `./node_modules/.bin/tsc --noEmit --jsx react` pass.

Full suite command: `./node_modules/.bin/jest --runInBand --silent`. Result: 332 passed, 9 failed, 1 skipped suites; 3063 passed, 11 failed, 39 skipped, 2 todo tests. Both call handler suites passed. Failing suites (outside edited files):

- `test/components/views/elements/AppTile-test.tsx` — React `createEvent` on null.
- `test/components/structures/RoomView-test.tsx` — expected chat panel open; received closed.
- `test/components/views/messages/MLocationBody-test.tsx` — `Symbol(shapeMode)` snapshot mismatch.
- `test/components/views/beacon/BeaconMarker-test.tsx` — `Symbol(shapeMode)` snapshot mismatch.
- `test/stores/widgets/StopGapWidget-test.ts` — `No iframe supplied`.
- `test/components/views/beacon/BeaconStatus-test.tsx` — `Symbol(shapeMode)` snapshot mismatch.
- `test/components/views/location/SmartMarker-test.tsx` — `Symbol(shapeMode)` snapshot mismatch.
- `test/components/views/location/LocationViewDialog-test.tsx` — `Symbol(shapeMode)` snapshot mismatch.
- `test/components/views/location/ZoomButtons-test.tsx` — `Symbol(shapeMode)` snapshot mismatch.

Repository detail: this checkout has `src/LegacyCallHandler.tsx`; the requested listener path did not exist, so it was added at `src/legacy/LegacyCallHandler/handleEvent.ts`.
