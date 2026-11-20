# Popper RTL placement checkpoint

- Goal: expose visual placement values for RTL layouts through Popper middleware.
- Implemented `getInvertedRTLPlacement` and `rtlPlacement` in `packages/components/components/popper/utils.ts` and exported both from the Popper index.
- `usePopper` now reports the middleware's adjusted placement after Floating UI resolves the final position.
- Added placement matrix, middleware direction, and hook integration tests.
- Verification: both Popper test files pass (9 tests); components TypeScript check, targeted ESLint, Prettier check, and `git diff --check` pass.
