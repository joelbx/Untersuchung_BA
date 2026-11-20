Task: Refactor Pill to a functional component with a public usePermalink hook and named exports.
Status: Complete. Pill now uses hook-based hover state; permalink parsing, room/member lookup, avatar selection, text, and user click handling live in usePermalink. Pill callers and @room splitting use named exports. Added focused Pill coverage.
Verification: Pill, pillify, ReplyChain, and Reply tests passed (28 tests total across the final relevant runs). ESLint and Prettier passed on changed files; git diff --check passed. Full TypeScript check reported only existing errors in untouched LoginWithQR, Notifications, and VectorPushRulesDefinitions files caused by missing SDK exports.
Constraints observed: Local repository code and existing tests only; no git history/index/harness changes.
