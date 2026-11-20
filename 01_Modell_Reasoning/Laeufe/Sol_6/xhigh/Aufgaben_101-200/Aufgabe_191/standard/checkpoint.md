# InteractiveAuth registration token support

Status: complete.

Plan: inspect existing authentication stage mapping and entry views, implement stable and unstable registration token stages, then run relevant existing tests.

Initial state: working tree clean; no repository AGENTS.md found.

Findings: matrix-js-sdk already has both AuthType values, passes through the selected stage, and adds the session during submission. The UI selector previously fell back for both token stages.

Changes: added a dedicated registration token entry component, mapped both identifiers to it, added English strings, and added integration and view tests.

Verification: the new InteractiveAuth tests and existing InteractiveAuthDialog and Registration tests passed (9 total). ESLint, Prettier, and git diff whitespace check passed. Repository-wide TypeScript checking still reports existing Sliding Sync API type errors in unrelated files; it reported no errors in the changed files.
