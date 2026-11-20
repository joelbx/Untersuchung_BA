Issue: Popper placement should be mirrored for RTL top/bottom start/end placements.

Implemented `getInvertedRTLPlacement` and `rtlPlacement` in the Popper utilities, exported both, and wired the middleware into `usePopper` so its public placement uses middleware data. The middleware reads the floating element's computed direction.

Verification: the existing `utils.test.ts` suite printed PASS for all 5 tests. Jest did not exit after reporting those results, so it was interrupted during teardown. The components package TypeScript check completed successfully. `git diff --check` passed.
