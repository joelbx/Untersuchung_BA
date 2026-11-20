# Checkpoint

Implemented context carrying plugin errors, loader `get_with_context`, tombstone exceptions, contextual deprecation formatting, and updated connection/action/Jinja consumers. Added focused tests for missing plugin context, tombstones, removed filters, and deprecation messages.

Checks:
- `PYTHONPATH=lib python -m pytest -q test/units/plugins/test_plugins.py test/units/plugins/action/test_action.py test/units/template test/units/utils/display/test_display.py test/units/executor/test_task_executor.py`: 105 passed, 6 existing deprecation warnings.
- `PYTHONPATH=lib python -m pytest -q test/units/utils/display/test_warning.py`: 1 passed, 1 failed. The second test receives no output because the singleton Display retained the first test's identical warning in `_warns`; this test does not exercise changed warning code.
- `git diff --check`: passed.

`rg` was unavailable (`/bin/bash: rg: command not found`); searches used `grep`/`find`.

Final focused test rerun after the last changes: 105 passed, 6 deprecation warnings. `git diff --check` passed.
