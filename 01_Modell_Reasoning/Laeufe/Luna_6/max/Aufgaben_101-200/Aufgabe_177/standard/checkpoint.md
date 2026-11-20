# Chat Allow/Deny List checkpoint

## Objective
Implement chat privacy settings (`disableIncomingMessages`, `chatAllowList`, `chatDenyList`), enforce them for all chat initiation and room creation paths, and add the repeatable 4.3.0 migration from legacy `restrictChat` follow lists.

## Initial state
- Repository: `/app`
- Working tree was clean at start.
- `rg` is unavailable in the environment; use `find`/`grep` for repository searches.

## Progress
- Started repository and instruction discovery.

## Validation
- Pending.

## Findings
- `Messaging.canMessageUser` is the shared policy check for chat initiation and API room invitations; the account settings API stores arbitrary per-user settings through `User.saveSettings`.
- New rooms and member additions also have internal callers, so privacy must be checked in the messaging room layer as well as at API entry points.
- User settings are stored as database hash values; chat lists will be JSON encoded at rest and parsed into string UID arrays on read.
- Account settings are rendered from the active theme package. The checked-out account client can replace the legacy control and render/manage the new settings without editing ignored build output or dependencies.
- The new migration will batch through `users:joindate`, read legacy `restrictChat` and both follow sets, and only seed users without a valid existing allow list.

## Implementation plan
- Add parsing/defaults/save handling for the three user settings and account controls.
- Centralize privacy evaluation with block precedence and admin/global moderator exemption; enforce it for new room creation and member additions.
- Add `src/upgrades/4.3.0/chat_allow_list.js`, update OpenAPI/admin field naming and affected tests.
- Run relevant existing messaging and user tests, then inspect the final diff and legacy-name references.

## Completed changes
- Added normalized boolean and UID-list parsing/defaults/saving for `disableIncomingMessages`, `chatAllowList`, and `chatDenyList`.
- Added ordered server-side chat privacy checks: recipient blocks first, then incoming-chat disable, deny list, and non-empty allow list. Admins and global moderators bypass list rules after the block check.
- Enforced privacy checks in `canMessageUser`, low-level room creation, and room member addition.
- Added account controls for the disable toggle and newline-separated UID allow/deny lists; updated the admin default setting and OpenAPI schema.
- Added the batched, repeatable 4.3.0 migration from legacy follow lists. Valid existing allow lists are preserved on reruns.
- Renamed old setting references in checked-in code and tests; the migration retains the legacy field name to read prior data.

## Validation
- ESLint and JavaScript syntax checks passed for changed JavaScript files.
- Updated language JSON files parse successfully.
- `npm test -- --grep='Messaging Library|User'`: 309 passing.
- `npm test -- --grep='^(API|Upgrade)'`: 22 passing, including OpenAPI checks and migration discovery/run.
- A broad grep `API|upgrade` unintentionally selected a Flags test through its `(v3 API)` title and failed its history assertion (`test/flags.js:985`); the explicit API/Upgrade suite selection passed.
- Redis was started locally for test execution and shut down afterward.
