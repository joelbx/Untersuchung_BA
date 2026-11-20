Fixed the BSD sysctl parser so blank lines inside multiline values are preserved, and added a regression test.

The sysctl tests pass (16/16). The full facts suite had one remaining timing-sensitive timeout failure (368 passed, 5 skipped); that test passed when rerun alone. `git diff --check` passed.