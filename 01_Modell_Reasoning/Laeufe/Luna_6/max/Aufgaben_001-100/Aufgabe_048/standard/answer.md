Implemented plugin resolution metadata and consistent deprecation handling.

- Added contextual plugin errors and `PluginLoader.get_with_context`; `get()` now delegates and returns the plugin object. Tombstones raise `AnsiblePluginRemovedError` with resolution context in [loader.py](/app/lib/ansible/plugins/loader.py:765) and [errors/__init__.py](/app/lib/ansible/errors/__init__.py:279).
- Centralized deprecation and removal messages in [display.py](/app/lib/ansible/utils/display.py:253). Updated connection loading, action module resolution, and Jinja handling to use the context API.
- Updated the action loader test double for the new lookup method.

Verification: **140 tests passed**; six existing deprecation warnings. `git diff --check` passed.