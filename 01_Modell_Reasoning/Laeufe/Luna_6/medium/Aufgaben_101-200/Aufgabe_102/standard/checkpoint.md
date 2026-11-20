# Checkpoint

Implemented `LinuxNetwork.get_locally_reachable_ips(ip_path)` and exposed its `ipv4`/`ipv6` lists as `locally_reachable_ips` in populated Linux network facts. It queries the local route table per address family, retains `scope host` entries, emits host routes as bare IPs and network routes as canonical CIDRs, and sorts/deduplicates output. Missing IPv6 support or unavailable route data returns empty family lists without interrupting other fact collection.

Verification: `python -m compileall -q lib/ansible/module_utils/facts/network/linux.py` succeeded; `python -m pytest -q test/units/module_utils/facts/network` passed (5 tests).
