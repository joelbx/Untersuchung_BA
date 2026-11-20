# PassAliases drawer issue

Status: complete.

Implemented:
- The bridge now looks up the oldest eligible active vault without creating one. `createDefaultVault` refreshes that lookup, creates `Personal` only when needed, and caches the created vault.
- The provider uses the named `usePassAliasesSetup` hook and the full `PassAliasesProviderReturnedValues` interface.
- Alias helpers filter trashed items, sort recent aliases, and fetch aliases plus access with a five minute TTL.
- Initialization handles accounts without a vault as an empty state. Opening the creation flow creates a vault when needed. Saving refetches aliases with `maxAge: 0`, updates counts and cached items, copies the email, and shows the required notifications or upsell.
- The drawer displays “No aliases” and the “Get an alias” action.

Validation:
- Components PassAliases Jest suites: 3 passed, 10 tests passed.
- Pass bridge Jest suite: 1 passed, 1 test passed.
- Components and Pass TypeScript checks passed.
- Focused ESLint, Prettier, and `git diff --check` passed.

Constraints observed: local code and existing test framework only; git history, index baseline, and harness configuration unchanged.
