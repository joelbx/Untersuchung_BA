Implemented greedy merging of adjacent search results when their timelines share the boundary event. Merged tiles render the full timeline, highlight only direct matches, and link each match to its own event ID. Updated the existing tile test fixture and checkpoint.

Verification passed: focused Jest suites (2 suites, 8 tests), TypeScript, Prettier, ESLint, and `git diff --check`.