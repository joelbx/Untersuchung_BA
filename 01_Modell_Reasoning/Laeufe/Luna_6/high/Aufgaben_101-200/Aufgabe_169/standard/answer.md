Implemented adjacent search result merging. Overlapping timelines render once with the duplicate pivot skipped; match indices preserve highlighting, and each matched event links to its own ID. Non-overlapping results remain separate.

Validation passed: 2 targeted Jest suites (9 tests), TypeScript checks, targeted ESLint, Prettier, and `git diff --check`.