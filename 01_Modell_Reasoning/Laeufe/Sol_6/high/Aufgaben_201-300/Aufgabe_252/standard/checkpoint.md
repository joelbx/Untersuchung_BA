Task: Fix BSD gather_facts uptime and sysctl parsing in the checked-out repository.
Status: Implemented BSD uptime collection through `sysctl -n kern.boottime` for FreeBSD/DragonFly, NetBSD, OpenBSD, and Darwin. Improved shared sysctl parsing, multiline handling, and warnings. Added focused unit tests.
Verification: 103 passed, 5 skipped in focused facts tests; `git diff --check` passed. Broader facts suite: 364 passed, 5 skipped, 1 unrelated timeout test failed in suite but passed alone.
Constraints: Use local code/tests only; preserve git history, index, and harness configuration.
