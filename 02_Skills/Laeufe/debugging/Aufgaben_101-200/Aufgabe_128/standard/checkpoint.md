# Checkpoint

Task: add ipset set-extension support to the iptables module.
Process: systematic debugging; root-cause investigation underway.
Initial environment: `rg` is unavailable (`/bin/bash: rg: command not found`); use local `find`/`grep`.

Root cause: `iptables.main` does not accept `match_set` or `match_set_flags`, and `construct_rule` has no path to emit `--match-set`. Existing `iprange` handling provides the explicit/implicit match pattern. `append_param` already implements `!` inversion for values. The module uses Ansible's `required_together` elsewhere in the repository (debconf).
Hypothesis: adding paired arguments and emitting one set match clause in `construct_rule` will support both match forms without changing unrelated rule ordering.

Reproduction: added tests first; `PYTHONPATH=lib:test python -m pytest -q test/units/modules/test_iptables.py -k match_set` failed because `match_set` and `match_set_flags` were unsupported parameters.
Implementation: documented and registered both parameters, constrained flags to the four requested values, required the pair, and emitted the set extension once whether or not `match: ['set']` is given. Existing `append_param` handles `!` inversion. Added an SSH ipset example and unit coverage for rule construction, inversion, validation, and insertion through the append path.
Verification: `PYTHONPATH=lib:test python -m pytest -q -o addopts='' test/units/modules/test_iptables.py` passed (27 tests); `git diff --check` passed. No offline tooling blocked a check.
