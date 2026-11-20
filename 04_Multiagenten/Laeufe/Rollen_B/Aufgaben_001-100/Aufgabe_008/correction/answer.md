The current `useLink` patch addresses the repeated fetches, and the reviewer identified no correctness defect. No further code change was needed in this correction round.

The exact flagged test command passed **17/17 tests**. `git diff --check` also passed. No test environment problem remains.