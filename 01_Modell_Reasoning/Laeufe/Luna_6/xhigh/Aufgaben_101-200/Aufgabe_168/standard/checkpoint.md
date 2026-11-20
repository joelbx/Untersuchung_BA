# Checkpoint: admin action duplicate invocation

Issue: rapid activation of Kick, Ban, or Mute in the room member user info panel can launch duplicate operations.

Implemented in `src/components/views/right_panel/UserInfo.tsx`: a synchronous lock keyed by room and member is shared privately through context across Kick, Ban, and Mute, without changing the exported button props. It starts before confirmation, drives disabled and `aria-disabled="true"` state for all three controls, and releases on cancellation, early exit, success, or failure. Operations are awaited, failures present one clear action error, and room update indicators stop in a `finally` path.

Validation: `yarn test --runInBand test/components/views/right_panel/UserInfo-test.tsx` passes (68 tests); file ESLint, Prettier, and `git diff --check` pass. `tsc --noEmit --jsx react` reports only existing dependency/SDK type mismatches in other files; it reports no errors in the changed file. Harness configuration is unchanged.
