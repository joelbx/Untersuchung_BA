Added the Linux `locally_reachable_ips` fact with separate IPv4 and IPv6 lists. It collects host scoped routes, normalizes and deduplicates addresses and prefixes, and orders them consistently. If a query is unavailable, that family returns an empty list with a warning; other facts continue to gather.

The new gather subset is documented in [setup.py](/app/lib/ansible/modules/setup.py:20), with implementation in [linux.py](/app/lib/ansible/module_utils/facts/network/linux.py:67) and coverage in [test_linux.py](/app/test/units/module_utils/facts/network/test_linux.py:10).

Verification: 147 tests passed, 5 skipped; `git diff --check` passed.