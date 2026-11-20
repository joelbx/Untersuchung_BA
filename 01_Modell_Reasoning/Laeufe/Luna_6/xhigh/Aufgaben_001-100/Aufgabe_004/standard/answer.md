Implemented the PassAliases drawer and bridge changes. The drawer now shows the full filtered alias list or a clear “No aliases” state. Starting alias creation creates a default vault when needed, and successful creation refreshes the list and quota count.

Added the requested setup hook and helpers, moved the provider contract into `interface.ts`, and updated PassBridge to look up vaults without implicitly creating one.

**Verification:** PassAliases Jest suites passed (2 suites, 6 tests); components and Pass type checks, targeted ESLint, and `git diff --check` passed.