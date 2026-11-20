Task: Add Linux locally reachable scope-host IP range facts.
Status: Complete. Linux network facts expose locally_reachable_ips with ipv4 and ipv6 lists from the local route table. Destinations are canonicalized, deduplicated, and numerically ordered. Unsupported route queries warn and return empty lists without affecting other families.
Validation: python -m pytest -q test/units/module_utils/facts/network (10 passed); git diff --check (passed).
Files: lib/ansible/module_utils/facts/network/linux.py; test/units/module_utils/facts/network/test_linux.py.
