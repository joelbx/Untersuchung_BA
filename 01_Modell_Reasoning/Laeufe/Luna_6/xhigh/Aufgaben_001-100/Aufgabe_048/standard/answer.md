Implemented contextual plugin resolution and consistent removal/deprecation handling.

- Added `AnsiblePluginError` and contextual plugin exceptions; tombstones now raise `AnsiblePluginRemovedError` with resolution metadata.
- Added `get_with_context()` and its named tuple result; `get()` delegates to it and returns the plugin object.
- Centralized deprecation and removal formatting in `Display.get_deprecation_message()`.
- Updated connection, action module, and Jinja plugin loading to use contextual results.

Relevant changes: [errors](/app/lib/ansible/errors/__init__.py:279), [loader](/app/lib/ansible/plugins/loader.py:769), [display](/app/lib/ansible/utils/display.py:253), [task executor](/app/lib/ansible/executor/task_executor.py:914), [action loader](/app/lib/ansible/plugins/action/__init__.py:195), [template loader](/app/lib/ansible/template/__init__.py:405).

Verification: 145 relevant unit tests passed; a focused 56 test rerun passed. `git diff --check` passed.