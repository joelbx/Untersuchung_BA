Added the `locally_reachable_ips` fact, with separate `ipv4` and `ipv6` lists. The Linux collector gathers host-scope routes, normalizes and sorts destinations, and warns while returning empty lists when routes or the `ip` command are unavailable. Registered the fact for collector filtering.

Validation: `git diff --check` passed; relevant existing unit tests passed (141 passed, 5 skipped).

Changed [linux.py](/app/lib/ansible/module_utils/facts/network/linux.py:48) and [base.py](/app/lib/ansible/module_utils/facts/network/base.py:49).