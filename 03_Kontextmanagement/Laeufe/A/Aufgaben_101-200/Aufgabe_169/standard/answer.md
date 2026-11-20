Room search now combines adjacent results whose context timelines overlap at the same event. The merged tile shows events in order, highlights each direct match, and links each match to its own event. A regression test covers a three result chain with a call event at the overlap and a separate result.

Verification passed: 9 focused tests, TypeScript, ESLint, Prettier, and `git diff --check`.