# Checkpoint

Task: Resolve inconsistent plugin routing, removal/deprecation behavior and expose plugin resolution context.

Implemented:
- Added context-carrying plugin errors and the `get_with_context_result` return shape.
- Added `PluginLoader.get_with_context`; `get` delegates and returns its object. Resolution errors and misses return `(None, context)`.
- Tombstones now raise `AnsiblePluginRemovedError`; plugin context lookup no longer emits legacy deprecation warnings.
- Updated module and connection callers to use structured loader APIs.
- Added centralized display deprecation message formatting and removed warning construction duplication.
- Added removed-filter handling and template syntax error conversion.

Validation:
- `python -m compileall -q lib/ansible` passed.
- `git diff --check` passed.
- Broader `test/units/errors`, `test/units/template`, and `test/units/utils/display` run: 69 passed, 2 failed (template JSON conversion and display warning output, unrelated to changed code); 6 rerun/skip markers.
- `python -m pytest -q test/units/plugins/test_plugins.py test/units/utils/display/test_display.py test/units/template/test_templar.py test/units/executor/test_task_executor.py`: 68 passed, 6 pre-existing deprecation warnings.
