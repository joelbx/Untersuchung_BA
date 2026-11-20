Implemented RTL placement reporting. `getInvertedRTLPlacement` swaps `start` and `end` for top and bottom placements in RTL, and `rtlPlacement` detects direction from the floating element. `usePopper` now reports the middleware-adjusted placement.

The components TypeScript check passed. All five existing Popper utility tests reported PASS, but Jest did not exit after reporting results, so I interrupted it during teardown. `git diff --check` passed.

Changed [utils.ts](/app/packages/components/components/popper/utils.ts), [usePopper.ts](/app/packages/components/components/popper/usePopper.ts), and [index.ts](/app/packages/components/components/popper/index.ts).