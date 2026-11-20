# Checkpoint

Task: Add `destination_ports` list support to the iptables module via multiport matching.
Status: Investigating existing rule construction and tests before editing module behavior.
Constraints: Local evidence only; do not alter git history, index baseline, or harness configuration.

Investigation: `destination_port` is a scalar emitted as `--destination-port`; `destination_ports` is absent from docs, argument_spec, and construct_rule. Existing `append_match` and `append_csv` provide the required multiport command construction. Existing iprange logic avoids adding a duplicate match when `match` already contains the extension. Main constructs the rule immediately after argument parsing, so protocol validation must precede that construction.
Hypothesis: registering a list parameter and emitting `-m multiport --dports` from it, with protocol validation before rule construction, yields a valid single rule and prevents use with unsupported protocols.

Reproduction: `PYTHONPATH=/app/lib:/app/test python -m pytest -q --reruns 0 test/units/modules/test_iptables.py -k destination_ports` exited 1: `Unsupported parameters ... destination_ports` from local `lib/ansible/module_utils/basic.py`. Initial invocation without PYTHONPATH used installed Ansible, so all subsequent checks will set PYTHONPATH. The unsupported-protocol test currently passes only because the parameter is unknown; its message assertion will be strengthened after implementation.

Implementation: Added documented `destination_ports` list (default `[]`); construct_rule uses append_match for `-m multiport` unless already in `match`, and append_csv for `--dports`; main rejects non-tcp/udp/udplite/dccp/sctp protocols when the list is nonempty. Added tests for numeric ports, ranges, all permitted protocols, unsupported protocols, and explicit multiport match.
Verification: `PYTHONPATH=/app/lib:/app/test python -m pytest -q --reruns 0 test/units/modules/test_iptables.py` exited 0, 24 passed. `git diff --check` exited 0. No offline tooling block remains.
