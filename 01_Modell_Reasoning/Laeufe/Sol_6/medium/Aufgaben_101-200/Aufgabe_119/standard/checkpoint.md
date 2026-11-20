# Pill refactor checkpoint

Task: Refactor Pill to a functional component, extract public usePermalink hook, migrate imports, and run relevant existing tests.
Status: Complete.
Changes: Pill and notification helpers are named exports; permalink resolution and profile lookup live in usePermalink; pillify, ReplyChain, and BridgeTile use named imports.
Verification: ReplyChain and pillify Jest suites passed (5 tests). ESLint and git diff --check passed. TypeScript reports existing SDK compatibility errors outside changed files; no diagnostics in changed files.
