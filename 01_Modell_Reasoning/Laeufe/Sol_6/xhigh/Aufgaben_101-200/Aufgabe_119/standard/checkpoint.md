# Checkpoint

Task: Refactor Pill into a functional component with named exports and extract permalink resolution into `usePermalink`.

Completed:
- Replaced class Pill with a functional component, named exports, and `@room` helpers.
- Added `usePermalink` with type detection, room/member/profile resolution, avatars, text, and user action.
- Updated `pillify`, `ReplyChain`, and `BridgeTile` imports.
- Added focused Pill tests.

Verification:
- Relevant Jest suites: 3 passed, 10 tests passed.
- ESLint on edited source and test files: passed.
- `git diff --check`: passed.
- Repository TypeScript check still reports pre-existing errors in unrelated SDK integration files; none refer to the changed files.
