# Checkpoint

Implemented BSD `kern.boottime` uptime collection for OpenBSD and FreeBSD. Uptime is queried with `sysctl -n kern.boottime`, included only after a successful numeric response, and computed as current time minus boot time. Missing or unexecutable `sysctl` raises `ValueError`.

Hardened shared sysctl collection to handle `=`, `:`, and whitespace separators, preserve indented continuation lines, warn and continue on malformed entries, and return an empty dictionary with a warning when command execution fails or exits nonzero.

Validation: `python -m pytest -q test/units/module_utils/facts/test_facts.py` passed (91 passed, 5 skipped); `git diff --check` passed.
