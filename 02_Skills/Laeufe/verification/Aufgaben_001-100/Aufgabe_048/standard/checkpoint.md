# Checkpoint

Implemented contextual plugin errors and loader `get_with_context` result, tombstone errors, centralized Display deprecation/removal formatting, and updated action, connection, and Jinja callers. Updated action test fixture for the new lookup API and added loader context tests.

Verification:
- `git diff --check && PYTHONPATH=lib python -m compileall -q lib/ansible/errors/__init__.py lib/ansible/plugins/loader.py lib/ansible/utils/display.py lib/ansible/executor/task_executor.py lib/ansible/plugins/action/__init__.py lib/ansible/template/__init__.py`: exit 0.
- `PYTHONPATH=lib python -m pytest -q test/units/plugins/test_plugins.py test/units/utils/display/test_display.py test/units/utils/collection_loader/test_collection_loader.py test/units/plugins/action/test_action.py test/units/plugins/filter test/units/plugins/connection/test_connection.py test/units/plugins/connection/test_local.py test/units/template`: 207 passed, 1 rerun, exit 0.
- Broader command `PYTHONPATH=lib python -m pytest -q test/units/plugins/test_plugins.py test/units/utils/display/test_display.py test/units/utils/collection_loader/test_collection_loader.py test/units/plugins/action test/units/plugins/filter test/units/plugins/connection`: 12 failed, 192 passed, 36 rerun, exit 1. The action mock failure was addressed. Remaining failures in that run include network facts expected `cisco.ios.ios_facts` but got `ios_facts`, SSH monkeypatch could not find `ansible.plugins.connection.ssh`, and WinRM tests could not execute `kinit` or received different subprocess errors. Those suites were not rerun after the action fixture update; their status remains uncertain.

Inspection tool limitation: `rg` unavailable (`/bin/bash: rg: command not found`); used `grep` and `find` locally.
