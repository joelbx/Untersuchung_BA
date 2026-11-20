# Checkpoint

Task: Fix BSD uptime fact collection and robust sysctl parsing in /app.
Status: Implementation and focused verification complete.
Changes: Numeric `sysctl -n kern.boottime` uptime collection is wired into FreeBSD/DragonFly, OpenBSD, NetBSD, and Darwin hardware facts. Shared sysctl parsing accepts `=`, `:`, and space delimiters, preserves multiline continuations (including blank lines), warns on malformed lines, and warns/returns no facts when bulk sysctl execution fails.
Verification: 22 focused and related tests passed. The facts suite excluding its timeout test passed (359 passed, 5 skipped). The full facts suite had one unrelated failure in `test_implicit_file_default_timesout`; that test passed when rerun alone. `git diff --check` passed.
Constraints: Local code/tests only; no git history, index baseline, or harness configuration changes.
