# Progress checkpoint

- Task: add the global `chat:privileged` gate throughout chat flows and expose `canChat` on user profiles.
- Repository: `/app`; initial worktree clean. No `AGENTS.md` files found.
- Next: none; implementation and verification complete.
- Found: `user.isPrivileged` covers administrators, global moderators, and category moderators. Chat creation and invitations already call `messaging.canMessageUser` for each UID.
- Implemented: global privilege map and array-capable `can`; target gate in messaging; array checks in chat middleware and flows; profile `canChat` and OpenAPI/i18n.
- Complete: privileged targets require `chat:privileged` in `messaging.canMessageUser`, with `[[error:no-privileges]]` on denial. Array checks permit either chat privilege throughout middleware, messaging, API, page controller, and navigation. Profile API exposes a boolean `canChat` based on `messaging.canMessageUser`.
- Verification: focused existing messaging and middleware suites passed (94 tests); ESLint, `git diff --check`, translation JSON parsing, and OpenAPI YAML parsing passed. Temporary Redis used for tests was stopped and test logs removed.
