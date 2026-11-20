Popper now reports RTL-aware placement to consumers. `getInvertedRTLPlacement` swaps `start` and `end` for top and bottom placements in RTL; `rtlPlacement` reads the floating element’s direction, and `usePopper` returns the adjusted value.

The focused Popper tests pass (7 tests). TypeScript, Prettier, and `git diff --check` also pass.