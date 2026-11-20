Fixed Popper’s RTL placement reporting. `getInvertedRTLPlacement` swaps `start` and `end` for top and bottom placements in RTL; `rtlPlacement` reads the floating element’s direction, and `usePopper` exposes the adjusted value.

Verification: 23 Popper tests passed, the components TypeScript check passed, and `git diff --check` passed.