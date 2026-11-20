Task: Add unit-aware duration parsing for :later while preserving bare-integer milliseconds.
Status: Implemented parse_duration, wired :later, updated command help and unit tests. Relevant test files pass (191 tests) under xvfb-run with pytest's xvfb plugin disabled. No delegation used.
