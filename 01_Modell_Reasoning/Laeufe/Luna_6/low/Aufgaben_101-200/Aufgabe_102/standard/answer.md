Added the Linux `locally_reachable_ips` fact with sorted, deduplicated IPv4 and IPv6 scope host entries. Unsupported IPv6 returns an empty list; route query failures warn and leave that family empty.

Validation: `test_facts.py` passed (91 passed, 5 skipped); `git diff --check` passed.