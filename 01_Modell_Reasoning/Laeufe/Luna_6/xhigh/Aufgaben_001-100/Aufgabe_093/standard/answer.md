Implemented RTL-aware placement reporting.

- Added and exported `getInvertedRTLPlacement` and `rtlPlacement` in [utils.ts](/app/packages/components/components/popper/utils.ts:22). Top and bottom alignments swap `start` and `end` in RTL; left and right placements remain unchanged.
- Added the middleware to [usePopper.ts](/app/packages/components/components/popper/usePopper.ts:69) and use its placement data in the reported result.
- Exported both helpers from [index.ts](/app/packages/components/components/popper/index.ts:6).

Verification passed: existing Popper utility tests (5 tests), component type check, focused ESLint and Prettier checks, and `git diff --check`.