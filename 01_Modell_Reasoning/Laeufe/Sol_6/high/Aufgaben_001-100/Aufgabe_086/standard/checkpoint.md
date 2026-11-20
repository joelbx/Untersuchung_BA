Task: Add `destination_ports` support to the iptables module using multiport, with protocol restrictions.
Status: Implemented and verified. `destination_ports` is a list of strings with an empty default, generates `-m multiport --dports`, and rejects unsupported protocols. Added documentation, an example, and unit tests for supported and unsupported protocols.
Verification: `PYTHONPATH=/app/lib:/app/test python -m pytest -q test/units/modules/test_iptables.py` (23 passed); `git diff --check` passed.
Constraints: Edit checked-out files only; run relevant existing tests; do not change git history, index baseline, or harness configuration.
