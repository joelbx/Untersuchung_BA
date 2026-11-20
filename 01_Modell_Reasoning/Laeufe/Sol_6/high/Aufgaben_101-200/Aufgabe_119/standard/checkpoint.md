# Pill refactor checkpoint

Status: complete.

Implemented functional named-export Pill; reusable usePermalink hook; named @room token helpers; named imports in pillify, ReplyChain, and BridgeTile; shared PillType enum re-exported by Pill. Added tests for invalid links, exact message href, user click and tooltip, room and Space styling, avatar order, @room, and helper functions.

Verification: 2 relevant Jest suites passed (7 tests); ESLint and Prettier passed on edited files; git diff --check passed. Full TypeScript check is blocked by existing SDK API errors in LoginWithQR, Notifications, and VectorPushRulesDefinitions; it reported no errors in edited files.
