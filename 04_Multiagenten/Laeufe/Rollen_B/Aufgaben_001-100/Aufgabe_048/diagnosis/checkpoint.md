Fault localization complete. No project source or tests changed.

Likely change points:
- lib/ansible/errors/__init__.py:279-291: plugin exceptions inherit AnsibleRuntimeError, have no plugin_load_context; AnsiblePluginRemoved has legacy name.
- lib/ansible/plugins/loader.py:119-155,430-475,527-553,759-813: PluginLoadContext already tracks redirects/deprecation/removal fields; tombstones set resolved=True and return context, redirect cycle raises without context, lookup emits deprecation warnings directly, get() returns a bare instance/None and drops context. New result tuple/get_with_context should carry context through all normal failure branches (missing path/base class/abstract class). Consider Jinja2Loader.get override at 954.
- lib/ansible/utils/display.py:54,257-304: tagged version parsing and removal/deprecation formatting live in deprecated(); no reusable get_deprecation_message. Loader's record_deprecation also formats strings separately.
- lib/ansible/executor/task_executor.py:893-924: _get_connection calls get() directly.
- lib/ansible/plugins/action/__init__.py:156-201: _configure_module calls find_plugin(), so unresolved redirects lose resolution detail.
- lib/ansible/template/__init__.py:354-415: collection Jinja filter/test lookup checks only builtin redirects and calls loader.get() for discovered modules; no explicit tombstone handling; errors from get() are wrapped in TemplateSyntaxError, but missing results can cause AttributeError.

Existing tests: test/units/plugins/test_plugins.py covers basic loader behavior, not routing/tombstones/context; test/units/plugins/action/test_action.py:111-174 mocks find_plugin and would need adaptation to find_plugin_with_context. test/units/utils/display/test_display.py has only a basic display case. No existing targeted routing tests located in these unit paths.

Uncertainty: issue wording says get() returns only object while failures of both methods yield a structured result; likely get() should continue returning None on lookup failure, with metadata available only from get_with_context(). The desired exception-vs-result behavior for tombstones should be reconciled by carrying context on AnsiblePluginRemovedError.
