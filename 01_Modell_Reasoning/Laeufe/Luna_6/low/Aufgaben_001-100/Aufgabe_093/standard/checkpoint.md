# Checkpoint: Popper RTL placement

- Added `getInvertedRTLPlacement` to invert start/end for top and bottom placements in RTL while preserving left/right and all LTR placements.
- Added `rtlPlacement` Floating UI middleware that reads direction from the floating element and publishes the adjusted placement in middleware data.
- Wired middleware data into `usePopper`'s exposed placement and exported both utilities.
- Added helper coverage to the existing Popper utils tests.
- Verification: `yarn workspace @proton/components test --runTestsByPath components/popper/utils.test.ts` passed; `yarn workspace @proton/components check-types` completed without diagnostics.
