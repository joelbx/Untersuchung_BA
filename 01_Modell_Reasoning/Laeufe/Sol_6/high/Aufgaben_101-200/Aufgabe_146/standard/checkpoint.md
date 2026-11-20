Task: add s390 `/proc/sysinfo` hardware facts in LinuxHardware and run relevant existing tests.
Initial state: clean worktree. `rg` is unavailable, so searches use grep/find.
Status: complete. Added `/proc/sysinfo` parsing and merged its five hardware facts after DMI facts in `populate()`. Added regression tests for absent/present files, missing values, serial normalization, and merge precedence.
Verification: `PYTHONPATH=lib python -m pytest -q test/units/module_utils/facts/hardware` (21 passed); `git diff --check` passed.
