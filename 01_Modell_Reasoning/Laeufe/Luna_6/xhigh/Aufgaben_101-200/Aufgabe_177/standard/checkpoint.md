# Chat Allow/Deny List checkpoint

- Objective: implement explicit chat allow/deny lists and a disable-incoming-chats setting in `/app`, including enforcement, migration, account management, and existing test coverage.
- Constraints: use local repository code and existing tests; do not modify git history, index baseline, harness configuration, or read credentials/private process/evaluator files.
- Initial inspection: `rg` is unavailable in this environment; switching to `find` and standard shell utilities.
- Findings: chat permissions are centralized in `Messaging.canMessageUser`; the API uses it for direct room creation and room invitations. Account settings templates are provided by the installed theme, but the core account settings view exposes a custom settings slot.
- Planned edits: replace legacy setting parsing/saving and enforcement, add account controls through the custom settings slot, update the admin default setting and OpenAPI schema, migrate legacy preferences in batches, and update existing references in tests.
- Implemented: per-user `disableIncomingMessages`, JSON-backed UID allow/deny lists with safe parsing, settings UI in the account page, permission gates for direct room starts, private room ID lookup, invitations, and messages in existing one-to-one rooms. Explicit blocks retain precedence and admins/global moderators bypass chat privacy lists.
- Upgrade: added `src/upgrades/4.3.0/chat_allow_list.js`; it migrates legacy per-user or default restrictions in 500-user batches, preserves existing valid lists, handles empty follow lists without reopening messages, and removes legacy fields after migration.
- Validation: `test/messaging.js` and `test/user.js` pass (353 tests) against a temporary local Redis instance; ESLint and Node syntax checks pass; all 3,724 language JSON files and the updated OpenAPI schema parse; `git diff --check` passes.
- Compatibility: the old setting name remains only where migration reads/deletes it and where account-page JavaScript removes the installed theme's stale control.
- Status: complete.
