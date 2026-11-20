Updated room search to combine adjacent results when their timelines share a boundary event. The combined tile renders the shared event once, tracks every direct match for highlighting, and links each match to its own event ID. Results without an overlap still render separately.

The existing SearchResultTile test, TypeScript check, ESLint, and `git diff --check` passed.