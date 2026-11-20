Popper now reports RTL-aware placement values. I added `getInvertedRTLPlacement` and `rtlPlacement`, then connected the middleware’s adjusted value to `usePopper` so consumers receive the placement that matches the visual position.

Verification passed: 8 Popper tests, the components type check, lint on the changed files, and `git diff --check`.