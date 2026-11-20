# Checkpoint

Task: Add ipset matching support (`match_set`, `match_set_flags`) to the Ansible iptables module.

Plan: Inspect module argument parsing/rule construction and unit tests; implement paired parameter validation, implicit/explicit `set` match handling, inversion and command ordering; update module docs/tests; run the relevant existing iptables unit tests.
