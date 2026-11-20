# Checkpoint

Task: gate QR sign-in with `feature_qr_signin_reciprocate_show`, default disabled, while retaining MSC3882/MSC3886 checks and QR flow.

Status: inspecting repository and test conventions; no implementation changes yet.

Implementation: registered experimental flag (default false), guarded QR section and both tab entry points, added flag regression tests. Focused Jest files passed (61 tests). ESLint on changed TS/TSX files passed.

Verification issue: `yarn lint:types` failed with `test/components/structures/RoomView-test.tsx(178,65): error TS2345: Argument of type '{ roomId: string; }' is not assignable to parameter of type '{ roomId: string; eventId: string; }'. Property 'eventId' is missing`. This is outside changed files; TypeScript verification remains incomplete.

Full `yarn test --runInBand` is still running.
Full-suite observation: `test/components/views/messages/MLocationBody-test.tsx` has failed a snapshot because the received event emitter includes `Symbol(shapeMode): false`; unrelated to QR changes. Full suite still running.

Final verification: `yarn test --runInBand` exited 1: 386 suites passed, 4 failed; 3606 tests passed, 6 failed. Failing suites: `test/components/views/messages/MLocationBody-test.tsx`, `test/components/views/location/SmartMarker-test.tsx`, and `test/components/views/location/LocationViewDialog-test.tsx` (snapshot differences containing `Symbol(shapeMode): false`); `test/stores/widgets/StopGapWidget-test.ts` (`No iframe supplied`). No QR test failed. These failures are outside changed files. `yarn lint:types` exited 2 with the RoomView test type error above. Changed-file ESLint and `git diff --check` passed.
