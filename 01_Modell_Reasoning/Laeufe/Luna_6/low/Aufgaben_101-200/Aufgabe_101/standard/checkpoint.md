Task: Fix list removal to accept multiple distinct string elements, preserve remaining order, and make updates visible immediately.

Implemented:
- Redis removes each requested value and waits for all removals before returning.
- MongoDB removes any requested values in one awaited update.
- PostgreSQL filters the list array against the requested values in one awaited update while retaining element ordinality.
- Added list database coverage for removing multiple present values, ignoring an absent value, preserving order, and observing the result immediately.

Verification:
- ESLint passed for the modified implementation and test files.
- `npx mocha test/database/list.js` could not run because Redis at 127.0.0.1:6379 refused the connection (0 tests ran).
- `git diff --check` passed.
