# Progress

- Added `getInvertedRTLPlacement` and `rtlPlacement`; `usePopper` now reports the middleware's RTL-aware placement.
- Exported both utilities from the Popper entry point and added tests for all placements plus middleware direction handling.
- `yarn workspace @proton/components test components/popper/utils.test.ts --coverage=false`: passed (7 tests).
- `yarn workspace @proton/components check-types --pretty false`: passed.
- `git diff --check`: passed.
- `rg` was unavailable (`/bin/bash: rg: command not found`); used local `grep`/`find`.
