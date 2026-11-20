# Checkpoint

Task: fix notification HTML rendering, secure links, and deduplication in checked-out repository files.

Completed:
- Notification strings containing markup render through DOMPurify; plain strings and React nodes remain supported.
- All rendered notification anchors receive `rel="noopener noreferrer"` and `target="_blank"`, including links added by React after initial render.
- Notification keys use explicit key, string text, or id precedence. Non-success notifications deduplicate by key; success notifications remain repeatable with distinct React render keys.
- Added focused rendering and manager tests.

Validation: 8 notification tests passed; `@proton/components` type check and ESLint passed; `git diff --check` passed. No existing notification test files were present.
