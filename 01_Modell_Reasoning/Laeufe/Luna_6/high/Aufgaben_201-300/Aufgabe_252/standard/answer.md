Implemented BSD uptime collection and hardened sysctl parsing.

- OpenBSD and FreeBSD now query `sysctl -n kern.boottime` and include `uptime_seconds` only when the command succeeds with numeric output. Missing or unexecutable `sysctl` raises `ValueError`.
- Sysctl parsing supports `=`, `:`, and whitespace separators, preserves indented continuation lines, and warns on malformed lines while continuing.
- Command failures now return an empty sysctl dictionary with a warning.

Validation: `test_facts.py` passed (91 passed, 5 skipped); `git diff --check` passed. Updated `.codex-role-output/checkpoint.md`.

Changed: [sysctl.py](/app/lib/ansible/module_utils/facts/sysctl.py), [openbsd.py](/app/lib/ansible/module_utils/facts/hardware/openbsd.py), [freebsd.py](/app/lib/ansible/module_utils/facts/hardware/freebsd.py).