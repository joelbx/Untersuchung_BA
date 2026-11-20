# Checkpoint

Task: Add `destination_ports` to the iptables module with multiport matching for tcp, udp, udplite, dccp, and sctp.

Completed: Added the list option with an empty-list default, documentation and example, multiport command construction using `append_match` and `append_csv`, and protocol validation. Added unit coverage for supported protocols, generated check/append commands, and unsupported protocols. The new tests failed first because the option was unrecognized, then passed after implementation.

Checks:
- `PYTHONPATH=lib:test python -m pytest -q test/units/modules/test_iptables.py`: 23 passed.
- `PYTHONPATH=lib:test python -m pytest -q test/units/modules`: 102 passed, 1 failed: `test/units/modules/test_pip.py::test_failure_when_pip_absent[patch_ansible_module0]` expected `pip needs to be installed`, got `one of the following is required: name, requirements`. Unrelated to iptables.
- `PYTHONPATH=lib:test python -m pytest -q`: attempted project-wide run. It reported 19 collection errors, including missing `validate_modules` and `botocore`, and many unrelated failures. Interrupted after 80 failed, 294 passed, 93 errors, and 463 reruns because it was continuing through unrelated failures. Full suite status remains unknown.
- `git diff --check`: passed.
