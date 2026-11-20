# Progress checkpoint

- Task: render safe HTML in notifications, secure notification links, and deduplicate non-success notifications by a stable key.
- Initial inspection: repository is a JavaScript/TypeScript monorepo; `rg` is unavailable, so searches will use `find` and `grep`.
- Implemented: notification strings are sanitized with a small HTML allowlist; all rendered anchors receive `rel="noopener noreferrer"` and `target="_blank"`, including anchors added later by React content.
- Implemented: create options accept an explicit key; non-success notifications deduplicate by explicit key, string text, or identifier. Repeated success notifications remain separate and use unique React list keys.
- Verification: components Jest suite passed (34 suites; 127 tests passed, 1 skipped). TypeScript, ESLint, Prettier, and `git diff --check` passed.
