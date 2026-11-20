# Checkpoint

Task: restore BSD uptime fact and robust sysctl parsing.
Status: investigating root cause before edits.
Environment: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find`/`grep`.

Root cause: FreeBSD and NetBSD hardware collectors never add uptime. OpenBSD relies on `kern.boottime` in a broad sysctl dump and unconditionally converts it. Shared sysctl parsing raises on malformed lines and silently returns on nonzero status.
Pattern: SunOS/Linux hardware collectors add `get_uptime_facts()` to `populate`; BSD collectors merge per-source dictionaries.
Hypothesis: A numeric-only `sysctl -n kern.boottime` read shared by BSD hardware classes, plus tolerant line parsing, yields uptime while preserving other facts. Reproduction test executed before patch: `PYTHONPATH=lib python -m pytest -q test/units/module_utils/facts/hardware/test_bsd_uptime.py` failed for the identified behavior. One test had an incompatible pytest helper and was corrected before implementation.

Implemented: private numeric-only BSD uptime reader using `sysctl -n kern.boottime`; merged uptime into FreeBSD, NetBSD, and OpenBSD hardware facts. Shared sysctl parser now handles `=`, `:`, and whitespace delimiters, multiline continuations, malformed-line warnings, and command failure warnings.
Verification: `PYTHONPATH=lib python -m pytest -q -o addopts='' test/units/module_utils/facts/hardware test/units/module_utils/facts/test_facts.py` exited 0: 119 passed, 5 skipped. `git diff --check` exited 0. No offline tooling blocked a check.
