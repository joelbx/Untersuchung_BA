Task: Add a Linux network fact for scope host reachable IPs.

Implemented `locally_reachable_ips` in the Linux network fact payload, with `ipv4` and `ipv6` lists. The method queries each supported family through `ip route show table local`, filters `scope host`, canonicalizes address/prefix values using `ipaddress`, de-duplicates and orders them deterministically. Unsupported IPv6 is represented by an empty list; command failures warn and leave the affected list empty.

Validation: `python -m pytest -q test/units/module_utils/facts/test_facts.py` passed (91 passed, 5 skipped); `git diff --check` passed.
