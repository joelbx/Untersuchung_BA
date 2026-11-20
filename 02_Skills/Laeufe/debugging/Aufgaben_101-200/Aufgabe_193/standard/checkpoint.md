# Checkpoint

Task: unify ansible-galaxy requirements installation for roles and collections.
Status: investigating CLI dispatch and existing tests before editing implementation.
Environment: `rg` unavailable (`/bin/bash: rg: command not found`); using grep/find.

Root cause: `__init__` rewrites implicit commands to `role`, losing whether role was explicit. `execute_install` branches exclusively on `type`; role `-r` uses `role_file`, collection `-r` uses `requirements`. Consequently mixed requirements cannot reach both installers. Existing dependency loop already appends unresolved role dependencies and skips installed ones unless forced.
Hypothesis: retain implicit-command state, initialize parser keys, and dispatch parsed requirements to separate role/collection installers. Default path permits both; custom roles path or explicit type limits dispatch.

Implementation: retained whether `role` was implicit and whether a roles path was supplied; initialized missing CLI context keys; parsed requirements once and dispatched roles and collections through separate install helpers. Empty YAML returns empty requirements. Collection install accepts legacy role-only files and reports skipped roles. Existing role dependency queue remains intact.

Verification:
- Initial `python -m pytest -q test/units/cli/test_galaxy.py -k test_parse_install` passed, but imported `/usr/local/lib/python3.9/dist-packages/ansible`; this did not verify checkout code.
- Initial reproduction test without `PYTHONPATH` failed with `KeyError: 'requirements'` against system Ansible; corrected test environment to `PYTHONPATH=lib:test`.
- `PYTHONPATH=lib:test python -m pytest -q test/units/cli/test_galaxy.py test/units/cli/galaxy` produced six failures: four warning-count differences from development warning and two tests whose mocked requirements dictionary lacked `roles`. The dictionary handling was fixed; warning-count tests require `ANSIBLE_DEVEL_WARNING=False` in this environment.
- `ANSIBLE_DEVEL_WARNING=False PYTHONPATH=lib:test python -m pytest -q test/units/cli/test_galaxy.py test/units/cli/galaxy`: 138 passed.
- `git diff --check`: passed.
- Final default-path regression added. `ANSIBLE_DEVEL_WARNING=False PYTHONPATH=lib:test python -m pytest -q test/units/cli/test_galaxy.py test/units/cli/galaxy`: 139 passed.
