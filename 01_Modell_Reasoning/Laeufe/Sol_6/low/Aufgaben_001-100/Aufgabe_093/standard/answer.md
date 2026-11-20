Implemented RTL-aware Popper placement reporting. `getInvertedRTLPlacement` swaps `start` and `end` for top and bottom placements in RTL, while `rtlPlacement` reads the floating element’s direction and supplies the adjusted value to `usePopper`.

Verification passed: 7 Popper tests, the components type check, and Prettier.