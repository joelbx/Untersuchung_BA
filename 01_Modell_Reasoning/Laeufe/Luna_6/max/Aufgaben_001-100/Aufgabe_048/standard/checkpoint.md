# Checkpoint

Task: Resolve inconsistent plugin redirection, removal, and deprecation handling.

Completed:
- Added `AnsiblePluginError` and contextual plugin error subclasses.
- Added `get_with_context_result` and `PluginLoader.get_with_context`; `get` delegates and returns the object.
- Tombstones now raise `AnsiblePluginRemovedError` with resolution context; routing deprecation details remain accessible without lookup-time warning output.
- Centralized deprecation/removal formatting in `Display.get_deprecation_message` and removed `TAGGED_VERSION_RE` from display formatting.
- Updated task connection loading, action module resolution, and Jinja removed-plugin handling.
- Updated the action loader unit test double for `find_plugin_with_context`.

Verification:
- `PYTHONPATH=lib:test/lib python -m pytest -q test/units/plugins/test_plugins.py test/units/plugins/action/test_action.py test/units/executor/test_task_executor.py test/units/template/test_templar.py test/units/utils/display/test_display.py test/units/utils/collection_loader/test_collection_loader.py`
- Result: 140 passed, 6 pre-existing deprecation warnings.
- `git diff --check` passed.

Constraints: Used only repository code and tests; no git history, index baseline, or harness configuration changes.
