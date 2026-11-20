# Plugin routing issue checkpoint

Implemented contextual plugin exceptions, structured `get_with_context` results, tombstone and redirect metadata, centralized display formatting, and caller updates in action, connection, and Jinja paths. Added focused loader and display tests and updated the action mock for the new context API.

Verification: `PYTHONPATH=lib python -m pytest -q test/units/plugins/test_loader_context.py test/units/plugins/action/test_action.py test/units/template test/units/utils/display/test_display.py test/units/plugins/test_plugins.py` — 95 passed. `git diff --check` passed.
