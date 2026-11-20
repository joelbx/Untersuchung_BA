# Checkpoint

Root cause: `PluginLoadContext` held redirect/deprecation state, but `get()` discarded it. Tombstones were marked resolved and returned instead of raising. Loader deprecation warnings used a separate formatting path, and Jinja did not identify removed filters explicitly.

Implemented a contextual plugin error base, tombstone exceptions, `get_with_context_result`, centralized deprecation/removal formatting, and updates to the action, connection, and Jinja callers. Updated the action test mock for the new context API and added regression tests for missing and removed plugins.

Initial reproduction: `PYTHONPATH=lib:test python -m pytest -q test/units/plugins/test_resolution_context.py` failed at collection with `ImportError: cannot import name 'AnsiblePluginRemovedError'` (expected before implementation).

Final check: `PYTHONPATH=lib:test python -m pytest -q test/units/plugins/test_resolution_context.py test/units/plugins/test_plugins.py test/units/utils/display/test_display.py test/units/plugins/action/test_action.py test/units/plugins/connection test/units/template test/units/executor/test_task_executor.py` passed: 163 tests, 6 pre-existing deprecation warnings.

`git diff --check` passed. `rg` was unavailable (`/bin/bash: rg: command not found`); local grep/find was used instead.
