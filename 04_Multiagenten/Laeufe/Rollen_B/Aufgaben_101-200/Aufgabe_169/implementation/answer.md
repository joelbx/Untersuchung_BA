Search results now merge greedily into one tile when adjacent timelines share a boundary event. The shared event appears once; every direct match is highlighted and links to its own event. Other results still render separately.

Verification passed: 9 focused tests, TypeScript, ESLint, Prettier, and `git diff --check`.