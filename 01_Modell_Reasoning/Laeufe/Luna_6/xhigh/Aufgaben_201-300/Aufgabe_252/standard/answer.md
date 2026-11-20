Implemented BSD uptime collection using `sysctl -n kern.boottime`, omitting uptime for failed or nonnumeric results and raising `ValueError` when the binary is missing. Sysctl parsing now handles `=`, `:`, and whitespace delimiters, preserves multiline values, and warns on malformed lines while continuing.

Updated [sysctl.py](/app/lib/ansible/module_utils/facts/sysctl.py) and the OpenBSD, FreeBSD, NetBSD, and Darwin hardware collectors. The checkpoint is in `.codex-role-output/checkpoint.md`.

Verification: 17 existing unit tests passed; changed modules compiled, and `git diff --check` passed.