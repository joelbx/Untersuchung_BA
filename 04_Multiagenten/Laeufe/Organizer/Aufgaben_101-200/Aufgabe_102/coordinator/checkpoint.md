Task: Add Linux scope-host locally reachable IP range facts.
Status: Implemented in LinuxNetwork.populate/get_locally_reachable_ips; added Linux network unit tests.
Verification: PYTHONPATH=lib:test pytest -q test/units/module_utils/facts/network (10 passed); git diff --check passed.
Delegation: none.
