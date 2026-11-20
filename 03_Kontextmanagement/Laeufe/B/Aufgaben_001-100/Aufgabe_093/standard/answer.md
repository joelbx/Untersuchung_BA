Resolved the Popper RTL placement issue. `usePopper` now reports mirrored `top` and `bottom` start/end placements in RTL through the new `getInvertedRTLPlacement` helper and `rtlPlacement` middleware. Left/right and LTR placements remain unchanged.

All eight Popper utility tests, the component type check, focused ESLint, and `git diff --check` passed.