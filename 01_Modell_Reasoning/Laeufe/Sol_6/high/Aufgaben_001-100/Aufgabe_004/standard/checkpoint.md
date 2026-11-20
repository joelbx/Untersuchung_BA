# Checkpoint

Task: repair Security Center PassAliases drawer/provider and PassBridge default vault behavior.

Implemented: split vault lookup and creation, moved provider state into `usePassAliasesSetup`, added alias fetch/filter helpers, explicit empty state, full alias list, and tests for helper and no-vault creation flow.

Verification: all four PassAliases suites passed (9 tests); components and Pass type checks passed; Prettier and `git diff --check` passed.
