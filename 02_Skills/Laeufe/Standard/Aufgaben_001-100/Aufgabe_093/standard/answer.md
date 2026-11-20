Popper now reports RTL-aware placement values. In RTL, `top` and `bottom` swap `start` and `end`; `left` and `right` stay unchanged. The new middleware reads the floating element’s direction, and `usePopper` uses its adjusted value when reporting placement.

The targeted Popper tests passed (7 tests), the components TypeScript check passed, and `git diff --check` passed.