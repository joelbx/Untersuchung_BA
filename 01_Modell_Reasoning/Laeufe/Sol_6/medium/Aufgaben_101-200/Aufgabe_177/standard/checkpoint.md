Task: Implement chat allow/deny lists, incoming chat disable setting, migration, account controls, and tests.
Status: Complete. Settings load/save parses string UID arrays safely; server permissions enforce explicit blocks first, then incoming disable, deny, and non-empty allow list, with admin/global moderator exemption; direct room creation and invitations checked. Upgrade seeds legacy restricted users' allow lists from follows without overwriting existing lists. Account UI, schema, labels, and tests updated.
Verification: ESLint and git diff --check passed. Full user suite: 276 passing. Messaging suite: 77 passing. Isolated local Redis used for tests and stopped afterward.
Constraints: Local repository only; git history, index, and harness configuration untouched.
