VERDICT: FIX

**Code defects**

- [Jinja filter lookup](/app/lib/ansible/template/__init__.py:400) enumerates files before consulting the loader. A tombstoned filter with no file raises `KeyError` instead of the required `TemplateSyntaxError`. An in-memory reproduction returned `KeyError` with zero loader calls. Check routing metadata for the requested filter before enumeration.
- [Plugin lookup](/app/lib/ansible/plugins/loader.py:537) no longer emits deprecation warnings, and [get_with_context](/app/lib/ansible/plugins/loader.py:750) does not emit the warnings it records. Deprecated routed plugins therefore load silently. Emit the recorded message through `Display.deprecated` at a consumer point.

**Tests:** `python -m pytest -q test/units/plugins/test_loader_context.py test/units/plugins/action/test_action.py test/units/utils/display/test_display.py test/units/executor/test_task_executor.py test/units/template/test_template_utilities.py` — **42 passed**. `git diff --check` passed.

**TEST_ENVIRONMENT_PROBLEM:** None. An earlier pytest command used the nonexistent path `test/units/utils/test_display.py` and exited 4 without running tests; the corrected command above succeeded. I made no project code or test changes.