Correction round: reviewed the existing sysctl parser and tests. The parser skipped empty lines, which removed blank lines inside multiline values. It now appends empty lines to the active value, and a regression test covers `first\n\n  third`.

Verification: sysctl tests 16 passed; full facts suite 1 failed, 368 passed, 5 skipped. The failure was the existing timing-sensitive `test_implicit_file_default_timesout`, which passed when rerun alone. `git diff --check` passed. No prepared dependency was missing.
