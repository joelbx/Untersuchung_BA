# Chat Allow/Deny List implementation

- Added `disableIncomingMessages`, `chatAllowList`, and `chatDenyList` user settings with safe array parsing and defaults.
- Centralized incoming chat checks in `Messaging.canMessageUser`: explicit recipient blocks take precedence; admins/global moderators bypass the privacy lists; everyone else is checked against disabled, denied, then allow-list rules. Direct room creation and invitations already call this gate.
- Added the 4.3.0 batched migration. It reads the legacy `restrictChat` flag and seeds the allow list from current follows; reruns write the same current follow list.
- Updated OpenAPI settings schema, admin setting identifier, and relevant test fixture names; added allow/deny precedence coverage.
- `npx eslint` for changed JS files and `git diff --check` pass.
- Relevant Mocha tests were attempted but could not start because Redis is unavailable (`ECONNREFUSED 127.0.0.1:6379`).
- Account settings UI template is provided by the installed external theme under `node_modules`; the checked-out repository has no such template to edit. Account settings API accepts and stores all three fields.
